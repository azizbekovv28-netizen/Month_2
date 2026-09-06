class Person:
    def __init__(self, name, birth_day, occupation, higher_education ):
        self.name = name
        self.birth_day = birth_day
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        if self.higher_education:
            education = 'высшее образование есть'
        else:
            education = 'высшее образование нет'

        print(f'Меня зовут {self.name}, я родился {self.birth_day}, '
              f'по професии я - {self.occupation}, {education}')

class Classmate(Person):
    def __init__(self, name, birth_day, occupation, higher_education, group_name):
        super().__init__(name, birth_day, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f'Меня зовут {self.name}, я учусь в {self.group_name}, '
              f'я родился {self.birth_day}, по профессии я - {self.occupation}, ')

class Friends(Person):
    def __init__(self, name, birth_day, occupation, higher_education, hobby):
        super().__init__(name, birth_day, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f'Меня зовут {self.name}, я родился {self.birth_day}, '
              f'по професии я - {self.occupation}, мое хобби {self.hobby}, ')

classmate_1 = Classmate("Адильхан",
                        "05.01.2005",
                        "программист",
                        True,
                        "ПИ-5-22")
classmate_2 = Classmate("Адиль",
                        "27.06.2004",
                        "инженер",
                        True,
                        "ИБ-3-22")
friend_1 = Friends("Мырза",
                   "16.08.2004",
                   "проектный менеджер",
                   True,
                   "футбол")
friend_2 = Friends ("Нариман",
                    "13.02.2005",
                    "разработчик",
                    True,
                    "бокс")

person_1 = Person("Азим",
                  "28.05.2004",
                  "админ",
                  True,)

classmate_1.introduce()
classmate_2.introduce()
friend_1.introduce()
friend_2.introduce()

#доп задание 1
print("\n")
people = [person_1, classmate_1, friend_1]
for person in people:
    person.introduce()

#доп задание 2
print("\n")
class BestFriend(Friends):
    def __init__(self, name, birth_day, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_day, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f'Наше общее воспоминание: {self.shared_memory}')

best_friend = BestFriend("Бектур",
                         "06.09.2004",
                         "ментор",
                         True,
                         "плавание",
                         "ездили на природу ")

best_friend.introduce()