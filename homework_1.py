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

person1 = Person('Азим', '28.05.2004', 'бариста', False)
person1.introduce()
print(person1.name)
print(person1.birth_day)
print(person1.occupation)
print(person1.higher_education)

person2 = Person('Адиль', '27.06.2004', 'повар', True)
person2.introduce()
print(person2.name)
print(person2.birth_day)
print(person2.occupation)
print(person2.higher_education)

person3 = Person('Мырза', '16.08.2004', 'продавец', True)
person3.introduce()
print(person3.name)
print(person3.birth_day)
print(person3.occupation)
print(person3.higher_education)


