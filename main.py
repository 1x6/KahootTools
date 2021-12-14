from kahoot import client
import string
import random
import time



bot = client()


def spamjoin() :
    print('KahootTools - made for haxxors (\'im kidding bro :l)') 
    gameid = input('Enter the game pin: ')
    botamount = input('Enter the amount of bots (max 2000): ')
    custom_usr = input('Enter the desired username for your bots: ')

    def joingame() :

        usrname = (custom_usr + str(random.randint(1, 100000)))

        bot.join((gameid), usrname)

        def joinHandle() :
            pass

        bot.on("joined", joinHandle)
        print(f"Joined game {gameid} with username {usrname}.")
        

    for x in range(0, (int(botamount) )) :
        joingame()

spamjoin()
