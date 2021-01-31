'''
###DEVELOPERS = Joshua Pickwell
###VERSION = Python 3.8.2
'''
import string, time, sys, random

version = "Python 3.8.2"

class GenPwd:
    strength = None
    pwd = None
    length = None
    charset = None
        
    def __init__(self):
        self.get_strength()
        self.get_len_charset()
        self.pwd = ''.join(list(self.gen_pwd()))
        print(f"\nYour password is: {self.pwd}")

    def get_strength(self):
        while True:
            self.strength = str(input("\nPlease enter the strength of password you would like to generate: W/M/S/XS")).lower()
            if self.strength in ["w", "m", "s", "xs", "weak", "medium", "strong", "extra strong"]: break
            else: print("\nInvalid type... Please try again")

    def get_len_charset(self):
        if self.strength in ["w", "weak"]: self.length = 5; self.charset = string.ascii_lowercase
        elif self.strength in ["m", "medium"]: self.length = 7; self.charset = string.ascii_lowercase + string.ascii_uppercase
        elif self.strength in ["s", "strong"]: self.length = 10; self.charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
        else: self.length = 15; self.charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    def gen_pwd(self):
        for _ in range(self.length): yield random.choice(self.charset)

class MainFuncs:
    def exit():
        time.sleep(0.5)
        sys.exit("Exitting program...")

class Program:
    def __init__(self):
        time.sleep(0.5)
        print(f"Welcome to Python Password Generator for {version}...")
        time.sleep(0.5)
        self.menu()

    def menu(self):
        while True:
            time.sleep(0.5)
            print("\nPlease enter the number of the function you would like to execute:")
            time.sleep(0.5)
            func = str(input("    [1] Run program\n    [2] Quit\n")).lower()
            if func in ["1", "run", "run program"]: GenPwd()
            elif func in ["2", "quit", "exit", "quit program", "exit program"]: MainFuncs.exit()
            else: print("\nInvalid function... Please try again")

if __name__ == "__main__":
    Program()
