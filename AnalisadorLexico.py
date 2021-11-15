from collections import namedtuple
letra_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letra_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letras = letra_lower+letra_upper
num = ["1","2","3","4","5","6","7","8","9",'0']
simbolos = [",",".",">","<",";","+","-","*","/","_","(",")","{","}","'", '"', " ","=","\n","\t",'EOF']
alfabeto = letras+num+simbolos
estados = ["s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15", "s16",
           "s17", "s18", "s19", "s20", "s21", "s22", "s23", "s24", "s25", "s26", "s27", "s28", "s29", "s30", "s31",
           "s32", "s33", "s34", "s35", "s36", "s37", "s38", "s39","sErro"]
estados_finais = ["s1","s3","s5","s7","s8","s9","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19","s20","s21","s22","s23","s25","s29","s39","sErro"]
estado_inicial = ["s0"]

special_case=['>=', '<=', '<>', '<-']
split_case=simbolos
split_case.remove(".")
split_case.remove("_")
split_case.remove("{")
split_case.remove("}")

ListaDeErros=[]#só para alguns testes
ListaDeSimbolos=[]
lista_de_palavras=[]#todas as palavras do codigo fonte

Token = namedtuple("Token", "classe lexema tipo")

PalavrasReservadas=["inicio", "varinicio", "varfim", "escreva", "leia", "se", "entao", "fimse", "repita", "fimrepita", "fim", "inteiro", "literal", "real"]
for i in PalavrasReservadas:# add palavras reservadas a tabela de Simbolos
    if i=="inteiro" or i=="literal" or i=="real":
      s=Token(classe=i, lexema=i, tipo=i)
      ListaDeSimbolos.append(s)
    else:
      s=Token(classe=i, lexema=i, tipo="Nulo")
      ListaDeSimbolos.append(s)

#Dado um determinado token verifica se este pertence a tabela de simbolos. Verifica se as classes e lexemas dos tokens são iguais, caso iguais retorna o token. 
def verifica_token_tabSimb(token_gerado):
    for token_lista_simb in ListaDeSimbolos:
        if token_lista_simb[1] == token_gerado[1]:
            return token_lista_simb
    ListaDeSimbolos.append(token_gerado)
    return token_gerado



def gera_token(palavra, estado, if_erro):#recebe lexema e estado final para gerar e classificar token 
    if estado in estados_finais and if_erro == 0:
        if estado == "s1": #Gera token id, verifica se este token está na tab de simbolos. Se estiver na tabela de simbolos retorna o token da tabela de simbolos, caso contrario acrescenta na tabela de simbolos e retorna o token.
            novo_token = Token(classe="id", lexema=palavra, tipo="Nulo")
            token1 = verifica_token_tabSimb(novo_token)
            return token1
        elif estado == "s3" or estado == "s5":
            return Token(classe="Lit", lexema=palavra, tipo="literal")
        elif estado == "s7":
            return Token(classe="Comentário", lexema=palavra, tipo="Nulo")
        elif estado == "s8" or estado == "s9" or estado == "s10" or estado=="s12" or estado == "s13":
            return Token(classe="OPR", lexema=palavra, tipo="Nulo")
        elif estado == "s11":
            return Token(classe="RCB",lexema=palavra,tipo="Nulo")
        elif estado == "s14" or estado == "s15" or estado == "s16" or estado == "s17":
            return Token(classe="OPM", lexema=palavra, tipo="Nulo")
        elif estado == "s18":
            return Token(classe="AB_P", lexema=palavra, tipo="Nulo")
        elif estado == "s19":
            return  Token(classe="FC_P", lexema=palavra, tipo="Nulo")
        elif estado == "s20":
            return Token(classe="PT_V", lexema=palavra, tipo="Nulo")
        elif estado == "s21":
            return Token(classe="VIR", lexema=palavra, tipo="Nulo")
        elif estado == "s23" or estado == "s29":
            return Token(classe="NUM", lexema=palavra, tipo="inteiro")
        elif estado == "s25" or estado == "s39":
            return Token(classe="NUM", lexema=palavra, tipo="real")
    elif estado not in estados_finais and estado == "s2" : #Não fechou aspas duplas
        return Token(classe="ERRO0", lexema=palavra, tipo="Nulo")        
    elif estado not in estados_finais and  estado == "s4": #Não fechou aspas simples
        return Token(classe="ERRO1", lexema=palavra, tipo="Nulo")
    elif estado not in estados_finais and estado == "s6":  #Não fechou comentário
        return Token(classe="ERRO2", lexema=palavra, tipo="Nulo")
    elif estado not in estados_finais:        #Estado Invalido
        return Token(classe="ERRO3", lexema=palavra, tipo="Nulo")
    else: #Erro de caracter invalido no Mgol
        return Token(classe="ERRO4", lexema=palavra, tipo="Nulo")

