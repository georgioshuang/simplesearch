
from re import X
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def query(request):
    return render(request, 'engine/home.html')

def about(request):
    return render(request, 'engine/about.html')
    

def seek(request):  
    site = "seek"
    query = request.GET.get('job')
    loc = request.GET.get('location')
    page_num = request.GET.get("page", 1)
    w = str(query)
    p = str(page_num)
    l = str(loc)
    L = l.capitalize
    url = "https://www.seek.co.nz/" + w + "-jobs" + "/in-" + l  + "?page=" + p + "&sortmode=ListedDate"
    
    error_text = "no results found on seek"
    try:

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
        
        if e_len == 1 or response.status_code == 404:
            return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
        else:
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
                    '''l = a.find("span", class_="yvsb870 _14uh9944u _1qw3t4i0 _1qw3t4i1x _1qw3t4i1 _1d0g9qk4 _1qw3t4i8")
                    if l != None:
                        global job_location
                        job_location = l.text'''
                    s = a.find("div", class_="yvsb870 _14uh9948z")#.find("span", class_="yvsb870 _14uh9944u _1qw3t4i0 _1qw3t4i1y _1qw3t4i1 _1d0g9qk4 _1qw3t4i8")find("div", class_="yvsb870 v8nw070 v8nw072").find("div", class_="yvsb870 _14uh99466").
                    if s != None:
                        global job_shortdesc
                        job_shortdesc = s.text
                    
                    search_results.append((job_url,job_title,job_shortdesc,job_company,job_time,L))
                

            search_pages = []
            pagination = soup.find_all("li", class_="yvsb870 _14uh9944q _14uh9944v _14uh9948b")
            for bb in pagination:
                cc = bb.find("a", class_="yvsb870 yvsb87f")
                seek_pagelink = cc.get('href').split("page=")[-1]
                aa = bb.find("span", class_="yvsb870 _14uh9944u _14uh994g2 _1qw3t4i0 _1qw3t4i1x _1qw3t4i1 _1qw3t4ia")
                if aa != None:
                    seek_pagenum = aa.text
                search_pages.append((seek_pagelink, seek_pagenum))

            prev_page = []    
            prev = soup.find("li", "yvsb870 _14uh9948m _14uh9948b _14uh994w")
            if prev != None:
                p_text = prev.find('span', class_='yvsb870 _14uh9944q _14uh9944z _14uh994da').text
                p_link = prev.find('a', class_='yvsb870 yvsb87f').get('href').split("page=")[-1]
                prev_page.append((p_link,p_text))
            
            next_page = []    
            next = soup.find("li", "yvsb870 _14uh9949m _14uh9949b _14uh994w")
            if next != None:
                n_text = next.find('span', class_='yvsb870 _14uh994ca').text
                n_link = next.find('a', class_='yvsb870 yvsb87f').get('href').split("page=")[-1]
                next_page.append((n_link,n_text))

            context = {
                'search_results':search_results,
                'query':query,
                'site':site,
                'loc':loc,
                'search_pages':search_pages,
                'prev_page':prev_page,
                'next_page':next_page,
                'job_counts':job_counts,
            
            }
            
            return render(request, 'engine/results.html', context)
            driver.quit()
    except:
        return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
  
        
                
def indeed(request):
    query = request.GET.get('job')
    loc = request.GET.get('location')
    site = "indeed"
    w = str(query)
    l = str(loc)
    page_num = request.GET.get("page", 1)
    p = str(page_num)
    if page_num == 1:
        url = "https://nz.indeed.com/jobs?q=" + w + '&l=' + l + "&sort=date"
    else:
        url = "https://nz.indeed.com/jobs?q=" + w + '&l=' + l + "&sort=date" + "&start=" + p
    
    error_text = "no results found on indeed"
    try:
