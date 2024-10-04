SELECT 
    p.name AS poll_name,
    q.seq_no AS question_number,
    q.question_text,
    c.seq_no AS choice_number,
    c.choice_text,
    COUNT(vr.id) AS vote_count
FROM 
    polls_poll p
JOIN 
    polls_question q ON p.id = q.poll_id
JOIN 
    polls_choice c ON q.id = c.question_id
LEFT JOIN 
    polls_vote_result vr ON c.seq_no = vr.choice_no AND vr.question_id = q.id
JOIN 
    polls_vote v ON v.poll_id = p.id AND v.id = vr.vote_id
GROUP BY 
    p.name, q.seq_no, q.question_text, c.seq_no, c.choice_text
ORDER BY 
    p.name, q.seq_no, c.seq_no;
