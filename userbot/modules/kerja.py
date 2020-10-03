import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern='^.harga(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("**PRICE LIST** **LAZARUZ STORE**\n"
			 f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
			 f"WEB P SUBDOMAIN PREMIUM\n"
			 f"\n"
			 f"SUBDOMAIN 0× Garansi - 20.000 \n"
			 f"SUBDOMAIN 1× Garansi - 30.000 \n"
			 f"SUBDOMAIN 3× Garansi - 50.000 \n"
			 f"*❗️GARANSI JIKA RF/RedFlag\n"
			 f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
			 f"DOMAIN TLD .COM .NET .ORG\n"
			 f"\n"
			 f"REQUEST - NO GARANSI: 100.000\n"
			 f"REQUEST - GARANSI 1 BULAN: 170.000\n"
			 f"NO REQUEST - NO GARANSI: 80.000\n"
			 f"NO REQUEST - GARANSI: 130.000\n"
			 f"❗️GARANSI JIKA RF/RedFlag\n"
			 f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
			 f"READY MWHM-WHM-CPANEL\n"
			 f"\n"
			 f"FITUR SERVER LAZAHOST\n"
			 f"-Send Mail Menggunakan SENDGRID 🚀\n"
			 f"-AUTO SSL (Otomatis Gembok Ijo🔒\n"
			 f"-Web Service Menggunakan LITESPEED\n"
			 f"-Result Masuk di Email Utama (tidak di spam)\n"
			 f"━━━━━━━━━━━━━━━━━━━━━━━━\n"
			 f"PM @ArdanzPanel\n"
			 f"PM @Lazaruzs")


@register(outgoing=True, pattern='^.unredflag(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("UNTUK DI INGAT SAJA\nBUAT YANG BLM TAU BERAPA LAMA PROSES UNREDFLAG ."
			f"\n\nBIASANYA PALING CEPAT ADALAH 1 MALAM DAN PALING LAMA ADALAH 1 - 3 HARI\nTHANKS BOSQU"
			f"PM @ArdanzPanel"
			)
	
@register(outgoing=True, pattern='^.1(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Silahkan kirim email kamu\n"
			 f"Dan request tampilan yang ingin kamu gunakan\n"
			 f"List Tampilan : [Klik Disini](https://t.me/DemoScript)")
	
