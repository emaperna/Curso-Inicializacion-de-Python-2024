#ATAJOS: VSCODE

#ALT + Z = REZIZEAR PANTALLA (ACOMODA TAMAÑO DE PANTALLA)

#CTRL + F = ENCONTRAR PALABRAS DENTRO DE NUESTRO CODIGO

#CTRL + H = BUSQUEDA Y REEMPLAZA PALABRA POR OTRA

#for x in range(0,10,1): #Range : inicio, final y pasos.
    #print(x)
    
#if n % 2 == 0 (el resto de la division es igual a 0 es par)

#Trivia WhatsApp

texto = "Los miles de millones de seres humanos que viven (conectados) " 

palabras_clave = ["conectados","seres"] 

palabra_detectada = next(palabra for palabra in palabras_clave if palabra in texto) 

print(f"Palabra detectada: {palabra_detectada}")