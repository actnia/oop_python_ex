"""
Title   셋 타입 | set
Author  kadragon
Date    2018.09.08
"""

my_set = {2, 4, 6, 8, 10}
print(my_set)
# 결과: {2, 4, 6, 8, 10}

my_set = {1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, }
print(my_set)
# 결과: {1, 2, 3, 4, 5}

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9}

print(A | B)  # 결과: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(A & B)  # 결과: {4, 5}
print(A - B)  # 결과: {1, 2, 3}
print(B - A)  # 결과: {8, 9, 6, 7}
print(A ^ B)  # 결과: {1, 2, 3, 6, 7, 8, 9}