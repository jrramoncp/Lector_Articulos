from gtts import gTTS
from newspaper import Article

url = input("Ingresa una URL de una noticia: ")

def crear_fichero():
    '''
    Una funcion, que lee, y crea un fichero.txt formateado según el articulo que le hayamos introducido en la url
    '''
    article = Article(url)
    article.download()
    article.parse()
    
    file = "articulo.txt"
    articulo = open(file,"w+")

    articulo.write(f"TITULO:{article.title}")
    fecha = article.publish_date
    articulo.write(f"CUERPO DE LA NOTICIA: {article.text}")
    try:
        autor = article.authors[0]
        articulo.write(f"AUTOR:{autor}")
    except:
        pass

    articulo.close

def leer_fichero():
    file = "articulo.txt"
    articulo = open(file, "r+")
    traduccion = gTTS(text=articulo.read(), lang="es")
    traduccion.save("noticia.mp3")
    articulo.close


    

crear_fichero()
leer_fichero()
