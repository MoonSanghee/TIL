없어진 기록 찾기
```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
WHERE ANIMAL_ID NOT IN (SELECT B.ANIMAL_ID
                       FROM ANIMAL_INS B)
```

있었는데요 없었습니다
```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
    ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE A.DATETIME < B.DATETIME
ORDER BY B.DATETIME
```

오랜 기간 보호한 동물(1)
```sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                      FROM ANIMAL_OUTS)
ORDER BY DATETIME
LIMIT 3
```

보호소에서 중성화한 동물
```sql
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
    ON A.ANIMAL_ID=B.ANIMAL_ID 
WHERE A.SEX_UPON_OUTCOME<>B.SEX_UPON_INTAKE
ORDER BY ANIMAL_ID
```
