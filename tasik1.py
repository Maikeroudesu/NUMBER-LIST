numbers = int(input("Enter a number: "))
list = []

for data in range(numbers):
    number = int(input("my number: "))
    list.append(number)
    
   
for data in list:
    if data < 0:
        print(str(data) + " " + "negative ")
    elif data > 0:
        print(str(data) + " " + "postive ")
  