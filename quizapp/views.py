import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Question, Option, UserQuestion
from . import utils


# Create your views here.

def home(request):
    sections = Category.objects.all()

    return render(request, 'quizapp/home.html', {'sections': sections})


# def category(request, section):
#    categories = Category.objects.filter(section__name=section)
#    return render(request, 'quizapp/category.html', {'categories':categories})

def question(request, category_id):
    context = {'category_id': category_id}
    question_number = 0

    
    if request.method == 'GET': [quest.save() for quest in utils.load_questions(category_id)]

    if request.method == 'POST':
        question_number = int(request.POST['question-number'])
        # asynchronous
        # better to use -1 to show it is an unanswered question
        selected_option_id = int(request.POST.get('option', "-1"))

        question_info = UserQuestion.objects.get(question_no=question_number)
        question_info.selected_option_id = selected_option_id

        question_info.save()
        
    question_left = UserQuestion.objects.filter(selected_option_id=0).count()
    if question_left:
        question = UserQuestion.objects.get(question_no=question_number + 1)
        options = list(Option.objects.filter(question_id=question.question_id))

        random.shuffle(options)
        context['question_info'] = question
        context['options'] = options

    else:
        context['done'] = 'done'

    return render(request, 'quizapp/question.html', context)


def result(request):
    correct_answer_count = 0

    questions_asked = list(UserQuestion.objects.all())
    correct_answers = Option.objects.filter(question__in=map(lambda quest: quest.question, questions_asked)).filter(
        correct=True).values_list('id', flat=True)

    for question in questions_asked:
        if question.selected_option_id in correct_answers: correct_answer_count += 1

    return render(request, 'quizapp/result.html', {'correct': correct_answer_count, 'amount': len(questions_asked)})


def review(request):
    context = {'review': True}

    question_number = (int(request.POST['question-number']) if request.method == 'POST' else 0)+1

    #Check if the question number exceeds the total in the DB
    #total_questions = UserQuestion.object.count()
    #if question_number == total_questions: return redirect()


    question = UserQuestion.objects.get(question_no=question_number)
    
    options = Option.objects.filter(question_id=question.question_id)
    correct_answer = options.get(correct=True)
    
    
    #Some options might be -1 when the user did not pick an answer, and since -1 is not present
    #in the Options db, it could lead to an error
    try:
        chosen_answer = options.get(id=question.selected_option_id)
    except Option.DoesNotExist:
        chosen_answer = None


    context['question_info'] = question
    context['options'] = options
    context['chosen_answer'] = chosen_answer
    context['correct_answer'] = correct_answer

    return render(request, 'quizapp/review.html', context)
