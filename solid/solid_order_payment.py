from abc import ABC, abstractmethod


class WrongPaymentException(Exception):
    pass


class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, item, price, quantity):
        self.items.append(item)
        self.prices.append(price)
        self.quantities.append(quantity)

    def total_price(self):
        tot_price = 0.00
        for i in range(0, len(self.items)):
            tot_price += self.prices[i] * self.quantities[i]
        return round(tot_price, 2)


class Payment(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class Authorizer():
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuth(Authorizer):
    authorized = False

    def verify_sms(self, sms_code):
        if sms_code == sms_code:
            self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobot(Authorizer):
    authorized = False

    def verify_robot(self):
        print("No not a robot..")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class DebitPayment(Payment):
    status = ""

    def __init__(self, sec_code):
        self.sec_code = sec_code

    def pay(self, order):
        print(f"Entered security code: {self.sec_code}")
        print(f"processing DEBIT payment of {order.total_price()} INR...")
        print("Transaction Successful")
        self.status = "Paid"


class CreditPayment(Payment):
    status = "not_Paid"

    def __init__(self, sec_code, auth: Authorizer):
        self.sec_code = sec_code
        self.auth = auth

    def pay(self, order):
        if self.auth.is_authorized():
            print(f"Entered security code: {self.sec_code}")
            print(f"processing CREDIT payment of {order.total_price()} INR...")
            print("Transaction Successful")
            self.status = "Paid"


class PaypalPayment(Payment):
    status = "not_Paid"

    def __init__(self, email_address, authorizer : Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if self.authorizer.is_authorized():
            print(f"Entered security code: {self.email_address}")
            print(f"processing Paypal payment of {order.total_price()} INR...")
            print("Transaction Successful")
            self.status = "Paid"
        else:
            raise Exception("Not Authorized")


new_d = Order()
new_d.add_item("Bulb", 5.1, 3)
new_d.add_item("Phone case", 6.25, 1)
new_d.add_item("Beer", 0.45, 6)
new_d.add_item("Nuts", 0.3, 6)

cred_auth = NotARobot()
tp = new_d.total_price()
print(f"The total price is {tp}")
cp = CreditPayment(sec_code=51365, auth=cred_auth)
cred_auth.verify_robot()
cp.pay(new_d)

next_od = Order()
next_od.add_item("Beer", 0.45, 6)
next_od.add_item("Nuts", 0.3, 6)

dp = DebitPayment(sec_code=41256)
dp.pay(next_od)

har_od = Order()
har_od.add_item("Chicken", 15, 1)
har_od.add_item("Dairy_milk", 5, 2)
auth = SMSAuth()
har_pay = PaypalPayment("har@gmail.com", auth)
auth.verify_sms(12345)
har_pay.pay(har_od)
