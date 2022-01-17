import time,random,os

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)
    
def co_ch():
    return random.randint(0,255)

inp="""██████╗░ ██████╗░ ░░░░░██╗
██╔══██╗ ██╔══██╗ ░░░░░██║
██████╔╝ ██║░░██║ ░░░░░██║
██╔══██╗ ██║░░██║ ██╗░░██║
██║░░██║ ██████╔╝ ╚█████╔╝
╚═╝░░╚═╝ ╚═════╝░ ░╚════╝░\n"""

a=[i+" " for i in inp.split(" ")]
while True:
    time.sleep(0.01)
    for i in a:
        print((colored(co_ch(),co_ch(),co_ch(),i)),end="")
    time.sleep(0.1)
    os.system('cls')
    


    
    
