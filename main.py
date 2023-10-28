import sys, random, datetime
from signal import signal, SIGINT
from utils import *
from getpass import getpass
import subprocess

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
Subject location:  "+bcolors.OKGREEN+"~/Desktop/zmrabet/subjects/only_a"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/Desktop/zmrabet/rendu/only_a"+bcolors.DEFAULT+"\n")
    if level >= 2:
        data = int(25 * 2)
        print("   Level "+bcolors.OKGREEN+"1"+bcolors.DEFAULT+":\n\
\t1: "+ bcolors.OKGREEN+"ft_split"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 2:
            print(" Assignment: " + bcolors.OKGREEN+"ft_split"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/Desktop/zmrabet/subjects/ft_split"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/Desktop/zmrabet/rendu/ft_split"+bcolors.DEFAULT+"\n")
    if level >= 3:
        data = int(25 * 3)
        print("   Level "+bcolors.OKGREEN+"2"+bcolors.DEFAULT+":\n\
\t2: "+ bcolors.OKGREEN+"microshell"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 3:
            print(" Assignment: " + bcolors.OKGREEN+"microshell"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/Desktop/zmrabet/subjects/microshell"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/Desktop/zmrabet/rendu/microshell"+bcolors.DEFAULT+"\n")
    if level >= 4:
        data = int(25 * 4)
        print("   Level "+bcolors.OKGREEN+"3"+bcolors.DEFAULT+":\n\
\t3: "+ bcolors.OKGREEN+"mini_serv"+bcolors.DEFAULT+" for " +  str(data) + " potential points \n\n")
        if level == 4:
            print(" Assignment: " + bcolors.OKGREEN+"mini_serv"+bcolors.DEFAULT+ " for "+ str(data)+"xp, try: 0\n\
Subject location:  "+bcolors.OKGREEN+"~/Desktop/zmrabet/subjects/miniserv"+bcolors.DEFAULT+"\n\
Exercise location: "+bcolors.FAIL+"~/Desktop/zmrabet/rendu/miniserv"+bcolors.DEFAULT+"\n")

    print("Here you don't need to use git.\n\n\
End date: "+ str(datetime.datetime.now().strftime('%Y-%m-%d')) +" 04:"+str(random.randrange(2, 30))+":29\n\
Left time: 2hrs, "+str(random.randrange(2, 30))+"min and 55sec\n\
==================================================================\n\
Use the <grademe> command to be graded.\n")

def level1():
    global level
    os.system("clear")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    print(" You are at level 0 ", end = "")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    loaderBanner(1)
    time.sleep(0.100)

def level2():
    global level
    os.system("clear")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    print(" You are at level 1 ", end = "")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    loaderBanner(2)
    time.sleep(0.200)

def level3():
    global level
    os.system("clear")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    print(" You are at level 2 ", end = "")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    loaderBanner(3)
    time.sleep(0.200)

def level4():
    global level
    os.system("clear")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    print(" You are at level 3 ", end = "")
    for i in range(14) :
        print("=",end="", flush=True)
        time.sleep(0.050)
    loaderBanner(3)
    time.sleep(0.200)


def levelLoader():
    global level, t1, t2, t3, t4
    if level == 1 and t1 == False:
        desktop_path = f'/Users/zmrabet/Desktop/ExamShell/subjects/only_a'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/only_a.txt", f"{desktop_path}/subject.en.txt")
        level1()
        t1 = True
    elif level == 2 and t2 == False:
        desktop_path = f'/Users/zmrabet/Desktop/ExamShell/subjects/ft_split'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/ft_split.txt", f"{desktop_path}/subject.en.txt")
        level2()
        t2 = True
    elif level == 3 and t3 == False:
        desktop_path = f'/Users/zmrabet/Desktop/ExamShell/subjects/microshell'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/microshell.txt", f"{desktop_path}/subject.en.txt")
        level3()
        t3 = True
    elif level == 4 and t4 == False:
        desktop_path = f'/Users/zmrabet/Desktop/ExamShell/subjects/mini_serv'
        os.system(f"mkdir -p {desktop_path} && touch {desktop_path}/subject.en.txt")
        shutil.copyfile("./subjects/mini_serv.txt", f"{desktop_path}/subject.en.txt")
        level3()
        t3 = True

def loginExam():
    global login
    print("ExamShell V2.1\n\n")
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
    exercice_dir = os.path.expanduser(f'/Users/zmrabet/Desktop/ExamShell/rendu/{exercice}')
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