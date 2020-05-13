from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

while(True):
	name = input('Enter the name of user or group: ')
	msg = input('Enter Your message: ')
	count = int(input('Enter the count: '))

	input('Enter aything after QR scan: ')
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	msg_box = driver.find_element_by_class_name('_1Plpp')

	for i in range(count):
	    msg_box.send_keys(f'{msg}_{i}th times!!!')
	    button = driver.find_element_by_class_name('_35EW6')
	    button.click()
