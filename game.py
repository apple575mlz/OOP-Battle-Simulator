from actionscreen import *
from openingsequence import *
from enemydefiner import *
from intermissionscreen import *

Gamerun = True

def main():
    runopening()
    while Gamerun == True:
        if checkalive(returnenemies(returnstage())):
            handleResponseToScreen(showscreen())
        else:
            handleintermission()

if __name__ == "__main__":
    main()