import random
while True:
	start = input('請輸入開始數字: ')
	end = input('請輸入結束數字: ')
	start = int(start)
	end = int(end)
	if end <= start:
		print('結束數字必須大於開始數字')
	else:
		break
r = random.randint(start, end)
count = 0

while True:
	guess = input('請猜數字: ')
	guess = int(guess)
	if guess == r:
		print('恭喜你猜中了!', '猜了', count + 1, '次')
		break
	elif guess < start or guess > end:
		print('輸入數字超出區間範圍')
		count = count - 1
	elif guess > r and r > start:
		print('大於目標數字', '目標數字介於', start, '跟', guess, '之間')
		print('第', count + 1, '次')
		end = guess
	elif guess < r and r < end:
		print('小於目標數字', '目標數字介於', guess, '跟', end, '之間')
		print('第', count + 1, '次')
		start = guess
	count = count + 1
		
