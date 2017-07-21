import requests # used to gain access to a website
from bs4 import BeautifulSoup  # used to view page source (inspect element) on a website


""""
In the url variable define a website to crawl. 
In the for loops in the various functions enter values for the following format in the code:

for item_name in soup.finaAll('opening tag', {'attribute' : 'value of the attribute'}):

The content to fill in the blanks can be taken from the inspect element page of the website


""""



def page_spider(max_pages): # defines URL and number of pages to crawl
    page = 1
    while page <=  max_pages:
        url = "" # enter URL to crawl
        source_code = requests.get(url) # gets url and stores it in a variable called source code
        plain_text = source_code.text # saves all the word content to crawl and stores it in a variable called plain text
        soup = BeautifulSoup(plain_text) # uses all the website source code and assigns it to the soup object to utilize the BeautifulSoup module
        for link in soup.findAll('', {'class':''}): # loops through all of source code and picks up the links with the class of vip
            href = "" + link.get('href')
            title = link.string

            print(href) # prints all of the links on the page
            print(title) # prints the title string of all the links on the page
            get_single_item_data(href) # calls the function that prints all the links on the page that each link led to




def get_single_item_data(item_url): # crawls the page that each link leads to
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for item_name in soup.finaAll('', {'' : ''}):
        print(item_name.string)


    for link in soup.findAll('', {'' : ''}):
        href = "" + link.get('href')
        print(href)


page_spider(1)
