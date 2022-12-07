p=0
c=0
for number in range(10,20):
    if number == 0 or number == 1:
        print(number, "is a Neither prime nor composite")    
    else:
        for i in range(2, number):
            if (number % i == 0):
                c+=1
                print(number, "is a Composite Number")
                break
        else:
            p+=1
            print(number, "is a Prime Number")
            
print("Total number of composite number",c)

print("Total number of prime number",p)







        
