from django.shortcuts import render, redirect
from .forms import accesForm


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException




browser = webdriver.PhantomJS("/home/firas/git/scripts-python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs",  service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
browser.set_window_size(1120, 550)

def auto_cheek(name,password):
        browser.get('http://instagram.com')
        time.sleep(10)
        browser.find_element_by_xpath("//a[contains(@class, '_b93kq')]").click()
        user_name = browser.find_element_by_name('username')
        user_name.clear()
        user_name.send_keys(name)
        password_el = browser.find_element_by_name('password')
        password_el.clear()
        password_el.send_keys(password)
        password_el.send_keys(Keys.RETURN)
        time.sleep(10)
        try:
                error = browser.find_element_by_id('slfErrorAlert')
        except NoSuchElementException:
                error = None
        if error != None:
                return error.text
        else:
                return 'acces valider'

def get_detail():
	time.sleep(5)
	browser.find_element_by_xpath("//a[contains(@class, '_8scx2 _gvoze coreSpriteDesktopNavProfile')]").click()
	time.sleep(10)
	detail = browser.find_elements(By.XPATH, "//span[contains(@class, '_fd86t')]")
	nb_post = detail[0].text
	nb_follow = detail[1].text
	nb_following = detail[2].text
	print(nb_post,"posts")
	print(nb_follow,"follower")
	print(nb_following,"following")
	time.sleep(5)

def follow():
    pass

def index(request):
	return render(request,'follow/index.html')

def acces(request):
	if request.method == "POST":
		form = accesForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['username']
			password = form.cleaned_data['password']
			print(name)
			print(password)
			result = auto_cheek(name,password)
			print(result)
			if result == 'acces valider':
				get_detail()
				#save login and password
			return render(request, 'follow/acces.html', {'form' : form, 'result' : result})
	else:
		form = accesForm()
	return render(request, 'follow/acces.html', {'form' : form})

