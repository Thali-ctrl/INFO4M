from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá mundo, essa é uma resposta HTTP')

def detail(request, question_id):
    return HttpResponse("Questão %s. " % question_id)

def detail(request, question_id):
    response = "Resposta %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Voto %s. " % question_id)