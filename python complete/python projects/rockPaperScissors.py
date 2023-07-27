import random

game= [1,2,3]

random_num=random.choice(game)

compuMove = " "

input=input("rock paper scissors")


def playGame(userMove):
    compMove = pickCompMove()
#    //   console.log(compMove);

    result = ''
#    //   for scissors
    if(userMove == 'scissors'):

        if(compMove =='rock'):
            result='you lose'
        elif(compMove=='paper'):
            result='you win'
        elif(compMove=='scissors'):
            result='tie'
     
   
#    // for paper
    if(userMove == 'paper'):
        if(compMove =='rock'):
            result='you win'
        elif(compMove =='paper'):
            result='tie'
        elif(compMove =='scissors'):
            result='you lose'
     
   

#    // for rock

   if(userMove == 'rock'):
        if(compMove =='rock'):
            result='tie'
        elif(compMove =='paper'):
            result='you lose'
        elif(compMove =='scissors'):
            result='you win'
     



# if random_num == 1:
#     compuMove = 'Rock'
# elif random_num == 2:
#     compuMove = 'paper'
# elif random_num == 3:
#     compuMove = 'scissors'


    