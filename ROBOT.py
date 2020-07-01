import os,sys


def style () :
    text = ("""
\033[1;31m
 ____   ___  ____   ___ _____           ______   __
|  _ \\ / _ \| __ ) / _ \\_   _|         / ___\\ \\ / /
| |_) | | | |  _ \\| | | || |    _____  \___ \\\\ V /
|  _ <| |_| | |_) | |_| || |   |_____|  ___) || |
|_| \\_\\\\___/|____/ \\___/ |_|           |____/ |_|
\033[1;33m
     _____           ____            _   _
    |_   _|         / ___|          | \\ | |
      | |    _____  \\___ \\   _____  |  \\| |
      | |   |_____|  ___) | |_____| | |\\  |
      |_|           |____/          |_| \\_|


\033[1;34m
      C7 TEAM / BLACK SHADOW / PROJECT SEGMA

\033[1;32m
""")


    print (text)



def up () :
    os.system ("""
pkg update
pkg upgrade
apt update
apt upgrade
pip install --upgrade pip
pkg install bash
pkg install php
pkg install git
pkg install tor

""")


def up2 () :
    os.system ("""

pkg install figlet
pkg install cowsay
pkg install curl
pkg install tar
pkg install zip
pkg install unzip
pkg install sudo
pkg install wget
pkg install wcalc
pkg install openssl
pkg install bmon



""")

def up3 () :
    os.system ("""

pkg install java
Pkg install google
pkg install perl
pkg install nmap
pkg install clang
pkg install macchanger
pkg install nano


""")

def up4 () :
    os.system ("""

pkg install python2
pkg install python3
pkg install ruby


""")

def metas () :
    os.system ("""

pkg update
pkg upgrade
pkg install unstable-repo
pkg install metasploit

""")






while True :
    os.system ("clear")
    
    os.system ("clear")
    style ()
    print ("")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 1- for update termux ")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 2- To download the basics (part 1) ")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 3- To download the basics (part 2) ")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 4- To download the basics (part 3) ")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 5- To install metasploit ")
    print ("\033[1;33m[\033[1;34m*\033[1;33m]\033[1;37m 6- exit ")
    print ("")


    df = input (">>>>>  ")

    if df == "1" :
        os.system ("clear")
        
        up ()
    elif df == "2" :
        os.system ("clear")
        
        up2 ()
    elif df == "3" :
        os.system ("clear")
      
        up3 ()
    elif df == "4" :
        os.system ("clear")
     
        up4 ()
    elif df == "5" :
        os.system ("clear")
      
        metas ()
    elif df == "6" :
       
        os.system ("clear")
        sys.exit ()
