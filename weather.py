import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.bing.com/search?q=weather+{city}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = soup.find('div', attrs={'class': 'b_hide'}).text
        return temp
    else:
        return "Failed to retrieve weather information"

# Example usage
city = "New York"
weather = get_weather(city)
print(weather)
