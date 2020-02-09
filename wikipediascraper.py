# Need to have python3 installed or you'll run into ASCII errors
# If you have python3, you can't run it unless you start with 'python3' (not 'python')
# Need to have Beautiful Soup and requests installed under python3 - have to install them with 'pip3 install BeautifulSoup4' and 'pip3 install requests' as opposed to 'pip install requests'

# I skipped the identify yourself step

# There only seemed to be one Wikipedia page on women computer scientists, so I had a list of one url

# Got a "Not Found" error message for .find_all('div', class_='mw-category-group'), so I changed the .find and .find_all functions to use single quotes intead of double quotes. This worked

import csv
import time
from bs4 import BeautifulSoup
import requests

rows=[]

urls = ["https://en.wikipedia.org/wiki/Category:Women_computer_scientists"]

def scrape_content(url):
	time.sleep(2)
	page = requests.get(url)
	page_content = page.content
	soup = BeautifulSoup(page_content, "html.parser")
	content = soup.find('div', class_='mw-category')
	all_groupings = content.find_all('div', class_='mw-category-group')
	for grouping in all_groupings:
		names_list = grouping.find("ul")
		category = grouping.find("h3").get_text()
		alphabetical_names = names_list.find_all("li")
		for alphabetical_name in alphabetical_names:
			name = alphabetical_name.text
			anchortag = alphabetical_name.find("a",href=True)
			link = anchortag["href"]
			letter_name = category
			row = { "name": name,
					"link": link,
					"letter_name": letter_name}
			rows.append(row)

for url in urls:
	scrape_content(url)

with open("all-women-computer-scientists.csv", "w+") as csvfile:
	fieldnames = ["name", "link", "letter_name"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for row in rows:
		writer.writerow(row)
