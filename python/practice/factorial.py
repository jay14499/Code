
def main():
    x=int(input("enter the number :"))
    fact=1
    for i in range(1,x+1):
        if (x>0):
            fact=fact*i

    print("factorial of x is:",fact)
      
if __name__ == "__main__":
    main()

