import sys, random, datetime
from signal import signal, SIGINT
from utils import *
from getpass import getpass
import subprocess

def quit_gracefully():
    print(bcolors.FAIL + 'leave the ExamShell V2.1' + bcolors.DEFAULT)


level = 1
t1 = t2 = t3 = t4 = False
login = ""

def handler(signal_received, frame):
    print("\n" + bcolors.FAIL + 'leave the ExamShell V2.1' + bcolors.DEFAULT)
    sys.exit(0)

def loaderBanner(level):
    print("\nCurrent Grade: "+str(int(25 * (level - 1)))+" / 100\n")
    if level >= 1:
        data = int(25 * 1)
        print("   Level "+bcolors.OKGREEN+"0"+bcolors.DEFAULT+":\n\
\t0: "+ bcolors.OKGREEN+"only_a"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 1:
            print(" Assignment: " + bcolors.OKGREEN+"only_a"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/subjects/only_a"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/rendu/only_a"+bcolors.DEFAULT+"\n")
    if level >= 2:
        data = int(25 * 2)
        print("   Level "+bcolors.OKGREEN+"1"+bcolors.DEFAULT+":\n\
\t1: "+ bcolors.OKGREEN+"ft_split"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 2:
            print(" Assignment: " + bcolors.OKGREEN+"ft_split"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/subjects/ft_split"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/rendu/ft_split"+bcolors.DEFAULT+"\n")
    if level >= 3:
        data = int(25 * 3)
        print("   Level "+bcolors.OKGREEN+"2"+bcolors.DEFAULT+":\n\
\t2: "+ bcolors.OKGREEN+"microshell"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 3:
            print(" Assignment: " + bcolors.OKGREEN+"microshell"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/subjects/microshell"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/rendu/microshell"+bcolors.DEFAULT+"\n")
    if level >= 4:
        data = int(25 * 4)
        print("   Level "+bcolors.OKGREEN+"3"+bcolors.DEFAULT+":\n\
\t3: "+ bcolors.OKGREEN+"mini_serv"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 4:
            print(" Assignment: " + bcolors.OKGREEN+"mini_serv"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/subjects/miniserv"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/rendu/miniserv"+bcolors.DEFAULT+"\n")

    print("Here you don't need to use git.\n\n\
End date: "+ str(datetime.datetime.now().strftime('%Y-%m-%d')) +" 04:"+str(random.randrange(2, 30))+":29\n\
Left time: 2hrs, "+str(random.randrange(2, 30))+"min and 55sec\n\
==================================================================\n\
Use the <grademe> command to be graded.\n")

def levelFunction():
    global level
    os.system("clear")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    print(f" You are at level {level - 1} ", end = "")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    loaderBanner(level)
    time.sleep(0.100)

def levelLoader():
    global level, t1, t2, t3, t4
    if level == 1 and t1 == False:
        desktop_path = os.path.expanduser(f'~/subjects/only_a')
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/only_a.txt", f"{desktop_path}/subject.en.txt")
        levelFunction()
        t1 = True
    elif level == 2 and t2 == False:
        desktop_path = os.path.expanduser(f'~/subjects/ft_split')
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/ft_split.txt", f"{desktop_path}/subject.en.txt")
        levelFunction()
        t2 = True
    elif level == 3 and t3 == False:
        desktop_path = os.path.expanduser(f'~/subjects/microshell')
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/microshell.txt", f"{desktop_path}/subject.en.txt")
        levelFunction()
        t3 = True
    elif level == 4 and t4 == False:
        desktop_path = os.path.expanduser(f'~/subjects/mini_serv')
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/mini_serv.txt", f"{desktop_path}/subject.en.txt")
        levelFunction()
        t4 = True

def loginExam():
    global login
    print("ExamShell V2.1\n\n")
    login = input("login : ")
    f_logins = open("./logins.txt", "r")
    s_logins = f_logins.read()
    f_logins.close()
    while (login not in s_logins):
        print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login incorrect")
        login = input("login : ")
    password = getpass()
    while login == "" or password == "":
        print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login or password incorrect")
        login = input("login : ")
        password = getpass()
    list = [1, 5, 7, 8, 9, 10, 11, 12]
    if (random.choice(list) == 7):
        print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login or password incorrect")
        while True :
            login = input("login : ")
            password = getpass()
            print(bcolors.FAIL + "Error: " + bcolors.DEFAULT + "login or password incorrect")

def splitTester(exercice):
    global level
    exercice_dir = os.path.expanduser(f'~/rendu/{exercice}')
    c_source_file = os.path.abspath(f"{exercice_dir}/{exercice}.c")
    with open(c_source_file, 'a') as file:
        file.write("\n#include <stdio.h>\nint main(){printf(\"%s\\n%s\", ft_split(\"zakariae mrabet\", ' ')[0], ft_split(\"zakariae mrabet\", ' ')[1]);return 0;}")
    executable = "a.out"
    compile_command = f"gcc {c_source_file} -o {executable}"
    compile_process = subprocess.Popen(compile_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    compile_process.communicate() 
    if compile_process.returncode == 0:
        run_command = f"./{executable}"
        run_process = subprocess.Popen(run_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout_output, stderr_output = run_process.communicate()
        if run_process.returncode == 0:
            if (stdout_output.decode('utf-8') == "zakariae\nmrabet"):
                waitingGrademe(7, True)
                return True
            else :
                waitingGrademe(7, False)
                return False
        else :
                waitingGrademe(7, False)
                return False
    else :
        waitingGrademe(7, False)
        return False

def mini_moulinette(exercice):
    global level
    exercice_dir = os.path.expanduser(f'~/rendu/{exercice}')
    if not os.path.isdir(exercice_dir) or not os.path.exists(f'{exercice_dir}/{exercice}.c'):
        waitingGrademe(7, False)
    elif level == 2:
        if splitTester(exercice) :
            level += 1
        print("(Press enter to continue...)")
        input()
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
                    list = [1, 5, 7, 8, 9, 10, 11, 12]
                    if (random.choice(list) == 7):
                        waitingGrademe(7, False)
                    else :
                        waitingGrademe(7, True)
                        level += 1
                elif (level == 3 and stdout_output.decode('utf-8') == ""):
                    waitingGrademe(7, True)
                    level += 1
                elif (level == 4 and stdout_output.decode('utf-8') == ""):
                    waitingGrademe(7, True)
                    level += 1
                else:
                    waitingGrademe(7, False)
                if (level == 5) :
                    print(bcolors.OKGREEN + "Congratulations! You have completed the ExamShell.\n\nCurrent Grade: 100 / 100\n\nuse the <finish> to finish the exam" + bcolors.DEFAULT)
            else:
                waitingGrademe(5, False)
        else:
            waitingGrademe(5, False)
        print("(Press enter to continue...)")
        input()


def main():
    try :
        signal(SIGINT, handler)
        loginExam()
        examBanner(login)
        input()
        os.system("clear")
        print("You have to work from a new window to keep this one available\nA random subject named subject.en.txt will be generated\n> You must write your file (example.c) in the assign folder (see subject),\n\nthis folder must be in folder: rendu\nOnce completed, you can push/correct your project with : grademe\nIf your level is validated, you move on to the next level\nIf not, you have to start again")
        print("\n\nWelcome to the ExamShell V2.1!\n\n")
        print("(Press enter to continue...)")
        input()
        initExam()
        while True :
            levelLoader()
            print(bcolors.WARNING+"examshell"+bcolors.DEFAULT+" /> ", end = "", flush = True)
            data = input()
            if data == "finish": sys.exit(1)
            elif data == "clear": os.system("clear")
            # elif data == "git add ." or "git add *":
                
            elif data == "grademe":
                if level == 1: mini_moulinette("only_a")
                elif level == 2: mini_moulinette("ft_split")
                elif level == 3: mini_moulinette("microshell")
                elif level == 4: mini_moulinette("mini_serv")
            else : print(bcolors.FAIL, "Error: command not found" + bcolors.DEFAULT)
    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    main()