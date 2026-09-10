#Абстракция
from abc import ABC, abstractmethod

class Notification (ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification (Notification):
    pass
    def send(self, message):
        print(f"Уведомление по почте: {message}")

class TelegramNotification (Notification):
    def send(self, message):
        print(f"Телеграм: {message}")

class IncompleteNotification (Notification):
    pass

# not1 = Notification()
not2 = EmailNotification()
not3 = TelegramNotification()
not2.send("У вас закончился баланс")
not3.send("У вас закончился баланс")
try:
    not4 = IncompleteNotification()
except TypeError:
    print("Нельзя иницилизировать класс с нереализованным send")
