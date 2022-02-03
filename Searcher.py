import requests
import os
import sys
from bs4 import BeautifulSoup

target = input("Target site: ")


def linkSearcher():
    a = source.find_all("a")

    for i in a:
        print(i.get("href"))
        page_0 = open("Links.txt", "a+")
        page_0.write(i.get("href") + "\n")
    page_0.close()


try:
    r = requests.get(target)
    source = BeautifulSoup(r.content, "lxml")
    targetSiteHeader = source.title
    print("Target's header: " + targetSiteHeader.text)
    linkSearcher()
except:
    print("Somethings wrong...")
    pass
