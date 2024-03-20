import requests, sys

def request(url):
    try:
        res = requests.get("https://" + url)
        if(res):
            print("[+] Subdomain discovered: " + url)
    except:
        pass


def main():
    # Target Url
    targetURL = sys.argv[1]

    # Open subdomain word list
    with open("./Files/subdmainwordlist.txt", "r") as wordlist:
        for line in wordlist:
            word = line.strip()
            
            testURL = word + "." + targetURL
            request(testURL)


main()