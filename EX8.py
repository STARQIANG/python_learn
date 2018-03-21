#for循环

magicians = ['alice', 'david', 'carolina']
for magician  in magicians:
    print(magician.title())

for  value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

enen_numbers = list(range(2,11,2))
print(enen_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

    print(squares)

print('------------------------------')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)



squares = [value**2 for value in range(1,100)]
print(squares)

