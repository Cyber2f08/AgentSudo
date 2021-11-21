from rich.align import Align
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich import print
from flask import redirect, Flask, session, send_from_directory, url_for, request, render_template, jsonify
from werkzeug.utils import secure_filename
from worker.service import npx
from worker.poolmem import *
from worker.service import tunnel
from utils import get_update_logs, flask_conf, get_emaild
from utils import get_emailp
from utils import get_passwdp
from worker.memwk import memCOM
from time import sleep
import math
import time
import base64 as enc
import random
import json

# Fun Module
from alive_progress import alive_bar

# System Module
import os
import sys
import shutil
import psutil
import platform

# Status
Status_C = "Development"

# from blueprint import *

# Network module
import requests
import socket

CONFG = flask_conf()

# Queue
# Author : Cyber2f80
# Github : https://www.github.com/Cyber2f08/

APIPI = ['https://api.myip.com', 'ipv4bot.whatismyipaddress.com',
    'https://api.ipify.org?format=json', 'https://api.my-ip.io/ip']

AUTH_NGROK = {
    'Cyber2f08': '1ls6nUtwRrLq5rkBX0bEBM4bjHj_3G6XkNC952WjExgyFoTW4'
}

# Local Service

def COM_NM(VERBOSE=False):
    # Get version and distribution of system
    if VERBOSE == True:
        print("[MEM] Reading some system information...")

    # Globalization 
    global MACHINE_
    global VER_
    global SYSTEM_
    global UNAME_
    global HOSTNAME
    global LOCATION_

    Data = requests.get(f'http://ipwhois.app/json/{ip[0]}')
    LOCATION_ = Data.json()['country']
    PROCESSOR_ = platform.processor()
    CPU_COUNT = psutil.cpu_count()
    ARCHITECH_ = platform.architecture()
    HOSTNAME = socket.gethostname()
    MACHINE_ = platform.machine()
    VER_ = platform.version()
    SYSTEM_ = platform.system()
    UNAME_ = platform.uname()
    print(f'''[MEM[E:0]] System Information (*): 
[MEM[E:0[0]]] Architect ({SYSTEM_}): {ARCHITECH_[0]}, (*)
[MEM[E:0[1]]] Machine: {MACHINE_}, (*)
[MEM[E:0[2]]] Processor: ({PROCESSOR_}) with {CPU_COUNT} cpu, (*)
[MEM[E:0[3]]] Version: {VER_}, (*)
[MEM[E:0[4]]] Platform: {SYSTEM_} ({UNAME_[2]}), (*)
[MEM[E:0[5]]] Hostname: {HOSTNAME}, (*)''')
def y2i():
    import subprocess
    print("[[cyan]NPX[/cyan]] Installing terminal packages: y2u, purify, emp, set, put, pull, sys2die, makup, sv2disk, purify2")
    time.sleep(19)
    print("[[yellow]NPX[/yellow]] Package has been installed...")
    time.sleep(3)
    print("[[cyan]NPX[/cyan]] Launching.. y2i")
    subprocess.call("start /wait C:/Windows/System32/cmd.exe")
def MEM_CAP(VERBOSE=False):
    # Get posible memory on system with bytes
    if VERBOSE == True:
        print("[MEM] Reading posible memory on the system...")
    global MEM
    MEM = psutil.virtual_memory().total
    print(f"[MEM[E:['{HOSTNAME}'][*]]] Memory: {MEM} bytes")
    print(f"[MEM[E:['{HOSTNAME}'][*]]] Country: '{LOCATION_}'")
