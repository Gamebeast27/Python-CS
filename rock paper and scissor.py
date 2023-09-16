import random
print('WELCOME')
print('Let\'s play rock paper and scissor')
ch = ['rock','paper','scissor']
rd=int(input('Enter numbers of rounds you want to play: '))
wc=0
wp=0
for i in range(rd):
    player=input('What you select?: ')
    com= random.choice(ch)
    print('Computer:',com)
    if player == com :
        print('Draw')
    elif (com=='rock'and player=='scissor') or (com=='paper' and player=='rock') or (com=='scissor' and player=='paper'):
        print('Computer Wins')
        wc+=1
    elif (player=='rock' and com=='scissor') or (player=='paper' and com=='rock') or (player=='scissor' and com=='paper'):
        print('Player wins')
        wp+=1
    if i <rd-1:
        print('Next Round')
print('Score: \n Computer:',wc,'\n Player: ', wp)
if wc>wp:
    print('COMPUTER WINS')
elif wc<wp:
    print('PLAYER WINS')
else :
    print('DRAW, TRY AGAIN')
