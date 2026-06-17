import requests
from bs4 import BeautifulSoup
import re
import argparse

parser = argparse.ArgumentParser(description="Scrape JavaScript file for hidden API endpoints")
parser.add_argument("url", help="The URL of the website to scrape")
args = parser.parse_args()

url = args.url
if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
pattern1 = r'["\']((?:/api/|/v\d/|/graphql|/auth/|/user/|/admin/|/rest/|/gql/)[^"\'?\s]{1,100})["\']'
pattern2 = r'fetch\(["\']([^"\']+)["\']'

total_matches_found = 0

script_tags = soup.find_all("script", src=True)
for tag in script_tags:
    
    js_url = tag["src"]
    print(js_url)


    if js_url.startswith("/"):
        js_url = url + js_url
    elif not js_url.startswith("http"):
        js_url = url + "/" + js_url


    js_response = requests.get(js_url)
    js_content = js_response.text

    matches1 = re.findall(pattern1, js_content)
    matches2 = re.findall(pattern2, js_content)
    all_matches = list(set(matches1 + matches2))
    
    if all_matches:
        print(f"Found API endpoints in {js_url}")
        total_matches_found += 1

        for match in all_matches:
            print(f"Found API Route: {match}")

if total_matches_found == 0:
    print("\nNo hidden API endpoints found on this entire website.")


        