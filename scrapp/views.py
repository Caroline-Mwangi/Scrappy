from django.shortcuts import render, redirect
import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from django.contrib import messages


def index(request):
    return render(request, "scrapp/index.html")
    
    
def index2(request):
    return render(request, "scrapp/index2.html")

def tw_login(request):
    if request.method == "POST":
        global tw_username
        global tw_password
        global tw_phone
        tw_username = request.POST['username']
        tw_password = request.POST['password']
        tw_phone = request.POST['phone']
        return render(request, "scrapp/index2.html")
    return render(request, "scrapp/tw_login.html")

def srchtag(request):
    try:
        if request.method == "POST":
            tag = request.POST['search_tag']
            env = environ.Env()
            environ.Env.read_env()

            url = env('URL')

            Tweets=[]
            Timestamp=[]
            
            lg_name = tw_username
            lg_pass = tw_password
            lg_phone = tw_phone
            

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(url)
            driver.implicitly_wait(150)
            
            driver.find_element(By.CSS_SELECTOR,'[data-testid="login"]').click()
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="text"]').send_keys(lg_name, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="text"]').send_keys(lg_phone, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="password"]').send_keys(lg_pass, Keys.ENTER)

            driver.find_element(By.CSS_SELECTOR,'[placeholder="Search Twitter"]').send_keys(tag, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.XPATH,"//span[text()='Latest']").click()
            driver.implicitly_wait(150)

            tweets = driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweet"]')
            driver.implicitly_wait(150)

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
                return render(request, "scrapp/index.html")
    except:
        messages.error(request, "OOPS! Something went wrong. Please try again.")
        return render(request, "scrapp/index.html")
    return render(request, "scrapp/srch_tag.html")

def username(request):
    try:
        if request.method == "POST":
            name = request.POST['username']
            env = environ.Env()
            environ.Env.read_env()

            url = env('URL')

            Tweets=[]
            Timestamp=[]
            
            lg_name = tw_username
            lg_pass = tw_password
            lg_phone = tw_phone
            

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(url)
            driver.implicitly_wait(150)
            
            driver.find_element(By.CSS_SELECTOR,'[data-testid="login"]').click()
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="text"]').send_keys(lg_name, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="text"]').send_keys(lg_phone, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[name="password"]').send_keys(lg_pass, Keys.ENTER)

            driver.find_element(By.CSS_SELECTOR,'[placeholder="Search Twitter"]').send_keys(name, Keys.ENTER)
            driver.implicitly_wait(150)
            driver.find_element(By.CSS_SELECTOR,'[href="/{}"]'.format(name)).send_keys(Keys.ENTER)
            driver.implicitly_wait(150)

            tweets = driver.find_elements(By.CSS_SELECTOR,'[data-testid="tweet"]')
            driver.implicitly_wait(150)

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
                return render(request, "scrapp/index.html")
    except:
        messages.error(request, "OOPS! Something went wrong. Please try again.")
        return render(request, "scrapp/index.html")
    return render(request, "scrapp/username.html")
    