#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###problem-1
#write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200(both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line


# In[ ]:


for num in range(2000,3201):
    if num%7 ==0 and num%5 !=0:
        print(num,end=',')


# In[ ]:


## problem-2
# write a python program to accept the users first name and last name and then getting them printed in the reverse order with a space between first name and last name


# In[ ]:


first_name = input('enter your first name: ')
last_name = input('enter your last name: ')
print(first_name[::-1]+' '+last_name[::-1])


# In[ ]:


## problem-3
#write a python program to find the volume of a sphere with diameter 12 cm.


# In[ ]:


diameter = 12
r = diameter/2
volume = (4/3)*(22/7)*(r**3)
print(volume)
    

