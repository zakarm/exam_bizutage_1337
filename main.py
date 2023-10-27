import sys, random
from signal import signal, SIGINT
from utils import *
from getpass import getpass
import subprocess

level = 1
t1 = t2 = t3 = False
login = ""

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
    print("\nAssignment name  : microshell\n")

def level3():
    global level
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print(" You are at level 3 ", end = "")
    for i in range(5) :
        print(".",end="", flush=True)
        time.sleep(0.300)
    print("\nAssignment name  : mini_serv \n")
    level += 1


def levelLoader():
    global level, t1, t2, t3
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
    elif level == 3 and t3 == False:
        desktop_path = f'/Users/zmrabet/Desktop/exam00/subjects/mini_serv'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/mini_serv.txt")
        shutil.copyfile("./subjects/microshell.txt", f"{desktop_path}/mini_serv.txt")
        level3()
        t3 = True

def loginExam():
    global login
    login = input("login : ")
    password = getpass()
    list = [1, 5, 7, 8]
    if (random.choice(list) == 7):
        print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login or password incorrect")
        while True :
            login = input("login : ")
            password = getpass()
            print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login or password incorrect")


def mini_moulinette(exercice):
    global level
    exercice_dir = os.path.expanduser(f'/Users/zmrabet/Desktop/exam00/rendu/{exercice}')
    if not os.path.isdir(exercice_dir) or not os.path.exists(f'{exercice_dir}/{exercice}.c'):
        waitingGrademe(7, False)
    else :
        c_source_file = os.path.abspath(f"{exercice_dir}/{exercice}.c")
        executable = "a.out"
        compile_command = f"gcc {c_source_file} -o {executable}"
        compile_process = subprocess.Popen(compile_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        compile_process.communicate()
        
        if compile_process.returncode == 0:
            run_command = f"./{executable}"
            run_process = subprocess.Popen(run_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout_output, stderr_output = run_process.communicate()
            if run_process.returncode == 0:
                if (level == 1 and stdout_output.decode('utf-8') == "a\n"):
                    waitingGrademe(7, True)
                    level += 1
                elif (level == 2 and stdout_output.decode('utf-8') == ""):
                    waitingGrademe(7, True)
                    level += 1
                elif (level == 4 and stdout_output.decode('utf-8') == ""):
                    waitingGrademe(7, True)
                    level += 1
                else:
                    waitingGrademe(7, False)
                if (level == 4) :
                    print(bcolors.OKGREEN + "Congratulations! You have completed the exam00." + bcolors.DEFAULT)
            else:
                waitingGrademe(5, False)
            
        else:
            waitingGrademe(5, False)


def main():
    try :
        signal(SIGINT, handler)
        loginExam()
        examBanner(login)
        input()
        print("Welcome to the Exam00!\n\n")
        initExam()
        print("commands : \"grademe\" \"clear\" \"finish\"\n")
        while True :
            levelLoader()
            print(bcolors.OKGREEN + "<42Cursus exam00> " + bcolors.DEFAULT, end = "", flush = True)
            data = input()
            if data == "finish": sys.exit(1)
            elif data == "clear": os.system("clear")
            elif data == "grademe":
                if level == 1: mini_moulinette("only_a")
                elif level == 2: mini_moulinette("microshell")
                elif level == 3: mini_moulinette("mini_serv")
            else : print(bcolors.FAIL, "Error: command not found" + bcolors.DEFAULT)

    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    main()