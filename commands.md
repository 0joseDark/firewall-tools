Aqui está uma lista útil de comandos da **Firewall do Windows** usando o **netsh**. Esses comandos podem ser usados para configurar, 
gerenciar e visualizar regras do firewall:

### Lista de Comandos da Firewall do Windows com `netsh`

1. **Exibir todas as regras do firewall:**
   ```bash
   netsh advfirewall firewall show rule name=all
   ```
   - Mostra todas as regras de firewall ativas.

2. **Adicionar uma regra para abrir uma porta TCP:**
   ```bash
   netsh advfirewall firewall add rule name="NomeDaRegra" protocol=TCP dir=in localport=[PORTA] action=allow
   ```
   - Adiciona uma regra que permite tráfego de entrada (inbound) em uma porta TCP específica.

3. **Adicionar uma regra para abrir uma porta UDP:**
   ```bash
   netsh advfirewall firewall add rule name="NomeDaRegra" protocol=UDP dir=in localport=[PORTA] action=allow
   ```
   - Adiciona uma regra que permite tráfego de entrada em uma porta UDP.

4. **Remover uma regra que abre uma porta TCP:**
   ```bash
   netsh advfirewall firewall delete rule name="NomeDaRegra" protocol=TCP localport=[PORTA]
   ```
   - Remove a regra que permite tráfego de entrada na porta TCP especificada.

5. **Remover uma regra que abre uma porta UDP:**
   ```bash
   netsh advfirewall firewall delete rule name="NomeDaRegra" protocol=UDP localport=[PORTA]
   ```
   - Remove a regra que permite tráfego de entrada na porta UDP.

6. **Exibir regras para uma porta específica:**
   ```bash
   netsh advfirewall firewall show rule name=all | findstr [PORTA]
   ```
   - Filtra as regras para uma porta específica.

7. **Desabilitar todas as regras de firewall:**
   ```bash
   netsh advfirewall set allprofiles state off
   ```
   - Desativa a firewall para todos os perfis (público, privado e domínio).

8. **Habilitar todas as regras de firewall:**
   ```bash
   netsh advfirewall set allprofiles state on
   ```
   - Ativa a firewall para todos os perfis.

9. **Exibir o status atual do firewall:**
   ```bash
   netsh advfirewall show allprofiles
   ```
   - Mostra o status do firewall para todos os perfis.

10. **Exibir as configurações de firewall do perfil de domínio:**
    ```bash
    netsh advfirewall show domain
    ```
    - Exibe as configurações de firewall para o perfil de domínio.

11. **Exibir as configurações de firewall do perfil privado:**
    ```bash
    netsh advfirewall show private
    ```
    - Exibe as configurações de firewall para o perfil privado.

12. **Exibir as configurações de firewall do perfil público:**
    ```bash
    netsh advfirewall show public
    ```
    - Exibe as configurações de firewall para o perfil público.

13. **Exibir conexões bloqueadas pelo firewall:**
    ```bash
    netsh advfirewall firewall show blockedconnections
    ```
    - Lista as conexões que estão sendo bloqueadas pela firewall.

14. **Criar uma regra de saída (outbound) para bloquear um programa:**
    ```bash
    netsh advfirewall firewall add rule name="BloquearPrograma" dir=out program="C:\Caminho\Para\Programa.exe" action=block
    ```
    - Cria uma regra de saída que bloqueia um programa específico.

15. **Criar uma regra de entrada (inbound) para bloquear uma aplicação:**
    ```bash
    netsh advfirewall firewall add rule name="BloquearEntrada" dir=in program="C:\Caminho\Para\Programa.exe" action=block
    ```
    - Cria uma regra que bloqueia o tráfego de entrada de um programa específico.

16. **Redefinir a firewall para as configurações padrão:**
    ```bash
    netsh advfirewall reset
    ```
    - Restaura a firewall para as configurações padrão de fábrica.

17. **Exibir regras de firewall específicas por nome:**
    ```bash
    netsh advfirewall firewall show rule name="NomeDaRegra"
    ```
    - Mostra detalhes de uma regra de firewall específica pelo nome.

18. **Modificar uma regra existente para uma porta:**
    ```bash
    netsh advfirewall firewall set rule name="NomeDaRegra" new localport=[PORTA]
    ```
    - Modifica uma regra existente, trocando a porta.

19. **Criar uma regra para permitir um intervalo de portas:**
    ```bash
    netsh advfirewall firewall add rule name="PermitirPortas" protocol=TCP dir=in localport=5000-5050 action=allow
    ```
    - Adiciona uma regra que permite tráfego de entrada em um intervalo de portas.

20. **Excluir todas as regras de firewall:**
    ```bash
    netsh advfirewall firewall delete rule name=all
    ```
    - Remove todas as regras de firewall.

### Uso Combinado com `PowerShell`:

o PowerShell para gerenciar a Firewall do Windows, que oferece uma interface mais moderna e flexível. Um exemplo básico seria:

```powershell
Get-NetFirewallRule
```
- Exibe todas as regras de firewall usando PowerShell.

Essa lista cobre comandos úteis para gerenciar a firewall no Windows 10.