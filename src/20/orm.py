from django.db.models import Count

# Query to get vote summary
vote_summary = (Poll.objects
    .filter(vote__isnull=False)  # Ensures that only polls with votes are considered
    .values('name', 'question__seq_no', 'question__question_text', 'question__choice__seq_no', 'question__choice__choice_text')
    .annotate(vote_count=Count('question__choice__voteresult'))
    .order_by('name', 'question__seq_no', 'question__choice__seq_no')
)

# Example of how to print or use the result
for poll in vote_summary:
    print(f"Poll: {poll['name']}")
    print(f"Question {poll['question__seq_no']}: {poll['question__question_text']}")
    print(f"  Choice {poll['question__choice__seq_no']}: {poll['question__choice__choice_text']} - {poll['vote_count']} votes")
