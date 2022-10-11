## Django Auth를 활용한 회원가입이 가능한 서비스를 개발

### model 생성

```python
# 앱/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
```



### forms 생성

```python
from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UsersForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
```



이전의 CRUD를 사용하는 방법과 다른점은 유사하나 django.contrib.auth에서 필요한 정보들을 가져와서 사용한다.

익숙해질 수 있도록 많은 반복이 필요할 것 같다.


### 예습
#### login, logout 구현
```
urls.py
from django.contrib.auth import views as auth_views

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
```

django.contrib.auth 에 저장되어있는 함수를 쓰므로 현재 위치에서 views에 새로 정의해 줄 필요 X