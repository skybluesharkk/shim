-- 코드를 입력하세요
select Round(avg(df),0) as AVERAGE_FEE
from 
(SELECT daily_fee as df
from car_rental_company_car
where car_type = 'SUV') as dfs