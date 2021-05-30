#1.Write a  program to find length of a string.
'''
st=str(input("Enter the String for find Length : "))

count=0

for i in range(len(st)):
    count=count+1

print("Length of String : ",count)

'''
#2.Write a  program to copy one string to another string.
'''
st=str(input("Enter the String  : "))
another_st=" "

for i in range(len(st)):
    another_st=another_st+st[i]

print(another_st)

'''

#3.Write a  program to concatenate two strings.
'''
st=str(input("Enter the String : "))

another_st=str(input("Enter the String  : "))

join_st=st+" "+another_st

print(join_st)

'''
#4.Write a  program to compare two strings.
'''
st=str(input("Enter the String : "))

another_st=str(input("Enter the String  : "))

first_string_len=len(st)
second_string_len=len(another_st)

if first_string_len==second_string_len:
    check=1
    for i in range(first_string_len):
        if st[i] != another_st[i]:
            check=0
            break
        
    if check==0:
        print("String are not Equal ")
    else:
        print("String are  Equal ")
        
else:
    print("String are not Equal ")
        
'''

#5.Write a  program to convert lowercase string to uppercase.
'''
st=str(input("Enter the String : "))
upper_st=" "
for i in range(len(st)):
    if st[i]>='a' and st[i]<='z':
        upper_st=upper_st+chr ((ord (st[i]) -32))

    else:
        st=st+st[i]

print(str(st))
print()
print(str(upper_st))
'''
#6.#5.Write a  program to convert  string  uppercase to lowercase.

'''
st=str(input("Enter the String : "))
lower_st=" "
for i in range(len(st)):
    if st[i]>='A' and st[i]<='Z':
        lower_st=lower_st+chr ((ord (st[i]) +32))

print(str(st))
print()
print(str(lower_st))

'''
#7.Write a  program to toggle case of each character of a string.
'''
st=str(input("Enter the String : "))
toggle_string=' '
for i in range(len(st)):
    
    if st[i]>='a' and st[i]<='z':
        toggle_string=toggle_string +chr((ord(st[i])-32))
        
    elif  st[i]>='A' and st[i]<='Z':
        toggle_string=toggle_string +chr((ord(st[i])+32))
        
    else:
       
        toggle_string = toggle_string + st[i]

print(st)
print()
print(toggle_string ," ")

'''

#8. Write a  program to find total number of alphabets, digits or special character in a string.
'''
st=str(input("Enter the String : "))

alphabets=0
digits=0
special_character=0

for i in range(len(st)):
    if st[i]>='a' and st[i]<='z' or  st[i]>='A' and st[i]<='Z':
        alphabets=alphabets+1

    elif st[i]>='0' and st[i]<='9' :
        digits=digits+1

    else:
        special_character=special_character+1


print("Total number of alphabets : ",alphabets)

print("Total number of digits : ",digits)

print("Total number of special character : ",special_character)
        

'''

#9.Write a  program to count total number of vowels and consonants in a string.

'''
st=str(input("Enter the String : "))

vowels=0
consonants=0

for i in range(len(st)):
    if st[i]>='a' and st[i]<='z' or  st[i]>='A' and st[i]<='Z':

        if st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o' or st[i]=='u' or st[i]=='A' or st[i]=='E' or st[i]=='I' or st[i]=='O' or st[i]=='U':
            vowels=vowels+1
        else:
            consonants=consonants+1

print("Total number of vowels : ",vowels)
print("Total number of consonants : ",consonants)

'''

#10.Write a  program to count total number of words in a string.
'''
str1 = input("Please Enter your Own String : ")
total = 1
i = 0

while(i < len(str1)):
    if(str1[i] == ' ' or str1[i] == '\n' or str1[i] == '\t'):
        total = total + 1
    i = i + 1

print("Total Number of Words in this String = ", total)

'''
#11.Write a  program to find reverse of a string.
'''
st = input("Please Enter your Own String : ")

for i in range(len(st)-1,-1,-1):
    print(st[i],end='')

'''

#12.Write a  program to check whether a string is palindrome or not.
'''
st = input("Please Enter your Own String : ")
rev_st=''
for i in st:
    rev_st=i+rev_st
print(rev_st)

if rev_st==st:
    print(rev_st," is Palindrome")
else:
    print(rev_st," is not Palindrome")

'''

#13.Write a  program to reverse order of words in a given string.
'''
st = input("Please Enter your Own String : ")
rev_st=''
rev_word=''
for i in st:
    rev_st=i+rev_st

#reverse the string in sentence  
print(rev_st)

#reverse again the string and sentence 
for j in rev_st:
    rev_word=rev_st+i

print(rev_word)

(still not solved)

'''

#14. program to find the first occurrence of a character in a string
'''
st = input("Enter your Own String : ")

len_st=len(st)
i=0

find_first_occurrence=input("Enter a Character : ")

while i<len_st:
    if st[i]==find_first_occurrence:
        print(f"Found {find_first_occurrence} at Index : {i}")
        break
    i=i+1

'''

#15.Write a program to find last occurrence of a character in a given string.
'''
st = input("Enter your Own String : ")
last_occurrence_character=input("Enter a Character : ")
found=-1
for i in range(len(st)):
    if st[i]==last_occurrence_character:
        found=i
if found==-1:
    print(" Character dosent exsist in String ")
else:
    print(f"Found {last_occurrence_character} at index {found+2}")

'''

#16.Write a  program to search all occurrences of a character in given string.

'''
st = input("Enter your Own String : ")

len_st=len(st)
i=0

find_all_occurrence=input("Enter a Character : ")

while i<len_st:
    if st[i]==find_all_occurrence:
        print(f"Found {find_all_occurrence} at Index : {i}")
        
    i=i+1

'''

#17.program to count occurrences of a character in a string
'''
st = input("Enter your Own String : ")

len_st=len(st)
i=0
count=0

find_all_occurrence=input("Enter a Character : ")

while i<len_st:
    if st[i]==find_all_occurrence:
        count=count+1     
    i=i+1

print(f"Found {find_all_occurrence} and its repate at {count} times")

'''



#18.program to remove  occurrence of a character from string

'''
st = str(input("Enter your Own String : "))
rev_chr=str(input("Enter your  character for remove : "))
result=''
for i in st:
    if i !=rev_chr:
        result=result+i
print(result)
    
'''

