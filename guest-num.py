import random
start = input('請決定開始值:')
end = input('請決定結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count +=1 # =count + 1
	n = input('請猜一個隨機整數: ')
	n = int(n)
	if n == r:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif n > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次')

