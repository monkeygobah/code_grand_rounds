import praw

def search_reddit_posts(keyword):
    reddit = praw.Reddit(
        client_id='6UOraNifVAl4iwAN0VePrw',
        client_secret='IOR8Axdyc7UqIHBfrJa1NvqVtmmFXg',
        user_agent='code_grand_rounds'  # This can be a simple string like "my_reddit_script"
    )

    # Search posts for the keyword in all of Reddit
    for post in reddit.subreddit('all').search(keyword, limit=10):
        print(f"Title: {post.title}, URL: {post.url}")

        # Get the ALL comments for the post
        post.comments.replace_more(limit=None)  
        # iterate through the comments
        for comment in post.comments.list():
            print(f"    Comment: {comment.body}")

search_reddit_posts('plasticsurgery')
