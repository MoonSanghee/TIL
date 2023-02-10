## DOM

Document Object Model의 약자로, HTML 요소를 Object(JavaScript Object)처럼 조작(Manipulation)할 수 있는 Model입니다.



#### DOM 다루기 



#### CRUD - CREATE, READ, UPDATE, DELETE + APPEND

Read

```javascript
const all Divs = document.getElementsByTagName('div');
// 모든 div 태그 선택
const helloElement = document.getElementById('hello');
// id가 hello인 태그 선택
const hiClassElement = document.getElementsByClassName('hi');
// class가 hi인 태그 선택
const allDivs = document.querySelectorAll('변수');
// '변수'에 'div' 입력시 모든 div 태그 선택, 
// '변수'에 '.hi' 입력시 hi 태그 선택
// '변수'에 '#hello' 입력시 id가 hello인 태그 선택 
```

\* querySelectorAll을 사용하여 조회한 HTML 요소들은 배열처럼 for문을 사용하실 수 있습니다.

\*\*  그러나 조회한 HTML 요소들은 배열이 아닙니다!!! 정식 명칭은 Array-like Object이고 유사 배열, 배열형 객체 등 다양한 이름으로 불립니다.



Create

```javascript
const newDivElement = document.createElement('div');
const newAnchorElement = document.createElement('a');
```



Append

```javascript
const newDivElement = document.createElement('div');
document.body.append(newDivElement);
// body 태그의 자식으로 div 태그 생성

const newDivElement2 = document.createElement('div');
newDivElement.appendChild(newDivElement2);

// append 메서드를 활용하면 노드 객체(Node object)나 DOMString(text)를 사용할 수 있습니다. 또한 한번에 여러 개의 자식 요소를 설정할 수 있습니다.
// append 메서드는 return 값을 반환하지 않습니다.

// appendChild 메서드는 append 메서드와는 다르게 오직 Node 객체만 받을 수 있습니다. 그리고 한번에 오직 하나의 노드만 추가할 수 있습니다.
```



Update

```javascript
const mainElement = document.querySelector('main');
const newDivElement = document.createElement('div');

newDivElement.textContent = '<h1>HELLO!!</h1>';
// newDivElement.innerHTML = '<h1>HELLO!!</h1>';
// newDivElement.innerTEXT = '<h1>HELLO!!</h1>';

newDivElement.classList.add('new-div');
// newDivElement.classList.add('new-div2');

newDivElement.style.color = 'red';
// ~~more style~~

mainElement.appendChild(newDivElement);
// body 태그의 자식으로 div 태그 생성
```



```javascript
const mainElement = document.querySelector('main');
const newDivElement = document.createElement('div');

newDivElement.innerHTML = '<h1>HELLO!!</h1>';

newDivElement.remove();
```