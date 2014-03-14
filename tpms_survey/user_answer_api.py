from models import UserAnswer
from question_answer_api import answer_dict, question_dict
from datetime import datetime

def get_user_answer_object(user_id):
	return UserAnswer.objects.filter(user_id = user_id)

def user_answer_dict (user_answer):
	return {
		"question": question_dict(user_answer.question),
		"answer": user_answer.answer and answer_dict(user_answer.answer) or {},
		"answer_text": user_answer.answer_text,
		"answer_score": user_answer.answer_score,
		"status_cd": user_answer.status_cd,
		"created_by": user_answer.created_by,
		"updated_by": user_answer.updated_by,
		"created_date": user_answer.created_date.strftime("%Y-%m-%d %H:%M:%S"),
		"updated_date": user_answer.updated_date.strftime("%Y-%m-%d %H:%M:%S")
	}

def add_user_answer(get_data):
	data = {}
	user_id = get_data.get('user_id')
	question_id = get_data.get('question_id')
	answer_id = get_data.get('answer_id')
	answer_text = get_data.get('answer_text')
	status_cd = get_data.get('status_cd')
	created_by = get_data.get('created_by')
	now_date = datetime.now()
	if user_id and question_id and answer_id and answer_text and status_cd and created_by:
		user_answer_data = UserAnswer(
				user_id = user_id,
				question_id = question_id,
				answer_id = answer_id,
				answer_text = answer_text,
				status_cd = status_cd,
				created_by = created_by,
				updated_by = created_by,
				created_date = now_date,
				updated_date = now_date
			)
		user_answer_data.save()
		data['status'] = 1
		data['msg'] = 'User Answer Added succssfully'
		data['data'] = {'question_id': user_answer_data.user_answer_id}
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def get_user_answer_by_user_id (get_data):
	data = {}
	user_id = get_data.get('user_id')
	user_answer = get_user_answer_object(user_id)
	if user_answer:
		data["data"]  = []
		data["status"] = 1
		for ua in user_answer:
			data["data"].append(user_answer_dict(ua))
	else:
		data["status"] = 0
		data["msg"] = "Question does not exist."
	return data