import random 
print("wellcome to casino")
money = 1000
win_price = 100
loss_price = 20
new_value = 0


number1 = random.randint(1,3)
number2 = random.randint(1,3)
number3 = random.randint(1,3)


def spin():
	if number1 == number2 == number3:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You won {win_price} $")
	else:
		spin = [number1,number2,number3]
		print(spin)
		print(f"You lost {loss_price} $")
spin()
while money > 0:
	inter1 = input("Do you want to spin again? (type SPIN): ")
	if inter1 == "spin":
		spin()
	else:
		break