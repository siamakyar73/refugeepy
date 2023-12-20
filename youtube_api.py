from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Specify the video ID for which you want to scrape comments
video_id = 'ZY_AfUcftiM'

# Request the comments for the specified video
next_page_token = None
comments = []

while True:
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token
    ).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comment_text = comment['textDisplay']
        comment_length = len(comment_text)
        comment_date = comment['publishedAt']
        comments.append({
            'text': comment_text,
            'length': comment_length,
            'date': comment_date
        })

    # Check if there are more pages of comments
    if 'nextPageToken' in response:
        next_page_token = response['nextPageToken']
    else:
        break

# Store the comments in a csv file

import pandas as pd
df=pd.DataFrame(comments)
df.to_csv('cy4.csv')

