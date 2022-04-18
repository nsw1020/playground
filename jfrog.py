import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

URL = "https://jfrog.com/blog/"

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
}

rq = requests.get(URL)
soup = bs(rq.content, 'html.parser')

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-3069989903011-3133301087427-0e3JncqvT0RHBrGSaeDCAf51"
#postsWrap > article:nth-child(1) > header > div > div > div.col-md-6.blog-post-title > a

test=soup.select("div.col-md-6.blog-post-title > a")
#test2=soup.select("div.blog-post-date > p")[0]

#for i in soup.findAll("div",class_="col-md-6.blog-post-title"):
#    href=i.findAll('a')
#    print(href)
    #post_message(myToken,"#splunk",href.find('a'))

for i in test:
    href=i.attrs['href']
    print(href)
    post_message(myToken,"#article",href)
#for i in test2:
#    #aa=i.find('div',class_='div.blog-post-date > p')
#    aa=i.get_text()
#    bb=aa.replace(" ",'')
#    print(bb)


#print(datetime.today().strftime("%d"))
#>= datetime.today().strftime("%d")
#postsWrap > article:nth-child(1) > header > div > div > div.col-md-6.blog-post-title > div.blog-post-date > p
#//*[@id="postsWrap"]/article[1]/header/div/div/div[2]/div[1]/p/text()

#PSNTZO8gXFUe\+cpCZyApw0vEKWPT4b14D6teBEocIAE\=_17f18f6bbe4\:6cd0302\:c8b06589_main > div.content > a
#//*[@id="PSNTZO8gXFUe+cpCZyApw0vEKWPT4b14D6teBEocIAE=_17f18f6bbe4:6cd0302:c8b06589_main"]/div[2]/a


