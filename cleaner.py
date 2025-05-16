import re, string, os
from langs_map import lang_code_map
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer, SnowballStemmer

class Cleaner():
    
    def __init__(self):
        self.rslp = RSLPStemmer()
        self.snowball = {
            'english': SnowballStemmer("english"),
            'spanish': SnowballStemmer("spanish"),
            'french': SnowballStemmer("french"),
        }
        self.emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            u"\U00002700-\U000027BF"
            u"\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE
        )

    def clean_text(self, text, text_lang):
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        text = self.emoji_pattern.sub(r'', text)

        text = text.translate(str.maketrans('', '', string.punctuation))
        
        language = lang_code_map.get(text_lang, 'portuguese')

        tokens = text.lower().split()
        stop_words = set(stopwords.words(language))
        filtered_words = []
        for word in tokens:
            if word in stop_words or not word.isalpha():
                continue
            
            if language == 'portuguese':
                stemmed = self.rslp.stem(word)
            elif language in self.snowball:
                stemmed = self.snowball[language].stem(word)
            else:
                stemmed = word

            filtered_words.append(stemmed)

        return ' '.join(filtered_words)

    def clean_all_replies(self, base_path='replies'):
        for tweet_id in os.listdir(base_path):
            tweet_path = os.path.join(base_path, tweet_id)
            if not os.path.isdir(tweet_path):
                continue

            for file in os.listdir(tweet_path):
                if not file.endswith('.txt'):
                    continue

                file_path = os.path.join(tweet_path, file)

                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                file_created_at = ''
                file_is_clean = False
                file_lang = ''

                raw_text = ''
                for line in lines:
                    if line.startswith('created_at:'):
                        file_created_at = line[11:].strip()
                        continue
                    if line.startswith('is_clean:'):
                        is_file_clean_str = line[9:].strip()
                        if is_file_clean_str == 'true':
                            file_is_clean = True
                            break
                    if line.startswith('lang:'):
                        file_lang = line[5:].strip()
                        continue
                    if line.startswith('text:'):
                        raw_text = line[5:].strip()
                        break
                
                if file_is_clean:
                    continue

                cleaned_text = self.clean_text(raw_text, file_lang)

                clean_file_path = os.path.join(tweet_path, str(file))
                with open(clean_file_path, 'w', encoding='utf-8') as f:
                    f.write(f'created_at: {file_created_at}\n')
                    f.write(f'is_clean: true\n')
                    f.write(f'lang: {file_lang}\n')
                    f.write(f'text: {raw_text}\n')
                    f.write(f'cleaned_text: {cleaned_text}')