def LOCIP():
    try:
        print("[MEM] Locating your public address through online...")
        global ip
        ipl = socket.gethostbyname(socket.gethostname())
        ip = []
        rp = requests.get(APIPI[3], timeout=5)
        rp = rp.text
        ip.append(rp)
    except Exception:
        print("[MEM] Retrying with another api requests")
        try: 
            rp = requests.get(APIPI[1])
        except Exception:
            print("[MEM] Unable to contact any of the requests. Maybe check your internet (*) ")
            print("[[red]NPX[/red]] [purple]Unable to connect to any web server of apis..[/purple]")
            time.sleep(4)
            print("[[yellow]NPX[/yellow]] Initiating safemode terminal")
            time.sleep(6)
            y2i()
    try:
        print(f"[MEM] IP: {ip[0]}")
    except IndexError:
        print("[MEM] Failed to connect to any web server.... (*).")
        sys.exit()
    print(f'''[MEM] Configuration (NOTICE):
[MEM:1] PORT: {CONFG['port']}
[MEM:2] LOCAL (IP): ({ipl})
[MEM:3] WEB: http://{ipl}:{CONFG['port']}/
[[yellow]MEM[/yellow]] Initially started, NPX Management v1''')


def GTE(exec):
    # Fetch current credential session!
    try:
        if(exec == True and session['username'] in SAM_Agent):
            for x in range(len(SAM_Agent)):
                b = 1
                if SAM_Agent[x-b] == session['username']:
                    bl = x-b
                    return {
                    'AGENT': DESAM_Agent[bl]
                    }
                else:
                    b += 1
        print(ERR_COM_TYP['CREDENTIAL_FRAUD'].format(session['username']))
    except Exception as e:
        com_CL01(True)
        print("[MEM] Something when wrong error occured...")
        print(f"[MEM] Error: {e}")
        sys.exit("[MEM] Exitting cleanly")

def IGV(STRING, path=True):
    try:
        if os.path.isfile(STRING) and path == True:
            RESPONSE = GTE(exec=True)
            if RESPONSE['AGENT'].strip() in DESAM_Agent:
                shutil.move(f'{STRING}', 'static/uploads/'+RESPONSE['AGENT']+'/')
            else:
                print(ERR_COM_TYP['CREDENTIAL_FRAUD'].format(session['username']))
        else:
            print(ERR_COM_TYP['FILENOTFOUND'].format(STRING))
    except Exception as e:
        com_CL01(True)
        print("[MEM] Something when wrong error occured...")
        print(f"[MEM] Error: {e}")
        sys.exit("[MEM] Exitting cleanly")
        
# Boot
INSTALLED_T = False
INIT_THEME_BOOT = True

# Styles Variable
OPT_BOOT = ['START', 'CONSOLE', 'EXIT', 'CONFIG', 'ABOUT']

# ERROR VAR

ERR_CONSOLE = '''
	Access Denied. (*)
	'''
ERR_COM_TYP = {
    'FILENOTFOUND': f'''
    File not Found. (*) [{0}]
    ''',
    'CREDENTIAL_FRAUD': f'''
    Credential is invalid. (*) ["{0}"]
    '''
}

# Headers

HEADER_MUW = '<link rel="shortcut icon" href="static/favicon.ico">'
ERR_MU = f'''
		{HEADER_MUW}
		Access Denied.'''
DECOY_MOD = None

EN_TITLE = {
    'DASHBOARD': '<title>Dashboard | Terminal</title>',
    'LOGIN': '<title>Locker | Terminal</title>'
}

INPUT_ERR = {
    'EMPTY': 'INPUT CANNOT BE BLANK!'
}

# Javascript Static

EN_JS = {
    'WARN': '<script src="static/js/warn.js"></script>'
}

# Styles Module

console = Console()

# Update Table

table = Table(show_header=True, header_style="bold cyan")
table.add_column("Date", style="dim", width=12)
table.add_column("Updates")
table.add_column("Author")
table.add_column("Status")
table.add_column("Description")

# November 5, 2021

log_update = get_update_logs()
tB = 0
def tB_ADD():
    global tB
    tB += 1
for x in range(len(log_update)):
    if tB == len(log_update):
        break
    table.add_row(
            f"{log_update[tB]['date']}",
            f"{log_update[tB]['title']}",
            f"{log_update[tB]['author']}",
            f"{log_update[tB]['status']}",
            f"{log_update[tB]['description']}"
            )
    tB_ADD()
