from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    return HttpResponse('Olá mundo, essa é uma resposta HTTP')

def detail(request, question_id):
    return HttpResponse("Questão %s. " % question_id)

def results(request, question_id):
    response = "Resposta %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voto %s. " % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))