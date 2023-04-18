##################################################################################################
#Author Name: Trishna Jaithwa
#Purpose: To run test automation on Luma/Magento Shopping website
#Steps followed to run the test automation are:
# 		1 - Open site https://magento.softwaretestingboard.com/
# 		2 - Add to cart 4 - Gwyn Endurance Tee Medium Green
# 		3 -	Address should United Kingdom
# 		4 -	Check cart total is $92.00 (discount applied)
# 		5 -	Update the Quantity of  Gwyn Endurance Tee Medium Green to 3
# 		6 -	Add to cart 1 - Gwyn Endurance Tee Small Yellow
# 		7 -	Add to cart 1 Quest Lumaflex™ Band
# 		8 - Check cart total is $116.00
###################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# Step 1: Open URL and maximize window
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

# Function Description: This function will help in searching the item from the search bar and select the
# specified item's color, size and quantity
def selectProduct(product_name, size, color, quantity):
	driver.find_element(By.XPATH,"//*[@id='search']").send_keys(product_name)
	driver.find_element(By.XPATH,"//*[@id='search_mini_form']/div[2]/button").click()
	time.sleep(2)
	productColor = {
		"green": "//*[@id='option-label-color-93-item-53']",
		"yellow": "//div[@id='option-label-color-93-item-60']"
	}
	productSize = {
		"S": "//*[@id='product-options-wrapper']/div/div/div[1]/div/div[2]",
		"M": "//*[@id='product-options-wrapper']/div/div/div[1]/div/div[3]",
	}

	driver.find_element(By.XPATH,"//*[@id='maincontent']/div[3]/div[1]/div[2]/div[2]/ol/li[1]/div/div/strong/a").click()
	time.sleep(5)
	if size != "na" and color != "na":
		driver.find_element(By.XPATH, productSize[size]).click()
		driver.find_element(By.XPATH, productColor[color]).click()
	driver.find_element(By.XPATH, "//*[@id='qty']").clear()
	driver.find_element(By.XPATH, "//*[@id='qty']").send_keys(quantity)
	driver.find_element(By.XPATH, "//*[@id='product-addtocart-button']").click()

# Function Description: This function will open and view the cart items summary
def CheckOut():
	driver.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div/a").click()

# Function Description: This function helps to compare the expected total amount with the actual cart total amount
def validateTotal(expectedTotal):
	cartTotal = driver.find_element(By.XPATH,"//*[@id='cart-totals']/div/table/tbody/tr/td/strong").text
	cartTotal = cartTotal.split("$")[1]
	if cartTotal != expectedTotal:
		print("Cart total", cartTotal, "is not matching the expected value of", expectedTotal)
	else:
		print("Cart total", cartTotal, "is matching the expected value of", expectedTotal)

# Step 2: Add to cart 4 - Gwyn Endurance Tee Medium Green
selectProduct("Gwyn Endurance Tee", "M", "green", 4)
CheckOut()
time.sleep(10)

# Step 3: Address to be changed to United Kingdom
driver.find_element(By.XPATH,"//*[@id='block-shipping-heading']").click()
country_list = Select(driver.find_element(By.NAME, 'country_id'))
country_list.select_by_visible_text("United Kingdom")

# Step 4: Check cart total is $92.00 (discount applied)
time.sleep(10)
validateTotal("92.00")

# Step 5: Update the Quantity of Gwyn Endurance Tee Medium Green to 3
driver.find_element(By.XPATH,"//a[@title='Edit item parameters']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='qty']").clear()
driver.find_element(By.XPATH,"//*[@id='qty']").send_keys("3")
driver.find_element(By.XPATH,"//*[@id='product-updatecart-button']").click()

# Step 6: Add to cart 1 - Gwyn Endurance Tee Small Yellow
time.sleep(10)
selectProduct("Gwyn Endurance Tee", "S", "yellow",1)

# Step 7: Add to cart 1 Quest Lumaflex™ Band
time.sleep(10)
selectProduct("Quest Lumaflex™ Band", "na", "na",1)
CheckOut()

# Step 8: Check cart total is $116.00
validateTotal("116.00")