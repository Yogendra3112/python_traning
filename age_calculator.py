"""
Name: 
    Age Calculator         
Filename:
    age_cal.py
Problem Statement:
    Lets assume your present age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back
Data:
    Not required
Extension:
    Take the present age of the user from input 
Hint: 
    You need to add 5 to present age to calculate future age 
    You need to subtract 10 present age to calculate your past age
Algorithm:
    Not Available  
Boiler Plate Code:
    Not Available 
Sample Input:
    Not Available 
Sample Output:
    Not Available 
"""   


age = input('Your present age, Please')
n = input('no of years')
t = str(input('Please enter F for future age and P for past age'))
if t == 'f' or t == 'F':
    print(int(age)+int(n))a
elif t == 'p' or t == 'P':
    print(int(age)-int(n))
else:
    print('invalid input')

output==================================================================


Your present age, Please21
no of years5
Please enter F for future age and P for past agep
16
