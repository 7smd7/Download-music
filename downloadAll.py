from selenium import webdriver
import time
import threading
import requests

class download(object):
    def add(self,name, url):
        thread = threading.Thread(target=self.run, args=(name,url))
        thread.daemon = True
        thread.start()

    def run(self,name, url):   
        r = requests.get(url, allow_redirects=True)
        name= name.replace("/"," ").replace("\\"," ").replace("?"," ").replace("*"," ").replace(">"," ").replace("<"," ").replace("|"," ").replace(":"," ").replace("\""," ")
        open(name+".mp3", 'wb').write(r.content)

driver = webdriver.PhantomJS()
counter=1
lastsource="soundcloud and youtube"
dl = download()

while(True):
    music = []
    driver.get("https://www.mp3juices.cc/")
    driver.find_element_by_id("query").clear()
    print("it's your %s'th search:" %counter)
    if counter==1:
        search=input("what do you want to listen?\n")
    else:
        search=input("what do you want to listen again?\n")
    source=input("input your search source (default press enter,other just type them):\nyoutube/soundcloud/vk/yandex/4shared/promodj/archive/default(%s)\n"%lastsource)
    if(source!=""):
        driver.find_element_by_id("control_sources").click()

        if ("youtube" in source) != ("youtube" in lastsource):
            driver.find_element_by_id("yt").click()
        if ("soundcloud" in source) !=("soundcloud" in lastsource):
            driver.find_element_by_id("sc").click()
        if ("vk" in source) != ("vk" in lastsource):
            driver.find_element_by_id("vk").click()
        if ("yandex" in source) != ("yandex" in lastsource):
            driver.find_element_by_id("yd").click()
        if ("4shared" in source) != ("4shared" in lastsource):
            driver.find_element_by_id("4s").click()
        if ("promodj" in source) != ("promodj" in lastsource):
            driver.find_element_by_id("pd").click()
        if ("archive" in source) != ("archive" in lastsource):
            driver.find_element_by_id("ar").click()
        
        lastsource=source
    driver.find_element_by_id("query").send_keys(search)
    driver.find_element_by_id("button").click()
    i=1
    print("\nRESULT")
    print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    while(True):
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[%s]/div[1]"%i).text
            break
        except:
            try:
                driver.find_element_by_xpath("//*[@id=\"error\"]").text
                print("")
                print(driver.find_element_by_xpath("//*[@id=\"error\"]").text)
                break
            except:
                time.sleep(1)
    try:
        while(True):
            name = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[%s]/div[1]"%i).text
            details = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[%s]/div[2]"%i).text
            driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[%s]/div[3]/a[1]"%i).click()
            time.sleep(2)
            i=i+1
            url=""
            while(url==""):
                time.sleep(1)
                url=driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[%s]/div[3]/a[1]"%i).get_attribute("href")
            print(name)
            print(details)
            print(url)
            dl.add(name,url)
            print("======================================")
            i=i+1
    except:
        print("FINISH\n")
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        counter=counter+1

