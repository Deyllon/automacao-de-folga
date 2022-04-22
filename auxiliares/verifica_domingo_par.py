from calendar import  day_name


def verific_se_domingo_e_par(dia, feriados):
    
    numero_do_dia = dia.day
    
    if (numero_do_dia % 2 == 0 and day_name[dia.weekday()] == "Sunday") or (numero_do_dia % 2 == 0 and dia in feriados ):
        return True