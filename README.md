# santander_cybersec_ramsonware_keylogger

Construí o primeito desafio do ramsonware usando o vscode com python instalado e seguindo as instruções das aulas. Comecei no arquivo importando a biblioteca do Fernet que foi usada para gerar a chave de criptografia, em seguida a biblioteca os do sistema operacional para abrir e ler arquivos, e daí em diante criei as funções a serem usadas. As funções foram basicamente 5 delas, não incluindo a função main. Coloquei todos os arquivos dentro de uma pasta, e dentro dessa pasta fiz uma subpasta com os arquivos que seriam criptografados, o "dados confidenciais.txt" e "senhas.txt". Ao rodar o arqvuivo ramsonware.py, esses dois arquivos com seus conteúdos originais foram criptografados. 

Em seguida construí o código para descriptografar os arquivos recém criptografados pelo malware. Esse arquivo é mais simples, levando apenas 3 funções excluindo a main, e ao executá-lo, os dois arquivos criptografados voltam ao seu estado original. 
