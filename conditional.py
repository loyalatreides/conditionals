a = -5
if a > 0:
    print('a is a positive number')
else:
    print('a is a negative number')

a = 1
if a > 0:
    print('a is a positive number')
elif a < 0:
    print('a is a negative number')
else:
    print('a is zero')

a = 3
print('a is positive') if a > 0 else print('a is negative')

a = -6
if a > 0:
    if a % 2 == 0:
        print('a is positive number and even number')
    else: 
        print('a is positive number')
elif a == 0:
    print('a is zero')
else:
    print('a is a negative number')

    a = -9
if a > 0 and a % 2 == 0:
    print('a is positive and an even number')
elif a > 0 and a % 2 != 0:
    print('a is positive number')
elif a == 0:
    print('a is 0')
else:
    print('a is negative')

user = 'Kamran'
access_level = 6
if user == 'admin' or access_level >=4:
    print('Access Granted')
else:
    print('Access Denied')

    #Exercise-Level-1
#1
age = int(input('Enter your age: '))
age_1 = 18 - age
if age > 18:
    print('You are old enough to learn to drive.')
else:
    print('You need {} more to learn to drive.'.format(age_1))

#2
your_age = int(input('Enter your age:'))
my_age = 25
if your_age > my_age:
    older_diff = your_age - my_age
    print('You are {} older than me.'.format(older_diff))
elif your_age < my_age:
    younger_diff = my_age - your_age
    print('You are {} younger than me.'.format(younger_diff))
else:
    print('We both are of same age.')

#3
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
if a > b:
    print('{} is greater than {}'.format(a,b))
elif a < b:
    print('{} is greater than {}'.format(b,a))
elif a == b:
    print('{} is equal to {}'.format(a,b))

#Exercise-Level-2
#1
score = int(input('Enter the score:'))
if score >= 80 and score <= 100:
    print('Congratulations! You have scored A Grade')
elif score >= 70 and score <= 89:
    print('Congratulations! You have scored B Grade')
elif score >= 60 and score <= 69:
    print('You have scored C Grade, you can do better')
elif score >= 50 and score <= 59:
    print('You have scored D, Work hard')
elif score >=0 and score <= 49:
    print('You got F, Work hard and try again. All the best')

#2
#a = input('Enter the season: ')
#b = ['September','October','November']
#c = ['December', 'January', 'February']
#d = ['March', 'April','May']
#e = ['June', 'August', 'July']
#if a == b :
 #   print('The entered month comes in Autumn')
#elif a == c :
 #   print('The entered month comes in Winter')
#elif a == d :
 #   print('The entered month comes in Spring')
#elif a == e :
 #   print('The entered month comes in Summer')

 #2 Not favourable result
month = input('Enter the month: ')
if month == 'January':
    print('It is winter')
elif month == 'September':
    print('It is autumn')
elif month == 'June' :
    print('It is summer')
elif month == 'March':
    print('It is spring')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit name: ')
if new_fruit != fruits :  #and new_fruit == 'papaya':
    fruits.append(new_fruit)
    print('The fruit in the list is {}'.format(new_fruit))
else:
    print('That fruit already exist in the list')

#Exercise-Level-3
#4
person = {
    'first_name': 'Kamran',
    'last_name': 'Habib',
    'age': 25,
    'country': 'Finland',
    'is_married': False,
    'skills': ['Python','SQL','HTML'],
    'address': {
        'street': 'Park Avenue',
        'city': 'New York City'
    }
}
