import requests
import os
import sys
import socket
import re
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Color
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX
white = Fore.WHITE
cyan = Fore.LIGHTCYAN_EX
yellow = Fore.LIGHTYELLOW_EX

init(autoreset=True)
s = requests.Session()

def banner():
    os.system("cls||clear")
    __banner__ = f"""{red} (                (   (     
 )\ )             )\ ))\ )  
(()/(  (   )     (()/(()/(  
 /(_))))\ /(( ___ /(_))(_)) 
(_)) /((_|_))\___(_))(_))   
| _ (_)) _)((_)  |_ _| _ \  {cyan}[ {white}Mass Reverse IP to Domain {cyan}]
{red}|   / -_)\ V /    | ||  _/     {cyan}[ {white}Created By X-MrG3P5 {cyan}]
{red}|_|_\___| \_/    |___|_|    """
    print(__banner__ + "\n\n")

def domainFixer(url):
    try:
        url = url.split("://")[1].split("/")[0]
        if ":" in url:
            url = url.split(":")[0]
        return url
    except:
        return url

def ConvertCIDR(cidr):
    try:
        cidr_range = "/" + cidr.split("/")[1]
        cidr_ip_range = ".".join(cidr.split("/")[0].split(".")[:2]) + ".0.0"
        return cidr_ip_range + cidr_range
    except:
        return cidr

def ReverseCIDR(cidr):
    cidr = ConvertCIDR(cidr.strip("\n\r"))
    try:
        req = s.get(f"https://rapiddns.io/s/{cidr}?full=1#result").text
        all_domain = re.findall(r"</th>\n<td>(.*?)</td>", req)
        
        if len(all_domain) != 0:
            sys.stdout.write(f"\n{white}---> {cidr} : {green}{len(all_domain)} {white}Domain")
            open("res-cidr.txt", "a").write("\n".join([x.replace("cpcalenders.", "").replace("www.", "").replace("cpanel.", "") for x in all_domain]))
        else:
            sys.stdout.write(f"\n{red}---> {cidr} : BAD CIDR!!!")
    except:
        sys.stdout.write(f"\n{red}---> {cidr} : BAD CIDR!!!")

def ReverseIP_API_1(ip):
    ip = ip.strip("\n\r")
    try:
        req = s.get(f"http://ip.yqie.com/iptodomain.aspx?ip={ip}", headers={
            "User-Agent": "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }).text
        all_domain = re.findall('<td width="90%" class="blue t_l" style="text-align: center">(.*?)</td>', req)[1:]
        if len(all_domain) != 0:
            sys.stdout.write(f"\n{white}---> {ip} : {green}{len(all_domain)} {white}Domain")
            open("res-revip-api1.txt", "a").write("\n".join([x for x in all_domain]))
        else:
            sys.stdout.write(f"\n{red}---> {ip} : BAD DOMAIN!!!")
    except:
        sys.stdout.write(f"\n{red}---> {ip} : BAD DOMAIN!!!")

def ReverseIP_API_2(ip):
    ip = ip.strip("\n\r")
    try:
        req = s.get(f"https://rapiddns.io/sameip/{ip}?full=1#result", timeout=10).text
        all_domain = re.findall(r"</th>\n<td>(.*?)</td>", req)
        if len(all_domain) != 0:
            open("res-revip-api2.txt", "a").write("\n".join([x for x in all_domain]))
            sys.stdout.write(f"\n{white}---> GOOD : {green}{ip} {white}({len(all_domain)} Domain)")
        else:
            sys.stdout.write(f"\n{white}---> BAD IP : {red}{ip}")            
    except:
        sys.stdout.write(f"\n{white}---> BAD IP : {red}{ip}")

if __name__=="__main__":
    banner()
    menu = f"""{red}[{white}1{red}] {white}ReverseIP ({green}API 1{white})
{red}[{white}2{red}] {white}ReverseIP ({green}API 2{white})
{red}[{white}3{red}] {white}ReverseCIDR to grab all domain
{red}[{white}0{red}] {white}Exit\n"""
    print(menu)
    choose = int(input(f"{red}[{white}?{red}] {white}Choose : "))
    if choose == 1:
        input_list = open(input(f"{red}[{white}?{red}] {white}Give Me List : "), "r").readlines()
        Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
        pool = ThreadPool(int(Thread))
        banner()
        pool.map(ReverseIP_API_1, input_list)
        pool.close()
        pool.join()
        sys.stdout.write(f"\n{cyan}[{white}-{cyan}] {white}DONE {cyan}[{white}-{cyan}]")
    elif choose == 2:
        input_list = open(input(f"{red}[{white}?{red}] {white}Give Me List : "), "r").readlines()
        Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
        pool = ThreadPool(int(Thread))
        banner()
        pool.map(ReverseIP_API_2, input_list)
        pool.close()
        pool.join()
        sys.stdout.write(f"\n{cyan}[{white}-{cyan}] {white}DONE {cyan}[{white}-{cyan}]")
    elif choose == 3:
        input_list = open(input(f"{red}[{white}?{red}] {white}Give Me List : "), "r").readlines()
        Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
        pool = ThreadPool(int(Thread))
        banner()
        pool.map(ReverseCIDR, input_list)
        pool.close()
        pool.join()
        sys.stdout.write(f"\n{cyan}[{white}-{cyan}] {white}DONE {cyan}[{white}-{cyan}]")
    elif choose == 0:
        exit(f"{red}[{yellow}!{red}] {white}Aborted.")
    else:
        exit(f"{red}[{yellow}!{red}] {white}Aborted.")
