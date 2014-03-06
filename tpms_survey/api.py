from models import Template, Question, Answer
from django.http import HttpResponse, Http404
import json
from django.views.decorators.csrf import csrf_exempt

def get_template_by_id(get_data):
	'''
	@summary: to get template data
	'''
	data = {}
	template_id = get_data.get('template_id')
	if template_id:
		template = Template.objects.filter(template_id = template_id)
		if template:
			template = template[0]
			data['status'] = 1
			data['template_id'] = template.template_id
			data['template_name'] = template.template_name
			data['template_desc'] = template.template_desc
			data['project_team_id'] = template.project_team_id
			data['presentation_order'] = template.presentation_order
			data['status_cd'] = template.status_cd
			data['created_by'] = template.created_by
			data['updated_by'] = template.updated_by
			data['created_date'] = template.created_date.strftime("%Y-%m-%d %H:%M:%S")
			data['updated_date'] = template.updated_date.strftime("%Y-%m-%d %H:%M:%S")
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist'
	return data

def add_template(get_data):
	'''
	@summary: to add template
	@param: <data> template data dictionary
	'''
	data = {}
	template_name = get_data.get('template_name')
	template_desc = get_data.get('template_desc')
	project_team_id = get_data.get('project_team_id','')
	presentation_order = get_data.get('presentation_order','')
	status_cd = get_data.get('status_cd')
	created_by = get_data.get('created_by')
	updated_by = get_data.get('updated_by')
	created_date = get_data.get('created_date')
	updated_date = get_data.get('updated_date')
	if template_name and template_desc and project_team_id.isdigit() and presentation_order.isdigit() and status_cd and created_by:
		template_data = Template(
			template_name = template_name,
			template_desc = template_desc,
			project_team_id = project_team_id,
			presentation_order = presentation_order,
			status_cd = status_cd,
			created_by = created_by,
			updated_by = updated_by,
			created_date = created_date,
			updated_date = updated_date)
		template_data.save()
		data['status'] = 1
		data['msg'] = 'Template Added succssfully'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def update_template(get_data):
	'''
	@summary: to add template
	@param: <data> template data dictionary
	'''
	data = {}
	template_id = get_data.get('template_id')
	template_name = get_data.get('template_name')
	template_desc = get_data.get('template_desc')
	project_team_id = get_data.get('project_team_id','')
	presentation_order = get_data.get('presentation_order','')
	status_cd = get_data.get('status_cd')
	created_by = get_data.get('created_by')
	updated_by = get_data.get('updated_by')
	created_date = get_data.get('created_date')
	updated_date = get_data.get('updated_date')
	if template_id and template_name and template_desc and project_team_id.isdigit() and presentation_order.isdigit() and status_cd and created_by:
		template_data = Template.objects.filter(template_id = template_id)
		if template_data:
			template_data = template_data[0]
			template_data.template_name = template_name
			template_data.template_desc = template_desc
			template_data.project_team_id = project_team_id
			template_data.presentation_order = presentation_order
			template_data.status_cd = status_cd
			template_data.created_by = created_by
			template_data.updated_by = updated_by
			template_data.created_date = created_date
			template_data.updated_date = updated_date
			template_data.save()
			data['status'] = 1
			data['msg'] = 'Template updated succssfully'
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data


def delete_template(get_data):
	data = {}
	template_id = get_data.get('template_id')
	if template_id:
		template = Template.objects.filter(template_id = template_id)
		if template:
			template.delete()
			data['status'] = 1
			data['msg'] = 'Template deleted succssfully.'
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist.'
	return data