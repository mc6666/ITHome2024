from django.urls import path
from . import views

urlpatterns = [
    # 問卷
    path("", views.index, name="index"),
    path("<int:poll_id>/", views.poll_detail, name="poll_detail"),
    path("poll/insert/", views.poll_insert, name="poll_insert"),
    path("poll/update/", views.poll_update, name="poll_update"),
    path("poll/delete/<int:poll_id>/", views.poll_delete, name="poll_delete"),
    path("summary/<int:poll_id>/", views.vote_summary, name="vote_summary"),

    # 問題
    path("question/<int:question_id>/", views.question_detail, name="question_detail"),
    path("question/insert/<int:poll_id>/", views.question_insert, name="question_insert"),
    path("question/update/", views.question_update, name="question_update"),
    path("question/delete/<int:question_id>/", views.question_delete, name="question_delete"),

    # 答案選項
    path("choice/<int:choice_id>/", views.choice_detail, name="choice_detail"),
    path("choice/insert/<int:question_id>/", views.choice_insert, name="choice_insert"),
    path("choice/update/", views.choice_update, name="choice_update"),
    path("choice/delete/<int:choice_id>/", views.choice_delete, name="choice_delete"),
]