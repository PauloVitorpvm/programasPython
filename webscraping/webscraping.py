from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.globo.com/").content
#Objeto site recebendo o conteudo da requisição http do site....
soup = BeautifulSoup(site, 'html.parser')
#Obejeto soup baixando do site o html
#print(soup.prettify())
#transforma o html em string e o print vai exibir o html
print(soup.get_text())