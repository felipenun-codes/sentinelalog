
# SentinelaLog

Sistema desenvolvido em Python para monitoramento de acessos em um ambiente de laboratório, com registro de atividades, gerenciamento de usuários e identificação de possíveis comportamentos suspeitos.

## Sobre o projeto

O **SentinelaLog** é um sistema de monitoramento que busca auxiliar no controle de acesso a laboratórios. Ele permite cadastrar usuários, consultar registros de acesso e manter um histórico de operações realizadas no programa.

O projeto também possui mecanismos de análise de risco, considerando fatores como tentativas de acesso malsucedidas, utilização de máquinas bloqueadas e acessos realizados fora do horário permitido.

## Funcionalidades

- **Cadastro de usuários:** permite registrar nome, matrícula e perfil do usuário.
- **Gerenciamento de usuários:** permite editar e excluir usuários cadastrados.
- **Controle de acesso:** considera horários permitidos de acordo com o perfil:
  - Estudante: das 7h às 18h.
  - Professor: das 7h às 20h.
  - Administrador: das 7h às 22h.
- **Proteção de matrículas:** exibe as matrículas parcialmente ocultas durante a consulta de usuários.
- **Visualização de matrícula:** possui uma opção específica para consultar a matrícula completa, mediante autorização.
- **Registro de acessos:** armazena o usuário, a data, o horário, a máquina de origem e o resultado do acesso.
- **Log de auditoria:** registra operações importantes realizadas no sistema.
- **Análise de risco:** classifica acessos como normais, suspeitos ou críticos.
- **Máquinas bloqueadas:** utiliza o arquivo `maquinas_bloqueadas.txt` para identificar máquinas que apresentam restrições.


## Tecnologias utilizadas

- Python 
- Biblioteca `os`
- Biblioteca `datetime`


## Como executar

1. Instale o Python em seu computador.
2. Baixe este repositório.
3. Abra a pasta do projeto.
4. Execute o arquivo principal pelo terminal:

python sentinela.py

Caso o arquivo principal tenha outro nome, substitua `sentinela.py` pelo nome correto.

## Arquivos de armazenamento

O sistema utiliza arquivos `.txt` para armazenar informações e manter os registros entre execuções.

| Arquivo | Finalidade |
|---|---|
| `registrodus.txt` | Armazena os dados dos usuários |
| `registroda.txt` | Armazena os registros de acesso |
| `registroaud.txt` | Armazena o histórico de auditoria |
| `ext_nomes_u.txt` | Armazena os nomes cadastrados |
| `ext_matriculas.txt` | Armazena as matrículas |
| `ext_perfis.txt` | Armazena os perfis dos usuários |
| `maquinas_bloqueadas.txt` | Lista as máquinas bloqueadas |



## Autores

Desenvolvido por: **[Bernardo Valença, Felipe Nunes Leal, Guilherme Motta , Guilherme Staundinger, João Vincius Mendonça, Mateus Mendonça, ]**

Projeto Fundamentos de Programação — SentinelaLog.
