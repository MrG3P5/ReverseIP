#!/usr/bin/env python3
import requests
import os
import re
import sys
from colorama import Fore, init
from multiprocessing.dummy import Pool as ThreadPool

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
    __banner__ = f"""{red} (                              (   (     
 )\ )                           )\ ))\ )  
(()/(  (   )     (  (        ( (()/(()/(  
 /(_))))\ /((   ))\ )(  (   ))\ /(_))(_)) 
(_)) /((_|_))\ /((_|()\ )\ /((_|_))(_))   
| _ (_)) _)((_|_))  ((_|(_|_)) |_ _| _ \  {cyan}[ {white}ReverseIP With Multithread {cyan}]
{red}|   / -_)\ V // -_)| '_(_-< -_) | ||  _/     {cyan}[ {white}Created By X-MrG3P5 {cyan}]
{red}|_|_\___| \_/ \___||_| /__|___||___|_|    """
    print(__banner__)
    print("\n")

def ReverseIP(ip):
    try:
        ip = ip.strip("\n\r")
        req = s.get(f"https://rapiddns.io/sameip/{ip}?full=1#result", timeout=10).text
        all_domain = re.findall(r"</th>\n<td>(.*?)</td>", req)
        if len(all_domain) != 0:
            open("res-domain.txt", "a").write("\n".join([x for x in all_domain]))
            sys.stdout.write(f"\n{white}---> GOOD : {green}{ip} {white}({len(all_domain)} Domain)")
        else:
            sys.stdout.write(f"\n{white}---> BAD IP : {red}{ip}")            
    except:
        sys.stdout.write(f"\n{white}---> BAD IP : {red}{ip}")

if __name__=="__main__":
    banner()
    input_list = open(input(f"{red}[{white}?{red}] {white}IP List : "), "r").readlines()
    Thread = input(f"{red}[{white}?{red}] {white}Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(ReverseIP, input_list)
    pool.close()
    pool.join()
    sys.stdout.write(f"\n{green}---> DONE!!!")
