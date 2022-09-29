import requests
import objectpath
import json
import urllib.request
from moviepy.editor import *
from pytube import YouTube

CLIENT_ID = "dRx3MqCjlQnXU-XRgF4xIg"
SECRET_TOKEN = "FMDZ6J21EVcANnhIb_hejhHbKBbk0w"
USERNAME = "QuarterIcey"
PASSWORD = "1monkeys"
# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
print(TOKEN)

res = requests.get("https://oauth.reddit.com/r/tiktokcringe",
                   headers=headers)
allvideos = []
print(res.json)
tree_obj = objectpath.Tree(res.json())
content = (tuple(tree_obj.execute('$.data.children.data.media_embed.content')))
c = 5
url = ""
for i in content:       
        urlc = i.find("src")
        while i[urlc+c] != "?":
                 url += (i[urlc+c])
                 c = c + 1
        c = 5        
        print(url)
        print("https://www.youtube.com/watch?v="+url[30:])
        yt = YouTube("https://www.youtube.com/watch?v="+url[30:])
        ys = yt.streams.get_highest_resolution()
        ys.download()
        allvideos.append(yt.title+".mp4")
        url = ""
        next
        
fallbackurl = (tuple(tree_obj.execute('$.data.children.data.secure_media.reddit_video.fallback_url')))
print(type(fallbackurl))

output_path = ".mp4"

for i in fallbackurl:
        try:

                print(i)
                vidname ="./videos/" + i[18:26]+ ".mp4"
                urllib.request.urlretrieve(
                        i,
                        filename=(vidname),
                        )
                newAudio= i[:37] + "audio.mp4?source=fallback" 
                print(newAudio)
                audioname = "./videos/" + i[18:26]+"audio"+".mp4"
                urllib.request.urlretrieve(
                        newAudio,
                        filename=(audioname),
                        )
                print(i[18:26]+ ".mp4")
        
                clip = VideoFileClip(vidname)
                audioclip = AudioFileClip(audioname)
                videoclip = clip.set_audio(audioclip)
                duration = clip.duration
                print(duration)
                if duration <= 35 and duration >= 5:
                         allvideos.append(videoclip)
        except:
                print("error")
                print(i[18:26]+ ".mp4")
finalClip = concatenate_videoclips(allvideos, method="compose")      
finalClip.write_videofile("meme3.mp4", threads = 8)
  

  
