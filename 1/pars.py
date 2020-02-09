from bs4 import BeautifulSoup
import urllib.request


req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()


soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item')

results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

file = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    file.write(f'Новость # {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: https://www.ua-football.com{item["href"]}\n\n')
    i += 1
file.close()

print(results)


