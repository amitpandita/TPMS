from django.shortcuts import render_to_response
from forms import TemplateForm
from django.template import RequestContext
import api
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def get_template(request):
	return HttpResponse(json.dumps(api.get_template_by_id(request.GET)), content_type="application/json")
@csrf_exempt
def add_template(request):
	return HttpResponse(json.dumps(api.add_template(request.POST)), content_type="application/json")
@csrf_exempt
def update_template(request):
	return HttpResponse(json.dumps(api.update_template(request.POST)), content_type="application/json")
@csrf_exempt
def delete_template(request):
	return HttpResponse(json.dumps(api.delete_template(request.POST)), content_type="application/json")

# Create your views here.
def template(request):
	data = {}
	if 'POST' == request.method:
		template = TemplateForm(request.POST)
		if template.is_valid():
			if request.POST.get('template_id'):
				template_data = template.update()
				data['template_id'] = template_data.template_id
				data['msg'] = 'Template Updated Successfully'
				data['type'] = 'success'
			else:
				template_data = template.save()
				data['template_id'] = template_data.template_id
				data['msg'] = 'Template Added Successfully'
				data['type'] = 'success'
		return render_to_response('tpms_survey/template.html', locals(), context_instance=RequestContext(request))
	else:
		template_id = request.GET.get('template_id')
		template_data = get_template_by_id(template_id)
		if template_data:
			template = TemplateForm(template_data)
			data['template_id'] = template_data['template_id']
		else:
			template = TemplateForm()
		return render_to_response('tpms_survey/template.html', locals(), context_instance=RequestContext(request))