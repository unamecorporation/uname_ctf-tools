#CTF Tools
<h2>Agradecimentos especiais para:</h2>
<h3><a href="https://github.com/JesusFromHellz">Jesus</a></h3>
<h3><a href="https://github.com/zero10101">Zero</a></h3>
<h3><a href="https://github.com/ninj4c0d3r">D.K.R</a></h3>
<h3><a href="https://github.com/B4nned">B4nned</a></h3>
<h3><a href="https://github.com/RogerMonteiro124">rmdir</a></h3>

<hr>

<h2>CTF Tools, por Uname Team</h2>
<h5>Repositório disponível para ferramentas de CTF, em breve, mais novidades</h5>

<hr>

<h3>Fique de olho em <a href="https://www.facebook.com/unamecorporation">UnameCorp</a>, por que o futuro não pode ser nomeado</h3>

<hr>

<p>
  Lista de ferramentas disponíveis
  <ul>
    <li>
      1337:
      <ul>
        <li>
          Ferramenta de LeetCode, para cifrar e traduzir leet em  3 modos, básico, avançado 1 e 2.
          Conta também com um menu de dicionrio de possibilidades em LeetCode.
          <blockquote>
            -a | --advanced: gera um leetcode robusto, envolvendo meta caracteres<br>
            -b | --basic: gera um leetcode básico, apenas substituição letra=>número<br>
            -d | --dict: apresenta um dicionário de leetcode(pode não conter todas as referências).<br>
            -t | --translate: gera uma possível tradução para o leet informado<br>
            -h | --help: vai te ajudar a entender isso<br>
          </blockquote>
        </li>
      </ul>
    </li>
    
    <li>
      asciiconv
      <ul>
        <li>
          Programa para conversão de base decimal(ASCII) para texto, texto para ASCII, ASCII para binário e decimal.
          <blockquote>
            -h | --help: Chama esse menu de ajuda<br>
            -a | --ascii: Converte de Texto para ASCII<br>
            -b | --bin: Converte de Decimal para Binário<br>
            -c | --code: Converte de Texto para Binário<br>
            -t | --txt: Converrte de ASCII para Texto   <br>
          </blockquote>
        </li>
      </ul>
    </li>
    
    <li>  
      Caesarcyf
      <ul>
        <li>
          Fork de VandalVNL: <a href="https://github.com/vandalvnl/cesarcyf">cesarcyf</a>.
          desenvolvida para o projeto Uname CTF Team.
          <blockquote>
            ./caesarcyf "string informada" -1<br>
            -a | --all: Informa todas as possibilidades alfabéticas<br>
            -n(n == número de 1 a 25): informa a string em passos numéricos referentes a "n"<br>
          </blockquote>
        </li>
      </ul>
    </li>
    
    <li>
      Charcount
      <ul>
        Contador de caracteres em uma string informada, retornando o IC(kappa) da string, auxiliando
        em identificações de padrões de criptografia de cifras mono/polialfabéticas.
        <li>
          <blockquote>
            Não possui parâmetros, apenas informar a string entre aspas duplas.
          </blockquote>
        </li>
      </ul>
    </li>
    
    <li>
      Codemorse
      <ul>
        Cifra e decifra um código morse de acordo com a string informada, através dos parâmetros informados.
        <li>
          <blockquote>
            -h or --help:\tChama esse menu de ajuda<br>
            -c or --cypher:\tEncripta com código morse<br>
            -d or --decode:\tDecripta o código morse<br>
            ./morsecoder -c 'frase para morse'<br>
            ./morsecoder -d '..- -----'<br>
          </blockquote>
        </li>
      </ul>
    </li>
    
    <li>
      vigenere
      <ul>
        Cifra e decifra uma string de acordo com a cifra de Vigenere. É necessário informar uma chave para criptar ou decriptar a string que foi informada.
        <li>
          <blockquote>
              -h		HELP.
              -t     		TEXT.	(Texto a ser encriptado/decriptado)<br>
              -k 		KEY.	(Chave a ser usada para encriptar/decriptar)<br>
              -e 		ENCRYPT.	(Encriptar)<br>
              -d 		DECRYPT.	(Decriptar)<br>
	            Example: ./vigenere -t "ATACAR BASE SUL" -k limao -e<br><br>
              <hr>
              Para executar um código C em Linux, você precisa primeiro compilar utilizando o GCC:
              <code>
                gcc vigenere.c -o vigenere<br>
                ../vigenere -t "ATACAR BASE SUL" -k limao -e
              </code>
          </blockquote>
        </li>
      </ul>
    </li>
    
  </ul>
 </p>
