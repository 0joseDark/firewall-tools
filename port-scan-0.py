import subprocess
import tkinter as tk
from tkinter import messagebox

# Função para varrer e exibir as portas abertas junto com os programas
def varrer_portas():
    try:
        # Comando para listar as regras de firewall do Windows
        result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=all'], capture_output=True, text=True)
        regras = result.stdout
        
        # Limpar a lista antes de exibir as novas portas e programas
        lista_portas.delete(0, tk.END)
        
        programa = ''
        porta = ''
        for linha in regras.split('\n'):
            # Se encontrar o caminho de um programa
            if "Program" in linha:
                programa = linha.split(":")[1].strip()
            
            # Se encontrar uma porta local
            if "LocalPort" in linha:
                porta = linha.split(":")[1].strip()
                
                # Exibir o formato "programa + porta"
                if programa:
                    lista_portas.insert(tk.END, f"{programa} + {porta}")
                else:
                    lista_portas.insert(tk.END, f"(Sem programa) + {porta}")
                
                # Resetar o programa para evitar exibição incorreta
                programa = ''
                
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para atualizar a lista de portas
def atualizar_lista():
    varrer_portas()

# Função para sair do programa
def sair_programa():
    janela.quit()

# Criação da janela principal
janela = tk.Tk()
janela.title("Firewall do Windows - Portas Abertas e Programas")
janela.geometry("600x400")

# Lista para exibir as portas abertas com os programas
lista_portas = tk.Listbox(janela, width=80, height=15)
lista_portas.pack(pady=10)

# Botões para varrer, atualizar e sair
botao_varrer = tk.Button(janela, text="Varrer", command=varrer_portas)
botao_varrer.pack(side=tk.LEFT, padx=10, pady=10)

botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_lista)
botao_atualizar.pack(side=tk.LEFT, padx=10, pady=10)

botao_sair = tk.Button(janela, text="Sair", command=sair_programa)
botao_sair.pack(side=tk.RIGHT, padx=10, pady=10)

# Inicializar a janela
janela.mainloop()
