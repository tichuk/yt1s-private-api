# yt1s-private-api

A Small Python code that wraps free unauthenticated api from [yt1s.com](https://yt1s.com)


## Install

Install requests and json using pip:

``pip install requests json``

Downlaod the latest repository using git:

``git clone https://github.com/tichuk/yt1s-private-api``

### Example Usage

```python
from yt1s_dl import ext_dl_link
from yt1s_dl import ext_video_id

video_url = "https://youtu.be/rUWxSEwctFU" # <- YOUR VIDEO URL HERE
video_id = ext_video_id(video_url)
res = "1080p"

print(ext_dl_link(video_id, video_url, res))
```

## Disclaimer
This is an unofficial API. Use at your own risk.
