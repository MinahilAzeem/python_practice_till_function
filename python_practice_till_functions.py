#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Minahil")
print("Azeem")


# In[53]:


print('     @    \n   *  * \n  *    * \n *      * \n*________*\n____[]____\n')


# In[3]:


print("Minahil", end=" ")
print("Azeem")


# In[5]:


print("Minahil","Azeem", sep=" *** ")


# ## Variable

# In[6]:


variable=780
print(variable)


# In[7]:


type(variable)


# ## BMI Calculator

# In[8]:


weight= 22
height= 3.56
bmi= weight /(height*height)
print(bmi)


# In[9]:


weight= float(input("Enter your weight: "))
height= float(input("Enter your height: "))
bmi= weight /(height*height)
print(bmi)


# ## Slicing

# In[10]:


name="Minahil Azeem"
print(name[5:9])


# In[39]:


lst=['amina','fiza','aira',78]
lst.append(67)
print(lst)


# In[40]:


lst.count('aira')


# In[41]:


lst.extend([["new","list"]])


# In[42]:


print(lst)


# In[43]:


lst.index('aira')


# In[44]:


lst.insert(1,'Minahil')


# In[45]:


print(lst)


# In[46]:


lst.remove(67)


# In[47]:


print(lst)


# In[48]:


lst.pop(4)


# In[49]:


lst.pop()


# ## TYPE CONVERSION

# In[55]:


age=19
type(age)


# In[56]:


float_val=float(age)
type(float_val)


# ## Loops

# In[1]:


marks=int(input("Enter your marks: "))
if marks>80:
    print('A grade')


# In[2]:


marks=int(input("Enter your marks: "))
if marks>80:
    print('A grade')
else:
    print('Pass')


# In[3]:


marks=int(input("Enter your marks: "))
if marks>=90:
    print('A grade')
elif marks>=70:
    print('B grade')
elif marks>=50:
    print('C grade')
else:
    print('Fail')


# In[4]:


num=int(input('Enter any number to check: '))
if num > 0:
    print(num, ' is positive')
elif num < 0:
    print(num, ' is negative')
else:
    print(num, ' is invalid')


# In[1]:


num=int(input('Enter any number to check: '))
if num > 0:
    print(num, ' is positive')
elif num < 0:
    print(num, ' is negative')
else:
    print(num, ' is invalid')


# In[2]:


num=int(input('Enter any number to check: '))
if num > 0:
    print(num, ' is positive')
elif num < 0:
    print(num, ' is negative')
else:
    print(num, ' is invalid')


# In[5]:


given_num=int(input('Enter number: '))   #get number from user
if given_num > 5:
    square= (given_num * given_num)
    print("Square of ", given_num, "is: ",square)
else:
    print('The given number is less than 6')


# ## Shorthand if

# In[7]:


num1,num2= 9,7
if (num1>num2): print(num1,' is greater than', num2)


# In[11]:


def password_check(password):
    if password == 'Amina45':
        print('Access accepted')
    else:
        print('Access Denied')
        


# In[13]:


password_check('Amina45')


# In[14]:


password_check('Amina5')


# In[16]:


for i in range(30):         #'in' is membership operator
    print('Minahil')


# In[17]:


lst1=['Minahil','Musfira','Amina','Abdullah','Azeem','Rubina']     #list of strings
for i in lst1:
    print(i,' is in list1')


# In[18]:


lst_of_num=[10,20,45,50,60,34]
length_of_lst=len(lst_of_num)
sum=0
for i in lst_of_num:
    sum= sum+ i
average=sum/length_of_lst
print('Average for list of numbers is ',average)


# In[19]:


word='Minahil Azeem'
for i in word:
    print(i)


# In[21]:


for k in range(2,7):
    print(k)


# In[28]:


list2=['apple','banana','Date','Grapes','Melon','Orange']
for i in range(len(list2)):
    print(i,list2[i])


# In[30]:


my_dic={1:'Maniha', 2:'Minahil', 3:'Musfira', 4:'Amina', 5:'Abdullah'}
for value in my_dic.values():
    print(value)


# In[31]:


my_dic={1:'Maniha', 2:'Minahil', 3:'Musfira', 4:'Amina', 5:'Abdullah'}
for key in my_dic.keys():
    print(key)


# In[32]:


lst3=[2,5,6,3,9,10,18,7,13]
for num in lst3:
    if num % 2 ==0:
        print(num, 'is even')
    else:
        print(num, 'is odd')
    


# In[2]:


current_num=-5
while current_num < 5:
    print(current_num)
    current_num += 1


# In[5]:


numb=1
total=0
while numb <= 10:
    total +=numb
    numb += 1
print("Sum of first ten number is :",total)


# In[1]:


value=12
while value > 0:
    print(value)
    value -= 2
    
print("Loop is completed")     


# In[4]:


count=0
n=180
while n > 10:
    n= n/3
    count= count+1
print('180 is divided by',count,' number of time')
        


# # Print even and odd numbers between 1 & given number

# In[2]:


given_num=int(input('Énter number: '))
num=1
while (1<=num<=given_num):
    if num%2==0:
        print(num,' is even')
        #num=num+1
    else:
        print(num,' is odd')
        #num=num+1
    num=num+1


# ## Function

# In[1]:


def greet():
    print("Hello everybody!")


# In[2]:


greet()


# In[3]:


def greeting(msg):
    print("hello!",msg)


# In[8]:


greeting("Minahil, How are you")


# In[9]:


#Function to add two numbers
def add_two_numbers():
    num1=12
    num2=5
    sum=num1+num2
    print("The sum of two numbers is:  ", sum)


# In[10]:


add_two_numbers()

#Generate full name
def full_name():
    first_name="Minahil"
    second_name="Azeem"
    space=" "
    full_name=first_name+space+second_name
    return full_name
    
# In[2]:


#Generate full name
def generate_full_name():
    first_name="Minahil"
    second_name="Azeem"
    space=" "
    full_name=first_name+space+second_name
    return full_name


# In[3]:


generate_full_name()


# ## function to display sum by getting input from user

# In[4]:


def user_input():
    num1=int(input('Enter first number: '))
    num2=int(input('Enter Second number: '))
    sum=num1+num2
    return sum


# In[5]:


user_input()


# ## Write a function to add two numbers using parameters

# In[3]:


def sum(a,b):
    return a+b


# In[4]:


sum(3,5)


# ## Write a function to tell that this specific number is even or odd

# In[5]:


def even_odd(num):
    if num%2==0:
        print(num, " is even ")
    else:
        print(num, " is odd")


# In[6]:


even_odd(6)


# In[8]:


even_odd(3)


# ## Getting input from user on runtime

# In[9]:


def even_odd():
    num=int(input('Enter num'))
    if num%2==0:
        print(num, " is even ")
    else:
        print(num, " is odd")


# In[10]:


even_odd()


# 

# 
# 

# ## Write a program to check whether num is positive, negative or zero

# In[21]:


def pos_neg(num3):
    if num3>0:
        print(num3," is positive")
    elif num3==0:
        print(num3," is zero")
    else:
        print(num3, " is negative")
    return


# In[18]:


pos_neg(7)


# In[22]:


pos_neg(-2)


# In[23]:


pos_neg(0)


# ## Calculate sum of numbers to the specified limit

# In[24]:


def sum_to_limit(limit):
    total_sum=0
    for i in range(limit+1):
        total_sum+=i
        
    return total_sum


# In[25]:


sum_to_limit(10)


# ## Calculate age

# In[26]:


def check_age(birth_date,current_year):
    age=current_year-birth_date
    return age


# In[29]:


check_age(2005,2024)

