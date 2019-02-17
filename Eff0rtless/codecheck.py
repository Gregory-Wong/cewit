def codecheck(code):
    #variables
    user_code = input("Code: ") #input
    a = False
    count = 1
    #code check
    while(a==False):
        #failure count
        if (count > 5):
            print("Too many tries! Try again later")
            a = True
        elif (user_code != code):
            print ("invalid code. Try again") #failure repeat
            user_code = input("Code: ") #input
            count += 1
        else:
            print ("good")
            a=True
    return a
code = '1'
a = codecheck(code)

print (a)