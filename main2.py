# if __name__ == '__main__':
# print('Hello, Word!')
# print(type('Hello, Word!'))
# print('Hello, WordПривет°!')
# print(123456789012355555555555000000000000000005**200)
# print(type(1.5))
# print(5!=50)

# # 1st program
# print('1st program')
# print(9**0.5*5)
# # 2nd program
# print('2nd program')
# print(9.99>9.98 and 1000 != 1000.1)
# # 3rd program
# print('3rd program')
# print(2*2+2)
# print(2*(2+2))
# print(2*2+2 == 2*(2+2))
# # 4th program
# print('4th program')
# print(int(float('123.456')*10)%10)

# print(type(5))
# 10 // 2 == 5 целочисленное деление
# 11 % 3 == 2 остаток от деления
# 10 ** 3 = 1000 возведение в степень
# sleep(2) ждать 2 сек. # from time import sleep

# import this # стиль питона
# from time import sleep
#
# a = 345
# print('111')
# sleep(3)
# print(222)

# ## цикл while
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# k = 0
# while k < len(my_list):
#     if my_list[k] < 0:
#         break
#     if my_list[k] > 0:
#         print(my_list[k])
#     k = k + 1
# ##
# ## цикл for
# list_ = [1, 2, 3, 4]
# # переворачиваем список, чтобы обработать все элементы при удалении
# for i in reversed(list_):
#     print(i)
#     if i == 3:
#         list_.remove(i)
# print(list_)
#
# list_2 = list(reversed(list_))
# print(list_2)
# r = list(reversed(range(1, 4)))
# print(r)

# dict_ = {'a' : 1, 'b' : 2, 'c' : 3}
# for i, k in dict_.items():
#     print(i,k)
#
# for i in dict_:
#     print(i, dict_[i])
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f'{i} x {j} = {i * j}')

# import random
# def lottery(tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], *args, **kwargs):
#
#     win1 = random.choice(tickets)
#     win2 = random.choice(tickets)
#     while win2 in [win1]:
#         win2 = random.choice(tickets)
#     win3 = random.choice(tickets)
#     while win3 in [win1, win2]:
#         win3 = random.choice(tickets)
#     win4 = random.choice(tickets)
#     while win4 in [win1, win2, win3]:
#         win4 = random.choice(tickets)
#     win5 = random.choice(tickets)
#     while win5 in [win1, win2, win3, win4]:
#         win5 = random.choice(tickets)
#     win6 = random.choice(tickets)
#     while win6 in [win1, win2, win3, win4, win5]:
#         win6 = random.choice(tickets)
#     print(*args)
#     return win1, win2, win3, win4, win5, win6
#
# z1, z2, z3, z4, z5, z6 = lottery(*[range(1, 36), 5, 6])
# # z1, z2 = lottery([1,2,6])
# # z1, z2 = lottery(1,2,6)
# print(z1, z2, z3, z4, z5, z6)
# print(*[1,2,3,4]) # распаковка параметров

# # крестики-нолики
# def draw_area():
#     for i in area:
#         print(*i)
#
# def check_win():
#     fwin = "*"
#     for j in range(0, z):
#         winX_count_0 = 0
#         winX_count_X = 0
#         winY_count_0 = 0
#         winY_count_X = 0
#         winL_count_0 = 0
#         winL_count_X = 0
#         winR_count_0 = 0
#         winR_count_X = 0
#         for k in range(0, z):
#             if area[j][k] == "0":
#                 winX_count_0 = winX_count_0 + 1
#             if area[j][k] == "X":
#                 winX_count_X = winX_count_X + 1
#             if area[k][j] == "0":
#                 winY_count_0 = winY_count_0 + 1
#             if area[k][j] == "X":
#                 winY_count_X = winY_count_X + 1
#
#             if area[k][k] == "0":
#                 winL_count_0 = winL_count_0 + 1
#             if area[k][k] == "X":
#                 winL_count_X = winL_count_X + 1
#             if area[z-1-k][k] == "0":
#                 winR_count_0 = winR_count_0 + 1
#             if area[z-1-k][k] == "X":
#                 winR_count_X = winR_count_X + 1
#
#         if z in [winX_count_0, winY_count_0, winL_count_0, winR_count_0]:
#             fwin = "0"
#             break
#         if z in [winX_count_X, winY_count_X, winL_count_X, winR_count_X]:
#             fwin = "X"
#             break
#
#     return fwin
#
# win = "*"
# area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
#
# z = area[0].count("*")
# draw_area()
# for turn in range(1, 10):
#     print(f'Ход: {turn}')
#     if(turn % 2 == 0):
#         turn_char = "0"
#         print("Ходят нолики")
#     else:
#         turn_char = "X"
#         print("Ходят крестики")
#     row = int(input("Введите номер строки(1,2,3): ")) - 1
#     column = int(input("Введите номер столбца(1,2,3): ")) - 1
#     if area[row][column] == "*":
#         area[row][column] = turn_char
#     else:
#         print("Ячейка занята. Повторите попытку")
#         turn = turn - 1
#
#     draw_area()
#     win = check_win()
#     # print(f"Победил: {win}")
#
#     if(win != "*"):
#         break
#
# if(win != "*"):
#     print(f"Победил: {win} !!!")
# else:
#     print("Ничья")
#
import random
def simple_num(fnum):
    list_ = list(range(1, fnum+1))
    list_2 = list(range(1, fnum))
    list_3 = list()
    list_4 = list()
    for i in reversed(list_):
        if fnum % i != 0:
            list_.remove(i)

    for j in list_:
        if j > 1: # j in fnum
            for i in reversed(list(range(1, j))): # list_2
                if(j-i < i):
                    # print(j-i, i)
                    list_3.append(j-i)
                    list_3.append(i)

    # сортировка пар
    for i in list_2:
        for j in list_2:
            for k in range(0, len(list_3)-1): # -1 т.к. пары
                if(k % 2 == 0):
                    if list_3[k] == i:
                        if list_3[k+1] == j:
                            list_4.append(list_3[k])
                            list_4.append(list_3[k+1])
    s = ""
    for k in range(0, len(list_4)):
        s = s + str(list_4[k])
    return s # list_4

lnum = int(input("Введите число(3..20): "))
passw = simple_num(lnum)
print("Пароль числа: ", passw) # *passw
