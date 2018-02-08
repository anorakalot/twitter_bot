import requests
from bs4 import BeautifulSoup



def web_scrape_to_list():
    #url = "https://bulbapedia.bulbagarden.net/wiki/Category:Anime"
    url = "https://bulbapedia.bulbagarden.net/wiki/Main_Page"
    fetch_url = requests.get(url)
    soup = BeautifulSoup(fetch_url.text,"lxml")

    list_of_links = []
    for link in soup.find_all('a'):
        if "None" not in str(link.get("href")):
            list_of_links.append((link.get("href")))
            #print (link.get("href"))

    return list_of_links




if __name__ == "__main__":
    list_links = web_scrape_to_list()
    #print ("\n\n\n\n\n\n")
    for x in list_links:
        print (x)
