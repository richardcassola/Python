#Input and Output

# Creating an empty list(array)
nums = [] 
# appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")
nums.append("5")
print(nums)

# getting input from user
name = input("Enter your name: ") 
#result will be Hello and his input
print("hello", name)

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
  
num3 = num1 * num2
print("Product is: ", num3)