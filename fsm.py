from transitions.extensions import GraphMachine

from utils import send_text_message


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
            return text.lower() == 'go to state5'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state6'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '減肥'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '幾歲'
        return False


    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請問您有什麼問題：\n(1)沒事\n(2)不想上課\n請回覆1或2。")


    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "你好無聊><")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "不行喔！給我去上課！")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "哈囉～我叫宋金操，目前是一名大學生")
        self.go_back()

    def on_exit_state4(self):
        print('Leaving state4')

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state5")
        self.go_back()

    def on_exit_state5(self):
        print('Leaving state5')

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state6")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state6')

    def on_enter_state7(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "希望你能繼續保持下去～加油！")
        self.go_back()

    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "目前21喔～")
        self.go_back()

    def on_exit_state6(self):
        print('Leaving state8')
