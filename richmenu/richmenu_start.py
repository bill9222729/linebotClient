import requests

headers = {"Authorization":"Bearer ASWKfQvAGiXrAOCMcRoc0+vUMYY8hFUFOFFbIgOhBF4v6MIWjr9aHvsdkKrIXdN8MO4vduONxiuFu84dDTcGzGpy6u8umCW0ifDavs3yiPoVdZ94Kk5uKkL25553eygfgdkgCqAcZninEIk5n06J9gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/{richmenu_id}'.format(richmenu_id='richmenu-6f3c43f6b9669744c332fe76eb30027a'),
                       headers=headers)
print(req.text)