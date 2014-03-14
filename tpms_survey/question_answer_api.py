from models import Question, Answer
from template_api import get_template_object
from datetime import datetime

def get_question_object(question_id):
	return Question.objects.filter(question_id = question_id)

def get_answer_object(answer_id):
	return Answer.objects.filter(answer_id = answer_id)

def question_dict (question):
	return {
		"question_id": question.question_id,
		"template_id": question.template_id,
		"question_type": question.question_type,
		"question_desc": question.question_desc,
		"is_question_rated": question.is_question_rated,
		"weight": question.weight,
		"presentation_order": question.presentation_order,
		"status_cd": question.status_cd,
		"created_by": question.created_by,
		"updated_by": question.updated_by,
		"created_date": question.created_date.strftime("%Y-%m-%d %H:%M:%S"),
		"updated_date": question.updated_date.strftime("%Y-%m-%d %H:%M:%S"),
		"answer": get_answers_by_question_id(question.question_id)
	}

def answer_dict (answer):
	return {
		"answer_id": answer.answer_id,
		"question_id": answer.question_id,
		"answer_text": answer.answer_text,
		"answer_rating": answer.answer_rating,
		"presentation_order": answer.presentation_order,
		"status_cd": answer.status_cd,
		"created_by": answer.created_by,
		"updated_by": answer.updated_by,
		"created_date": answer.created_date.strftime("%Y-%m-%d %H:%M:%S"),
		"updated_date": answer.updated_date.strftime("%Y-%m-%d %H:%M:%S")
	}

def get_question_by_id (get_data):
	data = {}
	question_id = get_data.get('question_id')
	question = get_question_object(question_id)
	if question:
		question = question[0]
		data = question_dict(question)
	return data

def get_questions_by_template_id (get_data):
	data = {}
	template_id = get_data.get("template_id")
	if template_id:
		question_data = Question.objects.filter(template_id = template_id)
		if question_data:
			data['data'] = []
			for qd in question_data:
				data['data'].append(question_dict(qd))
			data['status'] = 1
		else:
			data['status'] = 0
			data['msg'] = 'Question does not exist'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def add_question(get_data):
	'''
	@summary: to add question
	@param: <data> question data dictionary
	'''
	data = {}
	import pdb;pdb.set_trace()
	template_id = get_data.get('template_id')
	presentation_order = get_data.get('presentation_order','')
	question_type = get_data.get('question_type')
	question_desc = get_data.get('question_desc')
	is_question_rated = get_data.get('is_question_rated')
	weight = get_data.get('weight')
	status_cd = get_data.get('status_cd')
	created_by = get_data.get('created_by')
	now_date = datetime.now()
	if template_id and question_type and question_desc and presentation_order.isdigit() and is_question_rated and status_cd and created_by:
		question_data = Question(
			template_id = template_id,
			presentation_order = presentation_order,
			question_type = question_type,
			question_desc = question_desc,
			is_question_rated = is_question_rated,
			weight = weight,
			status_cd = status_cd,
			created_by = created_by,
			updated_by = created_by,
			created_date = now_date,
			updated_date = now_date)
		question_data.save()
		data['status'] = 1
		data['msg'] = 'Question Added succssfully'
		data['data'] = {'question_id': question_data.question_id, 'template_id': question_data.template_id}
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def update_question(get_data):
	'''
	@summary to update question
	@param <data> question data dictionary
	'''
	data = {}
	question_id = get_data.get('question_id')
	template_id = get_data.get('template_id')
	presentation_order = get_data.get('presentation_order','')
	question_type = get_data.get('question_type')
	question_desc = get_data.get('question_desc')
	is_question_rated = get_data.get('is_question_rated')
	weight = get_data.get('weight')
	status_cd = get_data.get('status_cd')
	updated_by = get_data.get('updated_by')
	now_date = datetime.now()
	if question_id and template_id and question_type and question_desc and presentation_order.isdigit() and is_question_rated and status_cd and created_by:
		template_data = get_template_object(template_id)
		if template_data:
			question_data  = get_question_object(question_id)
			if question_data:
				question_data = question_data[0]
				last_question_type =  question_data.question_type
				question_data.template_id = template_id
				question_data.presentation_order = presentation_order
				question_data.question_type = question_type
				question_data.question_desc = question_desc
				question_data.is_question_rated = is_question_rated
				question_data.weight = weight
				question_data.status = status
				question_data.updated_by = updated_by
				question_data.updated_date = now_date
				question_data.save()

				# if last stored question type is multi-choice and current question type is paragraph then detele all the multi-choices from Answer table
				if 'multi-choice' == last_question_type and 'paragraph' == question_type:
					delete_answer_by_question_id(question_id)
				data['status'] = 1
				data['msg'] = 'Question Updated succssfully'
			else:
				data['status'] = 0
				data['msg'] = 'Question does not exist'
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def delete_question (get_data):
	'''
	@summary to delete question
	@param <data> question data dictionary
	'''
	status = False
	data = {}
	question_id = get_data.get('question_id')
	if question_id:
		question_data  = get_question_object(question_id)
		if question_data:
			last_question_type =  question_data[0].question_type
			if 'multi-choice' == last_question_type:
				delete_answer_by_question_id(question_id)
			question_data.delete()
			status = True
	return status

