names = ['Bidesh', 'Biswas','Biki','X','Y','Z']
names[0] = 'Biki' #can be replaced list names
print(names[2:])
print(names)


##largest number
numbers = [3,6,2,8,4,10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)