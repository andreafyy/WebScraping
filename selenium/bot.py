# Import all necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from collections import defaultdict
import time
import pandas as pd
import re

# Chromedriver
gecko_path = 'C:\\Users\\Divij Pherwani\\AppData\\Local\\Programs\\Python\\Python39\\chromedriver.exe'

# Rotten Tomatoes URL
url = 'https://www.rottentomatoes.com/'

# Setting driver
options = webdriver.chrome.options.Options()
options.headless = False
driver = webdriver.Chrome(options=options, executable_path=gecko_path)

# Actual Program
driver.get(url)
print(driver.page_source)

time.sleep(2)

# Hover to "Movies" option
M = driver.find_element_by_xpath('/html/body/div[4]/header/nav/div[2]/ul/li[1]')
hover = ActionChains(driver).move_to_element(M)
hover.perform()
time.sleep(5)

# Click "Top Movies" in "Movies" menu option
DM = driver.find_element_by_xpath('/html/body/div[4]/header/nav/div[2]/ul/li[1]/div/section[3]/ul/li[1]')
DM.click()
time.sleep(5)

# Click on "View All" in "Best Movies of All time" list
Top = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[3]/div[4]/section/div/div/a')
Top.click()
time.sleep(5)

# Start time for the program
start_time = time.time()

r = []
for i in range(100):
    path = "/html/body/div[5]/div[2]/div[1]/section/div/table/tbody/tr[" + str(i + 1) + "]/td[3]/a"
    d = driver.find_element_by_xpath(path).get_attribute("href")
    r.append(d)

# Setting up pandas dataframe
df = pd.DataFrame(columns=['Name', 'Link', 'Rating', 'Box Office (Gross USA)', 'Genre', 'Original Language', 'Director', 'Producer', 'Writer',
                           'Release Date (Streaming)', 'Release Date (Theaters)', 'Runtime', 'Production Co', 'Aspect Ratio', 'Sound Mix'])

# Looping around all links of movies in list and extracting movie specific information
for i in r:
    # Go to movie specific web page
    driver.get(i)
    # Get name of the movie
    name = driver.find_element_by_xpath('/html/body/div[5]/div[3]/section/div[2]/div[2]/score-board/h1').text
    # Declaring and initializing dictionary
    dic = defaultdict()
    dic = {'Name': name, 'Link': i}
    # Extracting Movie specific information
    for j in range(1, 15):
        try:
            # finding labels and values by xpath
            lab = driver.find_element_by_xpath(
                '/html/body/div[5]/div[3]/section/div[2]/section[*]/div/div/ul/li[' + str(j) + ']/div[1]').text
            val = driver.find_element_by_xpath(
                '/html/body/div[5]/div[3]/section/div[2]/section[*]/div/div/ul/li[' + str(j) + ']/div[2]').text
            # Cleaning text of label and value
            lab = lab.strip()
            val = val.strip()
            val = re.sub("\s\s+", " ", val)
            lab = lab.split(":")[0]
            dic[lab] = val
        except NoSuchElementException:
            pass

    # Appending dictionary to dataframe
    dic = {key: value for key, value in dic.items() if key in df.columns}
    df = df.append(dic, ignore_index=True)

# Saving the dataframe as a csv file
df.to_csv("Top100_Selenium.csv", index=False)

# Print the time taken to get all movie info into a file using Selenium method
print("Total time taken is:", time.time() - start_time)

time.sleep(3)

# Close program
driver.quit()
