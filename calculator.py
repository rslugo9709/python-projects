def arithmetic_arranger(problems, show_answers=False):
    #hacemos las validaciones
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    primeraL = ""
    segundaL = ""
    guionesL = ""
    resultadosL = ""
    for index, element in enumerate(problems):
        elem = problems[index].split(" ")

        #print(elem)
        if not(elem[1]=="+" or elem[1]=="-"):
            return  "Error: Operator must be '+' or '-'."
        if not(elem[0].isnumeric() and elem[2].isnumeric()):
            return 'Error: Numbers must only contain digits.'
        if (len(elem[0])>4 or len(elem[2])>4): 
            return 'Error: Numbers cannot be more than four digits.'
               
#Aqui calculamos el resultado
        result= ""
        if(show_answers):
            
            if(elem[1]=="+"):
                result= str(int(elem[0])+int(elem[2]))
            else:
                result= str(int(elem[0])-int(elem[2]))
            #print(result) 

                       
       
        
        #chequeamos el mayor
        length= 0
        if (len(elem[0])>len(elem[2])):
            length= 2+len(elem[0])
        else:
            length= 2+len(elem[2])
        #print(length)
        guiones=""
        for i in range(length):
            guiones = guiones+"-"
        #print(guiones)
        ajustado = elem[1]+(elem[2]).rjust(length-1)
        if(index != (len(problems)-1)):
            #print("primeras lineas")
            primeraL = primeraL + elem[0].rjust(length)+ "    "
            
            segundaL = segundaL + ajustado+ "    "
            guionesL = guionesL + guiones+ "    "
            if(show_answers):
                resultadosL = resultadosL + result.rjust(length) + "    "
 
        elif (index == (len(problems)-1)):
            #print("ultima linea")
            primeraL = primeraL + elem[0].rjust(length)
            segundaL = segundaL + ajustado
            guionesL = guionesL + guiones
            if(show_answers):
                resultadosL = resultadosL + result.rjust(length)


    if(show_answers):
        ##Para unirlos todos separandolos por una linea
         #final = "\n".join([primeraL, segundaL, guionesL, resultadosL])
         final = primeraL+ "\n" + segundaL + "\n" + guionesL + "\n" + resultadosL
         return(final)
    else:
        #final = "\n".join([primeraL, segundaL, guionesL])
        final = primeraL+ "\n" + segundaL + "\n" + guionesL
        return(final)
    #aqui va el return
    

##
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"],True)}')
##print(" ")
##print(" ")
##print(" ")
##print("segundo test")
##print(" ")
##print(" ")
##print(" ")
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
##
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')

