def action(estado, classe):
    if estado == "0":
        if classe == "inicio":
            return ["2", "Shift"]
        else:
            return ["NULL", "Erro: esperado inicio"]

    if estado == "1":
        if classe == "$":
            return ["0", "acc"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "2":
        if classe == "varinicio":
            return ["4", "Shift"]
        else:
            return ["NULL", "Erro: esperado varinicio após inicio"]

    if estado == "3":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "repita":
            return ["14", "Shift"]
        elif classe == "fim":
            return ["75", "Shift"]
        else:
            return ["NULL", "Erro: esperado [leia, id, escreva,se, repita,fim]"]

    if estado == "4":
        if classe == "varfim":
            return ["18", "Shift"]
        elif classe == "inteiro":
            return ["20", "Shift"]
        elif classe == "real":
            return ["21", "Shift"]
        elif classe == "literal":
            return ["22", "Shift"]
        else:
            return ["NULL", "Erro: esperado [varfim,inteiro, real, literal]"]

    if estado == "5":
        if classe == "$":
            return ["2", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "6":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "repita":
            return ["14", "Shift"]
        elif classe == "fim":
            return ["75", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "7":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "repita":
            return ["14", "Shift"]
        elif classe == "fim":
            return ["75", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "8":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "repita":
            return ["14", "Shift"]
        elif classe == "fim":
            return ["75", "Shift"]
        else:
            return ["NULL","Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "9":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "repita":
            return ["14", "Shift"]
        elif classe == "fim":
            return ["75", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "10":
        if classe == "id":
            return ["27", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id]"]

    if estado == "11":
        if classe == "id":
            return ["31", "Shift"]
        elif classe == "lit":
            return ["29", "Shift"]
        elif classe == "num":
            return ["30", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,lit,num]"]

    if estado == "12":
        if classe == "rcb":
            return ["32", "Shift"]
        else:
            return ["NULL", "Erro: esperado sinal rcb"]

    if estado == "13":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimse":
            return ["37", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id, leia, escreva, se, fimse]"]

    if estado == "14":
        if classe == "ab_p":
            return ["38", "Shift"]
        else:
            return ["NULL", "Erro: esperado ['(']"]

    if estado == "15":
        if classe == "ab_p":
            return ["39", "Shift"]
        else:
            return ["NULL", "Erro: esperado ['(']"]

    if estado == "16":
        if classe == "id":
            return ["3", "Reduce"]
        elif classe == "leia":
            return ["3", "Reduce"]
        elif classe == "escreva":
            return ["3", "Reduce"]
        elif classe == "se":
            return ["3", "Reduce"]
        elif classe == "fim":
            return ["3", "Reduce"]
        elif classe == "repita":
            return ["3", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fim]"]

    if estado == "17":
        if classe == "varfim":
            return ["18", "Shift"]
        elif classe == "inteiro":
            return ["20", "Shift"]
        elif classe == "real":
            return ["21", "Shift"]
        elif classe == "literal":
            return ["22", "Shift"]
        else:
            return ["NULL", "Erro: esperado [varfim, inteiro, real, literal]"]

    if estado == "18":
        if classe == "pt_v":
            return ["41", "Shift"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "19":
        if classe == "id":
            return ["43", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id] "]

    if estado == "20":
        if classe == "id":
            return ["9", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id]"]

    if estado == "21":
        if classe == "id":
            return ["10", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id]"]

    if estado == "22":
        if classe == "id":
            return ["11", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id]"]

    if estado == "23":
        if classe == "$":
            return ["12", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "24":
        if classe == "$":
            return ["18", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "25":
        if classe == "$":
            return ["24", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "26":
        if classe == "$":
            return ["12", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

    if estado == "27":
        if classe == "pt_v":
            return ["44", "Shift"]
        elif classe == "$":
            return ['18', 'Reduce']
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "28":
        if classe == "pt_v":
            return ["45", "Shift"]
        elif classe == "$":
            return ['24', 'Reduce']
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "29":
        if classe == "pt_v":
            return ["15", "Reduce"]
        elif classe == "$":
            return ['32', 'Reduce']
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "30":
        if classe == "pt_v":
            return ["16", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "31":
        if classe == "pt_v":
            return ["17", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "32":
        if classe == "id":
            return ["48", "Shift"]
        elif classe == "num":
            return ["49", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id, num]"]

    if estado == "33":
        if classe == "id":
            return ["25", "Reduce"]
        elif classe == "leia":
            return ["25", "Reduce"]
        elif classe == "escreva":
            return ["25", "Reduce"]
        elif classe == "se":
            return ["25", "Reduce"]
        elif classe == "fimse":
            return ["25", "Reduce"]
        elif classe == "repita":
            return ["25", "Reduce"]
        elif classe == "fimrepita":
            return ["25", "Reduce"]
        elif classe == "fim":
            return ["25", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse,repita,fimrepita,fim]"]

    if estado == "34":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimse":
            return ["37", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "35":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimse":
            return ["37", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia, escreva, se,fimse] "]

    if estado == "36":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimse":
            return ["37", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "37":
        if classe == "id":
            return ["31", "Reduce"]
        elif classe == "leia":
            return ["31", "Reduce"]
        elif classe == "escreva":
            return ["31", "Reduce"]
        elif classe == "se":
            return ["31", "Reduce"]
        elif classe == "fimse":
            return ["31", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "38":
        if classe == "id":
            return ["48", "Shift"]
        elif classe == "num":
            return ["49", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,num]"]

    if estado == "39":
        if classe == "id":
            return ["48", "Shift"]
        elif classe == "num":
            return ["49", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,num]"]

    if estado == "40":
        if classe == "id":
            return ["4", "Reduce"]
        elif classe == "leia":
            return ["4", "Reduce"]
        elif classe == "escreva":
            return ["4", "Reduce"]
        elif classe == "se":
            return ["4", "Reduce"]
        elif classe == "repita":
            return ["4", "Reduce"]
        elif classe == "fim":
            return ["4", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "41":
        if classe == "id":
            return ["5", "Reduce"]
        elif classe == "leia":
            return ["5", "Reduce"]
        elif classe == "escreva":
            return ["5", "Reduce"]
        elif classe == "se":
            return ["5", "Reduce"]
        elif classe == "repita":
            return ["5", "Reduce"]
        elif classe == "fim":
            return ["5", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id, leia, escreva, se, repita, fim]"]

    if estado == "42":
        if classe == "pt_v":
            return ["56", "Shift"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "43":
        if classe == "pt_v":
            return ["8", "Reduce"]
        elif classe == "vir":
            return ["57", "Shift"]
        else:
            return ["NULL", "Erro: esperado [';'  ',']"]

    if estado == "44":
        if classe == "id":
            return ["13", "Reduce"]
        elif classe == "leia":
            return ["13", "Reduce"]
        elif classe == "escreva":
            return ["13", "Reduce"]
        elif classe == "se":
            return ["13", "Reduce"]
        elif classe == "fimse":
            return ["13", "Reduce"]
        elif classe == "repita":
            return ["13", "Reduce"]
        elif classe == "fimrepita":
            return ["13", "Reduce"]
        elif classe == "fim":
            return ["13", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse,repita,fimrepita,fim]"]

    if estado == "45":
        if classe == "id":
            return ["14", "Reduce"]
        elif classe == "leia":
            return ["14", "Reduce"]
        elif classe == "escreva":
            return ["14", "Reduce"]
        elif classe == "se":
            return ["14", "Reduce"]
        elif classe == "fimse":
            return ["14", "Reduce"]
        elif classe == "repita":
            return ["14", "Reduce"]
        elif classe == "fimrepita":
            return ["14", "Reduce"]
        elif classe == "fim":
            return ["14", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse,repita,fimrepita,fim]"]

    if estado == "46":
        if classe == "pt_v":
            return ["58", "Shift"]
        else:
            return ["NULL", "Erro: esperado [ ; ] "]

    if estado == "47":
        if classe == "pt_v":
            return ["21", "Reduce"]
        elif classe == "opm":
            return ["59", "Shift"]
        else:
            return ["NULL", "Erro: esperado ['; , opm']"]

    if estado == "48":
        if classe == "opr":
            return ["22", "Reduce"]
        elif classe == "opm":
            return ["22", "Reduce"]
        elif classe == "pt_v":
            return ["22", "Reduce"]
        elif classe == "fc_p":
            return ["22", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [opr,opm,se,pt_v,fc_p]"]

    if estado == "49":
        if classe == "opr":
            return ["23", "Reduce"]
        elif classe == "opm":
            return ["23", "Reduce"]
        elif classe == "pt_v":
            return ["23", "Reduce"]
        elif classe == "fc_p":
            return ["23", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [opr,opm,se,pt_v,fc_p]"]

    if estado == "50":
        if classe == "id":
            return ["28", "Reduce"]
        elif classe == "leia":
            return ["28", "Reduce"]
        elif classe == "escreva":
            return ["28", "Reduce"]
        elif classe == "se":
            return ["28", "Reduce"]
        elif classe == "fimse":
            return ["28", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "51":
        if classe == "id":
            return ["29", "Reduce"]
        elif classe == "leia":
            return ["29", "Reduce"]
        elif classe == "escreva":
            return ["29", "Reduce"]
        elif classe == "se":
            return ["29", "Reduce"]
        elif classe == "fimse":
            return ["29", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "52":
        if classe == "id":
            return ["30", "Reduce"]
        elif classe == "leia":
            return ["30", "Reduce"]
        elif classe == "escreva":
            return ["30", "Reduce"]
        elif classe == "se":
            return ["30", "Reduce"]
        elif classe == "fimse":
            return ["30", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse]"]

    if estado == "53":
        if classe == "fc_p":
            return ["60", "Shift"]
        else:
            return ["NULL", "Erro: esperado [')']"]

    if estado == "54":
        if classe == "opr":
            return ["61", "Shift"]
        else:
            return ["NULL", "Erro: esperado [opr]"]

    if estado == "55":
        if classe == "fc_p":
            return ["63", "Shift"]
        else:
            return ["NULL", "Erro: esperado [')']"]

    if estado == "56":
        if classe == "varfim":
            return ["6", "Reduce"]
        elif classe == "inteiro":
            return ["6", "Reduce"]
        elif classe == "real":
            return ["6", "Reduce"]
        elif classe == "literal":
            return ["6", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [varfim,inteiro,real,literal]"]

    if estado == "57":
        if classe == "id":
            return ["43", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id]"]

    if estado == "58":
        if classe == "id":
            return ["19", "Reduce"]
        elif classe == "leia":
            return ["19", "Reduce"]
        elif classe == "escreva":
            return ["19", "Reduce"]
        elif classe == "se":
            return ["19", "Reduce"]
        elif classe == "fimse":
            return ["19", "Reduce"]
        elif classe == "repita":
            return ["19", "Reduce"]
        elif classe == "fimrepita":
            return ["19", "Reduce"]
        elif classe == "fim":
            return ["19", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse,repita,fimrepita,fim]"]

    if estado == "59":
        if classe == "id":
            return ["48", "Shift"]
        elif classe == "num":
            return ["49", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,num]"]

    if estado == "60":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimrepita":
            return ["69", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimrepita]"]

    if estado == "61":
        if classe == "id":
            return ["48", "Shift"]
        elif classe == "num":
            return ["49", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,num]"]

    if estado == "62":
        if classe == "pt_v":
            return ["7", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "63":
        if classe == "entao":
            return ["71", "Shift"]
        else:
            return ["NULL", "Erro: esperado [entao]"]

    if estado == "64":
        if classe == "pt_v":
            return ["20", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [;]"]

    if estado == "65":
        if classe == "id":
            return ["33", "Reduce"]
        elif classe == "leia":
            return ["33", "Reduce"]
        elif classe == "escreva":
            return ["33", "Reduce"]
        elif classe == "se":
            return ["33", "Reduce"]
        elif classe == "repita":
            return ["33", "Reduce"]
        elif classe == "fim":
            return ["33", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim]"]

    if estado == "66":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimrepita":
            return ["69", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimrepita]"]

    if estado == "67":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimrepita":
            return ["69", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimrepita]"]

    if estado == "68":
        if classe == "id":
            return ["12", "Shift"]
        elif classe == "leia":
            return ["10", "Shift"]
        elif classe == "escreva":
            return ["11", "Shift"]
        elif classe == "se":
            return ["15", "Shift"]
        elif classe == "fimrepita":
            return ["69", "Shift"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimrepita]"]

    if estado == "69":
        if classe == "id":
            return ["37", "Reduce"]
        elif classe == "leia":
            return ["37", "Reduce"]
        elif classe == "escreva":
            return ["37", "Reduce"]
        elif classe == "se":
            return ["37", "Reduce"]
        elif classe == "repita":
            return ["37", "Reduce"]
        elif classe == "fim":
            return ["37", "Reduce"]
        elif classe == "fimse":
            return ["37", "Reduce"]
        elif classe == "fimrepita":
            return ["37", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim,fimse,fimrepita]"]

    if estado == "70":
        if classe == "fc_p":
            return ["27", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [ ; ]"]

    if estado == "71":
        if classe == "id":
            return ["26", "Reduce"]
        elif classe == "leia":
            return ["26", "Reduce"]
        elif classe == "escreva":
            return ["26", "Reduce"]
        elif classe == "se":
            return ["26", "Reduce"]
        elif classe == "fimse":
            return ["26", "Reduce"]
        elif classe == "repita":
            return ["26", "Reduce"]
        elif classe == "fimrepita":
            return ["26", "Reduce"]
        elif classe == "fim":
            return ["26", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,fimse,repita,fimrepita,fim]"]

    if estado == "72":
        if classe == "id":
            return ["34", "Reduce"]
        elif classe == "leia":
            return ["34", "Reduce"]
        elif classe == "escreva":
            return ["34", "Reduce"]
        elif classe == "se":
            return ["34", "Reduce"]
        elif classe == "repita":
            return ["34", "Reduce"]
        elif classe == "fim":
            return ["34", "Reduce"]
        elif classe == "fimse":
            return ["34", "Reduce"]
        elif classe == "fimrepita":
            return ["34", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim,fimse,fimrepita]"]

    if estado == "73":
        if classe == "id":
            return ["35", "Reduce"]
        elif classe == "leia":
            return ["35", "Reduce"]
        elif classe == "escreva":
            return ["35", "Reduce"]
        elif classe == "se":
            return ["35", "Reduce"]
        elif classe == "repita":
            return ["35", "Reduce"]
        elif classe == "fim":
            return ["35", "Reduce"]
        elif classe == "fimse":
            return ["35", "Reduce"]
        elif classe == "fimrepita":
            return ["35", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim,fimse,fimrepita]"]
    if estado == "74":
        if classe == "id":
            return ["36", "Reduce"]
        elif classe == "leia":
            return ["36", "Reduce"]
        elif classe == "escreva":
            return ["36", "Reduce"]
        elif classe == "se":
            return ["36", "Reduce"]
        elif classe == "repita":
            return ["36", "Reduce"]
        elif classe == "fim":
            return ["36", "Reduce"]
        elif classe == "fimse":
            return ["36", "Reduce"]
        elif classe == "fimrepita":
            return ["36", "Reduce"]
        else:
            return ["NULL", "Erro: esperado [id,leia,escreva,se,repita,fim,fimse,fimrepita]"]

    if estado == "75":
        if classe == "$":
            return ["38", "Reduce"]
        else:
            return ["NULL", "Erro: esperado $"]

def goto(estado, naoTerminal):
    if estado == '0':
        if naoTerminal == "P":
            return ["1", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '2':
        if naoTerminal == "V":
            return ["3", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '3':
        if naoTerminal == "A":
            return ["5", "Shift"]
        elif naoTerminal == "ES":
            return ["6", "Shift"]
        elif naoTerminal == "CMD":
            return ["7", "Shift"]
        elif naoTerminal == "COND":
            return ["8", "Shift"]
        elif naoTerminal == "CAB": #cabeçalho
            return ["13", "Shift"]
        elif naoTerminal == "R":
            return ["9", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '4':
        if naoTerminal == "LV":
            return ["16", "Shift"]
        elif naoTerminal == "D":
            return ["17", "Shift"]
        elif naoTerminal == "TIPO":
            return ["19", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '6':
        if naoTerminal == "A":
            return ["23", "Shift"]
        elif naoTerminal == "ES":
            return ["6", "Shift"]
        elif naoTerminal == "CMD":
            return ["7", "Shift"]
        elif naoTerminal == "COND":
            return ["8", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "R":
            return ["9", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '7':
        if naoTerminal == "A":
            return ["24", "Shift"]
        elif naoTerminal == "ES":
            return ["6", "Shift"]
        elif naoTerminal == "CMD":
            return ["7", "Shift"]
        elif naoTerminal == "COND":
            return ["8", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "R":
            return ["9", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '8':
        if naoTerminal == "A":
            return ["25", "Shift"]
        elif naoTerminal == "ES":
            return ["6", "Shift"]
        elif naoTerminal == "CMD":
            return ["7", "Shift"]
        elif naoTerminal == "COND":
            return ["8", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "R":
            return ["9", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '9':
        if naoTerminal == "A":
            return ["26", "Shift"]
        elif naoTerminal == "ES":
            return ["6", "Shift"]
        elif naoTerminal == "CMD":
            return ["7", "Shift"]
        elif naoTerminal == "COND":
            return ["8", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "R":
            return ["9", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '11':
        if naoTerminal == "ARG":
            return ["28", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '13':
        if naoTerminal == "ES":
            return ["34", "Shift"]
        elif naoTerminal == "CMD":
            return ["35", "Shift"]
        elif naoTerminal == "COND":
            return ["36", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP":
            return ["33", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '17':
        if naoTerminal == "LV":
            return ["40", "Shift"]
        elif naoTerminal == "D":
            return ["17", "Shift"]
        elif naoTerminal == "TIPO":
            return ["19", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '19':
        if naoTerminal == "L":
            return ['42', "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '32':
        if naoTerminal == "LD":
            return ['46', "Shift"]
        elif naoTerminal == "OPRD":
            return ['47', 'Shift']
        else:
            return ["NULL","Erro"]
    elif estado == '34':
        if naoTerminal == "ES":
            return ["34", "Shift"]
        elif naoTerminal == "CMD":
            return ["35", "Shift"]
        elif naoTerminal == "COND":
            return ["36", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP":
            return ["50", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '35':
        if naoTerminal == "ES":
            return ["34", "Shift"]
        elif naoTerminal == "CMD":
            return ["35", "Shift"]
        elif naoTerminal == "COND":
            return ["36", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP":
            return ["51", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '36':
        if naoTerminal == "ES":
            return ["34", "Shift"]
        elif naoTerminal == "CMD":
            return ["35", "Shift"]
        elif naoTerminal == "COND":
            return ["36", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP":
            return ["52", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '38':
        if naoTerminal == "OPRD":
            return ["54", "Shift"]
        elif naoTerminal == "EXP_R":
            return ["53", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '39':
        if naoTerminal == "EXP_R":
            return ["55", "Shift"]
        elif naoTerminal == "OPRD":
            return ["54", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '57':
        if naoTerminal == "L":
            return ["62", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '59':
        if naoTerminal == "OPRD":
            return ["64", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '60':
        if naoTerminal == "ES":
            return ["66", "Shift"]
        elif naoTerminal == "CMD":
            return ["67", "Shift"]
        elif naoTerminal == "COND":
            return ["68", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP_R":
            return ["65", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '61':
        if naoTerminal == "OPRD":
            return ["70", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '66':
        if naoTerminal == "ES":
            return ["66", "Shift"]
        elif naoTerminal == "CMD":
            return ["67", "Shift"]
        elif naoTerminal == "COND":
            return ["68", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP_R":
            return ["72", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '67':
        if naoTerminal == "ES":
            return ["66", "Shift"]
        elif naoTerminal == "CMD":
            return ["67", "Shift"]
        elif naoTerminal == "COND":
            return ["68", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP_R":
            return ["73", "Shift"]
        else:
            return ["NULL","Erro"]
    elif estado == '68':
        if naoTerminal == "ES":
            return ["66", "Shift"]
        elif naoTerminal == "CMD":
            return ["67", "Shift"]
        elif naoTerminal == "COND":
            return ["68", "Shift"]
        elif naoTerminal == "CAB":
            return ["13", "Shift"]
        elif naoTerminal == "CP_R":
            return ["74", "Shift"]
        else:
            return ["NULL","Erro"]
    else:
        return ["NULL", "Estado não possui desvios na tabela GOTO"]