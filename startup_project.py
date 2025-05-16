import subprocess
import sys
import os
import nltk

def install_requirements():
    print("[1/4] Checando dependências via pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"])

def download_nltk_data():
    print("[2/4] Checando dependências do NLTK...")
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
    try:
        nltk.data.find('corpora/rslp')
    except LookupError:
        nltk.download('rslp', quiet=True)

def run_main_script():
    print("[3/4] Executando o programa principal...")
    subprocess.run([sys.executable, "main.py"], check=True)

def final_message():
    print("[4/4] Finalizado com sucesso!")

if __name__ == "__main__":
    install_requirements()
    download_nltk_data()
    run_main_script()
    final_message()
