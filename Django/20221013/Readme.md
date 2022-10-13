## 1. 회원정보수정

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
class CustomUserChangeForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = get_user_model()
```

forms.py에 django.contrib.auth.forms에서 UserChangeForm을 불러와 사용

Meta 클래스 선언 이후 model을 get_user_model()로 선언해주고 사용할 필드 지정



```python
def update(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(request.POST, instance=request.user)
		# form = CustomUserChangeForm(data=request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('articles:index')
	else:
		form = CustomUserChangeForm(instance=request.user)
	context = {
		'form': form,
	}
	return render(request, 'accounts/update.html', context)
```

request의 user 정보를 이용하면 pk 값을 이용하여 models에서 값을 가져올 필요 없이 현재 값들을 가져 올 수 있으므로 instance를 활용해 주면 된다.



## 2.비밀번호 변경

```python
# accounts/views.py
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
    	pass
    else:
   	 form = PasswordChangeForm(request.user)
    context = {
    	'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

django.contrib.auth.forms에서 PasswordChangeForm을 불러와 사용한다.(따라 지정해 줄 필요 X)