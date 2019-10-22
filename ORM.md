# SQL과 django ORM

## 기본 준비 사항

* https://bit.do/djangoorm에서 csv 파일 다운로드

* django app

  * `django_extensions` 설치

  * `users` app 생성

  * csv 파일에 맞춰 `models.py` 작성 및 migrate

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users
    sqlite > SELECT COUNT(*) FROM users;
    ```



## 문제

> 아래의 문제들을 sql문과 대응되는 orm을 작성 하세요.

##### 기본 CRUD 로직

1. 모든 user 레코드 조회

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. user 레코드 생성

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

3. 해당 user 레코드 조회

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

4. 해당 user 레코드 수정

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

5. 해당 user 레코드 삭제

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

### 조건에 따른 쿼리문

1. 전체 인원수 

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 나이가 30인 사람의 이름

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 나이가 30이면서 성이 김씨인 사람의 인원 수

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

4. 지역번호가 02인 사람의 인원 수

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

5. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```



### 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람 10명

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 잔액이 적은 사람 10명

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 성, 이름 내림차순 순으로 5번째 있는 사람

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```



### 표현식

1. 전체 평균 나이

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 30대의 평균 나이

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 계좌 잔액이 가장 높은 user

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

4. 계좌 잔액 총액

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```