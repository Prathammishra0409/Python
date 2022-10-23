num = input("Please Enter Your  Character : ")

if((num>= 'a' and num <= 'z') or (num >= 'A' and num <= 'Z')): 
    print("The Given Character ", num, "is an Alphabet") 
elif(num >= '0' and num <= '9'):
    print("The Given Character ", num, "is a Digit")
else:
    print("The Given Character ", num, "is a Special Character")
