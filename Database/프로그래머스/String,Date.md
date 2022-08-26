루시와 엘라 찾기
```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME ='Lucy'or NAME ='Ella'or NAME ='Pickle'or NAME ='Rogan'or NAME ='Sabrina'or NAME ='Mitty'

```

이름에 el이 들어가는 동물 찾기
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' and ANIMAL_TYPE	='Dog'
ORDER BY NAME
```

중성화 여부 파악하기
```sql
SELECT 
    ANIMAL_ID, 
    NAME, 
    CASE 
        WHEN SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE '%Spayed%' 
            THEN 'O'
        ELSE 
            'X'
    END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

오랜 기간 보호한 동물(2)
```sql
SELECT A.ANIMAL_ID, B.NAME
FROM ANIMAL_OUTS A
INNER JOIN ANIMAL_INS B
    ON A.ANIMAL_ID=B.ANIMAL_ID
ORDER BY (A.DATETIME-B.DATETIME) DESC
LIMIT 2
```

DATETIME에서 DATE로 형 변환
```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS "날짜"
FROM ANIMAL_INS
```

