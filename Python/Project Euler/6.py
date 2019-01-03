sum_of_squares = 0
square_of_sum = 0

for x in range(101):
    sum_of_squares += x**2
    square_of_sum += x

square_of_sum = square_of_sum**2
print(square_of_sum - sum_of_squares)

k = input("END")