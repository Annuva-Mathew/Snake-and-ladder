import random
print('Play snake and ladder')
pp1=1  #player1position
pp2=1  #player2position
while True:
    if (pp1>=100 or pp2>=100):
        if pp1>pp2:
            print('Player 1 won')
        else:
            print('Player 2 won')
        break
    else:
        print('Roll the dice-- player1')
        player1=random.randint(1,6)
        pp1=pp1+player1
        print('Roll the dice-- player2')
        player2=random.randint(1,6)
        pp2=pp2+player2
        print(player1)
        if pp1==8 or pp1==52:
            pp1-=6
            print('snake bited player1')
        elif pp1==40 or pp1==85:
            pp1-=10
            print('snake bited player1')
        elif pp1==68 or pp1==26:
            pp1-=13
            print('snake bited player1')
        elif pp1==4 or pp1==51 or pp1==78:
            pp1+=10
            print('player1 in ladder')
        elif pp1==36 or pp1==87 or pp1==60:
            pp1+=8
            print('player1 in ladder')
        elif pp1==54:
            pp1+=45
            print('player1 in ladder')
            print(pp1)
        elif pp2==8 or pp2==52:
            pp2-=6
            print('snake bited player2')
        elif pp2==40 or pp2==85:
            pp2-=10
            print('snake bited player2')
        elif pp2==68 or pp2==26:
            pp2-=13
            print('snake bited player2')
        elif pp2==4 or pp2==51 or pp2==78:
            pp2+=10
            print('player2 in ladder')
        elif pp2==36 or pp2==87 or pp2==60:
            pp2+=8
            print('player2 in ladder')
        elif pp2==54:
            pp2+=45
            print('player2 in ladder')
        print(pp2)



        
