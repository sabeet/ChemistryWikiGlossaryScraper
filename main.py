import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Glossary_of_chemistry_terms"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

terms = soup.find_all("dfn", {'class' : 'glossary'})


for term in terms:
    print(term.get_text())