from AnalisadorLexico import *
from action_goto import *
from AnalisadorSemantico import *
import os

prod_gramatica = [
    ['1', "P'", ["P"]],
    ['2', "P", ["inicio", "V", "A"]],
    ['3', "V", ["varinicio", "LV"]],
    ['4', "LV", ["D", "LV"]],
    ['5', "LV", ["varfim", "pt_v"]],
    ['6', "D", ["id", "TIPO", "pt_v"]],
    ['7', "L", ["id", "vir", "L"]],
    ['8', "L", ["id"]],
    ['9', "TIPO", ["inteiro"]],
    ['10', "TIPO", ["real"]],
    ['11', "TIPO", ["literal"]],
    ['12', "A", ["ES", "A"]],
    ['13', "ES", ["leia", "id", "pt_v"]],
    ['14', "ES", ["escreva", "ARG", "pt_v"]],
    ['15', "ARG", ["lit"]],
    ['16', "ARG", ["num"]],
    ['17', "ARG", ["id"]],
    ['18', "A", ["CMD", "A"]],
    ['19', "CMD", ["id", "rcb", "LD", "pt_v"]],
    ['20', "LD", ["OPRD", "opm", "OPRD"]],
    ['21', "LD", ["OPRD"]],
    ['22', "OPRD", ["id"]],
    ['23', "OPRD", ["num"]],
    ['24', "A", ["COND", "A"]],
    ['25', "COND", ["CAB", "CP"]],
    ['26', "CAB", ["se", "ab_p", "EXP_R", "fc_p", "entao"]],
    ['27', "EXP_R", ["OPRD", "opr", "OPRD"]],
    ['28', "CP", ["ES", "CP"]],
    ['29', "CP", ["CMD", "CP"]],
    ['30', "CP", ["COND", "CP"]],
    ['31', "CP", ["fimse"]],
    ['32', "A", ["R", "A"]],
    ['33', "R", ["repita", "ab_p", "EXP_R", "fc_p", "CP_R"]],
    ['34', "CP_R", ["ES", "CP_R"]],
    ['35', "CP_R", ["CMD", "CP_R"]],
    ['36', "CP_R", ["COND", "CP_R"]],
    ['37', "CP_R", ["fimrepita"]],
    ['38', "A", ["fim"]]
]
# [0]Identificação, [1][2]Regra gramatical, [1]->[2]

naoTerminal = ["P'", 'P', 'V', 'A', 'LV', 'D', 'TIPO', 'L', 'ES', 'ARG', 'CMD', 'LD', 'OPRD', 'COND', 'CAB', 'CP',
               'EXP_R', 'CP_R']
terminal = ['inicio', 'varinicio', 'varfim', 'pt_v', 'vir', 'id', 'inteiro', 'real', 'literal', 'leia', 'escreva',
            'lit', 'num', 'rcb', 'opm', 'se', 'entao', 'opr', 'fimse', 'repita', 'fimrepita', 'fim', 'ab_p', 'fc_p',
            '$']


def ERROR_sintatico(estado, classe, linha, coluna):
    if estado == "0":
        if classe != "inicio":  # "Erro: esperado inicio"
            lexema = "inicio"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "2":
        if classe != "varinicio":  # "Erro: esperado varinicio após inicio"
            lexema = "varinicio"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "3" or estado == "6" or estado == "7" or estado == "8" or estado == "9" or estado == "16" or estado == "40" or estado == "41" or estado == "65":
        if classe != "fim":  # "Erro: esperado fim após inicio"
            lexema = "fim"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "4" or estado == "17" or estado == "56":
        if classe != "varfim":  # "Erro: esperado varfim após varinicio"
            lexema = "varfim"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "12":
        if classe != "rcb":  # "Erro: esperado rcb"
            lexema = "<-"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "13" or estado == "34" or estado == "35" or estado == "36" or estado == "37" or estado == "50" or estado == "51" or estado == "52":
        if classe != "fimse":  # "Erro: esperado fimse após se"
            lexema = "fimse"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "14" or estado == '15':
        if classe != "ab_p":  # "Erro: esperado ['(']"
            lexema = "("
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "18" or estado == "28" or estado == "29" or estado == "30" or estado == "31" or estado == "42" or estado == "46" or estado == "62" or estado == "64":
        if classe != "pt_v":  # "Erro: esperado [ ; ]"
            lexema = ";"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "55" or estado == '70':
        if classe != "fc_p":  # "Erro: esperado [')']"
            lexema = ")"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "66" or estado == "67" or estado == "68":
        if classe != "fimrepita":  # "Erro: esperado fimrepita após repita"
            lexema = "fimrepita"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "63":
        if classe != "entao":  # "Erro: esperado entao após se (EXP_R) "
            lexema = "entao"
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha:", linha, "Coluna:", coluna)
            return token

    if estado == "33" or estado == "44" or estado == "45" or estado == "58" or estado == "69" or estado == "71" or estado == "72" or estado == "73" or estado == "74":
        if classe != "fim" and classe != 'fimrepita' and classe != 'fimse':  # "Erro: esperado fim, fimse ou fimrepita"
            lexema = 'fim'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == "27" or estado == "43" or estado == "47" or estado == "48" or estado == "49":
        if classe != "pt_v" and classe != 'vir':  # "Erro: símbolo faltando [; ou ,]"
            lexema = ';'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == "75" or estado == "5" or estado == "23" or estado == "24" or estado == "25" or estado == "26":
        if classe != "eof":  # "Erro: símbolo faltando [$]"
            lexema = 'EOF'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == "54":
        if classe != "opr":  # "Erro: esperado um opr "
            lexema = '>'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == "11":
        if classe != "id" and classe != "lit" and classe != "num":  # "Erro: esperando id,num ou lit"
            lexema = '"erro"'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == "10" or estado == '19' or estado == '20' or estado == '21' or estado == '22' or estado == '57':
        if classe != "id":  # "Erro: esperado id "
            lexema = 'id_qualquer'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token

    if estado == '32' or estado == '38' or estado == '39' or estado == '59' or estado == '61':
        if classe != "id" and classe != "num":  # erro: esperando id ou num
            lexema = 'id_qualquer'
            token = SCANNER(lexema, linha, coluna + len(lexema))
            print("Token inserido.", "Linha: ", linha, "Coluna:", coluna)
            return token
    return


