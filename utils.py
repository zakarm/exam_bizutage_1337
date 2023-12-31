import time, os, shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = '\033[39m'

def loginInterface():
    global login
    print()
    printLoad()
    print(" Login: "+ login, end=" ")
    printLoad()
    print()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def loopprintProgressBar(prefix):
    items = list(range(0, 10))
    l = len(items)
    printProgressBar(0, l, prefix, suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        time.sleep(0.030)
        printProgressBar(i + 1, l, prefix, suffix = 'Complete', length = 50)

def examBanner(login):
    time.sleep(0.050)
    os.system("clear")
    print("\n")
    loopprintProgressBar(bcolors.FAIL + " Installing dependencies:" + bcolors.DEFAULT)
    print(bcolors.OKGREEN + " Dependencies installed successfully!" + bcolors.DEFAULT)
    print("\n")
    loopprintProgressBar(bcolors.FAIL +" Installing Packages:" + bcolors.DEFAULT)
    print(bcolors.OKGREEN + " Packages installed successfully!" + bcolors.DEFAULT)
    print("\n")
    loopprintProgressBar(bcolors.FAIL + " Installing Readline:" + bcolors.DEFAULT)
    print(bcolors.OKGREEN + " Readline installed successfully!" + bcolors.DEFAULT)
    print("\n")
    loopprintProgressBar(bcolors.OKGREEN + "## Future is loading ##" + bcolors.DEFAULT)
    print("l", end= "")
    time.sleep(0.050)
    print("o", end= "")
    time.sleep(0.050)
    print("g", end= "")
    time.sleep(0.050)
    print("i", end= "")
    os.system("clear")
    time.sleep(0.200)
    print(f"n : " + bcolors.OKBLUE + login + bcolors.DEFAULT + "\nlevel : " + bcolors.OKBLUE + "0.00%" + bcolors.DEFAULT + "\n")
    print("You're connected "+ bcolors.FAIL + login + bcolors.DEFAULT +"!\nYou can log out at any time. If this program tells you earned points,\n\
then they will be counted whatever happens.\n\nYou are about to start the project ExamShell at level 0.\n\
You would have" + bcolors.WARNING + " 3hrs" + bcolors.DEFAULT + " to complete this project.\n\
Press enter to start exam\
    ")

def initExam():
    subj_dir = os.path.expanduser("~/subjects")
    if os.path.isdir(subj_dir):
        shutil.rmtree(subj_dir)
    rendu_dir = os.path.expanduser("~/rendu")
    if os.path.isdir(rendu_dir):
        shutil.rmtree(rendu_dir)
    os.makedirs(subj_dir)
    os.makedirs(rendu_dir)

def waitingGrademe(r, bool):
    for i in range(0, r) :
        print(bcolors.DEFAULT + "waiting... " + bcolors.DEFAULT, flush = True)
        time.sleep(0.300)
    if bool == False:
        print(f"\n{bcolors.FAIL}>>>>>>>>>> FAILURE <<<<<<<<<<{bcolors.DEFAULT}\n\n")
    else:
        print(f"\n{bcolors.OKGREEN}>>>>>>>>>> SUCCESS <<<<<<<<<<{bcolors.DEFAULT}\n\n")



