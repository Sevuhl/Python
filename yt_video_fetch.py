'''This module is built specifically to take a singular Youtube channel ID
    and scrape all the videos for the following information : Published Date,
    Title, Description, and thumnailURL. I learned this from the "Mining Social
    Media" book written by Lam Thuy Vo. It is thanks to her ability to teach
    I am sharing this.'''

import requests
import json
import csv

channel_id = '' #Please insert Youtube Channel ID
yt_api_key = '' #Please insert YOUR API yt_api_key

base = 'https://www.googleapis.com/youtube/v3/search?'
fields = '&part=snippet&channelId='
api_key = '&key=' + yt_api_key
api_call = base + fields + channel_id + api_key
api_requests = requests.get(api_call)
videos = json.loads(api_requests.text)

# Change the first parameter of the with-open statement
# to a filename of your choice.
with open('default_name.csv', 'w') as video_file:
    csv_writer = csv.writer(video_file)
    csv_writer.writerow(['PublishedOn',
                        'Title',
                        'Description',
                        'ThumbnailURL'])
    next_page_available = True
    while next_page_available:
        if videos.get("items") is not None:
            for video in videos.get("items"):
                video_data = [
                            video['snippet']['publishedAt'],
                            video['snippet']['title'],
                            video['snippet']['description'],
                            video['snippet']['thumbnails']['default']['url']
                ]
                csv_writer.writerow(video_data)
        if "nextPageToken" in videos.keys():
            next_page_url = api_call + "&pageToken="+videos["nextPageToken"]
            next_page_videos = requests.get(next_page_url)
            videos = json.loads(next_page_videos.text)
        else:
            print("We have reached the end for videos on this Channel.")
            next_page_available = False
