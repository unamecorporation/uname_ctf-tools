# Fake Requests
##### Desenvolvedor: Roger Monteiro rmdir
##### Linguagem utilizada: Linguagem Python
##### Versão atual: 1.0.1 - Alpha
##### Licença: GPLv3
##### Ambiente de Teste: Ubuntu 16.10 Kali Linux 2.2 Linux Mint 18.2
### Chamada da ferramenta
>uname@kurupira[~]: python fakeRequests.py
</br>
Fake requests é uma ferramenta que foi desenvolvida com ituito de ajudar na resolução de desafios, nos quais, a flag a ser encontrada está em um local que só pode ser acessado com tal configuração.
Nesta versão está sendo oferecida a possibilidade de usar um user agent fake, de uma lista ou randômico, para acessar um host/página da WEB, que especifique as configurações de entradas aceitas.

### Menu da ferramenta
Ao fazer a chamada da fakeRequests será apresentado a seguinte tela, solicitando uma opção:
<img src="https://github.com/RogerMonteiro124/Python/blob/master/Menu.png"/>

Ao optar pela primeira opção “Usar um UserAgent especifico” será carregada na tela uma lista de possíves user agents que podem ser usados, caso a opção selecionada seja a opção 2 “Usar um user agent randomico”, o user agent usado sera gerado aleatoriamente dentre a lista de users agents possíves. 
Apos selecionar uma das opções, será solicitado o endereço da página que deseja ter acesso às informações.
<img src="https://github.com/RogerMonteiro124/Python/blob/master/host.png"/>

Ao final será exibido todo conteúdo da página, que antes só era acessível através de um determinado host/browser .
### Dependências
* Python 2.7.12 
* Módulo  “fake_useragent” - para fazer esta instalação use o comando:                             “pip install fake-useragent”
### Relatório de bugs:
Link de Download da Ferramenta: https://github.com/RogerMonteiro124/Python/blob/master/fakeRequests.py 
Link de relatório de bugs: https://github.com/RogerMonteiro124/Python/issues
