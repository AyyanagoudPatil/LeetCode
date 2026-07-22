/* Write your PL/SQL query statement below */
select today.id from Weather today join Weather yestarday on today.recordDate=yestarday.recordDate+1 where today.temperature > yestarday.temperature;