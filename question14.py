# 14. Implement method overriding for a `Notification` class where `send()` 
# is overridden in `EmailNotification` and `SMSNotification`.

class Notification:
    def send(self):
        print("notification is sent")
class Emailnotification(Notification):
    def send(self):
        super().send()
        print(" email notification")
class Smsnotification(Notification):
    def send(self):
        super().send()
        print("sms notification")
email=Emailnotification()
email.send()
sms=Smsnotification()
sms.send()

