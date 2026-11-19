SentinelaLog

O SentinelaLog é um sistema em Python que a gente fez para acompanhar quem acessa o laboratório e quando. Ele cadastra usuários, guarda um histórico de acessos e avisa quando alguma coisa parece estranha, como alguém entrando de madrugada ou errando a matrícula várias vezes seguidas.

Foi feito na disciplina de Fundamentos de Programação, então tudo roda no terminal e os dados ficam em arquivos .txt, sem banco de dados.

O que ele faz

Usuários

Cadastro com nome, matrícula (precisa ter 6 dígitos) e perfil: estudante, professor ou administrador.
Ao abrir o programa, a pessoa escolhe quem é na lista e confirma com a matrícula. São 4 tentativas.
Dá para editar e excluir usuários. Para isso é preciso digitar a matrícula do usuário que vai ser alterado.
As matrículas aparecem censuradas (12****) quando a lista de usuários é mostrada. Para ver a matrícula inteira, só com a senha de administrador.

Horários

Cada perfil tem um horário permitido. Fora dele, o acesso é negado e fica registrado.

Estudante: 7h às 18h
Professor: 7h às 20h
Administrador: 7h às 22h

Registros

Todo acesso é guardado com nome, data e hora, máquina usada, resultado (sucesso ou falha) e nível de risco.
Toda ação importante (cadastrar, editar, excluir, consultar relatórios) vai para o log de auditoria, dizendo quem fez e quem foi afetado.

Segurança

Bloqueio temporário: se um usuário erra demais em sequência, ele fica bloqueado por 2 horas.
Níveis de risco: a função classificar_acesso dá pontos para cada sinal de perigo e classifica o acesso como normal, suspeito ou crítico. Falha de acesso vale 1 ponto, máquina bloqueada vale 3, acesso fora do horário vale 2 e acesso de madrugada (1h às 5h) vale 4. Até 2 pontos é normal, de 3 a 6 é suspeito e 7 ou mais é crítico.
Máquinas bloqueadas: é só escrever o nome da máquina, uma por linha, no arquivo maquinas_bloqueadas.txt. Esse arquivo precisa ser criado na mão.
Máquinas compartilhadas: o programa avisa quando a mesma máquina foi usada por mais de uma pessoa.
Força bruta: ele olha o histórico e alerta quando alguém tem 3 ou mais falhas seguidas.
Relatório de segurança: só para administrador. Mostra o total de acessos, quem mais errou, os horários mais movimentados e quantos acessos foram suspeitos ou críticos.
IA: dá para fazer perguntas sobre os registros de usuários e de acessos. Essa parte fica no arquivo agente.py.
Menu
1. Visualizar usuários
2. Gerenciar usuários
3. Registrar usuário
4. Consultar acessos
5. Alertas de máquinas compartilhadas
6. Relatório de segurança
7. Consultar log de auditoria
8. Acionar detector de força bruta
9. Perguntar à IA
0. Sair
Como rodar

Precisa só do Python instalado. Baixe o repositório, abra a pasta no terminal (o agente.py tem que estar junto do arquivo principal) e rode:

bash
python sentinela.py

O programa usa o comando cls para limpar a tela, que é do Windows. No Linux ou no Mac pode aparecer uma mensagem de erro no começo, mas ele continua funcionando.

Arquivos que o programa cria

Os dados ficam em .txt na mesma pasta do programa.

registrodus.txt: lista de usuários, já com a matrícula censurada
registroda.txt: registro de acessos
registroaud.txt: log de auditoria
ext_nomes_u.txt, ext_matriculas.txt e ext_perfis.txt: guardam os usuários para o programa recarregar quando abrir de novo
ext_cont_falhas.txt e ext_usuarios_bloqueados.txt: guardam as falhas seguidas e os bloqueios
maquinas_bloqueadas.txt: lista de máquinas bloqueadas (criado manualmente)
acessos_permitidos.txt, acessos_negados.txt, ranking_negados.txt e horarios_movimento.txt: criados toda vez que o relatório de segurança é gerado
O que ainda falta melhorar
A senha de administrador (sentinela) está escrita direto no código. É provisória.
As matrículas ficam sem criptografia no ext_matriculas.txt.
Nome com vírgula quebra o carregamento dos dados, porque a vírgula é o separador.
A função classificar_acesso ainda não está ligada ao registro de acessos, então por enquanto o nível de risco é escolhido manualmente em cada chamada.
Editar e excluir usuário atualiza o registrodus.txt, mas não os arquivos ext_*. Ao reiniciar, essas mudanças podem voltar ao que era antes.
Na edição de dados, o programa pede "matrícula" com acento, mas só aceita "matricula" sem acento.
No relatório, os contadores de acessos permitidos e negados aparecem sempre como 0. Os arquivos gerados estão certos, só o número na tela que não.
Quem fez

Bernardo Valença, Felipe Nunes Leal, Guilherme Motta, Guilherme Staundinger, João Vinícius Mendonça e Mateus Mendonça.
