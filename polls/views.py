from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from .models import Question, Choice
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import PollForm
from django.forms.formsets import formset_factory
from django.utils import timezone

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, }

    return render(request, 'polls/index.html', context)




@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    current_user = request.user.id

    if current_user == question.user_id:
        return render(request, 'polls/error_response.html')
    else:
        return render(request, 'polls/detail.html', {'question': question})
   

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def add_question(request):
   
    if request.method == 'POST':
        form = PollForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse("polls:index"))

    else: 
        form = PollForm()
    
    return render(request, 'polls/add_question.html', {'form': form})

@login_required
def save_poll(request):
 
    newQuestion = Question(question_text= request.POST['question'], pub_date = timezone.now(), user_id=request.user.id)
   
    newQuestion.save()
   
    newQuestion.choice_set.create(choice_text=request.POST['choice_1'], votes =0)
    newQuestion.choice_set.create(choice_text=request.POST['choice_2'], votes =0)
    newQuestion.choice_set.create(choice_text=request.POST['choice_3'], votes =0)
    
    return HttpResponseRedirect(reverse("polls:index"))