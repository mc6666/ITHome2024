from django.db import models

# 問卷
class Poll(models.Model):
    name = models.CharField(max_length=50) # 問卷名稱
    description = models.TextField()       # 問卷摘要
    pub_date = models.DateTimeField("date published") # 問卷發行日期
    
# 問題
class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    seq_no = models.IntegerField(default=1) # 序號
    question_text = models.CharField(max_length=200) # 問題說明
    is_optional = models.BooleanField(default=False) # 是否為選擇性問題

# 答案選項
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    seq_no = models.IntegerField(default=1) # 序號
    choice_text = models.CharField(max_length=200) # 答案選項說明


# 問卷調查
class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE) # 填寫問卷
    user_id = models.CharField(max_length=20)            # 使用者代碼
    fill_date = models.DateTimeField("date filled") # 填寫日期
    
# 問卷調查結果
class Vote_Result(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE) # 填寫使用者及問卷
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   # 填寫問題
    choice_no = models.IntegerField(default=1) # 答案選項序號
    

