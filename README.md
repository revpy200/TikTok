# TikTok

TikTok Premium API client. A reverse-engineered implementation of the **TikTok** (previously musical.ly) app's API.

# Usage

```python

import requests as r

class TikTokApiClient:

    protocol = "http"
    host = "localhost"
    port = 4444

    base_url = protocol + "://" + host + ":" + str(port)

    tok_proxy = ""
    api_token = ""

    def __init__(self, proxy, token) -> None:
        self.tok_proxy = proxy
        self.api_token = token

    def device_register(self):
        path = "/device-register"
        payload={}
        headers = {
            'tok-proxy': self.tok_proxy,
            'api-token': self.api_token
            }
        return r.post("GET", self.base_url + path, headers=headers, data=payload)

```

## Premium

To request your **access token** for the **TikTok Premium API** you can contact me via [E-Mail](mailto:revpy200@gmail.com).

## Terms of use

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by TikTok or any of its affiliates or subsidiaries. This is an independent and unofficial API.  Use at your own risk. We do NOT support or tolerate anyone who wants to use this API to send spam or commit other online crimes. You will NOT use this API for marketing or other abusive purposes (spam, botting, harassment, massive bulk messaging...). **For education purposes only.**
