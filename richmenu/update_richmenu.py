from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('ASWKfQvAGiXrAOCMcRoc0+vUMYY8hFUFOFFbIgOhBF4v6MIWjr9aHvsdkKrIXdN8MO4vduONxiuFu84dDTcGzGpy6u8umCW0ifDavs3yiPoVdZ94Kk5uKkL25553eygfgdkgCqAcZninEIk5n06J9gdB04t89/1O/w1cDnyilFU=')

with open("D:\\Restaurant_Client_Linebot\\rich_menu01.jpeg",'rb') as f:
    print(f)
    line_bot_api.set_rich_menu_image("richmenu-aec048bea3ff9cebcc45f85f0a01ca1f", "image/jpeg", f)