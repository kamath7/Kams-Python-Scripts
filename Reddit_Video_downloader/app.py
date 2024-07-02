import requests, os 
url = input("Enter url")[:-1]+".json"
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})


data = r.json()[0]
video_url = data["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["fallback_url"]
print(video_url)

with open("video.mp4", "wb") as f:
    g = requests.get(video_url, stream=True)
    f.write(g.content)


    

