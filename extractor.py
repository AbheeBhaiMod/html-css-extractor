import requests, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = input("Enter Website URL: ")
folder = "extracted_site"
os.makedirs(folder, exist_ok=True)

res = requests.get(url)
html = res.text
with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("link", rel="stylesheet")

for i, link in enumerate(links):
    css_url = urljoin(url, link.get("href"))
    try:
        css_res = requests.get(css_url)
        with open(f"{folder}/style_{i+1}.css", "w", encoding="utf-8") as f:
            f.write(css_res.text)
        print(f"✔ Saved: style_{i+1}.css")
    except:
        print(f"✘ Failed to fetch: {css_url}")

print("\n✅ Done! Check the 'extracted_site/' folder.")