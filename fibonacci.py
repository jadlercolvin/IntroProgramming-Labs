def main():
    a,b = 1,1
    print("This is the program to find the Fibonacci numbers.")
    n=eval(input("What is n?"))
    n_int=int(n-2)
    for i in range(n_int):
        a,b=b,a+b
    print(b)
    
main()


    
