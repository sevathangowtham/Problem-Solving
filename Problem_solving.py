#Start from Zero 
# List of problems to solve


#1. A list stores many values
list_of_values = [10, 20, 30 , 40, 50]
print('Access the first index',list_of_values[0]) #  access  one value
print('Last index vslues: ',list_of_values[-1]) # access last index values
print('adding a  new values into the list :',list_of_values.append(60)) # add the new value in the last
list_of_values[3] = 51
print('Whole List :',list_of_values)
print('Len of the list :',len(list_of_values)) # lenth of the list

#2. A loop visits each item and we need to add all the vales like 20 

list_1 = [10,20,30,40]
total_value = 0
for i in list_1:
    total_value = total_value + i
print(total_value)

#3) finding the  even number
def find_even(num):
    if num % 2 ==0:
        print(f'{num} is even')
find_even(2)

#4) find the maximum of the number 
list_2 = [10,20,30,25,0,30]
max_list = list_2[0]
for find_max in list_2:
    if find_max  > max_list:
        max_list = find_max
print(f'{max_list} is maximum of the list')

#5) count the even number using for loop
count_even = [2,4,6]
count = 0 
for find_evem_count in count_even:
    if find_evem_count % 2 == 0 :
        count += 1
print(f'{count} is the total even number')

#5) reverce the list using for loop

def reverce_list(num):
    for i in range(len(num)-1 ,-1 ,-1):
        print(num[i])
reverce_list(num=[1,2,3,10,4,5,6,7,8])


#6) fizzbuzz(n) prints 1 to n, but “Fizz” for multiples of 3,
#  “Buzz” for multiples of 5, and “FizzBuzz” for both.

def fizzbuzz(n):
    for i in range(1 ,n):
        if i % 5==0 & i % 3==0:
            print('FizzBuzz')
        elif i % 3==0 :
            print('Fizz')
        elif i % 5 ==0:
            print('Buzz')
        else :
            print('not divided by any : ',i)
fizzbuzz(10)



#Lesson 2: Strings and dictionaries

word = 'hello'
print(word[0]) #Acces only one letter.
print(word[-1]) #  Access the last one element
print(word[::-1]) #Access the reverce 
print(word[1 : 4]) #Access the element from index of 1 to till 3rd index
print('Lenth ofthe String',len(word))# lenth of the string

#Access each ofthe element 

for ch in word:
    print(ch)


#Dictinory 
#dict is key : value pair key is very fast that's which why base of hashmap problem

ages = {'Ravi' : 25 ,'Anu': 30}
print(ages['Anu']) #print the value of anu it so faster because its not searhing throuh the list 
ages['renshow'] = 30 # by asigning a new key we can add the new values
ages['Anu']=26 #update the new valus why assgnig to old key to replace new values
print('Ravi' in ages) 
print(ages)
for key in ages:
    print(key , ages[key]) # loop over the key , visit the every key

#question 1 
#count the each charecter of the dict

def count_aeach_ch (text):
    counts= {}
    for ch in text:
        if ch in counts:
            counts[ch] +=1
        else:
            counts[ch] = 1 
    return counts

print(count_aeach_ch('LLM is Neural network try to predict the nett token  or pices of word the word which you have given so far '))

# Question 2 return the string in reverse order using for loop
def reverse_string(s):
    result = ""
    for character in range(len(s)-1 ,-1 ,-1):
        result += s[character]
    return result
print(reverce_list('apple'))

# Question 3 treurn TRUE if the string reads the same forward and backward for example(MADAM)

def s_palindrom(s):
    a =[]
    b =[]
    for forward in s:
        a.append(forward)
    for backward in range(len(s)-1,-1,-1):
        b.append(s[backward])
    if a ==b:
        return True
    else:
        return False
print(s_palindrom('gowtham'))


# return the vowels are in the string 

def count_vowels(s):
    vowels_leter = ['a','e','i','o','u']
    count_let_vowels = 0
    for ch in s . lower() :
        if ch in vowels_leter:
            count_let_vowels += 1
    return count_let_vowels
print(count_vowels('Appl'))

# Leson 3 big O Notation used to measure rining time and space as our program grows as input size gorw as 


#nested for loop 

visit_each_time= [1,2,3]
for i in visit_each_time:
    for j in visit_each_time:#
        print(i,j)  # so the inner loop fenish before move to the oupter loop


#Code	3 numbers	1,000 numbers	Big O
#nums[0]	1 step	1 step	O(1)
#One loop	3 steps	1,000 steps	O(n)
#Loop inside a loop	9 steps	1,000,000 steps	O(n²)

# understanding of each time complexity in the first one is big O notation O(1) even if we have a milion of value we are going to take the only one values so its a O(1) 
# the second one is it will incrice as input gorw as which means it will check each item of the list 
# taird one is  nested loop n*n

#O(1) 
nums = [10,20,30,40,50,]
print(nums[0]) # so we can see here we accessing only one values even if we have 4 or 4 milion we are doing onyu one step 

#O(n) just impagine we have a some targe valus we need to find out the target tis 40 we know the values but we don't have any idea se we need to check every box

def find_target(numbers , target):

    for find in range (len(numbers)):
        if numbers[find] == target:
            return find
    return -1 

print(find_target([100, 20, 30, 40], 30))  

#find_min(nums) returns the smallest number, using a loop like your find_max.
find_valus = [100,20,30]

finding_min = find_valus[0]

for find_mas in find_valus:

    if find_mas <  finding_min:

        finding_min = find_mas
        
print(finding_min)