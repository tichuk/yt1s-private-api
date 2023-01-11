"""Module only used for parsing the download link/s from yt1s.com"""

import requests, json

def convert_res(resolution):

    if resolution == "auto":        res = "auto"
    elif resolution == "1080p":     res = "137"
    elif resolution == "720p":      res = "22"
    elif resolution == "480p":      res = "135"
    elif resolution == "360p":      res = "18"
    elif resolution == "240p":      res = "133"
    elif resolution == "144p":      res = "160"

    else: res = "auto"

    return res

def ext_video_id(video_url):
    fo = "https://youtu.be/"
    foo = "https://youtube.com/watch?v="

    if fo in video_url:        video_id = video_url.replace(fo, '')
    elif foo in video_url:     video_id = video_url.replace(foo, '')
    else:                      video_id = None

    return video_id

def yt1s_api_payload_k(video_url, resolution):
    
    url = "https://yt1s.com/api/ajaxSearch/index"
    payload = {'q': video_url, 'vt': 'home'}    
    response = requests.post(url, data=payload)
    json_response_obj = json.loads(response.text)
    res = convert_res(resolution)
    k_post_payload = json_response_obj["links"]["mp4"][res]["k"]

    return k_post_payload

def ext_dl_link(video_id, video_url, res):
    
    url = "https://yt1s.com/api/ajaxConvert/convert"
    payload = {'vid': video_id,'k': yt1s_api_payload_k(video_url, res)}
    response = requests.post(url, data=payload)
    video_dl_json = response.json()
    video_dl_link = video_dl_json["dlink"]

    return video_dl_link
