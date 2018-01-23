import re
from robobrowser import RoboBrowser

url = 'http://testerhome.com/account/sign_in/'
b = RoboBrowser(history=True)
b.open(url)

login_form = b.get_form(action='/acount/sign_in')
print login_form

login_form['user[login]'].value = 'your account'
login_form['user[password]'].value = 'your password'

b.submit_form(login_form)

print b.select('.alert.alert-success')[0].text