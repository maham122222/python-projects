import random

f=open('file.txt','r')
print(f)
# word=f.read
word= f.read()
# print(word)
f.close()
# r->for read file
# w->for write file
# rt->for opening txt file its by default
# rb->open it as a binary file
# word.split()

random.choice(word)
print("Word guessing game")

# if random_word in (word):
#     print("word is realted to fruit")



user_guess=''
chances=3


while chances >0:
    wrong_guess=0
    for ch in (word):
        if ch in user_guess:
            print(ch, end =' ')
        else:
            wrong_guess+=1
            print('_' ,end =' ')
    if wrong_guess ==0:
        print( 'you win the game',word)
        break
    guess=input('guess the word')
    user_guess+=guess

    if guess not in (word):
        chances-=1
        print (f"incorrect you have left {chances} chances")
        if chances==0:
            print('game over try again')
