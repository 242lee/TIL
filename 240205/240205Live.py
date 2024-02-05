# s1 = 'abc'
# s2 = 'abc'
# print(s1 == s2) #True
# print(s1 is s2) #True

# s3 = s1[:2] + 'c'
# print(s1 == s3) #True
# print(s1 is s3) #False

#-----------------------------

# print(ord('0'))

# print(chr(65)) #Ascii -> num

#------------------------------
def itoa(a):
    s =''
    while a>0:
        s = chr((a % 10) + ord('0')) + s
        a //= 10
    return s

print(itoa(123))       #123
print(type(itoa(123))) #<class 'str'>
