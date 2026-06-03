import requests
from bs4 import BeautifulSoup

URL = "https://www.idealista.com/alquiler-viviendas/jaca-huesca/con-precio-hasta_700/"

html = requests.get(URL).text

print(html[:500])
# prueba
