from django.shortcuts import render, get_object_or_404
from polls.models import *
from django.contrib.auth.decorators import login_required
from django.db import DatabaseError, transaction
from datetime import datetime

def home(request):
    poll_list = Poll.objects.order_by("-pub_date")
    context = {"poll_list": poll_list}
    return render(request, "home.html", context)

@login_required()
def vote(request, poll_id):
    if request.method == "GET": # 顯示輸入表單
        poll = get_object_or_404(Poll, pk=poll_id)
        return render(request, "vote.html", {"poll": poll})
    elif request.method == "POST": # 將表單輸入內容存入資料表
        poll = Poll.objects.get(id=poll_id)
        with transaction.atomic(): # 交易
            vote = Vote(poll=poll, user_id=request.user.username, 
                        fill_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            vote.save()  # 存入Vote資料表      
            question_list = poll.question_set.all().order_by("seq_no")
            for question in question_list:
                choice_no = request.POST.get("q_"+str(question.id), "")
                if choice_no.isdigit():
                    vote_result = Vote_Result(question=question, choice_no=int(choice_no), 
                                            vote=vote) 
                    vote_result.save()  # 存入Vote_Result資料表                                
        return home(request)
        
