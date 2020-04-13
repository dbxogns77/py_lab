#!/usr/bin/python

n = int(input("fibonacci number? "))

F = []
F.append(1)
F.append(1)

for i in range(2, n):
	F.append(F[i-1] + F[i-2])

for i in range(0, n):
	if(i == n-1):
		print(F[i])
	else:
		print(F[i], end = ',')

print("F{} = {}".format(n, F[n-1]))
