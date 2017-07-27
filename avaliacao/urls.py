from django.conf.urls import url
from . import views

app_name='avaliacao'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^questionario/(?P<avaliacao_id>\d+)?', views.questionario, name='questionario'),
	url(r'^questionario/(?P<avaliacao_id>\d+)?/(?P<questao_id>\d+)?/', views.questionario, name='questionario'),
	# url(r'^questionario/', views.questionario, name='questionario'),
]