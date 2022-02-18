# # # # # print("hello start")
# # # # # # print(type(1),type(True), (type(0==False)))



# # # # from datetime import datetime


# # # # this_year = input("출생년도>")
# # # # age = datetime.today().year - int( this_year)
# # # # print (age)


# # # # []

# # # test = ['3',"-3",'1','+2','a','-1',' ']
# # # test.insert(5,3)
# # # print(test)

# # # print (test)

# # # def temp(a, b, c):
# # #     a+=1
# # #     b+=1
# # #     c+=5
# # #     return a+b

# # # temp(a,b,c)




# # # """ kjflkjflsdklfdds """""" """  """ """

# # # def skill2():
# # #     print("test")
# # # skill = "test2"

# # # skill2()
# # # print(f"{skill}")

# # # class Monster:
# # #     max=100
# # #     def __init__(self, txt):
# # #         self.txt = txt
# # #         print(txt, Monster.max)

# # # #a=Monster("곽경호")
# # # print(Monster.max)

# # # from unicodedata import name


# # # class Item:
# # #     def __init__(self, name, price, weight, isdropable):
# # #         self.name = name
# # #         self.price = price
# # #         self.weight = weight
# # #         self.isdropable = isdropable

# # #     def sale():
# # #         pass
# # #     def discard():
# # #         pass

# # # class WareableItem(Item):
# # #     def __init__(self, name, price, weight, isdropable,effect):
# # #         super.__init__( name, price, weight, isdropable)
# # #         self.effect = effect

# # #     def wear():
# # #         pass

# # # class UsableItem(Item):
# # #     def __init__(self, name, price, weight, isdropable,effect):
# # #         super.__init__( name, price, weight, isdropable)
# # #         self.effect = effect
# # #     def wear():
# # #         pass

# # # from math import *

# # # import pyautogui as pg

# # # pg.move(-500, 500, duration=5)

# # import csv

# # stockData = [
# #     ["종목", "매입가", "수랑", "목표가"],
# #     ["삼성전자",85000,10,90000],
# #     ["NAVER", 380000, 5, 400000]
# # ]
# # file = open("./myvenv/mystock.csv", "w", newline="", encoding="UTF-8")
# # writer = csv.writer(file)
# # for d in stockData:
# #     writer.writerow(d)
# # file.close();
# # print("테스트시작")
# # file = open("./myvenv/mystock.csv", "r", newline="", encoding="UTF-8")
# # print("테스트시작2")
# # reader = csv.reader(file)
# # header = next(reader)
# # for data in reader:
# #     target = (int(data[3])-int(data[1]))*int(data[2])
# #     benefit = (int(data[3])/int(data[1])-1)*100
# #     print(f"{data[0]} {target} {benefit:.2f}")

# # file.close()


# # word_list = ['apple','watch','apolo', 'star', 'abocdo']
# # print(word_list)
# # word_list2 = [s for s in word_list if s.find('o') != -1]
# # print(word_list2)
# # if True == 2:
# #     print("false") 

# # word_list =['오메가3', None, '비타민C500', None, '홍삼절편']
# # print (word_list)
# # word_list2 = [s if s !=None else '' for s in word_list]
# # print (word_list2)

# time = ["1시간 30분", "2시간", "30분"]
# for s in time:
#     tmp = s.split(" ")
#     if len(s.split(" ")) > 1:
#         hour = tmp[0].split("시간")[0]
#         minute =tmp[1].split("분")[0]
#         print(int(hour)*60 +int(minute))
#     else:
#           hour = tmp[0].split("시간")[0]
#         minute =tmp[1].split("분")[0]
#         print(int(hour)*60 +int(minute))


class Unit:
    
    def __init__(self, name, mineral, gas, hp, shield, demage):
        self.name = name
        self.mineral = mineral
        self.gas = gas
        self.hp = hp
        self.shield = shield
        self.demage = demage
        

    

class Player:
    def __init__(self, name, mineral, gas):
        self.name = name
        self.gas = gas
        self.mineral = mineral
        self.unit_list = []

    def produce(self, unit_info):
        if self.mineral < unit_info["mineral"]:
            print("미네랄이 부족합니다.")
        elif self.gas < unit_info["gas"]:
            print("가스가 부족합니다.")
        else:
            unit = Unit(unit_info["name"],unit_info["mineral"],unit_info["gas"],unit_info["hp"],unit_info["shield"],unit_info["demage"] )
            self.unit_list.append(unit)
            self.mineral -= unit_info["mineral"]
            self.gas -= unit_info["gas"]

    def __str__(self):
        return str(self.unit_list)

unit_info = {
    "probe":{
        "name": "프로브",
        "mineral": 50,
        "gas": 0,
        "hp": 20,
        "shield":20,
        "demage": 5
    },
    "zelot": {
        "name": "질럿",
        "mineral": 100,
        "gas": 0,
        "hp": 100,
        "shield":60,
        "demage": 16
    }
}

player = Player("bisu", 150, 0)
player.produce(unit_info["probe"])
player.produce(unit_info["zelot"])

for unit in player.unit_list:
    print(unit.name)