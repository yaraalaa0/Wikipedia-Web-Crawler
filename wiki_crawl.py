import requests
from bs4 import BeautifulSoup
import urllib
import time
start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
def find_first_link(url):
    response=requests.get(url)
    html=response.text
    soup=BeautifulSoup(html, 'html.parser')
    article_body=soup.find(id='mw-content-text').find(class_='mw-parser-output')
    first_link = None
    for element in article_body.find_all("p", recursive = False):
        first_link = element.find("a", recursive = False)
        if first_link:
           first_link = first_link.get('href')
           break
    if first_link:
       first_link = urllib.parse.urljoin('https://en.wikipedia.org/',first_link)
       return first_link
    else:
       return False
	   
def continue_crawl(search_history, target_url, max_steps = 25):
    if search_history[-1] == target_url:
       print('We have found the target article')
       return False 
    elif len(search_history) > max_steps:
       print('Too long searching')
       return False
    elif search_history[-1] in search_history[:-1]:
       print('We are going on a loop')
       return False
    else:
       return True

article_chain = [start_url]
while continue_crawl(article_chain, target_url):
      print(article_chain[-1])
      link = find_first_link(article_chain[-1])
      if not link:
         print('No links')
         break
      article_chain.append(link)
      time.sleep(2)

print(article_chain)
    


