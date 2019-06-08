import nltk
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def reviews(check):
    positive = 0
    negative = 0
    neutral = 0
    url_name = "https://www.imdb.com" + check + "reviews?ref_=tt_ql_3"
    #print(url_name)
    url = requests.get(url_name, timeout = 5)
    soup = BeautifulSoup(url.content, "html.parser")
    soup.prettify()
    review = soup.find_all("div",attrs = {"class" : "text show-more__control"})
    for text_1 in review:
        #print(text_1.text)
        blob1 = TextBlob(text_1.text)
        x = blob1.sentiment.polarity

        if x < 0:
            #print("Negative review")
            negative = negative + 1
        elif x > 0:
            #print("Positive review")
            positive = positive + 1
        else:
            #print("Neutral review")
            neutral = neutral + 1

    sum1 = positive + negative + neutral
    
    if sum1 == 0:
        print("No movie found")
    else:
        print("Positive reviews are : ", positive)
        print("Negative reviews are : ", negative)
        print("Neutral reviews are : ", neutral)    


def search():
    name1 = input("Enter name of Movie : ")
    name1.strip()
    name2 = name1.replace(" ", "+")
    url_name = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + name2 +"&s=all"
    #print(url_name)
    url = requests.get(url_name, timeout = 5)
    soup1 = BeautifulSoup(url.content, "html.parser")
    soup1.prettify()
    movie = soup1.find("div",attrs = {"class" : "findSection"}).find("td", attrs = {"class" : "primary_photo"})
    check = movie.find('a')['href']
    reviews(check)
 
search()
    

