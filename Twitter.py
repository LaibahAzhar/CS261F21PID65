#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import csv
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from msedge.selenium_tools import Edge,EdgeOptions

options=EdgeOptions()
options.use_chromium=True
driver =Edge(options=options)

driver.get('https://twitter.com/login')
driver.maximize_window()

def get_username(user):
    username = driver.find_element_by_xpath('//input[@name="username"]')
    username.send_keys(user)
    username.send_keys(Keys.RETURN)
    
def get_phone(ph):
    phone = driver.find_element_by_xpath('//input[@name="text"]')
    phone.send_keys(ph)
    phone.send_keys(Keys.RETURN)

def get_password(password):
    passfield = driver.find_element_by_xpath('//input[@name="password"]')
    passfield.send_keys(password)
    passfield.send_keys(Keys.RETURN)

def search(searchterm):
    search_input = driver.find_element_by_xpath('//input[@class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-xyw6el r-641cr4 r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
    search_input.send_keys(searchterm)
    search_input.send_keys(Keys.RETURN)

def open_detail():
    driver.find_element_by_link_text('Latest').click()
    
def get_tweet_data(card):
    """Extracting data from tweet data""" 
    username= card.find_element_by_xpath('.//span').text
    handle= card.find_element_by_xpath('.//span[contains(text(),"@")]').text
    try:
        postdate=card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return
    text = card.find_element_by_xpath('.//div[@class="css-1dbjc4n"]').text
    reply_count=card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    try:
        retweet_count = card.find_element_by_xpath('.//div[data-testid="retweet"]').text
    except:
        retweet_count='0'
    try:
        like_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    except:
        like_count='0'
    
    tweet=(username,handle,postdate,text,reply_count,retweet_count,like_count)
    print(tweet)
    return tweet

def save_in_csv(datas):
    with open('twitter.csv', 'w', encoding='UTF8', newline='') as f:
        header = ['User Name','Handle','TimeStamp','Text','Like','Retweets']
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(datas)
def start_scraping():
    data = []
    tweet_ids = set()
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True

    while scrolling:
        page_cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
        for card in page_cards[-100:]:
            tweet = get_tweet_data(card)
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)
#    const pause = (scroll) => window.clearTimeout(scroll)       
        scroll_attempt = 0
        
        while True:
        # check scroll position
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(2)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
            # end of scroll region
                if scroll_attempt >= 3:
                    scrolling = False
                    save_in_csv(data)
                    driver.close()
                    break
                else:
                    sleep(2) # attempt another scroll
            else:
                last_position = curr_position
            break
        print(data)
        save_in_csv(data)
    # close the web driver
    driver.close()

if __name__=='__main__':
        
    u = input('username:')    
    done=input('Done?')
    get_username(u)
    n = input('Phone/Username:')
    done=input('Done?')
    get_phone(n)
    p = getpass('password:')
    done=input('Done?')
    get_password(p)
    si = input("Search: ")
    done=input('Done?')
    search(si)
    done=input('Done?')
    open_detail()
    done=input('Done?')
    save_in_csv(start_scraping())
    done=input('Done?')

