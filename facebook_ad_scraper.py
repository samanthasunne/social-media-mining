# STEP BY STEP INSTRUCTIONS

#1 Import your libraries. You must have BeautifulSoup installed (separately)
#2 Create an empty list object (called rows)
#3 Create a changeable folder name. This is so that other people can use this code and substitute their own username)
#4 Open the page
#5 Save the page as a Python object (called soup)
#6 Pull out the main div we want
#7 Make a list of all the sub divs in it
#8 For every subdiv, pull the text from two sub-subdivs
#9 Create field names for your dictionary and populate them with these sub-subdivs
#10 Make a row for each subdiv in the for loop, and append them to the "rows" list at the top
#11 Create a CSV and assign it to an object (csvfile)
#12 Define the field names for your CSV. They should be the same ones as in your dictionary
#13 Call DictWriter and store it as the writer object (I don't actually understand this part)
#14 Write a header row
#15 Write a row in your CSV of all the rows in your rows list


import csv
from bs4 import BeautifulSoup

rows = []

foldername = "facebook-samanthasunne"

with open("%s/ads_and_businesses/advertisers_you've_interacted_with.html" % foldername) as page:
	soup = BeautifulSoup(page,"html.parser")
	contents = soup.find("div", class_="_4t5n")
	ad_list = contents.find_all("div", class_="uiBoxWhite")

	for item in ad_list:
		advert = item.find("div", class_="_2let").get_text()
		metadata = item.find("div", class_="_2lem").get_text()
		row = { "advert": advert,
				"metadata": metadata
		}
		rows.append(row)

with open("%s-all-advertisers.csv" % foldername, "w+") as csvfile:
	fieldnames = ["advert", "metadata"]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for row in rows:
		writer.writerow(row)


