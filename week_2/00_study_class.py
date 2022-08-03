class Person:
    # 생성자
    def __init__(self, param_name):
        print("i am created! ", self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다")


person_1 = Person("Arsenal")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 = Person("Saka")
print(person_2.name)
print(person_2)
person_2.talk()
