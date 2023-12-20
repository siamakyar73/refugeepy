import praw
import pandas as pd
from datetime import datetime
# Initialize the Reddit API client
reddit = praw.Reddit(client_id='Your_id',
                     client_secret='secret_key',
                     user_agent='windows:com.example.myredditapp:v1.0.0 (by /u/username)')

# Specify the URL of the Reddit post
post_url = 'https://www.reddit.com/r/unitedkingdom/comments/13dl3nu/suella_braverman_says_illegal_immigration_out_of/'

# Get the post ID from the URL
post_id = reddit.submission(url=post_url).id

# Get the submission object
submission = reddit.submission(id=post_id)

# Fetch the comments for the submission
submission.comments.replace_more(limit=None)

# Create lists to store comment data
comment_texts = []
comment_lengths = []
comment_dates = []

# Iterate over the comments and collect their data
for comment in submission.comments.list():
    comment_texts.append(comment.body)
    comment_lengths.append(len(comment.body))
    comment_dates.append(datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'))

# Create a DataFrame from the collected comment data
data = {
    'Text': comment_texts,
    'Length': comment_lengths,
    'Date': comment_dates
}
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('red10.csv', index=True)
