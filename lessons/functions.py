# minimum search

data = [1, 2, 6.34, -9, 0.3]
minimum = data[0]

for item in data:
	if item < minimum:
		minimum = item

print('Min is', minimum)

# but

other_data = [-10, 23, -9, 0.12, 0.4, -1,4]

for item in other_data:
	if item < minimum:
		minimum = item

print('Other min is', minimum)

# но если минимум из кучи значений ? можно в функцию!!

def my_function(input_var1, input_var2):
	print(input_var1, input_var2)
	return(input_var1 + input_var2, 10 + 3)

my_function(30,24)

def secondF(x, z):
	print(x + z)
	print('function nya nya')

secondF(34,12)

def sum_numb(n1, n2, n3):
	print(n1, n2, n3, 'summing...')
	return n1 + n2 + n3

total = sum_numb(12, 0.4 , -15)
print(total)
