import requests
import time
from colorama import Fore
import argparse

print("""
 ▌▘      ▘▐▘▐▘    
▛▌▌▛▘▛▘▛▌▌▜▘▜▘█▌▛▘
▙▌▌▌ ▄▌▌▌▌▐ ▐ ▙▖▌ 
                                
""")


class sets:
    parser = argparse.ArgumentParser(description="Basic Dir Sniffer")
    parser.add_argument("-u", "--url", required=True, help="Search URL (For Exemple: https://exemple.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist for search")

    args = parser.parse_args()

    url = args.url
    wordlist_path = args.wordlist

    print(f"Search Url: {url}")
    print(f"Wordlist Path: {wordlist_path}")
    speed = float(input("Searches per Second: "))

@staticmethod
def reader():
    words = []
    try:
        with open(sets.wordlist_path, 'r') as payload:
            words = payload.read().splitlines()
    except FileNotFoundError:
        print("The file was not found.")
    return words



if __name__ == "__main__":
    
    
    words = reader()
    delay = 1 / sets.speed if sets.speed > 0 else 0


    for word in words:
        full_url = f"{sets.url}{word}"
        try:
            response = requests.get(full_url)
            if response.status_code == 404:
                print(Fore.RED, f"[{response.status_code}] {full_url}")
            elif response.status_code >= 200:
                print(Fore.GREEN,f"[{response.status_code}] {full_url}")
            else:
                print(Fore.BLUE,f"[{response.status_code}] {full_url}")
            
            
        except requests.RequestException as e:
            print(Fore.RED,f"[ERROR] Failed to connect to {full_url}: {e}")
        time.sleep(delay)