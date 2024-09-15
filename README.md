# Lector de Artículos

## Descripción

Este proyecto es un lector de noticias en línea desarrollado con Python. Permite extraer contenido de un artículo de prensa a partir de una URL y convertirlo en un archivo de audio `.mp3` para escuchar la noticia. Utiliza los módulos `gTTS` y `newspaper3k`.

## Funcionalidades

- Extrae el título, cuerpo y autor de un artículo de prensa desde una URL.
- Convierte el texto en un archivo de audio en formato `.mp3`.
- Permite escuchar las noticias de manera estructurada.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jrramoncp/Lector_Articulos.git
2. Instala las dependencias necesarias
    ```bash
    pip install -r requirements.txt

## Como usar

1. Ejecuta el script convesor.py
2. Introduce la URL del articulo cuando se te solicite
3. El programa creará un archivo .txt con la noticia y generará un archivo .mp3 con la lectura de la noticia

## Tecnologias Utilizadas

 - Python
 - gTTS: Para convertir texto a voz
 - newspaper3k: Para extraer la noticia

## Contribuir

Si quieres contribuir al proyecto, crea un fork del repositorio y envía un pull request con tus mejoras.
Toda sugerencia o mejora es bienvenida

## Licencia

Este proyecto está licenciado bajo la licencia MIT
