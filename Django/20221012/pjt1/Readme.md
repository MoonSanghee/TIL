## 회원가입, 로그인. 로그아웃

### 0. 모델, 폼 정의

```python
# model.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

# forms.py
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
```

model.py에 AbstractUser 모델을 상속하여 모델 등록

사용할 필드만 정의하여 form 정의 (password는 기본으로 등록됨)

model.py에 from django.contrib.auth.models import AbstractUser, forms.py에

### 1. 회원가입

urls.py에 도매인 등록 -> views.py에 함수 등록 -> templates에 페이지 생성

```python
# urls.py
    path('signup/', views.signup, name='signup'),

# views.py
def signup(request):
    if request.method == 'POST':
        # 입력 메서드 확인
        form = UserForm(request.POST)
        if form.is_valid():
            # 입력 값이 메서드이고 전부 사용 가능하면
            form.save()
            return redirect('accounts:home')
	        # 저장하고 홈으로반환
    else:
        form = UserForm()
    context = {
        'form': form
    }
    # 메서드가 아니라면 빈 폼을 반환
    return render(request, 'accounts/signup.html', context)
	# render로 반환시 도매인주소
    # redirect로 설정해둔 이름으로 return 설정을 해줘야함.
```



### 2. 로그인, 로그아웃

urls.py에 도매인 등록 -> views.py에 함수 등록 -> templates에 페이지 생성

```python
# urls.py
    path('login/', views.login, name='login'),
# views.py
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# urls.py
    path('logout/', views.logout, name='logout'),
# views.py
def logout(request):
    auth_logout(request)
    return redirect('accounts:home')
```

