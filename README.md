# Finviz-Webscraper-Tutorial
Given a finviz filter url, we can scrape a list of stock tickers from it.

This python program depends on the Selenium and Webdriver Manager libraries to run. 
Those can be installed with "pip install selenium" and "pip install webdriver_manager". If you get any 
error messages with the pip command that could be due to your python version. Try "pip3" instead.

First start by creating some screener in finviz. Here I selected any company in the technology sector that pays out a 3% of higher dividend.
Since finviz screeners parameters are saved into the url, the subsequent tutorial and code will work for any finviz screener.


<!---
![alt text](https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerSetUp.png?raw=true "Set Up")
-->


<img src="https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerSetUp.png" style=" width:750px ; height:450px "  >

Now that we have our generated screener we must now also see how many pages of tickers are generated as well. This is for us to iterate through
all of the pages without only getting the first few.

In our case, the last page will always be given by the last element with class='screener-pages'. In this screenshot I picked the set of all 
technology stocks to demonstrate that this is true even for larger screeer sets.

<img src="https://github.com/denged1/Finviz-Webscraper/blob/main/docs/screenerInspect.png" style=" width:750px ; height:450px "  >
