n=int(input("Choose the type of Item: 1 for footwear / 2 for apperals" " "))
print("You chosen :", n)
if n == 1:    
    f = float(input("Enter price of footwear per pair:"))
    print("Price /pair of footwear is:", f)
    if f<=500:
        print("GST Rate is: 5%")
        GSTAmount=(f*5/100)/100
        NetPrice=f+GSTAmount
    else:
        print("GST Rate is: 18%")
        GSTAmount=(f*18/100)/100
        NetPrice=f+GSTAmount
elif n==2:
    a = float(input("Enter price of apperals per piece:"))
    print("Price /piece of apperals is:", a)
    if a<=1000:
        print("GST Rate is: 5%")
        GSTAmount=(a*5/100)/100
        NetPrice=a+GSTAmount
    else:
        printf("GST Rate is: 12%")
        GSTAmount=(a*12/100)/100
        NetPrice=a+GSTAmount
print("Total Selling Price is: ", NetPrice)
