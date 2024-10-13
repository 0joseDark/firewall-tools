import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import datetime

# Função para varrer e exibir as portas abertas junto com os programas
def varrer_portas():
    try:
        # Comando para listar as regras de firewall do Windows
        result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all'], capture_output=True, text=True)
        regras = result.stdout
        
        # Limpar a lista antes de exibir as novas portas e programas
        lista_portas.delete(0, tk.END)
        
        programa = ''
        porta_tcp = ''
        porta_udp = ''
        
        # Percorrer as regras linha por linha
        for linha in regras.split('\n'):
            # Verificar se a linha contém o caminho do programa
            if "Program:" in linha:
                programa = linha.split(":")[1].strip()
            
            # Verificar portas TCP e UDP
            if "LocalPort" in linha:
                porta = linha.split(":")[1].strip()
                if "TCP" in linha:
                    porta_tcp = porta
                elif "UDP" in linha:
                    porta_udp = porta
            
            # Se encontrarmos o programa, TCP ou UDP, exibir as informações
            if programa and (porta_tcp or porta_udp):
                entrada = f"{programa} + UDP: {porta_udp if porta_udp else 'N/A'} + TCP: {porta_tcp if porta_tcp else 'N/A'}"
                lista_portas.insert(tk.END, entrada)
                log(entrada)
                
                # Resetar variáveis para evitar sobreposição de entradas
                programa = ''
                porta_tcp = ''
                porta_udp = ''
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para registrar no log
def log(mensagem):
    if log_pasta:
        log_file = os.path.join(log_pasta, f"log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(log_file, 'a') as f:
            f.write(mensagem + '\n')

# Função para definir o caminho do log
def definir_caminho_log():
    global log_pasta
    log_pasta = filedialog.askdirectory()
    entrada_log.delete(0, tk.END)
    entrada_log.insert(0, log_pasta)

# Função para abrir uma porta no firewall
def abrir_porta():
    porta = entrada_porta.get()
    if porta:
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', f'name=AbrirPorta{porta}', 'protocol=TCP', f'localport={porta}', 'action=allow'], capture_output=True, text=True)
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', f'name=AbrirPorta{porta}', 'protocol=UDP', f'localport={porta}', 'action=allow'], capture_output=True, text=True)
        messagebox.showinfo("Sucesso", f"Porta {porta} aberta no firewall.")
        varrer_portas()

# Função para fechar uma porta no firewall
def fechar_porta():
    porta = entrada_porta.get()
    if porta:
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', f'name=AbrirPorta{porta}', 'protocol=TCP', f'localport={porta}'], capture_output=True, text=True)
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', f'name=AbrirPorta{porta}', 'protocol=UDP', f'localport={porta}'], capture_output=True, text=True)
        messagebox.showinfo("Sucesso", f"Porta {porta} fechada no firewall.")
        varrer_portas()

# Função para sair do programa
def sair_programa():
    janela.quit()

# Criação da janela principal
janela = tk.Tk()
janela.title("Firewall do Windows - Portas Abertas e Programas")
janela.geometry("600x500")

log_pasta = ''

# Lista para exibir as portas abertas com os programas
lista_portas = tk.Listbox(janela, width=80, height=15)
lista_portas.pack(pady=10)

# Caixa de texto para definir o caminho do log
entrada_log = tk.Entry(janela, width=50)
entrada_log.pack(pady=5)
botao_caminho_log = tk.Button(janela, text="Escolher Caminho do Log", command=definir_caminho_log)
botao_caminho_log.pack(pady=5)

# Caixa de texto para especificar a porta
entrada_porta = tk.Entry(janela, width=15)
entrada_porta.pack(pady=5)

# Botões para abrir, fechar, varrer, atualizar e sair
botao_abrir_porta = tk.Button(janela, text="Abrir Porta", command=abrir_porta)
botao_abrir_porta.pack(side=tk.LEFT, padx=10, pady=10)

botao_fechar_porta = tk.Button(janela, text="Fechar Porta", command=fechar_porta)
botao_fechar_porta.pack(side=tk.LEFT, padx=10, pady=10)

botao_varrer = tk.Button(janela, text="Varrer", command=varrer_portas)
botao_varrer.pack(side=tk.LEFT, padx=10, pady=10)

botao_atualizar = tk.Button(janela, text="Atualizar", command=varrer_portas)
botao_atualizar.pack(side=tk.LEFT, padx=10, pady=10)

botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(side=tk.RIGHT, padx=10, pady=10)

# Inicializar a janela
janela.mainloop()
