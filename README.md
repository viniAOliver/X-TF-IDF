[![Typing SVG](https://readme-typing-svg.demolab.com?font=Pixelify+Sans&weight=600&size=42&letterSpacing=0.2rem&duration=7000&pause=2000&color=1DA1F2&vCenter=true&width=435&lines=X-TF-IDF)](https://git.io/typing-svg)

### About the Project
X-TF-IDF is a Python-based tool for collecting and analyzing Twitter posts. It uses web scraping with the API access to extract tweets from [X/Twitter](https://x.com/) and applies the TF-IDF (Term Frequency–Inverse Document Frequency) model to evaluate term relevance across the collected dataset. This tool is ideal for trend analysis, opinion mining, and NLP vectorization experiments.

### About TF-IDF
TF-IDF is a technique in Natural Language Processing (NLP) that transforms textual data into numerical vectors based on the relative importance of words. It highlights terms that are frequent in individual documents but infrequent across the entire corpus, helping to identify what is truly significant.

### Project Goals
The X-TF-IDF project aims to provide a practical and extensible implementation of text analysis focused on X/Twitter data. It is:

- **100% Python**, using well-known libraries such as `requests`, `beautifulsoup4`, `tweepy`, `scikit-learn`, and `pandas`.
- **User-friendly**, with command-line scripts for tweet scraping and TF-IDF matrix generation. Also a website for searching and testing.
- **Extensible**, allowing adaptation for other X/Twitter accounts sources.
- **Open-source only**, with no reliance on commercial software or APIs beyond X/Twitter API usage.

### Installation and Usage

Clone the repository:

```bash
$ git clone https://github.com/viniAOliver/X-TF-IDF.git
$ cd X-TF-IDF
$ python startup_project.py
