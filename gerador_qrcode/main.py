from pyqrcode import *
from png import *

url = pyqrcode.create('https://www.youtube.com/shorts/cRuQH12YQeE')
url.svg('ig-url.svg', scale=5) # svg usam arquivos com dados de imagem e texto, melhor para web pois ultrapassa os limites do html, 
# criando um conteúdo mais robusto e interativo
url.png('ig-url.png', scale=5, module_color=(127, 17, 224), background=(255, 255, 255, 255))
