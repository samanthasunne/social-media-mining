# This script scrapes multiple pages of MisinfoCon YouTube videos. MisinfoCon's channel ID is "UCYJ6tcB8PpBZjP7gW8I6Mew"

# You need an API key to run this. Put your API key in Line 17.

# This can take a LONG time to run depending on how many videos the channel has.


import csv
import json
import requests

channel_name = "MisinfoCon"

channel_id = "UCYJ6tcB8PpBZjP7gW8I6Mew"

youtube_api_key = "put your API key here"

def make_csv(page_id):
	base = "https://www.googleapis.com/youtube/v3/search?"
	fields = "&part=snippet&channelId="
	api_key = "&key=" + youtube_api_key
	api_url = base + fields + page_id + api_key
	api_response = requests.get(api_url)
	videos = json.loads(api_response.text)
	with open("%s_youtube_videos.csv" % channel_name, "w") as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow(["publishedAt",
			"title",
			"description",
			"thumbnailurl"])
		has_another_page = True
		while has_another_page:
			if videos.get("items") is not None:
				for video in videos.get("items"):
					video_data_row = [
					video["snippet"]["publishedAt"],
					video["snippet"]["title"],
					video["snippet"]["description"],
					video["snippet"]["thumbnails"]["default"]["url"]
					]
					csv_writer.writerow(video_data_row)
				if "nextPageToken" in videos.keys():
					next_page_url = api_url + "&pageToken=" + videos["nextPageToken"]
					next_page_posts = requests.get(next_page_url)
					videos = json.loads(next_page_posts.text)
				else:
					print("no more videos!")
					has_another_page = False

make_csv(channel_id)