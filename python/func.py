
def dectobin(x):
    if x>0:
        print(x%2,end=' ')
        dectobin(x//2)
        
x=int(input("enter the integer= "))
dectobin(x)


#Recursive Function to convert decimal to binary

def decimalToBinary(ip_val):
    if ip_val >= 1:
    # recursive function call
        decimalToBinary(ip_val // 2)
    
    # printing remainder from each function call
    print(ip_val % 2, end = '')
 
# Driver Code
if __name__ == '__main__':
    # decimal value
    ip_val = 24
     
    # Calling special function
    decimalToBinary(ip_val)
