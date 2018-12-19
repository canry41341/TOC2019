from bottle import route, run, request, abort, static_file
import requests
from fbmq import Page
from bs4 import BeautifulSoup

from fsm import TocMachine
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
VERIFY_TOKEN = "123"
PORT = os.environ['PORT']
d = {"ID":1}
page = Page(ACCESS_TOKEN)
google_url = 'https://www.google.com.tw/search'
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },{
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },{
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },{
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },{
            'trigger': 'advance',
            'source': 'state9',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },{
            'trigger': 'go_back',
            'source': [
                'state8',
                'state2',
                'state3',
                'state5',
                'state6',
                'state7',
                'state10',
                'state11'
            ],
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    #if mode == "subscribe" and token == VERIFY_TOKEN:
    if token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        sender_id = event['sender']['id']
        global d
        if sender_id in d:
            machine.state = d[sender_id]
        else:
            machine.state = "user"
        if event['message'].get('text'):
            machine.advance(event)
            d[sender_id] = machine.state

        if machine.state == "user":
            text = event['message']['text']
            if text.lower() != '你好' and text.lower() != '介紹' and text.lower() != '減肥' and text.lower() != '即時新聞':
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
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
