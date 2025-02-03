# 12. Write a `Payment` class with a method `process_payment()`. 
# Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment`
#  that override the method differently.


class Payment:
   
    def process_payment(self):
        print("payment processing...")
    class Creditcardpayment:
        def process_payment(self):
            print("payment processing through credit card")
    class Paypalpayment:
        def process_payment(self):
            print("payment processing through paypal")
    class Bitcoinpayment:
        def process_payment(self):
            print("payment processing through bitcoin")
payment=Payment()
payment.process_payment()
payment.c()

