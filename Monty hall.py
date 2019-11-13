from random import randint

#Taking input 1 - 3
while True:
    print(" ______    ______    ______ ")
    print(" |     |   |     |   |     |")
    print(" |  1  |   |  2  |   |  3  |")
    print(" |     |   |     |   |     |")
    print(" |_____|   |_____|   |_____|")
    choice = input("Select a door (1-3) :")
    choice_index = int(choice) - 1
    if int(choice) <= 0 or int(choice) > 3:
    	print("Enter number between 1 - 3")
    	print("Try Again !!!")
    else:
    	break

if choice == str(1):
    print(" ______    ______    ______ ")
    print(" |     |   |     |   |     |")
    print(" |  1  |   |  2  |   |  3  |")
    print("|selected| |     |   |     |")
    print(" |_____|   |_____|   |_____|")
elif choice == str(2):
    print(" ______    ______    ______ ")
    print(" |     |   |     |   |     |")
    print(" |  1  |   |  2  |   |  3  |")
    print(" |     |  |selected| |     |")
    print(" |_____|   |_____|   |_____|")
else:
    print(" ______    ______    ______ ")
    print(" |     |   |     |   |     |")
    print(" |  1  |   |  2  |   |  3  |")
    print(" |     |   |     |  |selected|")
    print(" |_____|   |_____|   |_____|")
        
        
print()
  
#Random list  1-3
list=["Nothing Here", "Nothing Here"]
list.insert(randint(0, 2), "You win")
 
 #offer func
def offer():
	global choice
	#print("You have chosen door " +                    str(choice) )
	inp=input( "Would you like to switch the door? y/n : ")
	if inp == "n" or inp == "N" :
            
	    return "n"
	elif inp == "y" or inp == "Y":
	    return "y"
	else:
	    print('Invalid input')

#Expose one door
if list[0] =="You win" and choice_index==0:
	expo = randint(1,2)
elif list[0]!="You win" and choice_index==0:
	if list.index("You win") == 1:
		expo = 2
	else:
		expo = 1

elif list[1]== "You win" and choice_index==1:
	expo = randint(1,2)
	if expo == 1:
		expo = 0
elif list[1]!= "You win" and choice_index==1:
	if list.index("You win")==0:
		expo = 2
	else:
		expo = 0

elif list[2] == "You win" and choice_index==2:
	expo = randint(0,1)
elif list[2]!="You win" and choice_index==2:
	if list.index('You win') == 0:
		expo = 1
	else:
		expo  = 0

if expo == 0:
    print(" Nothing                    ")
elif expo == 1:
    print("           Nothing          ")
elif expo == 2:
    print("                     Nothing")

print()
print("There's nothing in door " + str(expo+1))

reply = offer()
print()

if reply == "n":
    
    print(list[choice_index])
    print("It is in door " + str(list.index("You win") + 1))
          
          
elif reply == 'y':
    win_index = list.index("You win")
    list[expo] = "_"
    list[choice_index]= "_"
    print("Switching selected door...", end = "\n\n")
    for x in list:        
        if x != "_":            
            print(x)
            print("It is in door " + str(win_index + 1))
            

