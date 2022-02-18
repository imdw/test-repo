# weather = input("오늘 날씨는 어때요? ")
# if weather == "비":
#     print("우산을 챙기세요 ")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요")

# from random import *
# custumer = range(1,51)
# time = 0
# success = "O"
# result = 0
# for i in custumer:
#     time = randrange(5,51)
#     if 5<=time<=15 :
#         success = "O"
#         result += 1
#     else:
#         success = " "
#     print("[{0}] {1}번재 손님 (소요시간 : {2}분)".format(success, i, time))
    
# print("총 탑승 승객 : {0}".format(result))


# def std_weight(height, gender):
#         if(gender=="male"):
#             return round(height*height*22,2)
#         elif(gender=="female"):
#             return round(height*height*21,2)
# height = 175
# gender = "male"
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender,std_weight(height/100, gender)))


# score = {"수학":0, "영어":50, "국어":50}
# print(type(score))
# print("-------------")
# print(type(score{0}))

# score_file = open("score.txt", "a", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("이건 텍스트만")
# score_file.close()

# import pickle
# weeks = range(1,51)
# for week in weeks:
#     with open(str(week)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.writelines(str(week)+"주차 업무보고\n")
#         print("부서 :", file=report_file)
#         print("이름 :", file=report_file)
#         print("업무 요약 :", file=report_file)
        
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print("--------------------------")
#         print("위치: {0}".format(self.location))
#         print("건물타입: {0}".format(self.house_type))
#         print("거래타입: {0}".format(self.deal_type))
#         print("금액: {0}".format(self.price))
#         print("준공: {0}".format(self.completion_year))

# apt = House("강남", "아파트", "매매", "10억", "2010년").show_detail()
# officetel = House("마포", "오피스텔", "전세", "5억", "2007년").show_detail()
# villa = House("송파", "빌라", "월세", "500/50", "2000년").show_detail()


# class SoldOutError(Exception):
#     pass

# chicken = 10 
# waiting = 1
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     try:
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order <= 0:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
#             waiting += 1
#             chicken -= order
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError as err:
#         print("잘못된 값을 입력하였습니다.")

#     except SoldOutError as err:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break

        

import byme
byme.sign();