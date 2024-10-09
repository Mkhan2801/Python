def myfunction(n):
    safe_person = 1
    power = 0
    while(n>1):
        power = power+1
        if(n%2):
            n = ((n-1)/2)
            safe_person = pow(2,power)+safe_person
        else:
            n=n/2
    return safe_person



print(myfunction(100))

            
