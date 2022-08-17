from bs4 import BeautifulSoup as soup, BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
import Post

my_url = "https://www.marketwatch.com/economy-politics/calendar"
week_days = ['MONDAY', 'TUESDA', 'WEDNES', 'THURSD', 'FRIDAY']
client = uReq(my_url)
count = 0
next_week = 0

page_html = client.read()
page_soup = BeautifulSoup(page_html, 'html.parser')
message = ('\t\t_Keeping up with the FED brought to you by Market Watch_ \n\n' 
      '\t\t*U.S Economic Calendar for the Next two weeks*\n\n')
for tr_tags in page_soup.find_all('tr'):
    if count == 1 and next_week == 1:
        message = message + "\n\t\t\t*NEXT WEEK* \n"
    if count < 3:
        for td_tags in tr_tags.find_all('td'):
            tag_text = td_tags.get_text()
            #print(tag_text)
            if tag_text != "":
                if tag_text[0:6] in week_days:
                    #print(tag_text)
                    if tag_text[0:6] == 'MONDAY':
                        count += 1
                    if count < 3:
                        message = message + '\n' + "*" + tag_text + "*"
                elif 'am' in tag_text:
                    #print(tag_text)
                    message = message + '\n' + tag_text
                    data = 1
                elif 'pm' in tag_text:
                    #print(tag_text)
                    message = message + '\n' + tag_text
                    data = 1
                elif data == 1:
                    #print(tag_text)
                    message = message + '\n' + tag_text
                    data = 0
        message = message + "\n"
client.close()
Post.main(message)
#print(message)