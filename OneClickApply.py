import time
from random import randint
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--user-data-dir=/Users/hnahli/GitHub/chrome-data")
options.add_argument("--disable-infobars")
options.add_argument("--enable-file-cookies")
driver = webdriver.Chrome('/Users/hnahli/GitHub/chrome-data/chromedriver', options=options)
options.add_argument("user-data-dir=/Users/hnahli/GitHub/chrome-data/chrome-data")
options.add_argument("download.default_directory=/Users/hnahli/GitHub/chrome-data/download")
driver.get('https://www.ziprecruiter.com/candidate/search?radius=5000&search=Work+from+home&location=Vancouver%2C+BC+Canada')
driver.maximize_window()

#Add Cities You Are Interested To Find Work in
cities = [
    #'British Columbia, Canada',
    'Alberta, Canada',
    'Saskatchewan, Canada',
    'Manitoba, Canada',
    'Ontario, Canada',
    'Quebec, Canada',
    'New Brunswick, Canada',
    'Nova Scotia, Canada',
]

for c in cities:
    driver.get('https://www.ziprecruiter.com/candidate/search?radius=5000&search=Work+from+home&location=Vancouver%2C+BC+Canada')
    driver.find_element_by_css_selector('#search1').clear()
    driver.find_element_by_css_selector('#search1').send_keys('IT')
    driver.find_element_by_css_selector('#location1').clear()
    driver.find_element_by_css_selector('#location1').send_keys(c)
    driver.find_element_by_css_selector('body > div.main_site_header > section > div > form > div.submit > input[type=submit]').click()
    time.sleep(3)
    #Scroll down to the buttom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    #Click on load more button if exist
    try:
        driver.find_element_by_css_selector('#primary > section:nth-child(3) > div > button').click()
    except:
        pass

    scrolls = 0
    while scrolls <= 30:
        scrolls = scrolls + 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    html = driver.execute_script("return document.documentElement.outerHTML ")
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.findAll('div',{'class':'job_content'})

    for job in jobs:
        time.sleep(randint(15,45))
        try:
            link = job.find('button',{'class':'job_tool job_apply default one_click_apply'}).get('data-href')
            position = job.find('h2',{'class':'job_title'}).text.strip()
            location = job.find('a',{'class':'t_location_link location'}).text.strip()
            company = job.find('a',{'class':'t_org_link name'}).text.strip()
            driver.get(link)
            print('Applied Successfully To:',position,'With',company,'IN', location)
        except:
            print('Sorry Quick Apply Not Available For')

driver.quit()