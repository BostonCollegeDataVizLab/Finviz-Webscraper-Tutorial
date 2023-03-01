from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


#declaring a variable to store the url
urls = "https://finviz.com/screener.ashx?v=111&f=fa_div_o3,sec_technology"

#this function gets the urls for all the pages, and returns a list of urls
def get_page_urls(url):
    #instantiate a chrome driver object
    chrome = Service(ChromeDriverManager().install())
    #pass the chrome driver object to the webdriver.Chrome() function to instantiate a webdriver object
    driver = webdriver.Chrome(service=chrome)
    driver.get(url)
    #this will differ by page, right click on the element you want to get and click inspect, then copy the class name
    pages = driver.find_elements(By.CLASS_NAME, 'screener-pages')
    #this essentially found the last page number on a page to set up the for loop
    last_page = int(pages[-1].text)
    #url list, start with empty list
    url_list = [url]
    for i in range(1,last_page):
        #this is different per page as well, in my case the url is the same except for the number at the end
        text = '&r=' + str(i * 20 +1)
        url_list.append(url+text)
    return url_list

def get_ticker_symbols(url):
    #want a service type object, you can put "ChromeDriverManager().install()" directly in the webdriver.Chrome() function, but will
    #pass a deprecated warning
    chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome)
    driver.get(url)
    ################################### IMPORTANT: DON"T MISSPELL THE FUNCTION ########################################
    #use find_element to get the first element instead, this returns a list of the elements
    symbols = driver.find_elements(By.CLASS_NAME, 'screener-link-primary')

    #this function actually gets the ticker symbols from each page, iterating through the symbols list
    ticker_list = []
    for i in symbols:
        #the objects in the symbols list are selenium objects, so you need to use the .text function to convert to string
        ticker_list.append(i.text)
    #
    #print(ticker_list)
    return ticker_list

def get_tickers(url):
    #get the urls for all the pages
    url_list = get_page_urls(url)
    #get the ticker symbols for all the pages
    ticker_list = []
    for i in url_list:
        ticker_list += get_ticker_symbols(i)
    return ticker_list

#get_ticker_symbols(url)
print(get_tickers(urls))

#to get data from a website, you need to find the XPATH of the data you want
#to find the XPATH, right click on the data you want and click inspect