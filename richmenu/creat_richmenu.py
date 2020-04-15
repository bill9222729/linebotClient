#搖桿的
import requests
import json

headers = {"Authorization":"Bearer ASWKfQvAGiXrAOCMcRoc0+vUMYY8hFUFOFFbIgOhBF4v6MIWjr9aHvsdkKrIXdN8MO4vduONxiuFu84dDTcGzGpy6u8umCW0ifDavs3yiPoVdZ94Kk5uKkL25553eygfgdkgCqAcZninEIk5n06J9gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": 'true',
  "name": "richmenu0324",
  "chatBarText": "操作選單",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 830,
        "height": 840
      },
      "action": {
        "type": "message",
        "text": "預約訂位"
      }
    },
    {
      "bounds": {
        "x": 831,
        "y": 0,
        "width": 830,
        "height": 844
      },
      "action": {
        "type": "message",
        "text": "訂位管理"
      }
    },
    {
      "bounds": {
        "x": 1661,
        "y": 0,
        "width": 839,
        "height": 848
      },
      "action": {
        "type": "message",
        "text": "店內點餐"
      }
    },
    {
      "bounds": {
        "x": 0,
        "y": 835,
        "width": 831,
        "height": 851
      },
      "action": {
        "type": "message",
        "text": "當日外帶"
      }
    }
  ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)