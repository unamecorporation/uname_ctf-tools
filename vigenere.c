/*
############################
##Cifra de Vigenere#########
##Developed by rmdir########
##for KurupiraOS <3 :D######
############################
############################

#Sinta-se livre para editar, aprimorar, enxugar(kkk uso muito na fauldade),este codigo.
*/

//Bibliotecas usadas//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <getopt.h>
#include <ctype.h>

//Função para detecção da Plataforma do sistema operacional//
int so(){
	int SO;
	#ifdef __linux__
	SO=0;
	#endif
	#ifdef _WIN32
	SO=1;
	#endif
	return SO;
}
//Funcao para conversao de string para maiuscula e eliminacao de espacos//
char *strupr(char *str)
{
int posW = 0, posR = 0;
  unsigned char *p = (unsigned char *)str;

  while (*p) {
     *p = toupper(*p);
      p++;
  }
     for(posR = 0; posR < strlen(str); posR++) {
        if(str[posR] == ' ')
			continue;
		str[posW] = str[posR];
		posW++;
    }
    str[posW] = '\0';
    return str;
}
//Funcao HELP, mostra as opcoes e modo de uso da Tool//
void help(char *Text) {
    fprintf(stderr, "\n\
    	Usage: %s <options>\n\
           	 \n	Options:\n\
	-h		HELP.\n\
        -t     		TEXT.	(Texto a ser encriptado/decriptado)\n\
        -k 		KEY.	(Chave a ser usada para encriptar/decriptar)\n\
        -e 		ENCRYPT.	(Encriptar)\n\
        -d 		DECRYPT.	(Decriptar)\n\n\
	Example: %s -t \"ATACAR BASE SUL\" -k limao -e\n\n",Text,Text) ;
}
//Funcao Banner Mostra uma ASCII art do nome da TOOl na tela//
void banner(char* Text){
printf("\n	888     888d8b                                                \n	888     888Y8P                                                \n	888     888                                                   \n	Y88b   d88P888 .d88b.  .d88b. 88888b.  .d88b. 888d888 .d88b.  \n	 Y88b d88P 888d88P\"88bd8P  Y8b888 \"88bd8P  Y8b888P\"  d8P  Y8b \n	  Y88o88P  888888  88888888888888  88888888888888    88888888 \n	   Y888P   888Y88b 888Y8b.    888  888Y8b.    888    Y8b.     \n	    Y8P    888 \"Y88888 \"Y8888 888  888 \"Y8888 888     \"Y8888  \n	                   888                                        \n	              Y8b d88P                               KurupiraOS\n	               \"Y88P\"                                         \n");

}
//Funcao que encripta um texto usando a cifra de Vigenere//
void encript(char* Text,char* key){
	int i=0,j,lenText=0,lenkey=0;
	lenText=strlen(Text);
	char TextEncrypted[lenText];
	lenkey=strlen(key);
	char newkey[lenText];
	for(i=0;i<lenText;i++){
		j = i % strlen(key);
        newkey[i] = key[j];
    }
        newkey[lenText] = '\0';
		printf("\n	PALAVRA PURA= %s\n	CHAVE = %s\n",Text,key);
		printf("	TEXTO CIFRADO = ");
	for(i=0;i<lenText;i++){
		TextEncrypted[i]=(Text[i]+newkey[i])%26+65;
	printf("%c",TextEncrypted[i]);}
	printf("\n");
}
//Funcao que decripta um texto usando a cifra de Vigenere//
void decript(char* TextEncrypted,char* key){
    int lenTextEncrypted=strlen(TextEncrypted);
	char Text[lenTextEncrypted];
    char newkey[lenTextEncrypted];
	int h,i,j;
    for (i=0;i<strlen(TextEncrypted);i++){
		j=i%strlen(key);
		newkey[i]=key[j];
    }
    printf("\n	PALAVRA CIFRADA= %s\n	CHAVE = %s\n",TextEncrypted,key);
	printf("	TEXTO DESCIFRADO = ");
    for(i=0;i<lenTextEncrypted;i++){
		Text[i]=(TextEncrypted[i]-newkey[i]+26)%26+65;
		printf("%c",Text[i]);
	}
	printf("\n");
}
//Funcao principal//
int main(int argc, char **argv){
	if(so()==0){//Se a plataforma for linux uso o comando para mudar a cor do terminal//
		system("setterm -foreground green");
	}else if(so()==1){// Se windows uso o color para mudar a cor do cmd//
		system("color 02");
	}
	 int opt,i,aux;
	 int flag=0;
	 char* Text=NULL;
	 char* key=NULL;
	  const struct option stopcoes[] = {
        {"help",	no_argument,		0,	'h'},
        {"Text",	required_argument,	0,	't'},
        {"key",		required_argument,	0,	'k'},
        {"Encript",	no_argument,		0,	'e'},
        {"Decript",	no_argument,		0,	'd'},
        {0,			0,					0,	  0},
    } ;
    if ( argc < 3 ){//Se nao houver argumento suficiente chamo banner e menu//
	banner(argv[0]);
	help(argv[0]);
	}
    while( (opt = getopt_long(argc, argv, ":ht:k:ed", stopcoes, NULL)) >0) {
        switch ( opt ) {
            case'h':
                banner(argv[0]);
                help(argv[0]) ;
                break ;
            case 't':
            	flag++;
                Text = strupr(optarg);
				break ;
            case 'k':
            flag++;
                key = strupr(optarg) ;
				break ;
            case 'e':
				flag++;
                if(flag==3){
            		encript(Text,key);
				}
				break ;
				exit(1);
            case 'd':
				flag++;
                if(flag==3){
            		decript(Text,key);
				}
                break ;
                exit(1);
            default:
                fprintf(stderr, "Opcao invalida ou faltando argumento: '%c'\n", optopt) ;
                return -1 ;
        }
    }
	return 0;
}
