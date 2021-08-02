import pandas as pd
from os import path
import math


def banner():
    print ('''
        
███╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
████╗░██║██║░░░██║████╗░████║██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██╔██╗██║██║░░░██║██╔████╔██║██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║╚████║██║░░░██║██║╚██╔╝██║██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
██║░╚███║╚██████╔╝██║░╚═╝░██║╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
        [USE FOR COMPASS PURPOSE TO COMPARE REGISTERED PHONE] 
                [NUM AND GROUP MEMBERS PHONE NO]
                AUTHOR: NOOR RAIHAN ABD RAHIM
                ''')

banner()

dir_check2 = False
while dir_check2 == False:
  file = input("Enter excel filepath: ")
  dir_check2 = path.exists(file)
  if dir_check2 == False:
    print("\033[1;31;40mFile does not exist \033[1;37;40m")

r_number = pd.read_excel(file)

registered = r_number['registered'].tolist()
target = r_number['numbers'].tolist()


def main():
    fcount = 0
    for number in target:
        flag = False
        if math.isnan(number):
            continue
        else:
            print("Checking",int(number),"---> ", end="")

            for register in registered:
                if number == register:
                    print(int(register),"==> \033[1;32;40mVERIFIED!\033[1;32;37m\n")
                    flag = True
                    break
            
            if flag == False:
                print("===> \033[1;32;31mNOT VERIFIED!\033[1;32;37m\n")
                fcount+=1
            else:
                continue


main()
