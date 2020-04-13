#!/usr/bin/python

n = int(input("몇 개의 숫자를 입력하시곘습니까? : "))


sum = 0
for i in range(0, n):
	sum += float(input("숫자를 입력하세요 : "))
	

average = sum/n
print("average is ", average)
