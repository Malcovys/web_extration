import requests # library use for http request
from bs4 import BeautifulSoup

url = ""

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# element = balise
page_get_element_title = soup.title
page_get_element_title_string = soup.title.string
page_get_element_a = soup.find_all('a')
page_get_element_by_id = soup.find(id="")
page_get_element_div_with_class = soup.find_all("div", class_="")
page_get_article_titles = soup.find_all("", class_="")
page_get_decription = soup.find_all("", class_="")


def printListInPageStr (block):
    for list in block:
        print(list.string, "\n\n")
        
printListInPageStr(page_get_decription)