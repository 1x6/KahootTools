from kahoot import client
import string
import random
import time



bot = client()


def spamjoin() :
    print('KahootTools - Made for 1337\'ing up your k4h00t gam3s!')
    gameid = input('Enter the game pin: ')
    botamount = input('Enter the amount of bots (max 2000): ')
    custom_usr = input('Enter the desired username for your bots: ')

    def joingame() :
        #yep = gen_user()
        #bot.join((gameid), f"{yep}")

        usrname = (custom_usr + str(random.randint(1, 100000)))

        bot.join((gameid), usrname)

        def joinHandle() :
            pass

        bot.on("joined", joinHandle)
        print(f"Joined game {gameid} with username {usrname}.")
        # time.sleep(.1)

    for x in range(0, (int(botamount) )) : # + 10  this is not code
        joingame()

spamjoin()
