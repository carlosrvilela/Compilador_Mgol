import os
from AnalisadorLexico import *


# from AnalisadorSintatico import *

def write_arq(buffer):
    open("codigo_obj.c", "a").write(buffer)
    return


def AnalisadorSemantico(regra, pilha_s, buffer_as, tx, indentacao, buffer_repita):
    erro = False
    #print(pilha_s)

    if regra[0] == "2":
        header = "#include<stdio.h> \ntypedef char literal[256]; \nvoid main() { \n\t /*----Variáveis " \
                 "Temporárias----*/ \n"
        for x in range(tx):
            header += "{}int T{}; \n".format(indentacao * '\t', x)
        header += "{}/*-----------------------------*/ \n".format(indentacao * "\t")
        buffer_final = header + buffer_as + "}"
        write_arq(buffer_final)

    elif regra[0] == "4":
        # LV -> D, LV
        if pilha_s[-2][1] == "varinicio":
            LV = Token("LV", pilha_s[-1][1], pilha_s[-1][2])
            pilha_s.pop()
            pilha_s.append(LV)
        else:
            topo = pilha_s[-1]
            for i in regra[2]:
                pilha_s.pop()
            pilha_s.append(topo)

    elif regra[0] == "5":
        #print("Imprimir três linhas brancas no arquivo")
        # LV -> varfim pt_v
        buffer_as += "\n \n \n"
        for i in regra[2]:
            pilha_s.pop()
        # LV = Token(classe="varfim", lexema="LV", tipo="varfim")
        # pilha_s.append(LV)

    elif regra[0] == "6":
        # print(D→ TIPO L pt_v)
        # TIPO.tipo = L.tipo
        # D.tipo = Tipo.tipo e D.lexema = L.lexema
        # Atualiza Tabela de simbolos com o novo L.tipo

        buffer_as += ";"
        Dnovo = Token(classe="id", lexema=pilha_s[-2][1], tipo=pilha_s[-3][2])

        for i in range(len(pilha_s) - 1, 0, -1):
            if pilha_s[i][0] == "TIPO":
                posicao = i

                tipo = pilha_s[posicao][2]
                break

        for t in range(posicao, len(pilha_s) - 1, 1):

            if pilha_s[t][0] == "id" and pilha_s[t][2] == "Nulo":
                temp = pilha_s[t]
                pilha_s.remove(pilha_s[t])
                Dnovo = Token(classe="id", lexema=temp[1], tipo=pilha_s[posicao][2])
                pilha_s.insert(t, Dnovo)

                for token_lista_simb in ListaDeSimbolos:
                    if token_lista_simb[1] == Dnovo[1]:
                        if token_lista_simb[2] == "Nulo":
                            ListaDeSimbolos.remove(token_lista_simb)
                            ListaDeSimbolos.append(Dnovo)
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(Dnovo)

    elif regra[0] == "7":
        # L -> id vir L

        # L.tipo = id.tipo
        # L.lexema = id.lexema vir.lexema id.lexema
        buffer_as += "{} {}".format(pilha_s[-2][1], pilha_s[-3][1])

        L = Token(classe="id", lexema=pilha_s[-1][1], tipo=pilha_s[-3][2])
        Id = Token("id", pilha_s[-3][1], pilha_s[-3][2])

        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(Id)
        pilha_s.append(L)


    elif regra[0] == "8":
        # L -> id
        # L.lexema = id.lexema
        # L.tipo = id.tipo
        buffer_as += " {}".format(pilha_s[-1][1])
        L = Token(classe="id", lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
        # ListaDeSimbolos.pop()
        for token_lista_simb in ListaDeSimbolos:
            if token_lista_simb[1] == L[1]:
                ListaDeSimbolos.remove(token_lista_simb)
                ListaDeSimbolos.append(L)

        if L not in ListaDeSimbolos:
            ListaDeSimbolos.append(L)

        pilha_s.pop()
        pilha_s.append(L)

    elif regra[0] == "9":
        # Tipo.tipo = inteiro.tipo
        TIPO = Token(classe="TIPO", lexema="Tipo", tipo="inteiro")
        buffer_as += "\n{}int".format(indentacao * "\t")
        pilha_s.pop()
        pilha_s.append(TIPO)

    elif regra[0] == "10":
        # Tipo.tipo = real.tipo
        TIPO = Token(classe="TIPO", lexema="tipo", tipo=pilha_s[-1][2])
        buffer_as += "\n{}double".format(indentacao * "\t")
        pilha_s.pop()
        pilha_s.append(TIPO)

    elif regra[0] == "11":
        # Tipo.tipo = literal.tipo
        TIPO = Token(classe="TIPO", lexema="tipo", tipo=pilha_s[-1][2])
        buffer_as += "\n{}literal".format(indentacao * "\t")
        pilha_s.pop()
        pilha_s.append(TIPO)

    elif regra[0] == "13":
        # ES -> leia id pt_v
        if pilha_s[-2][2] != "Nulo":
            if pilha_s[-2][2] == "literal":
                buffer_as += '{}scanf("%s",&{}){} \n'.format(indentacao * "\t", pilha_s[-2][1], pilha_s[-1][1])
                for i in regra[2]:
                    pilha_s.pop()
                ES = Token(classe="ES", lexema="ES", tipo="")
                pilha_s.append(ES)
            elif pilha_s[-2][2] == "inteiro":
                buffer_as += '{}scanf("%d",&{}){} \n'.format(indentacao * "\t", pilha_s[-2][1], pilha_s[-1][1])
                for i in regra[2]:
                    pilha_s.pop()
                ES = Token(classe="ES", lexema="ES", tipo="")
                pilha_s.append(ES)
            elif pilha_s[-2][2] == "real":
                buffer_as += '{}scanf("%f",&{}){} \n'.format(indentacao * "\t", pilha_s[-2][1], pilha_s[-1][1])
                for i in regra[2]:
                    pilha_s.pop()
                ES = Token(classe="ES", lexema="ES", tipo="")
                pilha_s.append(ES)
        else:
            erro = True
            print("Erro1! Variável não declarada")

    elif regra[0] == "14":
        # ES -> escreva ARG pt_v
        if pilha_s[-2][2] == "real":
            buffer_as += '{}printf("%lf", {});\n'.format(indentacao * "\t", pilha_s[-2][1])
        elif pilha_s[-2][2] == "inteiro":
            buffer_as += '{}printf("%d", {});\n'.format(indentacao * "\t", pilha_s[-2][1])
        elif pilha_s[-2][2] == "literal" and pilha_s[-2][0] == "id":
            buffer_as += '{}printf("%s", {});\n'.format(indentacao * "\t", pilha_s[-2][1])
        else:
            buffer_as += '{}printf({});\n'.format(indentacao * "\t", pilha_s[-2][1])
        ES = Token(classe="ES", lexema=pilha_s[-2][1], tipo=pilha_s[-2][2])
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(ES)

    elif regra[0] == "15":
        # ARG -> lit
        ARG = Token(classe='lit', lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
        pilha_s.pop()
        pilha_s.append(ARG)

    elif regra[0] == "16":
        # ARG -> num
        ARG = Token(classe=pilha_s[-1][0], lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
        pilha_s.pop()
        pilha_s.append(ARG)

    elif regra[0] == "17":
        # ARG -> id
        if pilha_s[-1][2] != "Nulo":
            ARG = Token(classe=pilha_s[-1][0], lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
            pilha_s.pop()
            pilha_s.append(ARG)
        else:
            erro = True
            print("Erro2! Variável não declarada")

    elif regra[0] == "19":
        # CMD -> id rcb LD pt_v

        if pilha_s[-4][2] != "Nulo":

            if pilha_s[-4][2] == pilha_s[-2][2]:
                buffer_as += "{}{} = {};\n".format(indentacao * "\t", pilha_s[-4][1], pilha_s[-2][1])
                #print("##CMD -> id rcb LD pt_v###", pilha_s[-2], pilha_s[-4])
                CMD = Token(classe="CMD", lexema="", tipo="")
                for i in regra[2]:
                    pilha_s.pop()
                pilha_s.append(CMD)

            else:
                erro = True
                print("Erro4! Variavel não declarada")

        else:
            erro = True
            print("Erro3 ! Variavel nao declarada")

    elif regra[0] == "20":
        # LD -> OPRD opm OPRD
        # print(pilha_s[-1], pilha_s[-3])
        if pilha_s[-1][2] == pilha_s[-3][2] and pilha_s[-1][2] != "literal":

            buffer_as += "{}T{} = {} {} {}; \n".format(indentacao * "\t", tx, pilha_s[-3][1], pilha_s[-2][1], pilha_s[-1][1])

            LD = Token(classe="LD", lexema="T{}".format(tx), tipo=pilha_s[-1][2])
            tx += 1
            for i in regra[2]:
                pilha_s.pop()
            pilha_s.append(LD)
        else:
            erro = True
            print("Erro5 !Operandos incompatíveis")

    elif regra[0] == "21":
        # LD -> OPRD
        LD = Token(classe=pilha_s[-1][0], lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
        pilha_s.pop()
        pilha_s.append(LD)

    elif regra[0] == "22":
        # OPRD -> id
        if pilha_s[-1][2] != "Nulo":
            OPRD = Token(classe=pilha_s[-1][0], lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
            pilha_s.pop()
            pilha_s.append(OPRD)
        else:
            erro = True
            print("Erro 6! Variavel não declarada")

    elif regra[0] == "23":
        # OPRD -> num
        OPRD = Token(classe=pilha_s[-1][0], lexema=pilha_s[-1][1], tipo=pilha_s[-1][2])
        pilha_s.pop()
        pilha_s.append(OPRD)

    elif regra[0] == "25":
        # COND -> CAB CP
        indentacao-=1
        buffer_as += "{}".format(indentacao * "\t") + "}\n"
        
        COND = Token("COND", "COND", "")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(COND)
        
    elif regra[0] == "26":
        # CAB -> se ab_p EXP_R fc_p então
        #buffer_as += '{}if({})'.format(indentacao * "\t", pilha_s[-3][1]) + "{\n"
        buffer_as += '{}if(T{})'.format(indentacao * "\t", tx-1) + "{\n"
        indentacao+=1
        CAB = Token("CAB", lexema=pilha_s[-3][1], tipo="")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(CAB)

    elif regra[0] == "27":
        # EXP_R -> OPRD opr OPRD
        if pilha_s[-1][2] == pilha_s[-3][2]:

            buffer_as += "{}T{} = {} {} {}; \n".format(indentacao * "\t", tx, pilha_s[-3][1], pilha_s[-2][1], pilha_s[-1][1])
            tx += 1
            lexema = pilha_s[-3][1] + pilha_s[-2][1] + pilha_s[-1][1]
            EXP_R = Token(classe="EXP_R", lexema=lexema, tipo="")
            for i in regra[2]:
                pilha_s.pop()
            pilha_s.append(EXP_R)

    elif regra[0] == "33":
        #indentacao+=1
        # R -> repita ab_p EXP_R fc_p CP_R
        temp = "{"
        buffer_as += '\n{}while({}){} \n'.format(indentacao * "\t", pilha_s[-3][1], temp)
        for i in range(len(buffer_repita)-1, 0, -1):
            buffer_as +=buffer_repita[i]
        buffer_as += '{}'.format(indentacao * "\t")+"}\n"
        buffer_repita=[]
        R = Token("R", lexema=pilha_s[-3][1], tipo="repita")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(R)

    elif regra[0] == "34":
        #CP_R→ ES CP_R
        buffer_repita.append('{}printf({});\n'.format(indentacao * "\t", pilha_s[-2][1]))
        #print("##CP_R→ ES CP_R###", pilha_s[-1])
        CP_R = Token("CP_R", lexema=pilha_s[-1][1], tipo="repita")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(CP_R)

    elif regra[0] == "35":
        #CP_R→ CMD CP_R
        buffer_repita.append('{}printf({});\n'.format(indentacao * "\t", pilha_s[-2][1]))
        #print("##CP_R→ CMD CP_R###", pilha_s[-1])
        CP_R = Token("CP_R", lexema=pilha_s[-1][1], tipo="repita")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(CP_R)       

    elif regra[0] == "36":
        #CP_R→ COND CP_R
        buffer_repita.append('{}printf({});\n'.format(indentacao * "\t", pilha_s[-2][1]))
        #print("##CP_R→ COND CP_R###", pilha_s[-1])
        CP_R = Token("CP_R", lexema=pilha_s[-1][1], tipo="repita")
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(CP_R)  

    elif regra[0] == "37":
        # CP_R -> fimrepita
        temp = "}"
        buffer_repita.append("\t{}{}".format(indentacao * "\t", temp))
        CP_R = Token(classe="CP_R", lexema=pilha_s[-1][1], tipo="repita")
        pilha_s.pop()
        pilha_s.append(CP_R)

    else:
        topo = pilha_s[-1]
        for i in regra[2]:
            pilha_s.pop()
        pilha_s.append(topo)
    # print(ListaDeSimbolos)
    return pilha_s, buffer_as, tx, erro, indentacao, buffer_repita
