import tweepy, os

class Scraper():
    __slots__ = '_client', '_target'
    
    def __init__(self, bearer_token, target_username):
        self._client = tweepy.Client(bearer_token=bearer_token)
        self._target = self._client.get_user(username=target_username).data
    
    def get_newer_tweet(self):
        recent_tweets = self._client.get_users_tweets(
            id=self._target.id,
            max_results=5,
            tweet_fields=['id', 'text', 'created_at', 'public_metrics']
        )

        if not recent_tweets.data:
            raise ValueError(f'No tweets found in the {self._target.username} account.')

        first_tweet = recent_tweets.data[0]
        return first_tweet
    
    def get_replies(self, tweet):
        query = f'conversation_id:{tweet.id} is:reply'
        safe_max_results = max(10, min(tweet.public_metrics['reply_count'], 100))

        replies_response = self._client.search_recent_tweets(
            query=query,
            max_results=safe_max_results,
            tweet_fields=['author_id', 'created_at', 'id', 'text', 'lang']
        )
        
        return replies_response.data
    
    def save_as_files(self, parent, replies):
        base_path = os.path.join('replies', str(parent.id))
        os.makedirs(base_path, exist_ok=True)
        
        if replies:
            for reply in replies:

                file_path = os.path.join(base_path, f'{reply.id}.txt')
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f'created_at: {reply.created_at}\n')
                    f.write(f'is_clean: false\n')
                    f.write(f'lang: {reply.lang}\n')
                    f.write(f'text: {reply.text}')
        else:
            raise ValueError('None reply found.')
