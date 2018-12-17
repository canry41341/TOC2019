import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAcAuEo7Do8BAJPovcKLCLVUq6YRbR0m9ClabeXrGZB6RNhkJjMkXEPe2p2tP8oGXYN31mE10WniNb9mgeLjGNbZAnpuReNbn6mlqtOZAyGd1qMwp1iDiQhoFIyClIuA13gzWi3N6FGhDl9khnImAU9IKAIOmyMfIZBEujZAx3nRZAgyUi7avb"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