def tERROR_lexico(token):
    # print(token)
    if token[0][0] == 'ERRO0':
        print("Aspas dupas inserido", "Linha:", token[1][-1][0], "Coluna:", token[1][-1][1] + 1)
        token = SCANNER(token[0][1] + '"', token[1][0][0], token[1][0][1])
        return token
    if token[0][0] == 'ERRO1':
        print("Aspas simpes inserido", "Linha:", token[1][-1][0], "Coluna:", token[1][-1][1] + 1)
        token = SCANNER(token[0][1] + "'", token[1][0][0], token[1][0][1])
        return token
    if token[0][0] == 'ERRO2':
        print("Fecha chaves inserido", "Linha:", token[1][-1][0], "Coluna:", token[1][-1][1] + 1)
        token = SCANNER(token[0][1] + '}', token[1][0][0], token[1][0][1])
        return token
    if token[0][0] == 'ERRO4' or token[0][0] == 'ERRO3':
        return 1

    return


def reset_arq():
    try:
        os.remove("codigo_obj.c")
    except:
        pass


def PARSER():
    pilha_sintatica = ["0"]
    qtd_palavras = len(lista_de_palavras)
    cont_p = 0
    a = lista_de_palavras[cont_p]
    token = SCANNER(a[0], a[1], a[2])  # palavra, linha, coluna

    tx = 0
    pilha_semantica = []
    buffer = ""
    erro_semantico = False
    if_erro = False
    indentacao = 1
    
    buffer_repita = []
    
    reset_arq()

    while cont_p <= qtd_palavras:
        # print('pilha sintatica: ',pilhasintatica)
        s = pilha_sintatica[-1]
        while token == None:
            cont_p += 1
            a = lista_de_palavras[cont_p]
            token = SCANNER(a[0], a[1], a[2])  # palavra, linha, coluna
        if (type(token[0]) is str):  # token valido
            # print ("linha:", a[1])
            # print("Classe:",token[0],",","Lexema:",token[1],",","Tipo:",token[2])
            classe = str(token[0]).lower()
            # print('classe', classe)
            if classe in terminal:
                t = action(s, classe)  # t[0]=estado, t[1]=ação
                if t[1] == "Shift":
                    # print("Shift",t[0])
                    pilha_sintatica.append(t[0])
                    cont_p += 1
                    a = lista_de_palavras[cont_p]

                    '''atributos=[token[0], token[1], token[2]]
                    print("atributos:",atributos)'''
                    pilha_semantica.append(token)
                    # print("pilha semantica", pilha_semantica)

                    token = SCANNER(a[0], a[1], a[2])
                elif t[1] == "Reduce":
                    # print("Reduce",t[0])
                    producao = t[0]
                    for regra in prod_gramatica:
                        if producao == regra[0]:  # [0]=identificação, [1]=A, [2]=beta
                            regra_p = regra
                            print("Regra", regra[0], ":", regra[1], "->", regra[2])
                            A = regra[1]
                            for i in regra[2]:
                                pilha_sintatica.pop()
                                # print('pilha_sintatica: ',pilha_sintatica)
                            t = pilha_sintatica[-1]
                    # print('goto',t,A)
                    t = goto(t, A)
                    pilha_sintatica.append(t[0])
                    pilha_semantica, buffer, tx, erro_semantico, indentacao, buffer_repita = AnalisadorSemantico(regra_p, pilha_semantica, buffer, tx, indentacao, buffer_repita)  # pilha_s, buffer_as, tx, indentacao
                    if erro_semantico:
                        print("Erro semântico Linha:", a[1], "Coluna:", a[2] - len(token[1]))
                        if_erro=True

                elif t[1] == "acc":
                    print(prod_gramatica[0][0], ":", prod_gramatica[0][1], "->", prod_gramatica[0][2])
                    if if_erro:
                        reset_arq()
                    return  # fim da análise
                else:
                    print("Erro! Linha:", a[1], "Coluna:", a[2] - len(token[1]))
                    if_erro=True
                    print(t[1])
                    tERROR = ERROR_sintatico(pilha_sintatica[-1], classe, a[1], a[2] - len(token[1]))
                    if (tERROR) == None:
                        print("Fatal Error!")
                        reset_arq()
                        return
                    else:
                        token = tERROR
                        cont_p -= 1
                        # print(token)

        else:
            # print("erro lexico")
            ERROR(token)  # erro lexico
            tERROR = tERROR_lexico(token)
            if_erro=True
            if (tERROR) == None:
                print("Fatal Error!", "Linha:", a[1], "Coluna:", a[2])
                reset_arq()
                return
            elif (type(tERROR) is int):
                cont_p += 1
                a = lista_de_palavras[cont_p]
                token = SCANNER(a[0], a[1], a[2])
            else:
                token = tERROR
                cont_p -= 1
                # print(token)


PARSER()
