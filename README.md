# yt1s-private-api

A Small Python code that wraps free unauthenticated api from [yt1s.com](https://yt1s.com)


## Install

Install requests using pip:

``pip install requests``

Downlaod the latest module using wget:

``wget https://raw.githubusercontent.com/tichuk/yt1s-private-api/main/yt1s_dl.py``

### Example Usage

```python
from yt1s_dl import ext_dl_link
from yt1s_dl import ext_video_id

video_url = "https://youtu.be/rUWxSEwctFU" # <- YOUR VIDEO URL
res = "1080p" # <- DESIRED RESOLUTION (1080p, 720p, 480p, 360p, 240p, 144p, auto)

video_id = ext_video_id(video_url)

print(ext_dl_link(video_id, video_url, res))
```

## Disclaimer
This is an unofficial API. Use at your own risk.
