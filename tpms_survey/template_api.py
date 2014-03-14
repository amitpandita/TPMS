from models import Template
from datetime import datetime
import json

# start - template
def get_template_object (template_id):
	return Template.objects.filter(template_id = template_id)

def tempalte_dict(template):
	return {
		"template_id": template.template_id,
		"template_name": template.template_name,
		"template_desc": template.template_desc,
		"project_team_id": template.project_team_id,
		"presentation_order": template.presentation_order,
		"status_cd": template.status_cd,
		"created_by": template.created_by,
		"updated_by": template.updated_by,
		"created_date": template.created_date.strftime("%Y-%m-%d %H:%M:%S"),
		"updated_date": template.updated_date.strftime("%Y-%m-%d %H:%M:%S")
	}

def get_template_by_id(get_data):
	'''
	@summary: to get template data
	'''
	data = {}
	template_id = get_data.get('template_id')
	if template_id:
		template = get_template_object(template_id)
		if template:
			template = template[0]
			data['status'] = 1
			data.update(tempalte_dict(template))
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist'
	else:
		data = []
		templates = Template.objects.all()
		for template in templates:
			data.append(tempalte_dict(template))
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
	now_date = datetime.now()
	if template_name and template_desc and project_team_id.isdigit() and presentation_order.isdigit() and status_cd and created_by:
		template_data = Template(
			template_name = template_name,
			template_desc = template_desc,
			project_team_id = project_team_id,
			presentation_order = presentation_order,
			status_cd = status_cd,
			created_by = created_by,
			updated_by = created_by,
			created_date = now_date,
			updated_date = now_date)
		template_data.save()
		data['status'] = 1
		data['msg'] = 'Template Added successfully'
	else:
		data['status'] = 0
		data['msg'] = 'Some fields are missing'
	return data

def update_template(get_data):
	'''
	@summary: to add template
	@param: <data> template data dictionary
	'''
	now_date = datetime.now()
	data = {}
	template_id = get_data.get('template_id')
	template_name = get_data.get('template_name')
	template_desc = get_data.get('template_desc')
	project_team_id = get_data.get('project_team_id','')
	presentation_order = get_data.get('presentation_order','')
	status_cd = get_data.get('status_cd')
	updated_by = get_data.get('updated_by')
	if template_id and template_name and template_desc and project_team_id.isdigit() and presentation_order.isdigit() and status_cd and created_by:
		template_data = get_template_object(template_id)
		if template_data:
			template_data = template_data[0]
			template_data.template_name = template_name
			template_data.template_desc = template_desc
			template_data.project_team_id = project_team_id
			template_data.presentation_order = presentation_order
			template_data.status_cd = status_cd
			template_data.updated_by = updated_by
			template_data.updated_date = now_date
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
		template = get_template_object(template_id)
		if template:
			template.delete()
			data['status'] = 1
			data['msg'] = 'Template deleted succssfully.'
		else:
			data['status'] = 0
			data['msg'] = 'Template does not exist.'
	return data
# end - template