


def display(list):
    for ele in list:
        print(ele)
    
row3 = ['1','2','3']
row2 = ['4','5','6']
row1 = ['7','8','9']

inputbord=[[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]


print('Player 1 hase X and player 2 has O')

print('Chosse a position to put your mark')
display([row3,row2,row1])
print('Hares your Tic Tak To bord')
display(inputbord)

def userInput():
    if p1 :
        return int(input("Palyer 1 select your position: " ))
    else:
        return int(input("Palyer 2 select your position: " ))

    



def fill(p1):
    
    if p1:
        input = userInput()-1
        text = "X"
    
    else:
        input = userInput()-1
        text = "O"

    index = input%3
    row = int(input/3)
    if (inputbord[row][index] == ' '):
        inputbord[row][index] = text
        display(inputbord)
        
    else:
        print("Tis posiition is all ready filled")
        fill(p1)
    
 


p1=True
for x in range (0,9):
    
    fill(p1)
    p1 = not p1

