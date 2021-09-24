from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")

listOfTimes = {"06:00": 1,
               "07:00": 2,
               "07:00": 3,
               "08:15": 4,
               "08:15": 5,
               "09:30": 6,
               "09:30": 7,
               "10:45": 8,
               "10:45": 9,
               "12:00": 10,
               "12:00": 11,
               "13:15": 12,
               "13:15": 13,
               "14:30": 14,
               "14:30": 15,
               "15:45": 16,
               "15:45": 17,
               "17:00": 18,
               "18:15": 19,
               "19:30": 20,
               "20:45": 21,
               "20:45": 22}


StudentNumberField = "/html/body/main/div/div/div/div[2]/div/form/input[4]"
proceedWithBooking = "/html/body/main/div/div/div/div[2]/div/form/input[5]"
confirmBookingPathButton = "/html/body/main/div/div/div/div[2]/div/a[1]"

X_PathNumberForTime = 2
timeTextBoxElement = driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr/td/table/tbody/tr[{X_PathNumberForTime}]/td[1]").text

refresh = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/a")
counter = 0

if(timeTextBoxElement == "20:45"):
    print("Looking for booking link")
    while(1 == 1):
        print(counter)
        counter = counter+1
        try:
            time.sleep(1)
            print("trying to find link")
            bookingLink = driver.find_element_by_xpath(f"/html/body/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr/td/table/tbody/tr[{X_PathNumberForTime}]/td[6]/a")
            print("we got the hyperlink")
            bookingLink.click()
            try:
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/button").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/button").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/a").click()
                driver.find_element_by_xpath(StudentNumberField).send_keys("20387306")
                time.sleep(1)
                driver.find_element_by_xpath(proceedWithBooking).click()
                time.sleep(1)
                driver.find_element_by_xpath(confirmBookingPathButton).click()
                time.speep(3)
                print("I think you have just booked your gym slot")
            except:
                print("Looks like I failed at the last step")
        except:
            print("Looks like things aren't right let me refresh")
            driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[1]/a").click()

else:
    print(timeTextBoxElement)



# driver.close()
# driver.quit()