import requests
import csv

import os

# Function to load API key from a file
def load_api_key():
    try:
        with open("virustotal_api_key.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("API key file 'virustotal_api_key.txt' not found. Please add it to the project folder.")

# Use the API key
API_KEY = load_api_key()


BASE_URL = "https://www.virustotal.com/api/v3"

# Function to fetch domain info from VirusTotal
def fetch_domain_info(domain):
    url = f"{BASE_URL}/domains/{domain}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        stats = data.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
        reputation = data.get('data', {}).get('attributes', {}).get('reputation', "Unknown")
        return {
            "domain": domain,
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
            "undetected": stats.get("undetected", 0),
            "reputation": reputation
        }
    else:
        print(f"Error fetching data for {domain}: {response.status_code}")
        return None

# Function to save data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Main script execution
if __name__ == "__main__":
    # List of domains to check
    domains = ["niftypm.com", "quizlet.com", "github.com", "trello.com", "when2meet.com", "notion.com",
               "amazon.com", "nytimes.com", "verify-my-account.org", "win-free-prize-now.com",
                "support-help-desk.net", "cofc.edu", "learn.zybooks.com", "bankofamerica.com", "reddit.com", "youtube.com" ]
    results = []

    for domain in domains:
        print(f"Fetching data for {domain}...")
        info = fetch_domain_info(domain)
        if info:
            results.append(info)

    # Save the results to a CSV file
    if results:
        output_file = "data/domain_data.csv"
        save_to_csv(results, output_file)
        print(f"Data saved to {output_file}")
    else:
        print("No data to save.")
