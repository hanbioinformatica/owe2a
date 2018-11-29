'''
A web crawler for extracting email addresses from web pages.

Takes a string of URLs and requests each page, checks to see if we've
found any emails and prints each email it finds.
'''


import re
import urllib3


def requestHTML(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    retData = response.data
    return retData.decode('utf-8')




def process(data):
    for adres in re.findall(r'"https?:.*"\s', data):
        print(adres)


def main():
    data = requestHTML("http://nu.nl/")
    print((data))
    process(data)

if __name__ == '__main__':
  main()