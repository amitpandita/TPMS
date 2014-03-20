from django.shortcuts import render_to_response
from forms import TemplateForm
from django.template import RequestContext
import template_api, question_answer_api, user_answer_api
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#-------Template Starts-----------

def get_template(request):
	return HttpResponse(json.dumps(template_api.get_template_by_id(request.GET)), content_type="application/json")
@csrf_exempt
def add_template(request):
	return HttpResponse(json.dumps(template_api.add_template(request.POST)), content_type="application/json")
@csrf_exempt
def update_template(request):
	return HttpResponse(json.dumps(template_api.update_template(request.POST)), content_type="application/json")
@csrf_exempt
def delete_template(request):
	return HttpResponse(json.dumps(template_api.delete_template(request.POST)), content_type="application/json")

#-------Template Ends-------------

#-------Question Starts-----------

def get_question_by_id(request):
	return HttpResponse(json.dumps(question_answer_api.get_question_by_id(request.GET)), content_type="application/json")
def get_questions_by_template_id(request):
	return HttpResponse(json.dumps(question_answer_api.get_questions_by_template_id(request.GET)), content_type="application/json")
@csrf_exempt
def add_question(request):
	return HttpResponse(json.dumps(question_answer_api.add_question(request.POST)), content_type="application/json")
@csrf_exempt
def update_question(request):
	return HttpResponse(json.dumps(question_answer_api.update_question(request.POST)), content_type="application/json")
@csrf_exempt
def delete_question(request):
	return HttpResponse(json.dumps(question_answer_api.delete_question(request.POST)), content_type="application/json")

#-------Question Ends-----------	

#-------Answer Starts-----------

def get_answer_by_id(request):
	return HttpResponse(json.dumps(question_answer_api.get_answer_by_id(request.GET)), content_type="application/json")
@csrf_exempt
def add_answer(request):
	return HttpResponse(json.dumps(question_answer_api.add_answer(request.POST)), content_type="application/json")
@csrf_exempt
def update_answer(request):
	return HttpResponse(json.dumps(question_answer_api.update_answer(request.POST)), content_type="application/json")
@csrf_exempt
def delete_answer(request):
	return HttpResponse(json.dumps(question_answer_api.delete_answer(request.POST)), content_type="application/json")

#-------Answer Ends-----------	

#-------User_Answer Starts-----------

def get_user_answer_by_user_id(request):
	return HttpResponse(json.dumps(user_answer_api.get_user_answer_by_user_id(request.GET)), content_type="application/json")

@csrf_exempt
def add_user_answer(request):
	return HttpResponse(json.dumps(user_answer_api.add_user_answer(request.POST)), content_type="application/json")

#-------User_Answer Ends-----------	