#table.add_row(
#    "Nov 5, 2021",
#    "Alpha Terminal Web APP",
#    "Cyber2f08, cyber.2f08@gmail.com",
#    "Added color, rich module, template with flask framework. Still need css Styling."
#)
#
# November 8, 2021
#table.add_row(
#    "Nov 8, 2021",
#    "Added active bar loader, Typo fixes",
#    "Cyber2f08, cyber.2f08@gmail.com",
#    "Fixed typo on previous update log on author column, and added active bar loader."
#)




def com_CL01(exec=False):
    if exec != False:
        # Clearing screen of terminal
        try:
            import os
        except ImportError:
            print("You need to install os module")
        if os.name != 'nt':
            os.system('clear')
        else:
            os.system('cls')

# Configuration!

app = Flask(__name__, template_folder='template')

ints = {
    "A": 0,
    "P": 1,
    "F": 2
}

ints_0 = {
    "P": 0,
    "A": 1,
    "F": 2
}
keys = ["Google is Trash!", "People is drowning :)", "Forget it, it will end!"]

# popXBYT(0)

msIX_A = keys[ints["A"]].encode('ascii')
msIX_F = keys[ints["P"]].encode('ascii')
msIX_P = keys[ints["F"]].encode('ascii')
msBYT_A = enc.b64encode(msIX_A)
msBYT_F = enc.b64encode(msIX_F)
msBYT_P = enc.b64encode(msIX_P)
msGIX_A = msBYT_A.decode('ascii')
msGIX_F = msBYT_F.decode('ascii')
msGIX_P = msBYT_P.decode('ascii')

SAM_Agent = [msGIX_P, msGIX_A, msGIX_F]
DESAM_Agent = ["Agent P", "Agent A", "Agent F"]

# E CORP MODULES


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def xms_BYTCOMP():
    try:
        if session['username'] in SAM_Agent:
            return redirect(url_for('dashboard'))
    except KeyError:
        return redirect(url_for('login'))


@app.route('/dashboard')
def dashboard():
    try:
        EM = get_emaild()
        if session['email'] in EM:
            return render_template('admin.html')
    except KeyError:
        return redirect(url_for('login'))


@app.route('/pool/console')
def console():
    try:
        if session['username'] in SAM_Agent:
            for x in range(len(SAM_Agent)):
                b = 1
                if SAM_Agent[x-b] == session['username']:
                    bl = x-b
                    return f'''
					{EN_JS['WARN']}
					{HEADER_MUW}
					Hello {DESAM_Agent[bl]}'''
                else:
                    b += 1
    except KeyError:
        return ERR_MU


@app.route('/pool/upload')
def u_MService():
    try:
        if session['username'] in SAM_Agent:
            return render_template('scp.html')
    except KeyError:
        return ERR_MU


@app.route('/pool/upload', methods=['GET', 'POST'])
def u_Service():
    if session['username'] in SAM_Agent:
        if request.method == 'POST':
            f = request.files['file']
            f.save(secure_filename(f.filename))
            IGV(f.filename)
            return f'''
			<title>Upload Success</title>
			{EN_JS['WARN']}
			{HEADER_MUW}
			Uploaded, You can redownload the file with this params /static/uploads/{f.filename}'''
# TODO: FUCK ALL

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    emails = get_emailp()
    passwd = get_passwdp()
    email_d = get_emaild()
    try:
        if session['email'] in email_d:
            return redirect(url_for('dashboard'))
    except KeyError:
        pass
    if request.method == 'POST':
        FWP = request.form
        PW = FWP['key']
        EM = FWP['email']
        print("[[yellow]WEB[/yellow]] Email has been posted and the password...")
        print("[[yellow]WEB[/yellow]] Sensitive password:", PW)
        print("[[cyan]WEB[/cyan]] Email of recipient:", EM)
        if EM != emails["Cyber2f08"] or EM != emails["sp0f.p12"]:
            error = "Invalid Credentials. Please try again."
        if PW != passwd[EM]:
            error = "Invalid Credentials. Please try again."
        else:
            session['email'] = EM
            return redirect(url_for('dashboard'))
    return render_template('login.html')
# API Resource Center

# Bitly Creator
import validators
import pyshorteners

err_co_bit_invl = "invalid url"
err_co_bit_flgen = "failed to generate"

pl = None

