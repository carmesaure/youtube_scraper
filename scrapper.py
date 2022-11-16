import json
import requests
import re

from bs4 import BeautifulSoup



class Video:
    id: str
    title: str
    description: str
    author: str 
    likes: str

    def __init__(self, id) -> None:
        self.id = id
        self.title = None
        self.description = None
        self.author = None
        self.likes = None

    def get_infos_dict(self):
        r = requests.get("https://www.youtube.com/watch?v="+self.id)
        page = r.text

        soup = BeautifulSoup(page, 'html.parser')
        script_content = soup.body.script.string
        infos = json.loads(script_content[30:-1])

        return infos["videoDetails"]
    
    def get_infos_likes(self):
        r = requests.get("https://www.youtube.com/watch?v="+self.id)
        page = r.text

        soup = BeautifulSoup(page, 'html.parser')
        script_content = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
        infos = json.loads(script_content)  

        with open("script.json", "w") as f:
            json.dump(infos, f, indent = 4)

        likes_info = infos['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']  
        
        likes_str = likes_info.split('\u00a0')[0].replace('\u202f','')  
        return '0' if likes_str == 'Aucun' else likes_str

    def set_video_infos(self):
        infos = self.get_infos_dict()
        likes_info = self.get_infos_likes()

        self.title = infos["title"]
        self.description = infos["shortDescription"]
        self.author = infos["author"]
        self.likes = likes_info


        
        


f = open("input.json")
data = json.load(f)
ids_list = data["videos_id"]
f.close()

video_infos_list = []

for id in ids_list:
    video = Video(id)
    video.set_video_infos()
    video_infos_list.append(vars(video))


with open("output.json", "w") as f:
    json.dump(video_infos_list, f, indent = 4)