# configure webdriver
        chromeoptions = Options()
        chromeoptions.headless = True  # hide GUI
        chromeoptions.add_argument("--window-size=1920,1200")
        chromeoptions.add_argument("--disable-extensions")
        chromeoptions.add_argument("--disable-gpu")
        chromeoptions.add_argument("--no-sandbox")
        chromeoptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        chromeoptions.add_argument("--disable-infobars")
        chromeoptions.add_argument("--disable-browser-side-navigation")
        chromeoptions.add_argument("--ignore-certificate-errors")
        driver = webdriver.Chrome(options=chromeoptions)
        driver.get(url)
    
            # wait for page to load
        element = WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_element_located((By.ID, 'DesktopSERPJobAlertActivateButton')))
        
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        response = requests.get(url)
        error = soup.find("div", class_="jobsearch-NoResult-messageHeader")
        error1 = soup.find(" did not match any jobs.")
        
        if error != None or error1 != None or response.status_code == 404:
            return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
        else:
            job_c1 = soup.find('div', {'class': 'jobsearch-JobCountAndSortPane-jobCount'})
            if job_c1 :
                job_c11 = job_c1.text
                job_c2 = job_c11.split('of')
                job_c3 = job_c2[1]
                job_c4 = job_c3.split('jobs')
                if job_c4:
                    global job_counts 
                    job_counts = job_c4[0]
            
            search_results = []
            job_first = soup.find('ul', class_='jobsearch-ResultsList css-0')
            job_elements = job_first.find_all("li")
            if job_elements:
                for a in job_elements:
                    b = a.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")
                    if b != None:
                        link_elements = b.get("href")
                        job_url = "https://nz.indeed.com" + link_elements
                        job_title = b.text
                        c = a.find('span', class_='companyName')
                        if c != None:
                            global job_company
                            job_company = c.text
                        l = a.find(class_='companyLocation')
                        if l != None:
                            job_location = l.text
                        s = a.find("div", class_="job-snippet")
                        if s != None:
                            job_shortdesc = s.text
                        t = a.find('span', class_='date')
                        if t != None:
                            t1 = t.text
                            job_time = t1[6:]
                            search_results.append((job_url,job_title,job_shortdesc,job_company,job_time,job_location))
            
        
            search_pages = []
            p1 = soup.find(class_="css-jbuxu0 ecydgvn0")
            if p1:
                p2 = p1.find_all(class_='css-tvvxwd ecydgvn1')
                if p2:
                    for c in p2:
                        x = c.find("a")
                        if x:
                            page_link = x.get('href').split("start=")[-1]
                            page_n = x['aria-label']
                            if page_n == "Previous Page":
                                page_n = "Prev"
                            elif page_n == "Next Page":
                                page_n = "Next"
                            else:
                                page_n = page_n
                            search_pages.append((page_link,page_n))
            
        
            context = {
                'search_results':search_results,
                'job_counts':job_counts,
                'query':query,
                'site':site, 
                'loc':loc,
                'search_pages':search_pages
            }

            return render(request, 'engine/results.html', context)
            driver.quit()
    except:
        return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})





def trademe(request):
    
    query = request.GET.get('job')
    loc = request.GET.get('location')
    site = "trademe"
    w = str(query)
    l = str(loc)
    page_num = request.GET.get("page", 1)
    p = str(page_num)
    url = "https://www.trademe.co.nz/a/jobs/" + l + "/search?search_string=" + w + "&sort_order=expirydesc" + "&page=" + p
    error_text = "no results found on trademe"
    try:
        # configure webdriver
        chromeoptions = Options()
        chromeoptions.headless = True  # hide GUI
        chromeoptions.add_argument("--window-size=1920,1200")
        chromeoptions.add_argument("--disable-extensions")
        chromeoptions.add_argument("--disable-gpu")
        chromeoptions.add_argument("--no-sandbox")
        chromeoptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
        driver = webdriver.Chrome(options=chromeoptions)
        
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        response = requests.get(url)
        
        
        if response.status_code == 404:
            return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
        elif soup.find("main").find("div").find("tm-not-found") != None and "Oops"in soup.find("main").find("div").find("tm-not-found").find("h1").text:
            return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
        elif soup.find("tm-search-header-result-count") != None and "0 results" in soup.find("tm-search-header-result-count").find("h3").text:
            return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})
        else:
            search_results = []
            job_elements = soup.find_all("tm-jobs-search-card")
            job_counts = soup.find("tm-search-header-result-count").find("h3").text.split('Showing')[1].split('results')[0]
            for a in job_elements:
                job_url = "https://www.trademe.co.nz/a/" + a.find("a").get("href")
                job_location_time = a.find("div", class_="tm-jobs-search-card-header__location-and-time").text.split("Listed")
                job_location = job_location_time[0]
                job_time = job_location_time[-1]
                job_company= a.find("div", class_="tm-jobs-search-card-header__company").text
                job_title = a.find('div', class_="tm-jobs-search-card__title").text
                job_shortdesc = a.find(tmid="subtitle").text        
                search_results.append((job_url,job_title,job_shortdesc,job_company,job_time,job_location))

            search_pages = []
            pagination = soup.find_all("tg-pagination-link", class_="o-pagination__link")
            for bb in pagination:
                pagelink = bb.find("a").get('href').split("page=")[-1]
                pagenum = bb.text
                if pagenum not in ('Home', 'jobs', 'Jobs', 'jobs/auckland', 'Auckland'):
                    search_pages.append((pagelink, pagenum))     
            
            context = {
                'search_results':search_results,
                'job_counts':job_counts,
                'query':query,
                'site':site, 
                'loc':loc,
                'search_pages':search_pages
                
            }
            return render(request, 'engine/results.html', context)
            driver.quit()
    except:
        return render(request, 'engine/results.html', {'error_text':error_text, 'site':site, 'query':query,'loc':loc})


    














