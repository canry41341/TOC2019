from transitions.extensions import GraphMachine
from fbmq import Page, Attachment, Template, QuickReply
import requests
from bs4 import BeautifulSoup

ACCESS_TOKEN = "EAAcAuEo7Do8BAJPovcKLCLVUq6YRbR0m9ClabeXrGZB6RNhkJjMkXEPe2p2tP8oGXYN31mE10WniNb9mgeLjGNbZAnpuReNbn6mlqtOZAyGd1qMwp1iDiQhoFIyClIuA13gzWi3N6FGhDl9khnImAU9IKAIOmyMfIZBEujZAx3nRZAgyUi7avb"

page = Page(ACCESS_TOKEN)
r = requests.get('https://tw.yahoo.com/')
google_url = 'https://www.google.com.tw/search'

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '你好'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '介紹'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '即時新聞'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '減肥'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '1'
        return False

    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '2'
        return False

    def is_going_to_state11(self, event):
        if event.get("message"):
            text = event['message']['text']
            if text.lower() != '你好' and text.lower() != '介紹' and text.lower() != '減肥' and text.lower() != '即時新聞':
                return text.lower()
        return False
########

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        page.send(sender_id, "請問您有什麼問題：\n(1)沒事\n(2)不想上課\n請回覆1或2。")
###########

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        page.send(sender_id, "你好無聊><")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')
###########
    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        page.send(sender_id,Attachment.Image("https://i.imgur.com/syy1Cu4.jpg"))
        page.send(sender_id, "不行喔！給我去上課！")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')
############
    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        page.send(sender_id, "哈囉～我叫宋金操，目前是一名大學生\n你可以透過輸入以下數字來更瞭解我喔!:\n(1) 聯絡資料。\n(2) 想了解別人\n ")

#############
    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        page.send(sender_id, "抱歉沒有喔～")
        self.go_back()        

    def on_exit_state5(self):
        print('Leaving state5')
#############
    def on_enter_state6(self, event):
        print("I'm entering state6")
        i = 0
        sender_id = event['sender']['id']
        # 確認是否下載成功
        if r.status_code == requests.codes.ok:
        # 以 BeautifulSoup 解析 HTML 程式碼
            soup = BeautifulSoup(r.text, 'html.parser')
        # 以 CSS 的 class 抓出各類頭條新聞
            stories = soup.find_all('a', class_='story-title')
            for s in stories:
                i += 1
        # 新聞標題
                page.send(sender_id,"標題：" + s.text)
        # 新聞網址
                page.send(sender_id,"網址：" + s.get('href'))
                if i == 4:
                    break
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6')
##############
    def on_enter_state7(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        page.send(sender_id,Attachment.Image("https://i.imgur.com/t56acky.jpg"))
        page.send(sender_id, "希望你能繼續保持下去～加油！")
        self.go_back()
############
    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        page.send(sender_id, "目前21歲\n臉書: https://www.facebook.com/canry.dermawan \nIG: https://www.instagram.com/canry41341/?hl=zh-tw")
        self.go_back()

    def on_exit_state8(self):
        print('Leaving state8')
########
    def on_enter_state9(self, event):
        print("I'm entering state9")
        
        sender_id = event['sender']['id']
        page.send(sender_id, "是否想要知道其他人？\n(1)是\n(2)否")
        
######
    def on_enter_state10(self, event):
        print("I'm entering state10")

        sender_id = event['sender']['id']
        page.send(sender_id, "很好你很乖")
        self.go_back()

    def on_exit_state10(self):
        print('Leaving state10')
#######
    def on_enter_state11(self, event):
        print("I'm entering state11")

        sender_id = event['sender']['id']
        rr = requests.get(google_url, params = text)
        if rr.status_code == requests.codes.ok:
            soup = BeautifulSoup(rr.text,'html.parser')
            items = soup.select('div.g > h3.r > a[href^="/url"]')
            for s in items:
                i += 1
        # 新聞標題
                page.send(sender_id,"標題：" + s.text)
        # 新聞網址  
                page.send(sender_id,"網址：" + s.get('href'))
                if i == 4:
                    break
        self.go_back()

    def on_exit_state11(self):
        print('Leaving state11')
