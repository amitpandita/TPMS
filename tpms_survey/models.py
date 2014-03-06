from django.db import models


class Template(models.Model):
	template_id = models.AutoField(primary_key=True)
	template_name = models.CharField(max_length=50)
	template_desc = models.CharField(max_length=500, null=True, blank=True)
	project_team_id = models.IntegerField(null=True, blank=True)
	presentation_order = models.IntegerField(null=True, blank=True)
	status_cd = models.CharField(max_length=1)
	created_by = models.CharField(max_length=50)
	created_date = models.DateField(auto_now_add=True)
	updated_by = models.CharField(max_length=50, null=True, blank=True)
	updated_date = models.DateField(auto_now=True)


class Question(models.Model):
	question_id = models.AutoField(primary_key=True)
	template = models.ForeignKey(Template)
	question_type = models.CharField(max_length=20)
	question_desc = models.TextField()
	is_question_rated = models.CharField(max_length=1)
	weight = models.IntegerField(null=True, blank=True)
	presentation_order = models.IntegerField()
	status_cd = models.CharField(max_length=1)
	created_by = models.CharField(max_length=50)
	created_date = models.DateField(auto_now_add=True)
	updated_by = models.CharField(max_length=50, null=True, blank=True)
	updated_date = models.DateField(auto_now=True)


class Answer(models.Model):
	answer_id = models.AutoField(primary_key=True)
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=500)
	answer_rating = models.IntegerField(null=True, blank=True)
	presentation_order = models.IntegerField(null=True, blank=True)
	status_cd = models.CharField(max_length=1)
	created_by = models.CharField(max_length=50)
	created_date = models.DateField(auto_now_add=True)
	updated_by = models.CharField(max_length=50, null=True, blank=True)
	updated_date = models.DateField(auto_now=True)


class UserAnswer(models.Model):
	user_answer_id = models.AutoField(primary_key=True)
	question = models.ForeignKey(Question)
	answer = models.ForeignKey(Answer)
	user_id = models.CharField(max_length=64)
	answer_text = models.CharField(max_length=500, null=True, blank=True)
	answer_score = models.IntegerField()
	status_cd = models.CharField(max_length=1)
	created_by = models.CharField(max_length=50)
	created_date = models.DateField(auto_now_add=True)
	updated_by = models.CharField(max_length=50, null=True, blank=True)
	updated_date = models.DateField(auto_now=True)

