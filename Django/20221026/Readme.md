## 목표

댓글과 좋아요. JavaScript 이용하여 비동기화 처리



### 좋아요

```python
# articles/views.py
from django.http import JsonResponse

def likes(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.user in article.like_user.all():
        article.like_user.remove(request.user)
        is_liked = False
    else:
        article.like_user.add(request.user)
        is_liked = True
    context = {'isLiked': is_liked, 'likeCount': article.like_user.count()}
    return JsonResponse(context)
```

JsonResponse를 django.http에서 불러와 Json을 리턴해주고 템플릿에서 JavaScript에 사용할 수 있도록 반환



```html
<!--  articles/detail.html -->
    <i id="like-btn" data-article-id="{{ article.pk }}" class="bi bi-heart-fill fs-4" style="color: rgb(255, 29, 29);"></i>
```

아이콘에 data-article-id 값을 넣어주고 JS에서 사용할 id값을 정해줌.



```javascript
// JavaScript
<script>
  const likeBtn = document.querySelector('#like-btn')
  likeBtn.addEventListener('click', function (event) {
    console.log(event.target.dataset)
    axios({
      method: 'get',
      url: `/articles/${event.target.dataset.articleId}/likes/`
    })
    .then(response => {
      console.log(response)
      console.log(response.data)
      if (response.data.isLiked === true) {
        event.target.classList.add('bi-heart-fill')
        event.target.classList.remove('bi-heart')
      } else {
        event.target.classList.add('bi-heart')
        event.target.classList.remove('bi-heart-fill')
      }
      const likeCount = document.querySelector('#like-count')
      likeCount.innerText = response.data.likeCount
    })
  })

</script>
```

좋아요를 실행하기 위해 id 값을 준 부분을 찾아 변수에 저장해주고 'click' 이벤트를 추가하여줌.

axios의 url을 입력할때는 `(backtic 백틱)사이에 값을 넣어줌.

isLiked 값에 따라 표현되는 방식을 다르게 클래스에 정의하여 표현되는 방식을 바꾸어줌.



### 댓글

```javascript
// JavaScript
<script>
  const commentForm = document.querySelector('#comment-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  commentForm.addEventListener('submit', function (event) {
    event.preventDefault();
    axios({
      method: 'post',
      url: `/articles/${event.target.dataset.articleId}/comments/`,
      Headers: {'X-CSRFToken': csrftoken},
      data: new FormData(commentForm)
    })
    .then(response => {
      console.log(response.data)
      const comments = document.querySelector('#comments')
      const p = document.createElement('p')
      p.innerText = `${response.data.userName} | ${response.data.content}`
      const hr = document.createElement('hr')
      comments.append(p, hr) 
      commentForm.reset()
    })
  })

</script>
```

csrftoken 값도 지정해주어야함.

axios에 

Headers: {'X-CSRFToken': csrftoken} 으로 토큰 입력

data: new FormData(commentForm) 으로 입력 폼 저장

commentForm.reset() 사용한 폼은 비워줌.





## 소감

여러 페이지에 걸쳐 작업이 진행되므로 변수명을 헛깔리지 않도록 주의해야할 것 같습니다.

!!!!오타!!! 코드가 길어지면서 오타가 나오면 디버깅이 어려움. 조금 더 진정하고 실수를 줄이며 작업할 수 있도록 해야할 것 같습니다.