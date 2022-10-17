# 1. 프로젝트 진행 순서 및 참고

### 1. github 공유 repository 생성 및 프로젝트 생성

#### 1. repository생성

#### 2. repository에 공동 작업자 초대

#### 3. commit & push 진행, 공동 작업자들은 저장소 clone 수행



### 2. 장고 개발환경 설정

#### 1. 가상 환경 생성

#### 2. 패키지 목록 저장

#### 3. 프로젝트 생성

#### 4. 브랜치 생성하여 commit하고 push 한 후 merge 실행한 후 master 브랜치로 옮기고 브랜치 삭제

```
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치 이름 변경
git branch -m [기존 브랜치명] [변경할 브랜치명]
```

merge는 github에서 실행 가능



### 3. 회원가입

#### 1. 앱 생성

```terminal
$ python manage.py startapp accounts
```

#### 2. 앱 등록

#### 3. 모델 생성

```python
# 모델은 Django AbstractUser 모델 상속
# models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
# AbstractUser유저를 상속하여 쓸 것이므로 수정해 줄 필요X 
```



#### 4.폼 생성

```python
# UserCreationForm을 상속 받아서 CustomUserCreationForm 작성
#forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]
```



#### 5. 회원가입 기능 구현

##### 5-1. url 설정

````python
# urls.py
urlpatterns = [
    path("index/", views.index, name="index"),
]
````



##### 5-2. 함수 구현

```python
# views.py
from django.contrib.auth import get_user_model

def index(request):
    account_list = get_user_model().objects.order_by("-id")

    context = {"account_list": account_list}
    return render(request, "accounts/index.html", context)
```

##### 5-2. 화면 구현



#### 6. 브랜치 생성하여push 한 후 merge 실행하고브랜치 삭제



### 4. 로그인, 로그아웃 구현

#### 1. url 등록

#### 2. 함수 등록

```python
# views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("reviews:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:main")
```

django에 내장된 auth 아래 forms에서 AuthenticationForm을 불러와 폼을 사용하고 auth에서 login과 logout을 불러와 사용했습니다.



#### 3. 화면 구현



### 5. 회원 목록 조회, 회원 정보 조회

#### 1. url 추가

```python
# urls.py
urlpatterns = [
    ...
    path("<int:pk>/detail/", views.detail, name="detail"),
]
```



#### 2. 기능 구현

```python
# views.py
def detail(request, pk):
    account_detail = get_user_model().objects.get(pk=pk)

    context = {"account_detail": account_detail}

    return render(request, "accounts/detail.html", context)
```

#### 3. 중간 꾸미기 작업 시행



### 6. 회원 정보 수정 

#### 1. 폼에  CustomUserChangeForm 추가

```python
# forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
```



#### 2. url 추가

```python
# urls.py
urlpatterns = [
    ...,
	path("<int:pk>/detail/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
]
```



#### 3. 기능 구현

```python
# views.py
def detail(request, pk):
    account_detail = get_user_model().objects.get(pk=pk)

    context = {"account_detail": account_detail}

    return render(request, "accounts/detail.html", context)

def update(request, pk):
    update_user = get_user_model().objects.get(pk=pk)
    if request.method == "POST":
        update_form = CustomUserChangeForm(request.POST, instance=update_user)
        if update_form.is_valid():
            update_form.save()
            return redirect("accounts:detail", update_user.pk)
    else:
        update_form = CustomUserChangeForm(instance=update_user)
    context = {"update_form": update_form}
    return render(request, "accounts/update.html", context)
```

#### 4. 화면구현 



### 7. 네브바 구현

- 로그인 되어있는 계정이 다른 회원 정보 수정 막음.

#### 1. url 추가

```python
# urls.py
urlpatterns = [
    ...
    path('diff/', views.diff, name='diff'),
]
```



#### 2. 함수 추가

```python
# views.py
def update(request, pk):
        if request.user.pk == pk:
        if request.method == "POST":
            update_form = CustomUserChangeForm(request.POST, instance=request.user)
            if update_form.is_valid():
                update_form.save()
                return redirect("accounts:detail", request.user.pk)
        else:
            update_form = CustomUserChangeForm(instance=request.user)
        context = {"update_form": update_form}
        return render(request, "accounts/update.html", context)
    else:
        return render(request, 'accounts/diff.html')

def diff(request):
    return render(request, 'accounts/diff.html')
```



#### 3.화면구현

- base.html에 navbar 구현
- 로그인 유무 확인하여 로그인, 회원가입 버튼과 계정, 로그아웃 버튼이 보이도록 구분
- 리뷰보기 버튼 생성
- 로그인한 상태라면 글쓰기 버튼 보이게함
- 리뷰보기, 글쓰기 버튼은 기능 구현 전이므로 연결 주소 비워둠.



### 8. review 앱 추가, 생성 기능 추가

#### 1. 회원 목록 로그인 상태에서만 볼 수 있도록 수정

```python
#views.py

@login_required
def index(request):
    account_list = get_user_model().objects.order_by("-id")
```



#### 2. 앱추가, 등록, 도메인 추가

#### 3. 모델, 폼추가

```python
# models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# fomrs.py
from django import forms
from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'movie_name', 'grade']

        labels = {
            'title' : '리뷰 제목',
            'content' : '리뷰 내용',
            'movie_name' : '영화 제목',
            'grade' : '영화 평점'
        }
```



#### 4. url 추가

#### 5. 함수 추가

#### 6. 화면 구현

#### 7. 중간 꾸미기 실행



### 9. 리뷰 글 상세정보 추가

#### 1. url 등록

#### 2. 함수 등록

#### 3. 페이지 구현



### 10. 리뷰 글 수정, 삭제 추가

#### 1. url 등록

#### 2. 함수 등록

#### 3. 페이지 구현

#### 4. 중간 꾸미기



### 11. 최종 꾸미기 작업, 마무리



# 2. 소감

능력을 파악하고 작업을 분배하지 않고 작업량을 균등하게 분배한 탓인지 기본적인 기능을 구현하는데 시간이 쫓겨서 기본적으로 제시된 요구 기능들을 제외하고 다른 기능을 추가할 여유가 없었습니다. 작업을 시작하기에 앞서 짧게라도 각자의 능력을 파악하는 시간과 그에 따른 작업 영역을 분배하는것이 필요하겠다고 느꼈습니다. 

로그인, 로그아웃 부분이 아직 숙지가 미흡해 조금 더 반복 수행해보며 확실하게 숙지할 필요가 있겠다고 느꼈습니다.