TOKEN_D = "b4c7a7254a14a2c163e5bdcb25520211bbe0cd3c"

def bit_get(Link):
    try:
        l = Link
        srt = pyshorteners.Shortener(api_key=TOKEN_D)
        x = srt.bitly.short(l)
        return x
    except Exception:
        return 0
# Web App Service
@app.route('/api/bit', methods=['POST', 'GET'])
def bitly():
    link = request.args.get('l')
    if validators.url(link):
        f = bit_get(link)
        crt_link = {
            'bitlink': f"{f}"
        }
        if f == 0:
            return err_co_bit_flgen
        elif validators.url(f):
            return jsonify(crt_link)
    return err_co_bit_invl

# Local Service
def bitly_LOC(lik):
    if validators.url(lik) == True:
        f = bit_get(lik)
        if f == 0:
            return err_co_bit_flgen
        elif validators.url(f) == True:
            return f
    return err_co_bit_invl

# Matematika API
MATTY = ['t32', 'sqr4', 'mt7']
MEMQQ = {
    't32': 'argumen (opsi) -a (value variable a), -b dan -c\nDan buat satu variable di isi "?" untuk mencari variable itu! \nContoh: .mat t32 -a 3 -b 4 -c ?, Jawaban: Variable C yang hilang adalah 5',
    'sqr4': 'argumen (value), isi bagian value untuk mencari akar dari value itu! Contoh: .mat sqr4 49, Jawaban: Akar dari 49 adalah 7',
    'mt7': 'argumen (value), isi value pertama dengan angka, terus isi value kedua dengan operator seperti ini (*, /, +, -), value ketiga isi dengan angka lagi\nContoh: .mat mt7 8 * 8, Jawaban: 64\n\nKeterangan: \nOperator (*) adalah simbol perkalian, \nOperator (/) adalah simbol pembagian, \nOperator (-) adalah simbol mengurangi, \nOperator (+) adalah simbol menjumlah\n\nTambahan: Tidak bisa lebih dari 2 angka :('
}

def mat_solv(type, opsi=None, val=None, val2=None, val3=None):
    # t32, sqr4, mt7
    if type == MATTY[0]: # t32
        return {
           "answer": "wibu2" 
        }
    elif type == MATTY[1]: # sqr4
        SQRT = math.sqrt(val)
        if isinstance(SQRT, int):
            return {
                "answer": f"{SQRT}"
                    }
        return {
            "error": "Akar value ini adalah desimal (float)! Tidak bisa...."
                }
    elif type == MATTY[2]: # mt7
        return {
            "answer": "wibu"
                }
# Whatsapp API 

user_json = {
        "Agent A": {
            "email": "cyber.2f08@gmail.com"
            }
    }

APP_KEY = "whenthecodeisus"
from datetime import datetime
from bs4 import BeautifulSoup as bs4l

def get_cel_wet():
    rss_url = "https://www.google.com/search?q=cuaca+hari+ini+di+malang&rlz=1C1FKPE_idID978ID978&oq=Cuaca+har&aqs=chrome.0.69i59j69i57j0i131i433i512j0i131i433j0i512l6.1826j0j7&sourceid=chrome&ie=UTF-8"
    res = requests.get(rss_url)
    html_pg = res.content
    soup = bs4l(html_pg, 'html.parser')
    text = soup.find("span", {"id":"wob_tm"})
    return text

IP_LOCAL = socket.gethostbyname(socket.gethostname())

