from A import A
from AAAA import AAAA
from CNAME import CNAME
from MX import MX
from NS import NS
from TXT import TXT


domain = input("\nimport your domain: ")
dig = int(input("Do you wanna start this program? 0 = no and 1 = yes"))
while dig !=0:
    print(" ______        __             __    _______       ")
    print("|   _  \.-----|  .-----.-----|  |--|   _   |.--.--.")
    print("|.  |   |__ --|  |  _  |  _  |    <|.  |   |  |  |")
    print("|.  |   |_____|__|_____|_____|__|__|.  ____|___  |")
    print("|:  |   |                          |:  |   |_____|")
    print("|::.|   |                          |::.|          ")
    print("`--- ---'                          `---'          \n\n")

    print("\nChoose a option: \n")
    print("1 - A")
    print("2 - AAAA")
    print("3 - CNAME")
    print("4 - MX")
    print("5 - NS")
    print("6 - TXT")
    print("0 - exit\n\n")
    if dig == 1:
        A(domain)

    if dig == 2:
        AAAA(domain)

    if dig == 3:
        CNAME(domain)

    if dig == 4:
        MX(domain)

    if dig == 5:
        NS(domain)

    if dig == 6:
        TXT(domain)

    dig = int(input())