import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if "title" in s:
        m = re.search(r'(https?://(www\.)?youtube\.com/embed/.+ title)',s.strip())
    else:
        m = re.search(r'(https?://(www\.)?youtube\.com/embed/.+></iframe>)',s.strip())

    if m:
        final_url = m.group(1)
        final_url = final_url.replace("youtube.com/embed","youtu.be")
        final_url = final_url[:final_url.find('"')]
        if "www" in final_url:
            final_url = final_url.replace("www.","")
        if "http:" in final_url:
            final_url = final_url.replace("http:", "https:")
        return final_url
    else:
        return None

if __name__ == "__main__":
    main()