def funcao_de_transicao(estado, simbolo):#recebe símbolo e estado e faz a transição
  if estado == "s0":
    if simbolo in num:
      return ["s23", "Num"]
    elif simbolo in letras:
      return ["s1", "Identificador"]
    elif simbolo == "'":
      return ["s4", "Literal"]
    elif simbolo == '"':
      return ["s2", "Literal"]
    elif simbolo == "{":
      return ["s6", "Comentário"]
    elif simbolo == "<":
      return ["s8", "OPR"]
    elif simbolo == "=":
      return ["s22", "OPR"]
    elif simbolo == ">":
      return ["s12", "OPR"]
    elif simbolo == "+":
      return ["s14", "OPM"]
    elif simbolo == "-":
      return ["s15", "OPM"]
    elif simbolo == "*":
      return ["s16", "OPM"]
    elif simbolo == "/":
      return ["s17", "OPM"]
    elif simbolo == "(":
      return ["s18", "AB_P"]
    elif simbolo == ")":
      return ["s19", "FC_P"]
    elif simbolo == ";":
      return ["s20", "PT_V"]
    elif simbolo == ",":
      return ["s21", "VIR"]
    elif simbolo == " ":
      return ["s0", "Espaço"]
    elif simbolo == "\n":
      return ["s0", "Quebra de linha"]
    elif simbolo == "\t":
      return ["s0", "Tabulação"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s1":
    if simbolo in letras:
      return ["s1", "id"]
    elif simbolo in num:
      return ["s1", "id"]
    elif simbolo == "_":
      return ["s1", "id"]
    elif simbolo in alfabeto:  
      return ["sErro", "Estado Inválido"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s2":
    if simbolo == '"':
      return ["s3", "Literal"]
    elif simbolo in alfabeto:
      return ["s2", "Literal"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s4":
    if simbolo == "'":
      return ["s5", "Literal"]
    elif simbolo in alfabeto:
      return ["s4", "Literal"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s6":
    if simbolo == "}":
      return ["s7", "Comentario"]
    elif simbolo in alfabeto:
      return ["s6", "Comentario"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s8":
    if simbolo == "-":
      return ["s11", "RCB"]
    elif simbolo == "=":
      return ["s9", "OPR"]
    elif simbolo == ">":
      return ["s10", "OPR"]
    elif simbolo in alfabeto:
      return ["sErro","Estado Inválido"]
    else:
      return ["sErro", "Simbolo Inexistente no alfabeto"]
      

  if estado == "s12":
    if simbolo == "=":
      return ["s13", "OPR"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Inválido"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s23":
    if simbolo in num:
      return ["s23", "NUM"]
    elif simbolo == ".":
      return ["s24", "NUM"]   #real
    elif simbolo == "e":
      return ["s26", "NUM"]
    elif simbolo == "E":
      return ["s30", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s24":
    if simbolo in num:
      return ["s25", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s28":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s30":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo == "+":
      return ["s31", "NUM"]
    elif simbolo == "-":
      return ["s32", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s31":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s25":
    if simbolo in num:
      return ["s25", "NUM"]
    elif simbolo == "e":
      return ["s33", "NUM"]
    elif simbolo == "E":
      return ["s36", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s33":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo == "+":
      return ["s34", "NUM"]
    elif simbolo == "-":
      return ["s35", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s34":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo Inexistente no alfabeto"]

  if estado == "s35":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s29":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s36":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo == "+":
      return ["s37", "NUM"]
    elif simbolo == "-":
      return ["s38", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s27":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s26":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo == "+":
      return ["s27", "NUM"]
    elif simbolo == "-":
      return ["s28", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s32":
    if simbolo in num:
      return ["s29", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s37":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s38":
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro","Simbolo inexistente no alfabeto"]

  if estado == "s39":  #Ultimo Estado final possivel para nº real 
    if simbolo in num:
      return ["s39", "NUM"]
    elif simbolo in alfabeto:
      return ["sErro", "Estado Invalido"]
    else:
      return ["sErro", "Simbolo Inexistente no alfabeto"]
      
  if estado =="sErro":
    return ["sErro", "Palavra contendo erro"]
  if estado == "EOF":
    return ["EOF", "Fim do arquivo"]

def SCANNER(palavra, n_lina, n_coluna_fim):#recebe UMA palavra e a classifica 
  lexema=''
  n_coluna=n_coluna_fim-len(palavra)
  anterior=estado=estado_inicial[0]
  if_erro=0
  erros=[]
  
  if palavra==' ' or palavra=='\n' or palavra=='\t':#não retorna token paras esses símbolos
    #return [palavra,'reconhecido','ignorado']
    return
  if palavra=='EOF':
    novo_Token=Token(classe='$', lexema='EOF', tipo='Nulo')
    return novo_Token
  for simbolo in palavra:
    lexema+=simbolo
    #print(lexema,estado,if_erro)
    n_coluna+=1
    prox=funcao_de_transicao(estado, simbolo)
    anterior=estado
    estado=prox[0]
    if prox[0] == 'sErro':#registra erros
      if_erro=1
      tipo_erro=prox[1]
      erro=[n_lina, n_coluna, tipo_erro]
      erros.append(erro)
      estado=anterior
  if estado in estados_finais and if_erro==0:#token valido
    novo_Token=gera_token(palavra, estado, if_erro)
    if novo_Token[0]=='Comentário':
      return
    return(novo_Token)
  elif (estados in estados_finais)!=True or if_erro==1:#token invalido
    if(estados in estados_finais)!=True and if_erro==0:#gera erro de "abriu e não fechou"
      if_erro=1
      erro=[n_lina, n_coluna_fim, 'expected']
      erros.append(erro)   
    novo_Token=gera_token(palavra, estado, if_erro)
    novo_erro=[novo_Token, erros]
    ListaDeErros.append(novo_erro)
    return(novo_erro)
  return 0

def le_arquivo(nome_arquivo):#lê o arquivo e vai separando em palavras, adiciona todas as palavras em uma lista junto com sua posição
    arquivo = open(nome_arquivo,'r')
    n_linha=1
    palavra=''
    sair=0
    char_prev=''
    for linha in arquivo:
        n_coluna=1
        for simbolo in linha:
            palavra+=simbolo
            if palavra[0]=='"' and sair<2:#registra tudo entre ""
                if simbolo=='"':
                    sair+=1
            elif palavra[0]=="'" and sair<2:#registra tudo entre ''
                if simbolo=="'":
                    sair+=1 
            elif palavra[0]=='{' and sair<2:#registra tudo entre {}
                if simbolo=='}':
                    sair+=2
            elif (char_prev+simbolo) in special_case:#registra os símbolos especiais 
                del(lista_de_palavras[len(lista_de_palavras)-1])
                lista_de_palavras.append([char_prev+simbolo, n_linha, n_coluna])
                char_prev=''
                palavra=''
            elif simbolo in split_case:#quebra as palavras nos caracteres especiais
                char_prev=simbolo
                palavra=palavra[:-1]
                if palavra != '':
                    lista_de_palavras.append([palavra, n_linha, n_coluna-1])
                lista_de_palavras.append([simbolo, n_linha, n_coluna])
                palavra=''
            else:
                sair=0
            n_coluna+=1
        n_linha+=1
    if palavra!='':
      lista_de_palavras.append([palavra, n_linha-1, n_coluna-1])
    lista_de_palavras.append(['EOF', n_linha, n_coluna])
    arquivo.close()
    return 0

def ERROR(novo_erro):#recebe o token de erros junto com a lista de erros e imprime 
  print(novo_erro[0][0],'- ', end="")
  if novo_erro[0][0]=='ERRO0':#Não fechou aspas duplas
    print('Esperado "(fechar aspas dupas), ','Linha:',novo_erro[1][-1][0],', Coluna:',novo_erro[1][-1][1], end="; ")#lista de erros,linha e coluna do ultimo elemento
  elif novo_erro[0][0]=='ERRO1':#Não fechou aspas simples
    print("Esperado '(fechar aspas simpes),",'Linha:',novo_erro[1][-1][0],', Coluna:',novo_erro[1][-1][1], end="; ")
  elif novo_erro[0][0]=='ERRO2':#Não fechou comentário
    print('Esperado }(fecha chaves), ','Linha:',novo_erro[1][-1][0],', Coluna:',novo_erro[1][-1][1], end="; ")
  for i in novo_erro[1]:
    if(i[2]!='expected'):#já foi impresso 
      print(i[2]+', ','Linha:',i[0],', Coluna:',i[1], end="; ")
  print()

le_arquivo('codigo_fonte.txt')

  