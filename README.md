# SEL0337
PRATICA 5
# Projeto Blink LED com SystemD

Este repositório documenta a prática de configuração de um serviço personalizado utilizando `systemd` em uma Raspberry Pi. O objetivo do projeto é demonstrar como configurar um script para ser executado automaticamente no boot, gerenciando o piscar de um LED conectado a um GPIO da placa.

## Funcionamento do Projeto

O projeto consiste em:
1. **Script Bash (`blink.sh`)**: Controla o GPIO para alternar o estado do LED.
2. **Arquivo de Serviço (`blink.service`)**: Configura o `systemd` para gerenciar o script, permitindo sua inicialização automática no boot.
3. **Gerenciamento com Git/GitHub**: Controle de versão dos arquivos e documentação do projeto, com histórico completo dos commits.

### Etapas Implementadas
1. **Criação do Script (`blink.sh`)**:
   - Exporta e configura o GPIO 18 como saída.
   - Alterna o estado do LED em um loop infinito.

2. **Configuração do Serviço (`blink.service`)**:
   - Define o script como o processo a ser executado no boot.
   - Permite controle manual utilizando `systemctl` (start, stop, enable, disable).

3. **Documentação e Controle de Versão**:
   - Todos os arquivos e alterações estão registrados neste repositório Git.
   - O histórico de commits pode ser consultado no arquivo `historico_git.txt`.

## Fotografias da Montagem
- A montagem prática do circuito pode ser vista na imagem abaixo:
  ![Montagem do Circuito](link_para_fotografia)

- Funcionamento do projeto com o LED piscando:
  ![Funcionamento do Projeto](link_para_video)

## Scripts e Arquivos
- **[blink.sh](scripts/blink.sh)**: Script Bash que controla o piscar do LED.
- **[blink.service](services/blink.service)**: Arquivo de configuração do serviço.
- **[historico_git.txt](historico_git.txt)**: Histórico de alterações do projeto.

## Comandos Principais

### Configuração Inicial
1. Torne o script executável:
   ```bash
   chmod +x scripts/blink.sh
