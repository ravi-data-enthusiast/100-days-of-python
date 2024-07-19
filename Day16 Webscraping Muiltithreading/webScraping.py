'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.'''

import threading
import requests
from bs4 import BeautifulSoup #this library is used for webscraping any url

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]

def fetch_content(url):
    response = requests.get(url) #http get request is made and response is returned
    soup = BeautifulSoup(response.content,'html.parser') #parser parses the content of response
    print(f'Fetched {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    #Thread is created, function is specified and url to be parsed is passed as args
    thread = threading.Thread(target=fetch_content, args =(url,))
    threads.append(thread)
    #Starts the execution of the thread. The fetch_content function is called with the URL as its argument.
    thread.start()

'''Waits for the thread to complete its execution. This ensures that the main thread (the thread running the script) 
waits for all the child threads to finish before continuing.'''
for thread in threads:
    thread.join()
    
print("All webpages are fetched")    

'''
Concurrency: By using threads, multiple HTTP requests can be made concurrently, which can speed up the process of fetching multiple web pages.
I/O-bound Task: Fetching web pages is an I/O-bound task, where the program spends a lot of time waiting for network responses. Threading can be 
beneficial here because while one thread is waiting for a response, other threads can continue making requests.
'''