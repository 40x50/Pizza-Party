import requests
import threading

from dominos.dominos import Dominos

class Handler:
    def __init__(self, data, test=False):
        self.wait_times = []
        self.test = test
        self.test_text = ""
        self.data = data
        self.data["store_id"] = ""
        self.info = Dominos(self.data)

    def get_store(self, store):
        store_id = store["StoreID"]
        profile_url = f"https://order.dominos.com/power/store/{store_id}/profile"
        profile = requests.get(profile_url).json()    
        return profile["Region"], profile["StreetName"], profile["StoreID"], int(profile["EstimatedWaitMinutes"].split("-")[1])

    def closest_stores(self):
        store_url = f"https://order.dominos.com/power/store-locator?s={self.info.post.addr}&c={self.info.post.city}&type=Delivery"
        r = requests.get(store_url).json()["Stores"]
        stores = []

        print()
        
        for x in r:
            if x["IsOnlineNow"] and x["ServiceIsOpen"]["Delivery"]:
                region, street_name, store_id, wait_time = self.get_store(x)
                if region == self.info.post.state:
                    stores.append([street_name, store_id])
                    self.wait_times.append(wait_time)
                    print(f"Got Store: {street_name}, {region}; {store_id}")
        
        print()
        return stores

    def order_pizza(self, store_id):
        data = self.data
        data["store_id"] = store_id
        dominos = Dominos(data)

        if self.test:
            pass
        else:
            dominos.order()
            
    def fulfill_order(self):
        stores = self.closest_stores()
        temp = 0
        stores_num = len(stores)

        for v in stores:
            threading.Thread(target=self.order_pizza, args=(v[1],)).start()

        for x in self.wait_times:
            temp += x

        # print(temp, stores_num)
        return temp//stores_num, stores_num

# print(Handler({
#     "addr": "An ADDRESS",
#     "city": "Lakeland",
#     "state": "TN",
#     "postal_code": 38002,
#     "name": "as as",
#     "email": "as@g.com",
#     "phone": "9018888888"
# }, test=True).closest_stores())