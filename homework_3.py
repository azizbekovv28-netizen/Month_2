TRIP_COST = 20

class TransportCard:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def add_money(self, amount):
        if amount <= 0:
            raise ValueError ('Сумма должна быть положительной!')
        else:
            self.__balance += amount


    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            raise ValueError ("Недостаточно средств...")
        else:
            self.__balance -= TRIP_COST

card_1 = TransportCard('Azim')
card_1.add_money(50)
card_1.pay_for_trip()
print('Владелец: ', card_1.get_owner())
print('Баланс: ',card_1.get_balance())

print()

card_2 = TransportCard('Aidai')
card_2.add_money(60)
card_2.pay_for_trip()
print('Владелец: ', card_2.get_owner())
print('Баланс: ', card_2.get_balance())

print()

try:
    card_2.pay_for_trip()
    card_2.pay_for_trip()
    card_2.pay_for_trip()
except ValueError as error:
    print('Недостаточно средств')

print()

try:
    card_1.add_money(-20)
except ValueError as error:
    print('Сумма должна быть положительным')