import os
import os.path
import random
import numpy as np
import time


# zad3
# lplikow = len(os.listdir("/dev"))
# print("lplikow = ", lplikow)

# zad4
# code = "12098"
# locked = True
# while locked:
#     if input("Wpisz kod: ") == code:
#         print("Otwarte")
#         locked = False
#     else:
#         print("Zły kod")

# zad5
# def get_list_of_files(dirName):
#     #lista plikow
#     list_of_file = os.listdir(dirName)
#     all_files = list()
#
#     for entry in list_of_file:
#         full_path = os.path.join(dirName, entry)
#         # wez liste plikow w srodku jesli plik jest dir
#         if os.path.isdir(full_path):
#             all_files += get_list_of_files(full_path)
#         else:
#             all_files.append(full_path)
#
#     return all_files
#
#
# dirName = '.'
# listOfFiles = get_list_of_files(dirName)
#
# for elem in listOfFiles:
#     print(elem)
#
# print("****************")
#
# get_list_of_files = list()
# for (dirpath, dirnames, filenames) in os.walk(dirName):
#     listOfFiles += [os.path.join(dirpath, file) for file in filenames]
#
# for elem in listOfFiles:
#     print(elem)

#zad 7
# def delta(a, b, c):
#     delta = pow(b, 2) - 4 * a * c
#
#     if delta > 0:
#         x1 = (-b + pow(delta, 0.5))/ (2*a)
#         x2 = (-b - pow(delta, 0.5)) / (2 * a)
#         print("x1 = " + str(x1), ", x2 = " + str(x2))
#     elif delta == 0:
#         x0 = -b / (2 * a)
#         print("x0 = ", x0)
#     else:
#         print("brak pierwiastkow")
#
# delta(6, 12, 4)
# delta(4, 4, 1)
# delta(13, 3, 2)

#zad 8
# rand_numbers = list()
# for i in range(50):
#     rand_numbers.append(random.randrange(0, 100))
#
# def bubble(list):
#     for passnum in range(len(list)-1, 0, -1):
#         for i in range(passnum):
#             if list[i] > list[i+1]:
#                 temp = list[i]
#                 list[i] = list[i+1]
#                 list[i+1] = temp
#
# print(rand_numbers)
# bubble(rand_numbers)
# print(rand_numbers)

#zad 11
# a = [1, 2, 12, 4]
# b = [2, 4, 2, 8]
# c = list()
#
# for index in range(4):
#     c.append(a[index] * b[index])
#
# print(c)

#zad 12
# stworz macierze
# arr_size = 128
# A = np.zeros((arr_size, arr_size))
# B = np.zeros((arr_size, arr_size))
# C = np.zeros((arr_size, arr_size))
#
# for i in range(arr_size):
#     for j in range(arr_size):
#         A[i][j] = random.randrange(0, 100)
#         B[i][j] = random.randrange(0, 100)
#
# # zsumuj
# for i in range(arr_size):
#     for j in range(arr_size):
#         C[i][j] = A[i][j] + B[i][j]

#zad 13
# stworz macierze
# arr_size = 64
# A = np.zeros((arr_size, arr_size))
# B = np.zeros((arr_size, arr_size))
# C = np.zeros((arr_size, arr_size))
# # D = np.zeros((arr_size, arr_size))
#
# for i in range(arr_size):
#     for j in range(arr_size):
#         A[i][j] = random.randrange(0, 10)
#         B[i][j] = random.randrange(0, 10)
#
# # wymnoz
# start = time.time()
# for i in range(arr_size):
#     for j in range(arr_size):
#             for m in range(arr_size):
#                 C[i][j] += A[i][m] * B[m][j]
# print("Czas wykonania metody I: ", time.time() - start)
#
# # wymnoz II wariant pętli
# C1 = np.zeros((arr_size, arr_size))
# start = time.time()
# for j in range(arr_size):
#     for i in range(arr_size):
#             for m in range(arr_size):
#                 C[i][j] += A[i][m] * B[m][j]
# print("Czas wykonania metody Ia: ", time.time() - start)
#
# # szybsza opcja
# def matrix_multiplication(a, b):
#     zip_b = list(zip(*b))
#     return [[sum(element_a * element_b for element_a, element_b in zip(row_a, column_b))
#              for column_b in zip_b] for row_a in a]
#
#
# start = time.time()
# D = matrix_multiplication(A, B)
# print("Czas wykonania metody II: ", time.time() - start)

#zad 14
# stworz macierze
# arr_size = 2
# A = np.zeros((arr_size, arr_size))
#
# for i in range(arr_size):
#     for j in range(arr_size):
#         A[i][j] = random.randrange(0, 10)
#
# def det(A):
#     return A[0][0]*A[1][1] - A[0][1]*A[1][0]
#
#
# print(det(A))

