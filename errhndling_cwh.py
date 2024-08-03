a = input("Enter any value between 5 and 9: ")
try:
    if (int(a)<5 or int(a)>9):
        raise ValueError("Value should be between 5 and 9")

except:
    if a == str(a) and a !="quit":
        raise ValueError("Value should be between 5 and 9")
    
print("code ended successfuly")