import requests # library use for http request


url = ""
page = requests.get(url)

print(page.content) # print code source