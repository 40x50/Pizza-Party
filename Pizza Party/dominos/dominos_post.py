class DominosPost:
    def __init__(self, data):
        self.addr = data["addr"].upper()
        self.city = data["city"].upper()
        self.state = data["state"].upper()
        self.postal_code = data["postal_code"]
        self.email = data["email"]
        self.name = data["name"]
        self.phone = data["phone"]
        self.store_id = data["store_id"]
        
        try:
            self.prefix = data["prefix"]
        except:
            self.prefix = ""

    def get_post(self):
        return {
            "Address": {
                "Street": self.addr, 
                "StreetName": " ".join(self.addr.split(" ")[1:]),
                "StreetNumber": self.addr.split(" ")[0],
                "City": self.city, 
                "Region": self.state, 
                "PostalCode": self.postal_code,  
                "Type": "House",
                "UnitType": "#"
            },
            "Coupons": [],
            "CustomerID": "",
            "Email": self.email, 
            "Extension": "1",
            "FirstName": self.name.split(" ")[0], 
            "LastName": self.name.split(" ")[1], 
            "LanguageCode": "en",
            "OrderChannel": "OLO",
            "OrderID": "",
            "OrderMethod": "Web",
            "OrderTaker": None,
            "Payments":
                {
                "Type": "Cash",
                "Amount": 19.73, 
                "Number": "",
                "CardType": "",
                "Expiration": "",
                "SecurityCode": "",
                "PostalCode": "",
                "ProviderID": "",
                "PaymentMethodID": "",
                "OTP": "",
                "gpmPaymentType": ""
                },
            "Phone": self.phone, 
            "PhonePrefix": self.prefix,
            "Products": [
                {
                "Code": "14SCREEN",
                "Qty": 1,
                "ID": 1,
                "isNew": True,
                "ShowBestPriceMessage": False,
                "Options": {
                    "X": {
                    "1/1": "1"
                    },
                    "C": {
                    "1/1": "1"
                    }
                }
                }
            ],
            "ServiceMethod": "Delivery",
            "SourceOrganizationURI": "order.dominos.com",
            "StoreID": self.store_id,
            "Tags": {},
            "Version": "1.0",
            "NoCombine": True,
            "Partners": {},
            "HotspotsLite": False,
            "OrderInfoCollection": [],
            "NewUser": True,
            "metaData": {
                "dtmOrder": False,
                "PiePassPickup": False,
                "calculateNutrition": "True",
                "orderFunnel": "payments",
                "isDomChat": 0,
                "ABTests": []
            }
        }