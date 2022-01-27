import random
from colorama import init, Fore, Style

# init colorama
init()

# init strings
# Based on IBM Business Automation Workflow recommendations
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
symbol = "!(){}[]`:;?~#$%^&*+=_-."
all_strings = lower + upper + NUMBERS + symbol
i = 0


# check if password has all requirements since random in join
# IBM recommends not starting with '.' or '-'
def pass_requirements(passwd):
    if any(elem in passwd for elem in lower) \
            and any(elem in passwd for elem in upper) \
            and any(elem in passwd for elem in NUMBERS) \
            and any(elem in passwd for elem in symbol):
        if passwd[0] != "." and "-":
            return True
    return False


# generates password of given length
# join of random sample all defined strings
def generate_passwd(length):
    while True:
        passwd = "".join(random.sample(all_strings, length))
        if not pass_requirements(passwd):
            passwd = ""
            continue
        break
    print(Fore.LIGHTGREEN_EX + "Generated password is: ", passwd)
    print(Style.RESET_ALL)


# prompts advices for passwords
def prompt_advice():
    print(Fore.LIGHTMAGENTA_EX + "\n--- PASSWORD GENERATOR ---" + Style.RESET_ALL)
    print("Recommended length is " + Fore.YELLOW + "minimum 8" + Style.RESET_ALL
          + " and" + Fore.YELLOW + " maximum 64" + Style.RESET_ALL + " characters.")
    print("The password will contain: ")
    print(Fore.BLUE + "\tLower case" + Style.RESET_ALL + " characters: ", lower)
    print(Fore.BLUE + "\tUpper case" + Style.RESET_ALL + " characters: ", upper)
    print(Fore.BLUE + "\tNumbers: " + Style.RESET_ALL, NUMBERS)
    print(Fore.BLUE + "\tSymbols: " + Style.RESET_ALL, symbol)


# gets input from user
# prompts advice and check errors
def get_input():
    global i
    if i == 0:
        prompt_advice()
    i += 1
    length = input("> Select length of password: ")
    while True:
        if length.isdecimal():
            if 8 <= int(length) <= 64:
                length = int(length)
                break
            else:
                print("Please enter a number between 8 and 64.")
        else:
            print("Please enter a number.")
        length = input("> Select length of password: ")
    print("Selected length: ", length)
    return length


if __name__ == '__main__':
    generate_passwd(get_input())
    while True:
        response = input("Generate another? (y/n) > ")
        if response in ("y", "n"):
            if response == "y":
                generate_passwd(get_input())
            else:
                print("Closing password generator.")
                exit()
        else:
            print("Response must be y or n.")


