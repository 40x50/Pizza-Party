import requests

from dominos.dominos_post import DominosPost

class Dominos:
    def __init__(self, data):
        self.post = DominosPost(data)

    def order(self):
        url = "https://order.dominos.com/power/place-order"
        headers = {
            "Referer": "https://order.dominos.com/en/pages/order/",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
        }

        requests.post(url=url, headers=headers, json={"Order": self.post.get_post()})