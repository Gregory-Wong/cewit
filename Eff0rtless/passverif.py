def passstr(password):
    #variables
    a = False
    b = 0
    c = 0
    #count upper case
    for i in password:
        if(i.isupper()):
            b = b + 1
        if (i.isnumeric()):
            c = c + 1
    while (a == False):
        if ( len(password) < 8 and b < 1 and c < 1):
            print ("Invalid password")
            print ("Your password should contian at least 8 chacters,upper case letters and numbers.")
            password = input()
        elif (len(password) > 8 and b < 1 and c < 1):
            print ("Invalid password")
            print ("Your password is not long enough.")
            print ("You need at least one upper case letter.")
            print ("You need at least one number.")
            password = input()
        else:
            a = True            
            
