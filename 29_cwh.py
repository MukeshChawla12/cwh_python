#Recursion Program 
# printing a table of a given number using recursive function
def tab_rec_fun(n, i=1):
    if(i>10):
        return
    print(n, "*", i, "=", n*i)
    return tab_rec_fun(n, i+1)
num = int(input("Enter a number : "))
print("\nTable of", num, "is:")
tab_rec_fun(num)
##fibonacci series usinf recursive function
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
terms=int(input("Enter the no. of terms :"))
for i in range(terms):
    print(fibo(i),end=" ")

   


 