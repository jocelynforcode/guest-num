import random
r = random.randint(1,100)

while True:
	n = input('請猜一個隨機整數: ')
	n = int(n)
	if n == r:
		print('終於猜對了!')
		break
	elif n > r:
		print('比答案大')
	else:
		print('比答案小')

