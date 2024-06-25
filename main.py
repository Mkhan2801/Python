#Start Function

def start():
    print("Do tou want to start new game")
    enter = input("press y or n : " )
    
    if enter == "y" or enter == "Y":
        p1=True
        for x in range (0,9):
            updatebord(p1)
            p1 = not p1
        
        if not win():
            print("No One Win this Match")
            start()

    else:
        print("Thank you for playing")

# Display Bord function
def display(list):
    for ele in list:
        print(ele)
    
    

#position data
row = [['1','2','3'],['4','5','6'],['7','8','9']]

#Game bord
inputbord=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]




print('Player 1 hase X and player 2 has O')

print('Chosse a position to put your mark')

display(row)

print('Hares your Tic Tak To bord')

display(inputbord)

# Get input from user function
def userInput(p1tern):

    input_num = 'Wrong'

    while not input_num in range(1,10) and not win():

        if p1tern :
            input_num =  int(input("Palyer 1 select your position: " ))
        else:
            input_num =  int(input("Palyer 2 select your position: " ))

        if not input_num in range(1,10):
            print("Plese enter a valed input")

    return input_num



# update Bord function 
def updatebord(tern):
    
    
    if tern:
        input = userInput(tern)
        text = "X"
    
    else:
        input = userInput(tern)
        text = "O"

    input = input-1
    index = input%3
    row = int(input/3)
    if (inputbord[row][index] == ' '):
        inputbord[row][index] = text
        display(inputbord)
        
    else:
        print("Tis posiition is all ready filled")
        display(inputbord)
        updatebord(tern)

    if win():
        if tern:
            print("congratulation P1 win")
        else:
            print("congratulation P2 win")
        start()
    
 

def win():
    # some function 
    return False





start()