## 이미지 삽입, 썸네일 제작

모델 생성

모델 이름 : Article

```python
# model.py
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(300, 240)],
                                format='JPEG',
                                options={'quality': 50})
    #이미지는 입력되는 이미지를 업로드하여 받게하고 공백을 가질 수 있게 한다.
    # 썸네일은 이미지를 기준으로 사이즈 조절과 화질 조절을 하여 불필요하게 많은 용량을 사용하지 않게 한다.
```



```python
# pjt/settings.py
INSTALLED_APPS = [
    'imagekit',
    ...
]

MEDIA_ROOT = BASE_DIR / 'images'
MEDIA_URL = '/media/'
```



```python
# pjt/urls.py
urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



```
pip install django-imagekit
```



이미지 태그에 사진 크기 작성하여 사이즈 조절 할 수도 있음.

특정 사이즈로 변경 설정하여 썸네일로 사용 가능.