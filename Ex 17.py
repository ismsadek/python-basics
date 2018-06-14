# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 18:32:02 2018

@author: Ismael
"""

import requests
from bs4  import BeautifulSoup


url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)

def scrapeArticles():
    for story_heading in soup.find_all(class_='story-heading'):
        if story_heading.a: 
            print(story_heading.a.text.replace("\n", " ").strip())
        else: 
            print(story_heading.contents[0].strip())
