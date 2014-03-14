from django.conf.urls import patterns, include, url

urlpatterns = patterns("tpms_survey",
    url(r'^get_template/$', 'views.get_template', name='get_template'),
    url(r'^add_template/$', 'views.add_template', name='add_template'),
    url(r'^update_template/$', 'views.update_template', name='update_template'),
    url(r'^delete_template/$', 'views.delete_template', name='delete_template'),

    url(r'^get_question_by_id/$', 'views.get_question_by_id', name='get_question_by_id'),
    url(r'^get_questions_by_template_id/$', 'views.get_questions_by_template_id', name='get_questions_by_template_id'),
    url(r'^add_question/$', 'views.add_question', name='add_question'),
    url(r'^update_question/$', 'views.update_question', name='update_question'),
    url(r'^delete_question/$', 'views.delete_question', name='delete_question'),
     
    url(r'^get_answer_by_id/$', 'views.get_answer_by_id', name='get_answer_by_id'),
    url(r'^get_answers_by_question_id/$', 'views.get_answers_by_question_id', name='get_answers_by_question_id'),
    url(r'^add_answer/$', 'views.add_answer', name='add_answer'),
    url(r'^update_answer/$', 'views.update_answer', name='update_answer'),
    url(r'^delete_answer/$', 'views.delete_answer', name='delete_answer'),

    url(r'^get_user_answer_by_user_id/$', 'views.get_user_answer_by_user_id', name='get_user_answer_by_user_id'),
    url(r'^add_user_answer/$', 'views.add_user_answer', name='add_user_answer'),
         
    )