# Import all the necessary libraries.
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import re

# Start time for the program
start_time = time.time()

# Href list for links for each movie
href = []

# Lets download and import to Beautiful Soup already known page
url = "https://www.rottentomatoes.com/top/bestofrt/"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

# From the list of movies in table, extracting the href for each movie
temp = [td.find('a', {'class': 'unstyled articleLink'}) for td in soup.find_all('td')]
for i in temp:
    if i is not None:
        href.append(i.get('href'))

# Each link to a particular movie page has a similar structure, url = "https://www.rottentomatoes.com" + href"
links = []
for h in href:
    links.append("https://www.rottentomatoes.com" + h)

# Creating a pandas dataframe of the extracted values
df = pd.DataFrame(columns=['Name', 'Link', 'Rating', 'Box Office (Gross USA)', 'Genre', 'Original Language', 'Director', 'Producer', 'Writer',
                           'Release Date (Streaming)', 'Release Date (Theaters)', 'Runtime', 'Production Co', 'Aspect Ratio', 'Sound Mix'])

# Using loop to visit each link in top 100 movies and extracting information
for i in links:
    # Lets download and import to Beautiful Soup for each link
    data = requests.get(i).text
    soup = BeautifulSoup(data, 'html.parser')
    t = soup.find_all('ul', {'class': "content-meta info"})

    # Finding Movie Info for each movie
    row = t[0].find_all('li')

    # Creating a dictionary to save extracted values
    name = soup.find_all('h1', {"data-qa": "score-panel-movie-title"})
    name = name[0].text
    dic = {'Name': name, 'Link': i}

    for j in row:
        # Label Tag for each movie
        lab = j.find_all('div', {'data-qa': 'movie-info-item-label'})
        # Value for each movie
        val = j.find_all('div', {'data-qa': 'movie-info-item-value'})
        # Cleaning string for each string
        lab = lab[0].text.strip()
        val = val[0].text.strip()
        val = re.sub("\s\s+", " ", val)
        # Putting values for each label info into a dictionary
        dic[lab.split(":")[0]] = val
    # Appending dictionary to dataframe
    dic = {key: value for key, value in dic.items() if key in df.columns}
    df = df.append(dic, ignore_index=True)

# Saving the dataframe as a csv file
df.to_csv("Top100_BeautifulSoup.csv", index=False)

# Print the time taken to get all movie info into a file using Beautiful soup method
print("Total time taken is:", time.time() - start_time)
