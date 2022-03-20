
import pandas as pd
from selenium.webdriver.common.keys import Keys
import pyautogui

from rsc import *
from webdriver_manager.chrome import ChromeDriverManager


#Put csv file containing DOIs from CSD or the search query here
df = pd.read_csv('FILE PATH')

#go to https://doi-org.sheffield.idm.oclc.org/ and sign in when the Chrome window pops up
chrome = webdriver.Chrome(ChromeDriverManager().install())
login_url = 'https://doi-org.sheffield.idm.oclc.org/'
chrome.get(login_url)
time.sleep(30)

#The title of the file name is a number starting at n
n = 1
#Make sure there are no duplicate DOIs then this script will automatically download all HTML files
for doi in df['DOI']:
    chrome.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    url = 'https://doi-org.sheffield.idm.oclc.org/' + str(doi)
    chrome.get(url)
    time.sleep(7)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    n += 1
    pyautogui.typewrite(str(n)+'.html')
    time.sleep(5)
    pyautogui.hotkey('enter')
    time.sleep(10)


