from selenium import webdriver
import time
homeURL = "https://www.google.es/maps/dir//" 

def getBetweenStations(fromStation,toStation):
    time.sleep(5)
    driver.find_element_by_name('Acepto')
    #driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span/span')
    driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span') 
if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')
    options = webdriver.ChromeOptions()
    #options.setExperimentalOption("excludeSwitches")
    
    driver.get(homeURL)
    start = "38.07369012429733, 23.808313374302397" #Kiffisia  
    end = "38.065925720419365, 23.80402627067208"   #KAT
    getBetweenStations(start,end)
