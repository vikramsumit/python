import requests

API_KEY = "8c7ea17830824de8b0767ff41723a9b7"
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Set the parameters (you can change country/category)
params = {
    "country": "us",               # 'us', 'in', 'gb', etc.
    "category": "technology",      # 'general', 'sports', 'business', etc.
    "category": "sports",      # 'general', 'sports', 'business', etc.
    "apiKey": API_KEY
}

def fetch_news():
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Debug print (optional)
    # print(data)

    if data['status'] == 'ok':
        articles = data['articles']
        if not articles:
            print("No articles found for this category and country.")
            return

        for idx, article in enumerate(articles[:10], start=1):
            print(f"\n{idx}. {article['title']}")
            print(f"   👉 {article.get('description', 'No description')}")
            print(f"   🔗 {article['url']}")
    else:
        print("❌ Error fetching news:", data.get("message", "Unknown error"))

if __name__ == "__main__":
    print("📰 Top Tech Headlines:\n")
    fetch_news()
