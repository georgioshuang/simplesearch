'''
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        if interface is not None:
            sock.bind((interface, 0))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.connect((ip_address, port))
        for packet in packets
def create_magic_packet(F832E49A8814: str) -> bytes:
    
    Create a magic packet.

    A magic packet is a packet that can be used with the for wake on lan
    protocol to wake up a computer. The packet is constructed from the
    mac address given as a parameter.

    Args:
        macaddress: the mac address that should be parsed into a magic packet.

    
    if len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, "")
    elif len(macaddress) != 12:
        raise ValueError("Incorrect MAC address format")
        FFFFFFFFFFFF F832E49A8814
    return bytes.fromhex("F" * 12 + F832E49A8814 * 16
mac_address = input("input mac address: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.connect(("255.255.255.255", 9))
sock.send(bytes.fromhex("F" * 12 + f"{mac_address}" * 16))'''


from re import X
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''site = "seek"
query = request.GET.get('job')
loc = request.GET.get('location')
page_num = request.GET.get("page", 1)
w = str(query)
p = str(page_num)
l = str(loc)'''
url = "https://www.seek.co.nz/python-jobs/in-auckland?page=3&sortmode=ListedDate"



error_text = "no results found on seek"
'''try:'''

chromeoptions = Options()
chromeoptions.headless = True  # hide GUI
chromeoptions.add_argument("--window-size=1920,1200")
chromeoptions.add_argument("--disable-extensions")
chromeoptions.add_argument("--disable-gpu")
chromeoptions.add_argument("--no-sandbox")
chromeoptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver = webdriver.Chrome(options=chromeoptions)
driver.get(url)

# wait for page to load
element = WebDriverWait(driver=driver, timeout=10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div/section'))
)
soup = BeautifulSoup(driver.page_source, 'html.parser')
response = requests.get(url)
error = soup.find_all("div", class_="yvsb870 _14uh99476 _14uh99466 _14uh99496 _14uh99486 _14uh9945a _1qw3t4i14 _1qw3t4i17 _14uh99432 _14uh99435")
e_len = len(error)


global job_counts
job_counts = soup.find('div', class_='yvsb870 _14uh99496 _14uh99486 _14uh994ae _6za4j60').find('h1', class_='yvsb870').find('span').text

search_results = []

job_elements = soup.find_all("article")

if job_elements:
    for a in job_elements:
        b = a.find("div", class_="yvsb870 _14uh9944u _14uh9944s").find("a", class_="yvsb870 yvsb87f h3f08he _14uh9945e _14uh994j _14uh994k _14uh994l _14uh994m")
        if b != None:
            global job_url
            job_url = "https://www.seek.co.nz" + b.get("href")
        j = a.find("h3", class_="yvsb870 _1qw3t4i0 _1qw3t4ih _1d0g9qk4 _1qw3t4ip _1qw3t4i1x").find("a", class_="_1tmgvw5 _1tmgvw8 _1tmgvwb _1tmgvwc _1tmgvwf yvsb870 yvsb87f _14uh994h")
        if j != None:
            global job_title
            job_title = j.text
        c = a.find("span", class_="yvsb870 _14uh9944u _1qw3t4i0 _1qw3t4i1x _1qw3t4i2 _1d0g9qk4 _1qw3t4ie").find("a", class_="l2mi890")
        if c != None:
            global job_company
            job_company = c.text
        t = a.find('span', class_='yvsb870 _14uh9944u _1qw3t4i0 _1qw3t4i1x _1qw3t4i1 _1d0g9qk4 _1qw3t4i8').find("span", class_="yvsb870")
        if t != None:
            global job_time
            job_time = t.text
        l = a.find(data-automation = "jobLocation")
        if l != None:
            global job_location
            job_location = l.text
        print(l)