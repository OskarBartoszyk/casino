import random 
print("---wellcome to casino---")
money = 1000
win_price = 100
loss_price = 20
new_value = 0



def spin():
	number1 = random.randint(1,3)
	number2 = random.randint(1,3)
	number3 = random.randint(1,3)
	if number1 == number2 == number3:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You won {win_price} $")
		new_value = money + win_price
	else:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You lost {loss_price} $")
		new_value = money - loss_price
spin()
def check():
	print(new_value)
while money >= 20:
	inter1 = input("Do you want to spin again? (type SPIN) If you want to check your balance type CHECK: ")
	inter1 = inter1.lower()
	if inter1 == "spin":
		spin()
	elif inter1 == "check":
		check()
	else:
		break