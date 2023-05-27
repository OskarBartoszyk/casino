import random 
print("---wellcome to casino---")
money = 1000
win_price = 100
loss_price = 20
new_value = 0
def spin():
	global money
	global new_value
	number1 = random.randint(1,3)
	number2 = random.randint(1,3)
	number3 = random.randint(1,3)
	if number1 == number2 == number3:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You won {win_price} $")
		new_value = money + win_price
		print( new_value)
	else:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You lost {loss_price} $")
		new_value = money - loss_price
		print( new_value)
spin()
while True:
	inter = input("Do you want to spin again? (type SPIN) If you want to check your balance type CHECK: ")
	inter = inter.lower()
	if inter == "spin":
		spin()
	elif inter == "check":
		pass
	else:
		break