def process_wa(SENDER_, MESSAGE_, RULEID_, ISGROUP_, GROUPPART=True):
    WELCOMING_EMO = ['😁', '😀', '😎', '🤗']
    DAY = datetime.today().weekday()
    DAY_INDEX = {0: "Senin", 1: "Selasa", 2: "Rabu", 3: "Kamis", 4: "Jumat", 5: "Sabtu", 6: "Minggu"}
    DAY_NOW = DAY_INDEX[DAY]
    BUKU_INDEX = {0: "PAI (Modul), SBDP (LKS), Bahasa Arab (Modul)", 1: "Bahasa Indonesia (Modul & LKS), AlQuran, Bahasa Inggris (Modul)", 2: "PJOK (Modul & LKS), AlQuran, PPKN (Modul)",
            3: "IPA (Modul & LKS), Bahasa Jawa (Modul & LKS), IPS (Modul)", 4: "Matematika (Modul & LKS), AlQuran"}
    SERAGAM_INDEX = {0: "Putih biru", 1: "Batik", 2: "Biru muda, Olahraga", 3: "Putih biru", 4: "Pramuka, Kepanduan"}
    MDX = 0
    if MESSAGE_[0] == ".help":
        return {
                "replies":[
                        {
                            "message": f'''Halo di sana {WELCOMING_EMO[random.randint(1, 4)-1]}. \n\nSemoga hari mu baik baik saja {SENDER_} {WELCOMING_EMO[random.randint(1, 4)-1]}. \nCommands: \n\n> .help (Untuk membuka menu help) \n> .drk (Dapatkan hinaan dan darkjokes) \n> .web (List web sekolah) \n> .mat (Matematika Solver) \n> .btl (Bitly Shortener) \n> .echo (echo) \n> .wet (Cuaca saat ini!) \n> .srg, .srg besok (Seragam) \n> .bok, .bok besok (Buku) \n> .brnly (Brainly Jawaban Searcher😳) \n> .ver (Versi) \n> .about (Tentang creator) \n\n\nHari ini hari {DAY_NOW}. Semoga hari mu menyenangkan :) @Cyber2f08
                            '''
                        }
                    ]
                }
    elif MESSAGE_[0] == ".mat":
        try:
            if MESSAGE_[1] != None and MESSAGE_[1] in MATTY:
                if len(MESSAGE_) > 2: # t32, sqr4, mt7
                    if MESSAGE_[1] == MATTY[0]: # t32
                        return {
                            "replies":[
                                {
                                    "message": "t32"
                                }
                            ]
                        }
                    elif MESSAGE_[1] == MATTY[1]: # sqr4
                        data = mat_solv(MESSAGE_[1], None, MESSAGE_[2])
                        try:
                            return {
                                    "replies":[
                                            {
                                                    "message": "Akar dari {MESSAGE_[2] adalah {data['answer']}"
                                            }
                                        ]
                                    }
                        except IndexError:
                            return {
                                   "replies":[
                                            {
                                               "message": f"data['error']"
                                            }
                                        ]
                                    }
                    elif MESSAGE_[1] == MATTY[2]: # mt7
                        return {
                            "replies":[
                                {
                                    "message": "mt7"
                                }
                            ]
                        }
                return {
                        "replies": [
                                {
                                    "message": f"Tipe: {MESSAGE_[1]}, Harus memiliki {MEMQQ[MESSAGE_[1]]}"
                                }    
                            ]
                        }
            else:
                return {
                        "replies":[
                                {
                                    "message": f"Tidak menemukan tipe {MESSAGE_[1]}"
                                }
                            ]
                        }
        except IndexError:
            pass
        return {
                "replies":[
                        {
                            "message": "Syntax: '.mat (Tipe Matematik) (opsi) (value) (opsi2) (value2) (opsi3) (value3)' \n\n Tipe Matematik: \n1. Teorama Pythagoras (Tipe: t32, Rumus: C` = A` + B`, Status: Belum bisa) \n2. Matematika Biasa (Tipe: mt7) \n3. Akar dari (Tipe: sqr4) \n\nMasih Beta"
                        }
                    ]
                }
    elif MESSAGE_[0] == ".btl":
        try:
            if MESSAGE_[1] != None:
                rq = bitly_LOC(MESSAGE_[1])

                if rq == err_co_bit_flgen:
                    return {
                            "replies":[
                                {
                                    "message": "Error failed to generate!"
                                }
                            ]
                        }
                elif rq == err_co_bit_invl:
                    return {
                            "replies":[
                                {
                                    "message": "Sorry :p, Invalid typeof link"
                                }
                            ]
                        }
                return {
                        "replies":[
                            {
                                "message": f"The Link Generated 👌: {rq}"
                            }
                        ]
                    }
        except IndexError:
            pass
        return {
                "replies":[
                    {
                        "message": "Syntax: .btl <link>"
                    }
                ]
            }
    elif MESSAGE_[0] == ".echo":
        try:
            if MESSAGE_[1] != None:
                if len(MESSAGE_) > 2:
                    NEW = []
                    for x in range(len(MESSAGE_)-1):
                        x = x+1
                        NEW.append(MESSAGE_[x])
                        if(x == len(MESSAGE_)-1):
                            msgcon = " ".join(map(str, NEW))
                    return {
                            "replies":[
                                    {
                                        "message": f"{msgcon}"
                                    }
                                ]
                            }
                return {
                        "replies":[
                                {
                                    "message": f"{MESSAGE_[1]}"
                                }
                            ]
                        }
        except IndexError:
            pass
        return {
                "replies":[
                    {
                        "message": "Syntax: .echo <message>"
                    }
                ]
            }
    elif MESSAGE_[0] == ".ver":
        return {
                "replies":[
                    {
                        "message": "The version of this framework app is 4.3.21, \nCode: https://www.github.com/Cyber2f08/Koop"
                    }
                ]
            }
    elif MESSAGE_[0] == ".web":
        return {
                "replies":[
                    {
                        "message": "LMS: https://es.insanpermata.sch.id \nAmal Yaumi: https://bit.ly/AYIP82"
                    }
                ]
            }
    elif MESSAGE_[0] == ".drk":
        return {
                "replies":[
                    {
                        "message": "Fitur ini belum di tambah..."
                    }
                ]
            }
    elif MESSAGE_[0] == ".about":
        return {
                "replies":[
                    {
                        "message": "Github: @Cyber2f08, https://www.github.com/Cyber2f08 \nAlias: Cyber2f08 \nEmail: cyber.2f08@gmail.com \nContributor: @digitaldemon.p12, @sp0f.p12 \nSource Code: https://www.github.com/Cyber2f08/Koop"
                    }
                ]
            }
    elif MESSAGE_[0] == ".wet":
        return {
                "replies":[
                    {
                        "message": f"Temperature sekarang adalah {get_cel_wet()} C, Di scrape lewat (Google)"
                    }
                ]
            }
    elif MESSAGE_[0] == ".bok":
        try:
            if MESSAGE_[1] != None:
                if DAY_NOW != "Jumat" or DAY_NOW != "Sabtu":
                    try:
                        return {
                                "replies":[
                                        {
                                            "message": f"Besok adalah hari {DAY_INDEX[DAY+1]} maka besok membawa buku {BUKU_INDEX[DAY+1]}"
                                        }
                                    ]
                                }
                    except KeyError:
                        return {
                                "replies":[
                                        {
                                            "message": f"Besok adalah hari senin maka besok membawa buku {BUKU_INDEX[0]}"
                                        }
                                    ]
                                }
                else:
                    return {
                            "replies":[
                                    {
                                        "message": f"Besok libur tidak perlu membawa buku {WELCOMING_EMO[random.randint(1, 4)-1]}"
                                    }
                                ]
                            }
        except IndexError:
            if DAY_NOW != "Minggu" or DAY_NOW != "Sabtu":
                return {
                        "replies":[
                                {
                                    "message": f'''Buku Modul {WELCOMING_EMO[random.randint(1, 4)-1]}: \n\nSenin: PAI (Modul), SBDP (LKS), Bahasa Arab (Modul) \nSelasa: Bahasa Indonesia (Modul & LKS), AlQuran, Bahasa Inggris (Modul) \nRabu: PJOK (Modul & LKS), AlQuran, PPKN (Modul) \nKamis: IPA (Modul & LKS), Bahasa Jawa (Modul & LKS), IPS (Modul) \nJumat: Matematika (Modul & LKS), AlQuran \n\nHari ini adalah hari {DAY_NOW} jadi hari ini membawa buku {BUKU_INDEX[DAY]} \nSemoga hari ini menyenangkan :). @Cyber2f08
                                    '''
                                }
                            ]
                        }
            else:
                return {
                        "replies":[
                                {
                                    "message": "Hari ini libur tidak perlu membawa buku! 😎🤩"
                                }
                            ]
                        }
    elif MESSAGE_[0] == ".srg":

        try:
            if MESSAGE_[1] != None:
                # Seragam besok
                if DAY_NOW != "Jumat" or DAY_NOW != "Sabtu":
                    try:
                        return {
                                "replies":[
                                        {
                                            "message": f"Besok adalah hari {DAY_INDEX[DAY+1]} memakai seragam {SERAGAM_INDEX[DAY+1]}"
                                        }
                                    ]
                                }
                    except KeyError:
                        return {
                                "replies":[
                                        {
                                            "message": f"Besok adalah hari senin memakai seragam {SERAGAM_INDEX[0]}"
                                        }
                                    ]
                                }

                return {
                        "replies":[
                                {
                                    "message": "Besok libur 😳" 
                                }
                            ]
                        }
        except IndexError:
            if DAY_NOW != "Minggu" or DAY_NOW != "Sabtu":
                return {
                        "replies":[
                                {
                                    "message": f"List Seragam (FULL) {WELCOMING_EMO[random.randint(1, 4)-1]}: \n\nSenin: {SERAGAM_INDEX[0]} \nSelasa: {SERAGAM_INDEX[1]} \nRabu: {SERAGAM_INDEX[2]} \nKamis: {SERAGAM_INDEX[3]} \nJumat: {SERAGAM_INDEX[4]} \n\nHari ini hari {DAY_NOW}. Maka hari ini pakai {SERAGAM_INDEX[DAY]}. \nSemoga hari mu menyenangkan! :) @Cyber2f08"
                                }
                            ]
                        }
            return {
                    "replies":[
                            {
                                "message": f'''
                                Hore {SENDER_} hari ini libur 🥳'''
                            }
                        ]
                    }

