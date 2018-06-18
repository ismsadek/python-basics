# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different code, use the code from the solution),
#  and instead of printing the results to a screen, write the results to a txt file.
#  In your code, just make up a name for the file you are saving to.

# Extras:

# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
titles = []
for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        # print(story_heading.a.text.replace("\n", " ").strip())
        titles.append(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

name_file = input('Rename the file please ')

with open('{}.txt'.format(name_file), 'w') as open_file:
  open_file.write(str(titles))