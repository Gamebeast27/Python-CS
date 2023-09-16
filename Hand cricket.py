def hand_cricket():
    
    import random
    print('WELCOME!')
    print('Let\'s play Hand Cricket.')
    print()
    print('RULES: \n 1. upto six runs are allowed. \n 2. for taking wicket you have to show same number as opponent.')
    print()
    toss= ['head','tails']
    ct= random.choice(toss)
    print('Let\'s toss the coin..')
    pt=input('What you select (head/tails) ? : ')
    print()
    inn = ['batting','bowling']
    rn=[1,2,3,4,5,6]
    plruns=0
    cpruns=0
    #if player wins the toss
    if ct == pt:
        print('Player Wins the Toss.')
        print()
        pi=input('What do you want to do first (batting/ bowling)? :' )
        if pi == 'batting':
            print('OK, you selected batting first')
            print()
            print('1st inning')
            print()
            while True:
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    cr=random.choice(rn)
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Player is OUT!')
                        print('Finale Score:',plruns)
                        print('inning ends..')
                        break
                    else:
                        print('Player scored',pr)
                        plruns=plruns+pr
                        print('Total Runs:',plruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                print()
            ps=plruns
                
            print()
            print()
            print('Now player\'s turn to defend the score.')
            print()
            print('2nd innings')
            print()
            while True:
                cr=random.choice(rn)
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Computer is OUT!')
                        print('Finale Score:',cpruns)
                        print('inning ends..')
                        break
                    else:
                        print('Computer scored',cr)
                        cpruns=cpruns+cr
                        print('Total Runs:',cpruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                cs=cpruns
                print()
                if cs > ps:
                    print('End of inning.')
                   
                    break
        else:
            print('OK, you selected bowling first')
            print()
            print('1st inning')
            print()
            while True:
                cr=random.choice(rn)
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Computer is OUT!')
                        print('Finale Score:',cpruns)
                        print('inning ends..')
                        break
                    else:
                        print('Computer scored',cr)
                        cpruns=cpruns+cr
                        print('Total Runs:',cpruns)
                    
                else:
                    print('Value greater then 6 not allowed!!!!')
                print()
            cs=cpruns
                
            print()
            print()
            print('Now player\'s turn score.')
            print()
            print('2nd innings')
            print()
            while True:
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    cr=random.choice(rn)
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Player is OUT!')
                        print('Finale Score:',plruns)
                        print('inning ends..')
                        break
                    else:
                        print('Player scored',pr)
                        plruns=plruns+pr
                        print('Total Runs:',plruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                ps=plruns
                print()
                if ps>cs:
                    print('End of innings.')
                    
                    break
    #if computer wins the toss
    else:
        print('Computer Wins the Toss.')
        print()
        ci=random.choice(inn)
        print('Computer select',ci,'first.')
        print()
        if ci == 'bowling':
            
            print()
            print('1st inning')
            print()
            while True:
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    cr=random.choice(rn)
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Player is OUT!')
                        print('Finale Score:',plruns)
                        print('inning ends..')
                        break
                    else:
                        print('Player scored',pr)
                        plruns=plruns+pr
                        print('Total Runs:',plruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                
                print()
            ps=plruns
            print()
            print()
            print('Now Computer\'s turn to score.')
            print()
            print('2nd innings')
            print()
            while True:
                cr=random.choice(rn)
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Computer is OUT!')
                        print('Finale Score:',cpruns)
                        print('inning ends..')
                        break
                    else:
                        print('Computer scored',cr)
                        cpruns=cpruns+cr
                        print('Total Runs:',cpruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                cs=cpruns
                print()
                if cs > ps:
                    print('End of innings')
                    
                    break
        else:
            
            print()
            print('1st inning')
            print()
            while True:
                cr=random.choice(rn)
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Computer is OUT!')
                        print('Finale Score:',cpruns)
                        print('inning ends..')
                        break
                    else:
                        print('Computer scored',cr)
                        cpruns=cpruns+cr
                        print('Total Runs:',cpruns)
                    
                else:
                    print('Value greater then 6 not allowed!!!!')
                
                print()
            cs=cpruns
            print()
            print()
            print('Now player\'s turn score.')
            print()
            print('2nd innings')
            print()
            while True:
                pr=int(input('Enter your run(s): '))
                if pr<=6:
                    cr=random.choice(rn)
                    print('Computer select:',cr)
                    if pr==cr:
                        print('Player is OUT!')
                        print('Finale Score:',plruns)
                        print('inning ends..')
                        break
                    else:
                        print('Player scored',pr)
                        plruns=plruns+pr
                        print('Total Runs:',plruns)
                else:
                    print('Value greater then 6 not allowed!!!!')
                ps=plruns
                print()
                if ps>cs:
                    print('End of innings')
                    
                    break
    print()
    print()
    if cpruns == plruns:
        print('!! Match DRAW !!')
    elif cpruns > plruns:
        print('!! Computer WINS the Match !!')
    else:
        print('!! Player WINS the Match !!')

        
