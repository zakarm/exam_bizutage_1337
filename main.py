import sys
from Student import Student
from signal import signal, SIGINT
from utils import *

level = 1
t1 = t2 = t3 = False

def handler(signal_received, frame):
    print("\n" + bcolors.FAIL + 'leave the exam00 ...' + bcolors.DEFAULT)
    sys.exit(0)

def level1():
    global level
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print(" You are at level 1 ", end = "")
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print("\nAssignment name  : only_a \n")

def level2():
    global level
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print(" You are at level 2 ", end = "")
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print("\nAssignment name  : \n")

def level3():
    global level
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print(" You are at level 3 ", end = "")
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print("\nAssignment name  : \n")
    level += 1

def level4():
    global level
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print(" You are at level 4 ", end = "")
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print("\nAssignment name  : \n")
    level += 1

def levelLoader():
    global level
    global t1
    if level == 1 and t1 == False:
        desktop_path = f'/Users/zmrabet/Desktop/exam00/subjects/only_a'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/only_a.txt")
        shutil.copyfile("./subjects/only_a.txt", f"{desktop_path}/only_a.txt")
        level1()
        t1 = True
    elif level == 2 and t2 == False:
        desktop_path = f'/Users/zmrabet/Desktop/exam00/subjects/microshell'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/microshell.txt")
        shutil.copyfile("./subjects/microshell.txt", f"{desktop_path}/microshell.txt")
        level2()
        t2 = True

def main():
    try :
        signal(SIGINT, handler)
        examBanner()
        input()
        print("Welcome to the Exam00!\n\n")
        initExam()
        while True :
            levelLoader()
            print(bcolors.OKGREEN + "<42Cursus exam00> " + bcolors.DEFAULT, end = "", flush = True)
            data = input()
            if data == "exit": sys.exit(1)
            elif data == "clear": os.system("clear")
            

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    main()