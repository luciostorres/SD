# Sistemas Distribuídos

#O teste é dividido em Servidor, Cliente e Servidor diretório tendo também um arquivo de constante onde mantem-se os valores para o ip e a porta de conexão do servidor diretório.

#No arquivo server.py, primeiramente é feita a conexão ao servidor tiretório e depois obtem-se o IP da maquina onde esta em excecução e é iniciado o servidor;

#No directory-server.py, é registrado o nome e é feito o Lookup para então iniciar também o servidor.

#Obs.: Implementação futura: Tratamento da verificação de se o nome de servidor já existe e se o Lookup foi feito para o um nome existente;

#No cliente.server, é feita a conexão ao servidor e feito um Lookup para a Lista. Após ter o IP e numero da porta do servidor, resta somente fazer a conexão.

#Para teste foi feito chamadas RPC para a aplicação do servidor.