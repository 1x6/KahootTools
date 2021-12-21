import string, random, os, time, threading
from kahoot import client

bot = client()

class KahootSpammer:
    def __init__(self):
        print('KahootTools - Remastered by Nightmrs - Originally made by xeny')
        self.gamepin = input('PIN: ')
        self.botamount = input('Amount of bots (max 2000): ')
        self.custom_user = input('Enter desired username (5 or less chars) (leave blank if none): ')

    def joinHandle(self):
        pass

    def randName(self, integer):
        return ''.join(random.choice(string.ascii_letters) for _ in range(integer))

    def joingame(self):
        if self.custom_user == "":
            self.username = ('xeny ' + '| ' + self.randName(6))
        else:
            self.username = (self.custom_user + ' | ' + self.randName(6))

        bot.join(self.gamepin, self.username)
        bot.on("joined", self.joinHandle)
        print(f"Joined game {self.gamepin} with username {self.username}.")

if __name__ == '__main__':
    Client = KahootSpammer()
    for x in range(int(Client.botamount)):
       threading.Thread(target=Client.joingame()).start()
