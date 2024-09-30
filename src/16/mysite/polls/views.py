from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from dataclasses import dataclass
# from icecream import ic 

@login_required()
def index(request):
    # 取得所有問卷資料，並依發行日期排序
    poll_list = Poll.objects.order_by("-pub_date") 
    context = {"poll_list": poll_list}
    return render(request, "index.html", context)

@login_required()
def poll_detail(request, poll_id):
    # 取得特定問卷資料及所有問題
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, "poll_detail.html", {"poll": poll})

@login_required()
def question_detail(request, question_id):
    # 取得特定問題及所有答案選項
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "question_detail.html", {"question": question})

@login_required()
def choice_detail(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, "choice_detail.html", {"choice": choice})

@login_required()
def poll_insert(request):
    if request.method == "GET":
        return render(request, "poll_insert.html")
    elif request.method == "POST":
        poll = Poll()
        poll.name = request.POST.get("name", "")
        poll.description = request.POST.get("description", "")
        poll.pub_date = request.POST.get("pub_date", "").replace('/','-')
        poll.save()
        return index(request)

@login_required()
def question_insert(request, poll_id):
    if request.method == "GET":
        return render(request, "question_insert.html", {"poll_id": poll_id})
    elif request.method == "POST":
        question = Question()
        poll = get_object_or_404(Poll, pk=poll_id)
        question.poll = poll
        question.seq_no = request.POST.get("seq_no")
        question.question_text = request.POST.get("question_text", "")
        question.is_optional = request.POST.get("is_optional", "") == 'on'
        question.save()
        return poll_detail(request, poll_id)

@login_required()
def choice_insert(request, question_id):
    if request.method == "GET":
        return render(request, "choice_insert.html", {"question_id": question_id})
    elif request.method == "POST":
        choice = Choice()
        question = get_object_or_404(Question, pk=question_id)
        choice.question = question
        choice.seq_no = request.POST.get("seq_no")
        choice.choice_text = request.POST.get("choice_text", "")
        choice.save()
        return question_detail(request, question_id)

@login_required()
def poll_update(request):
    poll_id = request.POST.get("id", "")
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.name = request.POST.get("name", "")
    poll.description = request.POST.get("description", "")
    poll.pub_date = request.POST.get("pub_date", "")
    poll.save()
    return index(request)

@login_required()
def question_update(request):
    question_id = request.POST.get("id", "")
    question = get_object_or_404(Question, pk=question_id)
    poll_id = question.poll.id
    question.seq_no = request.POST.get("seq_no")
    question.question_text = request.POST.get("question_text", "")
    question.is_optional = request.POST.get("is_optional", "") == 'on'
    question.save()
    return poll_detail(request, poll_id)

@login_required()
def choice_update(request):
    choice_id = request.POST.get("id", "")
    choice = get_object_or_404(Choice, pk=choice_id)
    question_id = choice.question.id
    choice.name = request.POST.get("name", "")
    choice.seq_no = request.POST.get("seq_no")
    choice.choice_text = request.POST.get("choice_text", "")
    choice.save()
    return question_detail(request, question_id)

@login_required()
def poll_delete(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return index(request)

@login_required()
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    poll_id = question.poll.id
    question.delete()
    return poll_detail(request, poll_id)

@login_required()
def choice_delete(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    question_id = choice.question.id
    choice.delete()
    return question_detail(request, question_id)

# 問卷調查結果顯示
@dataclass
class Vote_Count:
    choice_no:int # 答案選項
    choice_text:str # 答案選項
    total:int # 票數

@login_required()
def vote_summary(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    question_id = poll.question_set.order_by("-seq_no")[0].id
    summary = Vote_Result.objects.filter(vote__poll__id=poll_id)\
        .filter(question__id=question_id) \
        .values('choice_no').annotate(total=Count('choice_no'))
    
    vote_result = []
    for item in summary:
        choice = get_object_or_404(Choice, seq_no=item['choice_no'], question__id=question_id) 
        vote_count = Vote_Count(choice_no=item['choice_no'],
                                choice_text=choice.choice_text, 
                                total=item['total']
                                )
        vote_result.append(vote_count)
    # ic(vote_result)
    
    
    context = {"poll": poll, "choice_list":choice, "vote_result":vote_result}
    return render(request, "vote_summary.html", context)
