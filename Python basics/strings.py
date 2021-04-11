course = "Python's Course for Beginners"
print(course)


course = 'Python for "Beginners"'
print(course)

#to write multiple line(''')
course= '''
Hi,

Here is our first email to you.

Thank you!
The support team!
'''
print(course)


# 012345 789 this is how describes each alphabates.
# if we use -1 it will start from the ending of the sentense
# if we use [0:3] it will print from beginning three alphabates
# if we use [2:] it will ignore first 2 alphabates      
course = 'Python for Beginners'     
print(course[:5])


course = 'Python for Beginners'   
another = course[:]  
print(another)

name = 'Jennifer'
print(name[1:-1])