@register(outgoing=True, pattern='^.2(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Oke ditunggu ya, saya akan memproses web phising sesuai dengan tampilan yang kamu mau`")
	

	
@register(outgoing=True, pattern='^.3(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Website Phising telah dibuat\n\n"
			 f"Garansi : Full\n"
			 f"Note : `Garansi tidak akan habis sebelum durasi website telah habis, dan ketika durasi di perpanjang maka garansi akan ikut diperpanjang`\n"
			 f"Usahakan untuk komplain / menggunakan garansi maka sertakan ORDER ID\n"
			 f"Order ID ada di data phising, dan itu sangatlah berguna")


@register(outgoing=True, pattern='^.whm(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Berikut Adalah List Harga dari **WHM** \n"
			 f"**Whm Mini**\n"
			 f"`Harga :` 40.000/1 Month\n"
			 f"`Create 15 cPanel`\n"
			 f"`10GB Web Space`\n"
			 f"`Unlimited Bandwith`\n"
			 f"`Free SSL Certificate`\n"
			 f"\n"
			 f"**Whm Medium**\n"
			 f"`Harga :` 50.000/1 Month\n"
			 f"`Create 25 cPanel`\n"
			 f"`15GB Web Space`\n"
			 f"`Unlimited Bandwith`\n"
			 f"`Free SSL Certificate`\n"
			 f"\n"
			 f"**Whm Extra**\n"
			 f"`Harga :` 60.000/1 Month\n"
			 f"`Create 40 cPanel`\n"
			 f"`20GB Web Space`\n"
			 f"`Unlimited Bandwith`\n"
			 f"`Free SSL Certificate`\n"
			 f"\n"
			 f"**Whm Super**\n"
			 f"`Harga :` 70.000/1 Month\n"
			 f"`Create 50 cPanel`\n"
			 f"`25GB Web Space`\n"
			 f"`Unlimited Bandwith`\n"
			 f"`Free SSL Certificate`\n"
			 f"Jangan lupa follow channel LazaruzStore! [klik disini](http://t.me/lazaruzstore)")
	
	
@register(outgoing=True, pattern='^.smm(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Berikut Adalah List Harga dari **WEBSMM** \n"
			 f"**SMM**\n"
			 f"`Harga Sewa :` 150.000, Bulanan 50.000\n"
			 f"`Harga Beli :` 300.000 Dapat SC + DB\n"
			 f"`**FITUR**`\n"
			 f"`Deposit otomatis OVO & BCA`\n"
			 f"`Auto Oper ke beberapa Provider`\n"
			 f"`Auto Refund & Status`\n"
			 f"`User Level : Member, Reseller, Admin, Agen`\n"
			 f"`Mobile & Desktop Responsive`\n"
			 f"`Demo ? [Demo](https://bit.ly/ard-panel`\n"
			 
@register(outgoing=True, pattern='^.ppob(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Berikut Adalah List Harga dari **WEBSMM** \n"
			 f"**SMM**\n"
			 f"`Harga Sewa :` 200.000, Bulanan 50.000\n"
			 f"`Harga Beli :` 400.000 Dapat SC + DB\n"
			 f"`**FITUR**`\n"
			 f"`Auto Oper ke beberapa Provider`\n"
			 f"`Create Kode Undangan`\n"
			 f"`Deposit otomatis OVO & BCA`\n"
			 f"`Auto Refund & Status`\n"
			 f"`User Level : Member, Reseller, Admin, Agen`\n"
			 f"`Mobile & Desktop Responsive`\n"
			 f"`Demo ? [Demo](https://bit.ly/ard-panel)")
	
@register(outgoing=True, pattern='^.tam(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Tampilan cek di :` @DemoScript")
	
@register(outgoing=True, pattern='^.proses(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("OK, Saya Akan Mengirimkan result dengan cara LIVE. Jadi nnti kalau sudah proses atau sudah giliranmu akan saya beritahu ~ Terimakasih \n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/lazaruzstore)")

@register(outgoing=True, pattern='^.mwhm(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Daftar harga **M.WHM**\n"
			 f"MINI : 80.000\n"
			 f"MEDIUM : 100.000\n"
			 f"EXTRA : 120.000\n"
			 f"SUPER : 150.000\n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/LazaruzStore)")


@register(outgoing=True, pattern='^.full(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("Mohon Maaf, Untuk sekarang result live **FULL** \n"
			 f"Info Lebih Lanjut! [klik disini](http://t.me/LazaruzStore)")


@register(outgoing=True, pattern='^.jual(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("OPEN WEBSITE PHISING\n"
			f"M.WHM, WHM, CPANEL\n"
			 f"\n\n`Send email lancar\nada SSL atau gembok ijo\nBisa request tampilan\nDan masih banyak lagi!!`\n\nHarga?\n\nDomain : Rp. 100.000 `Bisa Request Nama Web`\n"
			 f"Domain : Rp. 70.000 `Tidak bisa request nama web alias yang nentuin penjual`\n"
			 f"Subdomain : Rp. 20.000 `Tidak bisa request apapun kecuali request tampilan website`\n\n"
			 f"Payment via : DANA, OVO, GOPAY\n"
			 f"Mau lihat tampilan web ? Yuk ke demo [klik di sini](https://t.me/DemoScript)\n\n"
			 f"Chat ? [ARDANZPANEL](http://t.me/ArdanzPanel)\n"
			 f"Join channel telegram yuk! [klik disini](http://t.me/LazaruzStore)")


@register(outgoing=True, pattern='^.demo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Untuk melihat tampilan yang di inginkan\n Silahkan cek`\n [Disini](https://t.me/DemoScript) \n#DemoWeb")
	


# Create by myself @JejakCheat

@register(outgoing=True, pattern='^.sibuk(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Sebentar Ya BRO`")
	sleep(2)
	await typew.edit("`Masih Ngecek`")
	sleep(1)
	await typew.edit("`Oh Ternyata Saya Masih sibuk... Tunggu sebentar nanti akan dibaca \n#ARDBOT`")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.on(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Baru bangun wkwkk??` \n[#ARDBOT](t.me/Lazaruzs")
	
	# Create by myself @JejakCheat
	
# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.o(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Maaf baru online, ada apa bosqu?` \n#ARDBOT")
	
	# Create by myself @JejakCheat


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.perbedaan(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Saya jelaskan untuk perbedaan domain dan subdomain .\n\nDomain (pubg.com) **langsung tidak ada tambahan sama sekali\n\nSubdomain ( blablabla.pubg.com ) **ada Tambahan di depan domainnya .\n\nBot By : [#LazaBot](t.me/lazaruzs)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.ovo(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`OVO : `088224734804 `A/N BAYU TRI WIBOWO` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#ARDBOT](t.me/Lazaruzs)")

# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.DANA(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`DANA : `088224734804 `A/N BAYU TRI WIBOWO` \nSertakan Bukti Transfer Ya (Wajib) Untuk melanjutkan transaksi \nBot By : [#ARDBOT](t.me/Lazaruzs)")



# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.data(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`Kirim Email + Tampilan yang sudah di request di atas` (Sesuai nama di @DemoScript) \nBot By : [#ARDBOT](t.me/Lazaruzs)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.domainprice(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`UPDATE HARGA HARI INI` \n\nDOMAIN : 100.000 (Bisa Request Nama Web)\nDOMAIN : 70.000 (Tidak bisa request nama web)\nSUBDOMAIN : 20.000 \n\nBot By : [#ARDBOT](t.me/Lazaruzs)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.bug(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("`JIKA ADA ERROR ATAU BUG DI TAMPILAN PHISING KALIAN TINGGAL SURUH TEMAN KALIAN UNTUK MEMBUKA WEB KALIAN ITU \n\nSyarat : \n1. BEDA HP \n2. BEDA SINYAL \n3. BELUM PERNAH BUKA WEB ITU`\nBot By : [#ARDBOT](t.me/Lazaruzs)")


# Create by myself @JejakCheat
@register(outgoing=True, pattern='^.exp(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(0)
	sleep(0)
	await typew.edit("**EXP TIME !!** \nMaaf bos, phising saya matikan atau suspend \nDikarenakan Sudah melewati tanggal kadaluarsa \nDan jika mau perpanjang silahkan balas pesan ini  \n Dan jika tidak ingin perpanjang abaikan pesan ini \nBot By : [#ARDBOT](t.me/Lazaruzs)")


# Create by myself @JejakCheat
CMD_HELP.update({
    "done":
    "`.domainanim` = `DOMAIN` PUBG Mobile Season 12 `Animation Version`\n"
    "`.domaintourney` = `DOMAIN` PUBG Mobile Season 12 `Tournament`\n"
    "`.subdomainanim` = `SUBDOMAIN` PUBG Mobile Season 12 `Animation Version`"
    "`.subdomaintourney` = `SUBDOMAIN` PUBG Mobile Season 12 `Tournament`"
    "`.subdomainbokep1` = `SUBDOMAIN` Facebok Bokep `V1`"
    
})
