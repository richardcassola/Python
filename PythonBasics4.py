def getInt():
    result = int(input("Enter a number: "))
    return result
    
def Main():
    print("Started!")

# calling the getInt function and
# storing its returned value in the output var
    output = getInt()
    print(output)       

# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()