def get_answer_by_id (get_data):
	data = {}
	answer_id = get_data.get('answer_id')
	answer = get_answer_object(answer_id)
	if answer:
		answer = answer[0]
		data = answer_dict(answer)
	return data

def get_answers_by_question_id (question_id):
	data = []
	answer_data = Answer.objects.filter(question_id = question_id)
	for ad in answer_data:
		data.append(answer_dict[ad])
	return data

def add_answer(get_data):
	'''
	@summary: to add multi-choice answer
	@param: <data> answer data dictionary
	'''
	data = {}
	answer_text = get_data.get('answer_text')
	answer_rating = get_data.get('answer_rating','')
	presentation_order = get_data.get('presentation_order')
	question_id = get_data.get('question_id')
	status_cd = get_data.get('status_cd')
	created_by = get_data.get('created_by')
	now_date = datetime.now()
	if answer_text and answer_rating and presentation_order.isdigit() and question_id and status_cd and created_by:
		answer_data = Answer(
			answer_text = answer_text,
			answer_rating = answer_rating,
			presentation_order = presentation_order,
			question_id = question_id,
			status_cd = status_cd,
			created_by = created_by,
			updated_by = created_by,
			created_date = now_date,
			updated_date = now_date)
			
		answer_data.save()
		data['status'] = 1
		data['msg'] = 'Answer Added succssfully'
		data['data'] = {'question_id': answer_data.question_id, 'answer_id': answer_data.answer_id}
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def update_answer(get_data):
	'''
	@summary: to update multi-choice answer
	@param: <data> answer data dictionary
	'''
	data = {}
	answer_id = get_data.get('answer_id')
	answer_text = get_data.get('answer_text')
	answer_rating = get_data.get('answer_rating','')
	presentation_order = get_data.get('presentation_order')
	question_id = get_data.get('question_id')
	status_cd = get_data.get('status_cd')
	updated_by = get_data.get('updated_by')
	now_date = datetime.now()
	if answer_id and answer_text and answer_rating and presentation_order.isdigit() and question_id and status_cd and updated_by:
		answer_data = Answer.objects.filter(answer_id = answer_id)
		if answer_data:
			answer_data = answer_data[0]
			answer_data.answer_text = answer_text
			answer_data.answer_rating = answer_rating
			answer_data.presentation_order = presentation_order
			answer_data.question_id = question_id
			answer_data.status_cd = status_cd
			answer_data.updated_by = updated_by
			answer_data.updated_date = now_date
			answer_data.save()
			data['status'] = 1
			data['msg'] = 'Answer Updated succssfully'
			data['data'] = {'question_id': answer_data.question_id, 'answer_id': answer_data.answer_id}
		else:
			data['status'] = 0
			data['msg'] = 'Answer does not exist'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def delete_answer(get_data):
	'''
	@summary: to delete multi-choice answer
	@param: <data> answer data dictionary
	'''
	data = {}
	answer_id = get_data.get('answer_id')
	if answer_id:
		answer_data = Answer.objects.filter(answer_id = answer_id)
		if answer_data:
			answer_data.delete()
			data['status'] = 1
			data['msg'] = 'Answer deleted succssfully'
		else:
			data['status'] = 0
			data['msg'] = 'Answer does not exist'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def delete_answer_by_question_id (question_id):
	status = False
	answer_data = Answer.objects.filter(question_id = question_id)
	if answer_data:
		answer_data.delete()
		status = True
	return status