import requests

# Your NewsAPI key (replace with your own)
API_KEY = '8c7ea17830824de8b0767ff41723a9b7'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Set country and category
params = {
    'country': 'in',           # 'us' for USA, 'in' for India, etc.
    'category': 'technology',  # general, sports, tech, health, etc.
    'apiKey': API_KEY
}

def fetch_news():
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data['status'] == 'ok':
        articles = data['articles']
        for idx, article in enumerate(articles[:10], start=1):
            print(f"\n{idx}. {article['title']}")
            print(f"   👉 {article['description']}")
            print(f"   🔗 {article['url']}")
    else:
        print("Error fetching news:", data.get("message", "Unknown error"))

if __name__ == "__main__":
    print("📰 Top Tech Headlines:\n")
    fetch_news()
