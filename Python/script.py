Print ("I'm about to be the next Jeff Bezos")
list1 = [2, 3, 5, 8, 89]


print(list1[::-1])  #This is a way to reverse a list 

#list1.sort(reverse=True) - This is another way to reverse a list 

#print(list1)

#If i want to scout certain numbers I need from a list

listone = [3, 6, 9, 12, 15, 18, 21]
listtwo = [4, 8, 12, 16, 20, 24, 28]

listthree =[] #this is important to create so then i can at the end append the values I'm
#looking for

for x in listone:
    if x % 2 ==1: #for odd numbersin the list
        listthree.append(x) #this function will put my values i scouted in the empty list for me
        print(listthree)
for x in listtwo:
    if x% 2 ==0: #for even numbers in the list
        listthree.append(x)
        print(listthree)


sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]


list_1 = sampleList[:3]

print(list_1[::-1])
list_2 = sampleList[3:6]
print(list_2[::-1])
list_3 = sampleList[6:]
print(list_3[::-1])

str1 = "JhonDipPeta"

len(str1)
s1 = str1[4:7]
print(s1)

S1 = "Ault"
s2 = "kelly"

#this is the basi =c way to concatenate data by using the slicing method
s_1 = S1[:2]
s_2 = S1[2:]

print(s_1 + s2 + s_2)

#this is an alternative to concatenate data 

midle_number = int(len(S1)/2) # because the len is an integer the division had to occur outside if it's argument

result = S1[:midle_number] + s2 + S1[midle_number:]

print(result) #results must always be printed to view the outcome to see whether the code has successfully run!

#exercise 1
x = 2
w = 4

if x%2 == 0 and w%2 == 0:
    print (min (x,w))
else:
    print (max (x,w))

#exercise 2

a = 20
b = 10
if a+b == 20 and a or b == 20:
    print ("True")
else:
    print("False")
    
#exercise 3