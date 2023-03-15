# Finviz-Webscraper-Tutorial
Given a finviz filter url, we can use a python program to webscrape a list of stock tickers from it.
This tutorial assumes you have python set up and have a basic understanding of how to use it.

This python program depends on the Selenium and Webdriver Manager libraries to run. 
Those can be installed with the pip commands or with conda.
>pip install selenium

>pip install webdriver_manager

If you get any error messages with the pip command that could be due to your python version. Try "pip3" instead.

First start by creating or finding a screener in finviz. Here I selected any company in the technology sector that pays out a 3% of higher dividend.
Since finviz screeners parameters are saved into the url, the tutorial and code will work for any finviz screener.


<!---
![alt text](https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerSetUp.png?raw=true "Set Up")
-->


<img src="https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerSetUp.png" style=" width:750px ; height:450px "  >

Now that we have our generated screener we must now also see how many pages of tickers are generated as well. This is for us to iterate through
all of the pages without only getting the first few.

To find which web element describes the last page, which in the screenshot is page 40, simply right click and press "Inspect".
In our case, the last page will always be given by the last element with class='screener-pages'. In this screenshot I picked the set of all 
technology stocks to demonstrate that this is true even for larger screeer sets.

Using this information, we can now instantiate a webdriver object, navigate to the url and collect the page numbers.
If you have the ChromeDriver downloaded and are not using Webdriver Manager, use
>driver = webdriver.Chrome()

instead and it will automatically search for the path to it. (ChromeDriver can be downloaded at this url https://chromedriver.chromium.org/home)

```python
url = "https://finviz.com/screener.ashx?v=111&f=fa_div_o3,sec_technology"
chrome = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome)
driver.get(url)

pages = driver.find_elements(By.CLASS_NAME, 'screener-pages')
#since we now have a list of the page numbers shown, if we navigate to the last item in the list, we have the last page number
last_page = int(pages[-1].text)
```

<img src="https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerInspect.png" style=" width:750px ; height:450px "  >

Next we need to identify the class that describes the tickers. Once again we right click on the ticker and find the class name that describes it.
In this case, the ticker is given by class="screener-link-primary".
Similarly, we can now use find elements to access the ticker names. Now we can create a for loop and add each ticker on the page to a list.

```python
symbols = driver.find_elements(By.CLASS_NAME, 'screener-link-primary')
ticker_list = []
for i in symbols:
    #the objects in the symbols list are selenium objects, so you need to use the .text function to convert to string
    ticker_list.append(i.text)
```

<img src="https://github.com/denged1/Finviz-Webscraper/blob/main/docs/tickerInspect.png" style=" width:750px ; height:450px "  >

