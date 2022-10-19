### 목표

게시글과 댓글이 1 : N 관계로 매핑 된 게시글에 댓글을 작성할 수 있는 서비스를 개발합니다.



### 요구사항

#### 모델 Model

모델 이름 : Article

모델 필드

| 필드 이름 | 역할    | 필드 | 속성          |
| --------- | ------- | ---- | ------------- |
| title     | 글 제목 | Char | max_length=80 |
| content   | 글 내용 | Text |               |



모델 이름: Comment

모델 필드

| 필드 이름 | 열할        | 필드       | 속성                     |
| --------- | ----------- | ---------- | ------------------------ |
| article   | 참조 게시글 | ForeignKey | on_delete=models.CASCADE |
| content   | 댓글 내용   | Char       | max_length=80            |



### 사용 코드

```python
#articles/models.py
class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

글이 삭제되면 댓글도 같이 삭제하도록 해줍니다.



```python
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

댓글은 본문 안에 들어가므로 입력값을 받아 변수에 저장한 다음 article(본문 글)에 붙여줍니다.



### 소감

댓글은 그 자체로 값을 가지는 것이 아니고 본 문 글에 영역을 가지고 존재한다는 특성을 잘 기억해야 될 것 같습니다.