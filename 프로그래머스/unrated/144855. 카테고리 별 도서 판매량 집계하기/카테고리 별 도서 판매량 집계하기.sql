SELECT A.CATEGORY AS CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK A
JOIN BOOK_SALES B ON A.BOOK_ID = B.BOOK_ID
WHERE B.SALES_DATE >= "2022-01-01" AND B.SALES_DATE < "2022-02-01"
GROUP BY CATEGORY
ORDER BY CATEGORY