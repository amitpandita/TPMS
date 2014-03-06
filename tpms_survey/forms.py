from django import forms
from models import Template

class TemplateForm(forms.Form):
	template_id = forms.IntegerField(widget = forms.HiddenInput(), required=False)
	template_name = forms.CharField(label = "Template Name", max_length = 50, widget = forms.TextInput(), required=True)
	template_desc = forms.CharField(label = "Description", max_length = 500, widget = forms.Textarea(), required=True)
	project_team_id = forms.CharField(label = "Project Team", max_length = 50, widget = forms.TextInput(), required=True)
	presentation_order = forms.CharField(label = "Presentation Order", max_length = 50, widget = forms.TextInput(), required=True)
	created_by = forms.CharField(label = "Created By", max_length = 50, widget = forms.TextInput(), required=True)
	def save(self):
		data = self.cleaned_data
		template = Template(**data)
		template.save()
		return template

	def update(self):
		data = self.cleaned_data
		if data.get("template_id"):
			template = Template.objects.filter(template_id=data.get("template_id"))
			if template:
				template = template[0]
				template.template_name = data.get("template_name")
				template.template_desc = data.get("template_desc")
				template.project_team_id = data.get("project_team_id")
				template.presentation_order = data.get("presentation_order")
				template.created_by = data.get("created_by")
				template.save()
			else:
				raise forms.ValidationError('Template not Exist.')
		return template