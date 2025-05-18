libro = input( 'Ingrese el nombre del libro:')
autor = input( 'Ingrese el nombre del autor:')
precio = float(input( 'Ingrese el precio:'))
envioGratis = input('¿El envio es gratis?/("SI") o ("NO")')

if envioGratis != "SI" and envioGratis != "NO" : 
    envioGratis = "SI"

print (f'''
    Libro : {libro} 
    Autor : {autor}
    Precio : {precio} 
    envio es gratis: {envioGratis}
    ''')


#Dado el siguiente código, quiero saber si es Verdadero decir que el envío va a ser "gratis" si escribo algo distinto a SI o a NO , si es verdadero 👍 si es falso 🤌