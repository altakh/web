from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.urlresolvers import reverse

def test(request, *args, **kwargs):
   return HttpResponse('OK')

def new(request):
    questions = Question.objects.order_by("-id")
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'new.html', {
        'questions': page.object_list,
	'page': page, 
	'paginator': paginator,
})
#23
def popular(request):
    questions = Question.objects.order_by("-rating")
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {
        'questions': page.object_list,
	'page': page, 
	'paginator': paginator,
})

def question(request, id):
    if request.method is 'POST':
	return answer(request)
    question = get_object_or_404(Question, id=int(id))
    form = AnswerForm(initial={'question': question.id})
    return render(request, 'question.html', {'question': question, 
					   'answers': question.answer_set.all(), 
					   'form': form})
#45
def ask_add(request):
    if request.method == "POST":
	form = AskForm(request.POST)
	if form.is_valid():
	    question = form.save()
	    return HttpResponseRedirect("/question/"+str(question.id)+"/")
    else:
	form = AskForm()
    return render(request, 'ask_add.html', {'form': form})

def answer_add(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
	    url = '/question/%d/' % answer.question_id
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'answer_add.html', {
        "form": form
    })
	
