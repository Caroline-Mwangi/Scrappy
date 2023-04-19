from django.shortcuts import render, redirect
import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def index(request):
    return render(request, "scrapp/index.html")

def srchtag(request):
    return render(request, "scrapp/srch_tag.html")

def username(request):
    if request.method == "POST":
        name = request.POST['username']
        env = environ.Env()
        environ.Env.read_env()

        url = env('URL')

        Tweets=[]
        Timestamp=[]
        

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        driver.implicitly_wait(10)

        driver.find_element(By.CSS_SELECTOR,'[placeholder="Search Twitter"]').send_keys(name, Keys.ENTER)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR,'[href="/{}"]'.format(name)).send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        tweets = driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweet"]')
        driver.implicitly_wait(20)

        while True:
            for tweet in tweets:
                tweet_text = tweet.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text.encode("utf-8")
                Tweets.append(tweet_text)

                timestamp = driver.find_element(By.CSS_SELECTOR, 'time').get_attribute('datetime')
                Timestamp.append(timestamp)
                
                print(Tweets, Timestamp)
                driver.implicitly_wait(150) 
            
            driver.implicitly_wait(150)   
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            driver.implicitly_wait(150)
            tweets = driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweet"]')
            driver.implicitly_wait(150)
            Tweets2 = list(set(Tweets))
            if len(Tweets2) > 3:
                break
            driver.quit()
    return render(request, "scrapp/username.html")
    