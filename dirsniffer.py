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
    parser.add_argument("-u", "--url", required=True, help="Search URL (For Example: https://example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist for search")
    parser.add_argument("-t", "--searchpersecond", required=True, type=int, help="Search per Second")

    args = parser.parse_args()

    speed = args.searchpersecond
    url = args.url
    wordlist_path = args.wordlist

    print(f"Search URL: {url}")
    print(f"Wordlist Path: {wordlist_path}")
    print(f"Search per Second: {speed}")


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
