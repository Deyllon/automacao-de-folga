from datetime import  timedelta
from auxiliares.verifica_domingo_impar import verifica_se_domingo_e_impar
from auxiliares.verifica_domingo_par import verific_se_domingo_e_par
from auxiliares.adiciona_folga_impar import adiciona_folga_impar
from auxiliares.adiciona_folga_par import adiciona_folga_par


def folga(resultado):
    
    dias = timedelta(days=1)
    
    inicio_do_mes = resultado[1]
    fim_do_mes = resultado[2]
    folga_para_impares=[]
    folga_para_pares=[]
    
    while inicio_do_mes <= fim_do_mes:
        if verifica_se_domingo_e_impar(inicio_do_mes, resultado[0]) == True:
            folga_para_impares.append(adiciona_folga_impar(inicio_do_mes))
        
        if verific_se_domingo_e_par(inicio_do_mes, resultado[0]) == True:
            folga_para_pares.append(adiciona_folga_par(inicio_do_mes))
      
        inicio_do_mes += dias
    return folga_para_impares[-1], folga_para_pares[-1]