error_c = {
          "replies":[
              {
                  "message": "😱😭 Ada yang error di web server!"
              }
            ]
          }

@app.route('/api/msg', methods=['GET', 'POST'])
def gmsg():
    keys = request.args.get('key')
    if(keys != APP_KEY):
        return ERR_MU
    try:
        content = request.json
        content = json.dumps(content, indent=4)
        content = json.loads(content)
        messenger = content['messengerPackageName']
        sender = content['query']['sender']
        message = content['query']['message']
        message = message.split()
        isGroup = content['query']['isGroup']
        groupParticipant = content['query']['isGroup']
        ruleId = content['query']['ruleId']
        #if messenger == "com.whatsapp":
        try:
            jsonp = process_wa(sender, message, ruleId, isGroup)
        except KeyError as e:
            return error_c
        return jsonify(jsonp)
        #else:
        #    return "Guduk Whatsapp Tolol"
    except TypeError:
        return "Access Denied."

if __name__ == "__main__":
    com_CL01(True)
    LCL_CO = flask_conf()
    if LCL_CO["debug"] != True and LCL_CO["codebug"] != True:
        print("[MEM] Loading services...")
        if INIT_THEME_BOOT == True:
            print("[MEM] Installing theme module")
            try:
                install()
            except:
                com_CL01(True)
                print(ERR_CONSOLE)
            sleep(3)
            INSTALLED_T = True
        LOCIP()
        try:
            os.system(f'title {ip[0]}')
        except IndexError:
            os.system('title 0.0.0.0')
        time.sleep(1)
        COM_NM()
        MEM_CAP()
        time.sleep(2)
        try:
            os.system(f'title {ip[0]}:{HOSTNAME}')
        except IndexError:
            os.system('title 0.0.0.0:{HOSTNAME}')
        NGROK_PATH = "bin/ngrok.exe"
        print(f'''[MEM[NOTICE]] Symbols:
[MEM[P:0]] OK : (*)
[MEM[P:1]] FATAL/DECADES DONE : (FUCK)
[MEM[P:2]] WARNING : (*)! REASON: "REASONHERE"
[MEM[P:3][F]] CORRUPT : (-) Dead & Corrupt. Try redownload the source code on github''')
        if os.path.isfile(NGROK_PATH) == True and LCL_CO["ngrok"] == True:
            print("[MEM[N[0x00]]] Starting ngrok http on port {CONFG['port']}")
            tunnel.start()
        elif os.path.isfile(NGROK_PATH) == False and LCL_CO["ngrok"] == True:
            print(f"[MEM[N[0x00]]] Starting ngrok http on port {CONFG['port']}")
            print("[MEM[N[0x00]]] Cannot find ngrok executable, download it!")
        else:
            print(f"[MEM] Starting ngrok http on port {CONFG['port']}")
            print("[MEM] Failed to started, ngrok option disabled...")
        #print('[MEM:MX] Cleaning any posible memory and cache from python itself.')
        #print('[MEM:MX] Searching trash 🔍')
        print('[MEM:MX] Searching trash 🔍')
        print('[MEM:MX] Trash found ! to remove it (open .bat file): ')
        print('[MEM:MX[0]] Remove __pycache__: Launch pycache.bat, (*)')
        print('[MEM:MX[1]] Remove .pytest_cache: Launch pytest.bat, (*)')
        print('[MEM:MDX] Make sure you remove the trash after the server shutdown!')
        print('[[purple]MEM[/purple]] Initially running npx.... ')
        npx.script.install()
        print("[[blue]NPX[/blue]] Uniform created")
        time.sleep(random.uniform(2, 5))
        if(Status_C == "Development"):
            print(f"[MEM[WARNING]] (*)! Status: {Status_C} (mode+)")
        else:
            print("[MEM[WARNING]] (*)! Status: Production (mode+)")    
        print("[MEM] Booted up (*)")
        if(LCL_CO["debug"] != True):
            print("[MEM] Running flask instance (*), (FUCK)")
            with alive_bar(426) as bar:
                for i in range(426):
                    time.sleep(random.uniform(0.01, 0.0001))
                    bar()
        print("[MEM] Loading important live modules (*), (FUCK)")
        with alive_bar(6) as bar_live:
            for i in range(6):
                time.sleep(random.uniform(0.1, 0.01))
                bar_live()
        if(LCL_CO["debug"] != True):
            print("[MEM] Loading framework modules (*)")
            with alive_bar(11) as bar_live_frame:
                for i in range(11):
                    time.sleep(random.uniform(0.1, 0.01))
                    bar_live_frame()
        print("[MEM] Corrupting fake .sdk modules to create an interaction shells")
        time.sleep(5)
        com_CL01(exec=True)
        if INSTALLED_T == False:
            print("[MEM] Installing theme module")
            try:
                install()
            except:
                com_CL01(True)
                print(ERR_CONSOLE)
        sleep(3)
        EM_BACK = f'''
    >-----------------------------------------------
    | [WARN] THIS KEY IS IMPORTANT FOR LOGIN		
    | Agent P :  "{msGIX_P}"						
    | Agent F :  "{msGIX_F}"						
    | Agent A :  "{msGIX_A}"						
    | 												
    | For contact any further, cyber.2f08@gmail.com 
    >_______________________________________________
    	'''
        print(Align.center(EM_BACK))
        print("\n")
        print(Align.center("[UPDATES]\n"))
        console = Console()
        console.print(Align.center(table))
        print("\n\n\n")
    if LCL_CO["debug"] == True:
        os.system("title DEBUG MODE ACTIVE")
    app.secret_key = memGIX.load('SECRET')
    # If Codebug is True then put any commands in here
    if LCL_CO["codebug"] == True:
        os.system("title DEBUG MODE ACTIVE")
        nothing = None
    elif(LCL_CO["codebug"] != True):
        try:
            if LCL_CO["ngrok"] == True:
                tunnel.start()
            app.run('0.0.0.0', CONFG['port'], LCL_CO["debug"])
        except KeyboardInterrupt:
            com_CL01(True)
            print("[MEM:0[EXILE['1.CACHE(0)']]] Cleaning server cache...!")
            sleep(4)
            print("[MEM:0[EXILE['0.CACHE(-1)']]] Done. Exit cleaned!")
    else:
        print("[MEM] DEBUG FINISHED! If the error gone, turn of the DEBUG_ variable to other like '0'. Have fun 😁")
