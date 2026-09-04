"""
Task 3: Web Scraper for News Headlines
Tools used: Python, requests, BeautifulSoup4
Description: Fetches top news headlines from a public news site (BBC News),
             parses headline HTML tags (h2/h3), cleans the data, prints to console,
             and saves the resulting headlines to a text file.
"""

import os
import sys
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Target News Website URL
TARGET_URL = "https://www.bbc.com/news"
OUTPUT_FILE = "headlines.txt"

# HTTP Headers including a realistic User-Agent to avoid request blocking
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_html(url: str) -> str:
    """
    Fetches the HTML content of the target URL using HTTP GET request.
    Includes exception handling for network/HTTP errors.
    """
    print(f"[*] Fetching HTML content from: {url}...")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        # Raise HTTPError if status code is 4xx or 5xx
        response.raise_for_status()
        print(f"[+] Successfully fetched web page (Status Code: {response.status_code})")
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"[!] HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"[!] Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"[!] Request timed out: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"[!] An error occurred during request: {err}")
    return ""

def extract_headlines(html_content: str) -> list[str]:
    """
    Parses HTML content using BeautifulSoup to locate news headline tags (e.g. <h2>).
    Cleans text, filters out noise, and eliminates duplicates.
    """
    if not html_content:
        return []

    print("[*] Parsing HTML and extracting headline tags (<h2>/<h3>)...")
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Locate headline elements - typically <h2> tags on BBC News
    headline_elements = soup.find_all(["h2", "h3"])
    
    headlines = []
    seen = set()

    for elem in headline_elements:
        text = elem.text.strip()
        # Filter out short or duplicate titles
        if text and len(text) > 10 and text not in seen:
            seen.add(text)
            headlines.append(text)

    print(f"[+] Extracted {len(headlines)} unique headlines.")
    return headlines

def save_headlines_to_file(headlines: list[str], filepath: str) -> None:
    """
    Saves extracted headlines into a formatted text file.
    """
    if not headlines:
        print("[!] No headlines available to save.")
        return

    print(f"[*] Saving headlines to '{filepath}'...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write("====================================================\n")
            file.write(f"           TOP NEWS HEADLINES - SCRAPED DATA         \n")
            file.write(f" Source: {TARGET_URL}\n")
            file.write(f" Timestamp: {timestamp}\n")
            file.write(f" Total Headlines: {len(headlines)}\n")
            file.write("====================================================\n\n")

            for idx, headline in enumerate(headlines, start=1):
                file.write(f"{idx:02d}. {headline}\n")

        print(f"[+] Successfully saved {len(headlines)} headlines to '{filepath}'")
    except IOError as io_err:
        print(f"[!] Error writing to file '{filepath}': {io_err}")

def main():
    """
    Main function executing the scraping workflow.
    """
    print("=" * 60)
    print("      Task 3: News Headline Scraper (Python + BeautifulSoup)")
    print("=" * 60)

    # Step 1: Fetch HTML
    html = fetch_html(TARGET_URL)
    if not html:
        print("[!] Execution aborted due to fetch failure.")
        sys.exit(1)

    # Step 2: Extract Headlines
    headlines = extract_headlines(html)
    if not headlines:
        print("[!] No headlines found.")
        sys.exit(1)

    # Display Top 10 Headlines in Console
    print("\n--- Preview of Top 10 Extracted Headlines ---")
    for idx, title in enumerate(headlines[:10], start=1):
        print(f"{idx:02d}. {title}")
    print("---------------------------------------------\n")

    # Step 3: Save to .txt file
    save_headlines_to_file(headlines, OUTPUT_FILE)
    print("\n[+] Task 3 Web Scraper execution completed successfully.")

if __name__ == "__main__":
    main()
