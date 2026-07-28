/* Write your PL/SQL query statement below */
select user_id, count(*) prompt_count, round(avg(tokens),2) avg_tokens
from Prompts 
group by user_id 
having count(*)>=3 and max(tokens)>avg(tokens)
order by avg(tokens) desc, user_id ;