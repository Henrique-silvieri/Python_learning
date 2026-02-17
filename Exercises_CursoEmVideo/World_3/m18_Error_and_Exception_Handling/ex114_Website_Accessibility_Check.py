# Create a code in Python that tests whether the Pudim website (pudim.com.br) is accessible via the computer being used.

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim.com.br não está acessível')
else:
    print('Consegui acessar o site com sucesso')
