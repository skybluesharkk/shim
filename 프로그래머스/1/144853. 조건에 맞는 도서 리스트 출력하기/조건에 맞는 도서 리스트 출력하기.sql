-- 코드를 입력하세요
SELECT book.book_id as BOOK_ID, DATE_FORMAT(book.published_date, '%Y-%m-%d') as PUBLISHED_DATE
from book
where book.category = '인문' and year(book.published_date) = '2021'