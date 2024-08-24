from gtts import gTTS # Modulo traductor a voz
from newspaper import Article # Modulo para trabajar con noticias

url = input("Ingresa una URL de una noticia: ") # Pide la url de la noticía

def crear_fichero():
    '''
    Una funcion, que lee, y crea un fichero.txt formateado según el articulo que le hayamos 
    introducido en la url
    '''

    article = Article(url)
    article.download() # Descarga la noticia
    article.parse() # Formatea la noticia
    
    file = "articulo.txt" 
    articulo = open(file,"w+") # Creamos y abrimos el fichero

    articulo.write(f"TITULO: {article.title}") # Título de la noticia
    articulo.write(f"CUERPO DE LA NOTICIA: {article.text}") # Cuerpo de la noticia
    try: # Verifica si hay un autor y lo dice tambien
        autor = article.authors[0]
        articulo.write(f"AUTOR:{autor}")
    except:
        pass # Si no lo hubiera saltaría esta parte

    articulo.close # Cerramos el fichero

def leer_fichero():
    ''' Una funcion que lee el fichero generado de la función crear_fichero, y lo transforma a un 
    archivo de voz'''
    file = "articulo.txt"
    articulo = open(file, "r+") # Abrimos el fichero con el articulo

    traduccion = gTTS(text=articulo.read(), lang="es") # Convierte el fichero de texto
    traduccion.save("noticia.mp3") # Guarda el fichero como un mp3

    articulo.close # Cierra el fichero


    
crear_fichero()
leer_fichero()
