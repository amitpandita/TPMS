import urllib
import urllib2
#import pdb;pdb.set_trace()

def call_url(url=None, data={}, request_type="GET"):
	if url:
		data = urllib.urlencode(data)
		if "POST" == request_type:
			req = urllib2.Request(url, data)
		else:
			req = urllib2.Request(url + "?" + data)
		response = urllib2.urlopen(req)
		the_page = response.read()
		return the_page

def add_template():
	url = 'http://127.0.0.1:8000/add_template'
	values = {'template_name' : 'Cisco Survey',
		  'template_desc' : 'desc1',
		  'project_team_id' : 2,
		  'status_cd' : 'A',
		  'created_by' : 'Ankit Mittal' }

	print call_url(url, values, "POST")

def get_template1():
	url = 'http://127.0.0.1:8000/api/get_template/'
	values = {'template_id' : 1}
	print call_url(url, values)

def get_template2():
	url = 'http://127.0.0.1:8000/api/get_template/'
	values = {}
	print call_url(url, values)

def add_question():
        url = 'http://127.0.0.1:8000/api/add_question/'
	values = {'template_id' : 1,
		  'presentation_order' : 1,
		  'question_type' : 'paragraph',
                  'question_desc' :'What is your name ?',
                  'is_question_rated' : 'Y',
                  'weight' : 3,
		  'status_cd' : 'A',
		  'created_by' : 'Amit Pandita' }

	print call_url(url, values, "POST")

def get_question_by_id():
	url = 'http://127.0.0.1:8000/api/get_template/'
	values = {'template_id' : 1}
	print call_url(url, values)
        

if __name__ == "__main__":
	#add_template()
	#get_template1()
	#get_template2()
	add_question()
