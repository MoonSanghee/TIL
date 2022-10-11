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