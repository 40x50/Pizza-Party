import os
from colorama import init, Fore, Style

from handler import Handler

init(convert=True)

def logo():
    print(
        Style.BRIGHT + f"""
        {Fore.BLUE + "██████╗ "}{Fore.GREEN + "██╗"}{Fore.MAGENTA + "███████╗"}{Fore.RED + "███████╗"}{Fore.CYAN + " █████╗ "}{Fore.YELLOW + "██████╗ "}{Fore.BLUE + " █████╗ "}{Fore.CYAN + "██████╗ "}{Fore.GREEN + "████████╗"}{Fore.RED + "██╗   ██╗"}
        {Fore.BLUE + "██╔══██╗"}{Fore.GREEN + "██║"}{Fore.MAGENTA + "╚══███╔╝"}{Fore.RED + "╚══███╔╝"}{Fore.CYAN + "██╔══██╗"}{Fore.YELLOW + "██╔══██╗"}{Fore.BLUE + "██╔══██╗"}{Fore.CYAN + "██╔══██╗"}{Fore.GREEN + "╚══██╔══╝"}{Fore.RED + "╚██╗ ██╔╝"}
        {Fore.BLUE + "██████╔╝"}{Fore.GREEN + "██║"}{Fore.MAGENTA + "  ███╔╝ "}{Fore.RED + "  ███╔╝ "}{Fore.CYAN + "███████║"}{Fore.YELLOW + "██████╔╝"}{Fore.BLUE + "███████║"}{Fore.CYAN + "██████╔╝"}{Fore.GREEN + "   ██║   "}{Fore.RED + " ╚████╔╝ "}
        {Fore.BLUE + "██╔═══╝ "}{Fore.GREEN + "██║"}{Fore.MAGENTA + " ███╔╝  "}{Fore.RED + " ███╔╝  "}{Fore.CYAN + "██╔══██║"}{Fore.YELLOW + "██╔═══╝ "}{Fore.BLUE + "██╔══██║"}{Fore.CYAN + "██╔══██╗"}{Fore.GREEN + "   ██║   "}{Fore.RED + "  ╚██╔╝  "}
        {Fore.BLUE + "██║     "}{Fore.GREEN + "██║"}{Fore.MAGENTA + "███████╗"}{Fore.RED + "███████╗"}{Fore.CYAN + "██║  ██║"}{Fore.YELLOW + "██║     "}{Fore.BLUE + "██║  ██║"}{Fore.CYAN + "██║  ██║"}{Fore.GREEN + "   ██║   "}{Fore.RED + "   ██║   "}
        {Fore.BLUE + "╚═╝     "}{Fore.GREEN + "╚═╝"}{Fore.MAGENTA + "╚══════╝"}{Fore.RED + "╚══════╝"}{Fore.CYAN + "╚═╝  ╚═╝"}{Fore.YELLOW + "╚═╝     "}{Fore.BLUE + "╚═╝  ╚═╝"}{Fore.CYAN + "╚═╝  ╚═╝"}{Fore.GREEN + "   ╚═╝   "}{Fore.RED + "   ╚═╝   "}
        \n                             Press ctrl + c to quit
                                Test Mode: {test_toggle}"""
    )

test_toggle = False
os.system("title Pizza Party")

while True:
    logo()
    print(
    Fore.CYAN + f"""
                                    Options
      \t\t\t▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
      \t\t\t█ {Fore.GREEN + "[1] Pizza Party"}              {Fore.CYAN + "█"}
      \t\t\t{Fore.CYAN + "█"} {Fore.BLUE + "[2] Settings"}                 {Fore.CYAN + "█"}
      \t\t\t{Fore.CYAN + "████████████████████████████████"}
    \n"""
    )
    
    print(Fore.BLUE + "\n", end="")
    menu = input(">: ")

    if menu == "1":
        os.system("cls")
        logo()
        print(Fore.MAGENTA + "\n", end="")
        addr = input("Enter target's address >: ")
        city = input("Enter target's city >: ")
        state = input("Enter target's state >: ")
        postal_code = input("Enter target's postal code >: ")
        name = input("Enter name >: ")
        email = input("Enter email >: ")
        phone = input("Enter phone number >: ")

        print(Fore.GREEN, end="")

        handler = Handler({
            "addr": addr,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "name": name,
            "email": email,
            "phone": phone
        }, test=test_toggle)

        minutes, stores_num = handler.fulfill_order()

        print(Fore.CYAN + f"Successfully ordered from {stores_num} stores to {addr}")
        print(f"Estimated wait time: {minutes} minutes\n")
        input(Fore.MAGENTA + "Press ENTER to clear...")
    elif menu == "2":
        os.system("cls")
        logo()
        print(
        Fore.CYAN + f"""
                                        Options
      \t\t\t▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
      \t\t\t█ {Fore.BLUE + "[1] Test Mode: " + (str(test_toggle))}         {Fore.CYAN + "█"}
      \t\t\t{Fore.CYAN + "████████████████████████████████"}
        \n"""
        )

        print(Fore.BLUE + "\n", end="")
        option = input(">: ")

        if option == "1":
            test_mode = input("Test Mode: \"y\" or \"n\" >: ")
            if test_mode == "y":
                test_toggle = True
            else:
                test_toggle = False

    os.system("cls")