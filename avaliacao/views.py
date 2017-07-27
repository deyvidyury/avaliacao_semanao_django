from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html');

def questionario(request, avaliacao_id=False, questao_id=False):
	avaliacoes = Avaliacao.objects.all();
	# Caso id da avaliacao nao tenha sido especificado, pegar a avaliacao da semana corrente
	if not avaliacao_id:
		avaliacao_selecioanda = Avaliacao.objects.filter(periodo_inicio__lte=date.today(), periodo_fim__gte=date.today())[:1].get()
	else:
		avaliacao_selecioanda = Avaliacao.objects.get(id=avaliacao_id)

	if not questao_id:
		questao = avaliacao_selecioanda.questoes.all()[0]
	else :
		questao = avaliacao_selecioanda.questoes.get(id=questao_id)

	usuarios = Usuario.objects.filter(funcao__in=('O'))

	qnt_questoes = avaliacao_selecioanda.questoes.count()
	respostas = 0
	percentagem = (respostas / qnt_questoes) * 100;

	return render(request, 'questionario.html',
		{'avaliacoes': avaliacoes, 
		'avaliacao_selecioanda': avaliacao_selecioanda, 
		'questao': questao,
		'usuarios': usuarios,
		'qnt_questoes': qnt_questoes,
		'respostas': respostas,
		'percentagem': percentagem}
	);