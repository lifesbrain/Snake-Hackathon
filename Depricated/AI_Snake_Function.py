#The Snake AI to be pulled into the game as a second player
'''From the possitions of the AI Snake and the Pie
- The AI will decide whether to return up down left or right '''

up = (0,-1) 
down = (0,1)
left = (-1,0)
right = (1,0)

def aiSnakeController(aiS,hS,pi):
    aiHeadX, aiHeadY = aiS[0] #Assign coordinates for ai head
    piX, piY = pi #Assign coordinates for Pie

    disX = aiHeadX - piX #Distance of Pie on x axis, pos int left, neg int right
    disY = aiHeadY - piY #Distance of Pie on y axis, pos int up, neg int down

    if disX > 0: #Pie is Left
        return left
    
    elif disX < 0: #Pie is Right
        return right
    
    else: #Pie is horizontaly alligned
        if disY < 0: #Pie Down
            return down
        
        elif disY > 0: #Pie Up
            return up
        
        else: #The Snake is on the Pie
            print("On the Pie")
            return up


'''    
To add:
 Don't eat own body
 Don't eat other snakes

Could make a set of all squares - list of snakes and food and only let snake enter remainder?

if disX > 0 #Pie West
    if disY > 0 #Pie South West
    elif disY < 0 #Pie North West
    else: #Pie West

elif disX < 0 #Pie East
    if disY > 0 #Pie South East
    elif disY < 0 #Pie North East
    else: #Pie East

else #Pie is horizonal alligned
    if disY > 0 #Pie South
    elif disY < 0 #Pie North
    else: #Your on the Pie (Hightly unlikely, but better to plan)

'''
