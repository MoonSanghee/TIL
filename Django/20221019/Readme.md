### 목표

1. ModelForm을 활용한 CRUD 기능 구현
2. Django Model 1 : N 관계에 대해 이해하고, 코드 상에서 두 모델 매핑하기
3. Django Auth를 활용한 회원 관리 기능 개발에 대한 흐름 파악 및 개발
4. 로그인 상태에 따라 컴포넌트 출력 및 기능 제한



### 요구사항

#### 모델 Model

- 모델 이름 : User

  Django AbstractUser 모델 상속

- 모델 이름 : Article

  모델 필드

  | 필드이름 | 역할      | 필드       | 속성                    |
  | -------- | --------- | ---------- | ----------------------- |
  | user     | 글 작성자 | ForeignKey | on_delete=model.CASCADE |
  | title    | 글 제목   | Char       | max_length=80           |
  | content  | 글 내용   | Text       |                         |



#### 폼 Form

- 로그인

  Django 내장 로그인 폼 AuthenticationForm 활용





### 사용 코드

참조 예

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/form.html', context)
```

입력값을 다른 변수에 저장했다가 request의 유저 pk값을 폼과 묶어 글 정보에 저장함으로써 글에 유저 정보를 더해 줄 수 있음.



역참조 예

```html
account_detail.article_set.count
```

글정보중 작성 계정의 정보가 일치하는 값을 가져옴.



### 소감

오타로 인한 오류 발생이 너무 많이 발생했습니다. 코드 작성이 조금 느려지더라도 정확한 코드를 입력하도록 할 필요가 있다 느꼈습니다.

프로젝트 시작부터 작업을 시작해보았는데 기초적인 부분에서 모델 생성하고 서버 돌리는데 까지도 많은 오류를 만났습니다. 아직도 기초가 부족한 부분이 많음을 느꼈습니다.

이미지 파일을 저장할 수 있게 해주는데 많은 오류를 만났습니다. 세팅에 추가해 주는 부분이 많은 만큼 더 헛깔리는듯합니다. 반복적으로 숙지하는 노력이 필요하다고 느꼈습니다.