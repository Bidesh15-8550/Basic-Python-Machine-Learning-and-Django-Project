numbers = [5,2,1,7,4]
numbers.append(20) #enters numbers at the last
print(numbers)

numbers.insert(0,10) #enters numbers at first
print(numbers)

print(numbers.index(5)) #tells the location of the number

numbers.pop() #pops out last numeber
print(numbers)


print(numbers.index(5)) #tells the location of the number


numbers.append(5)
print(numbers.count(5))  #counts numbers

numbers.sort() #sorts number ascending
print(numbers)

numbers.reverse() #sorted decending order
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)

#numbers.remove(5) #remove the number
#print(numbers)

#numbers.clear() #clear all the numbers
#print(numbers)


#write a program to remove the duplicates in a list

numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

