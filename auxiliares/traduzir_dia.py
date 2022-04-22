from calendar import  day_name



def traduzir_dia(dia):
    nome_do_dia = day_name[dia.weekday()]
    if nome_do_dia == "Monday":
        nome_do_dia = "Segunda feira"
        return nome_do_dia
    
    elif nome_do_dia == "Tuesday":
        nome_do_dia = "Terça feira"
        return nome_do_dia
    
    elif nome_do_dia == "Wednesday":
        nome_do_dia = "Quarta feira"
        return nome_do_dia
    
    elif nome_do_dia == "Thursday":
        nome_do_dia = "Quinta feira"
        return nome_do_dia
    
    elif nome_do_dia == "Friday":
        nome_do_dia = "Sexta feira"
        return nome_do_dia
    
    elif nome_do_dia == "Saturday":
        nome_do_dia = "Sábado"
        return nome_do_dia
    
    nome_do_dia = "Domingo"
    
    return nome_do_dia
