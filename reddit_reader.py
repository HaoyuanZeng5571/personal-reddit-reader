import os
import praw

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="macos:personal-reddit-reader:v1.0 (by /u/Financial_Bet944)"
)


def search_posts(query, limit=20):
    results = reddit.subreddit("all").search(
        query,
        sort="new",
        limit=limit
    )

    posts = []

    for post in results:
        posts.append({
            "post_id": post.id,
            "title": post.title,
            "subreddit": str(post.subreddit),
            "score": post.score,
            "num_comments": post.num_comments,
            "url": post.url
        })

    return posts


if __name__ == "__main__":
    posts = search_posts("investing", limit=10)

    for post in posts:
        print(post["title"])
