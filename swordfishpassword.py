password = 'swordfish'
passwordattempts = 0
while passwordattempts < 3:
    print('Please enter your password: ')
    passwordinput = input()
    if passwordinput == password:
        print('Access granted.')
        break
    else:
        passwordattempts = passwordattempts + 1
        print('Incorrect password. You have ', str(3 - passwordattempts), ' attempts remaining.')
        if passwordattempts == 3 and passwordinput != password:
            print('Access denied.')

        

        
    
