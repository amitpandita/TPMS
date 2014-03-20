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

def get_template():
	url = 'http://127.0.0.1:8000/api/get_template/'
	values = {'template_id' : 2}
	print call_url(url, values)

def get_templates():
	url = 'http://127.0.0.1:8000/api/get_template/'
	values = {}
	print call_url(url, values)

def add_template():
	url = 'http://127.0.0.1:8000/api/add_template/'
	values = {
		'template_name' : 'Cisco Survey2',
		'template_desc' : 'Cisco Survey Description1.',
		'project_team_id' : 2,
		'presentation_order': 2,
		'status_cd' : 'A',
		'created_by' : 'Amit Pandita'
	}
	print call_url(url, values, "POST")

def update_template():
	url = 'http://127.0.0.1:8000/api/update_template/'
	values = {
		'template_id': 2,
		'template_name' : 'Cisco Survey2',
		'template_desc' : 'Cisco Survey Description2.',
		'project_team_id' : 2,
		'presentation_order': 2,
		'status_cd' : 'A',
		'updated_by' : 'Yogesh'
	}
	print call_url(url, values, "POST")

def delete_template():
	url = 'http://127.0.0.1:8000/api/delete_template/'
	values = {
		'template_id': 2
	}
	print call_url(url, values, "POST")


def get_question_by_id():
	url = 'http://127.0.0.1:8000/api/get_question_by_id/'
	values = {'question_id' : 3}
	print call_url(url, values)
		
def get_question_by_template_id():
	url = 'http://127.0.0.1:8000/api/get_questions_by_template_id/'
	values = {'template_id' : 2}
	print call_url(url, values)

def add_question():
	url = 'http://127.0.0.1:8000/api/add_question/'
	values = {
		'template_id' : 2,
		'presentation_order' : 2,
		'question_type' : 'paragraph',
		'question_desc' :'What is your name ?',
		'is_question_rated' : 'Y',
		'weight' : 3,
		'status_cd' : 'A',
		'created_by' : 'Amit Pandita'
	}
	print call_url(url, values, "POST")

def update_question():
	url = 'http://127.0.0.1:8000/api/update_question/'
	values = {
		'question_id' : 3,
		'template_id' : 2,
		'presentation_order' : 2,
		'question_type' : 'paragraph',
		'question_desc' :'What is your city ?',
		'is_question_rated' : 'Y',
		'weight' : 3,
		'status_cd' : 'A',
		'updated_by' : 'Yogesh Kumar'
	}
	print call_url(url, values, "POST")

def delete_question():
	url = "http://127.0.0.1:8000/api/delete_question/"
	values = {
		"question_id": 3
	}
	print call_url(url, values, "POST")

def get_answer_by_id():
	url = "http://127.0.0.1:8000/api/get_answer_by_id/"
	values = {
		"answer_id": 1
	}
	print call_url(url, values)

def add_answer():
	url = 'http://127.0.0.1:8000/api/add_answer/'
	values = {
		'question_id' : 4,
		'presentation_order' : 2,
		'answer_rating': 10,
		'answer_text': 'Gurgaon',
		'status_cd': 'A',
		'created_by' : 'Amit Pandita'
	}
	print call_url(url, values, "POST")

def update_answer():
	url = 'http://127.0.0.1:8000/api/update_answer/'
	values = {
		'answer_id': 1,
		'question_id': 4,
		'presentation_order': 2,
		'answer_rating': 10,
		'answer_text': 'Gurgaon',
		'status_cd': 'A',
		'updated_by': 'Yogesh'
	}
	print call_url(url, values, "POST")

def delete_answer():
	url = "http://127.0.0.1:8000/api/delete_answer/"
	values = {
		"answer_id": 1
	}
	print call_url(url, values, "POST")


def add_user_answer():
	url = 'http://127.0.0.1:8000/api/add_user_answer/'
	values = {
		'user_id' : 1,
		'question_id' : 4,
		#'answer_id': 1,
		'answer_text': 'Yogesh',
		'status_cd': 'A',
		'answer_score': 45,
		'created_by' : 'Yogesh Kumar'
	}
	print call_url(url, values, "POST")

def get_user_answer_by_user_id():
	url = "http://127.0.0.1:8000/api/get_user_answer_by_user_id/"
	values = {
		"user_id": 1
	}
	print call_url(url, values)

if __name__ == "__main__":
	print "Calling API"
	#get_template()
	#get_templates()
	#add_template()
	#update_template()
	#delete_template()

	#add_question()
	#get_question_by_id()
	#get_question_by_template_id()
	#update_question()
	#delete_question()

	#add_answer()
	#get_answer_by_id()
	#update_answer()
	#delete_answer()

	#add_user_answer()
	#get_user_answer_by_user_id()
