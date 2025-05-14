import tweepy, os, time
from dotenv import load_dotenv

load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=bearer_token)

user_response = client.get_user(username="CNN")
user_id = user_response.data.id

recent_tweets = client.get_users_tweets(
    id=user_id,
    max_results=5,
    tweet_fields=["id", "text", "created_at", "public_metrics"]
)

if not recent_tweets.data:
    print(f"Nenhum tweet encontrado de @{user_response.data.username}.")
    exit()

tweet_parent = recent_tweets.data[0]
tweet_id = tweet_parent.id

print(f"Tweet mais recente da conta @{user_response.data.username}:")
print('-------------------------------------------')
print(f"[{tweet_parent.created_at}] {tweet_parent.text}")
print(f"Tweet ID: {tweet_id}")
print('-------------------------------------------')

query = f"conversation_id:{tweet_id} is:reply"
safe_max_results = max(10, min(tweet_parent.public_metrics["reply_count"], 100))

replies_response = client.search_recent_tweets(
    query=query,
    max_results=safe_max_results,
    tweet_fields=["author_id", "created_at", "id", "text"]
)

base_path = os.path.join("replies", str(tweet_id))
os.makedirs(base_path, exist_ok=True)

print("\nRespostas ao tweet:")
print('-------------------------------------------')
if replies_response.data:
    for reply in replies_response.data:

        print(f"[{reply.created_at}] {reply.text}")
        print('-------------------------------------------')

        file_path = os.path.join(base_path, f"{reply.id}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"date: {reply.created_at}\n")
            f.write(f"get_date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"text: {reply.text}")
else:
    print("Nenhuma resposta encontrada.")
