## 클로저 (Closure)

클로저는 자신이 생성될 때의 환경(Lexical environment)을 기억하는 함수입니다



### 클로저 함수의 특징

- 함수를 리턴하는 함수의 형태입니다.
- 클로저는 리턴하는 함수에 의해 스코프(변수의 접근 범위)가 구분됩니다.
- 내부 함수는 외부 함수에 선언된 변수에 접근 가능합니다.
- 함수의 재활용이 가능한 것이 장점입니다.
- 함수를 실행하지 않고 함수 자체를 리턴 할 수 있습니다.



## 커링

하나 이상의 매개변수(Parameter)를 갖는 함수를 부분적으로 나누어 각각 단일 매개변수를 갖는 함수로 설정하는 기법입니다.

```javascript
//예시
//non-curried
function plusFunc(a, b, c){
  console.log(a + b + c);
}

plusFunc(1, 2, 3);   // 6

//curried
function plusFunc(a){
    return function(b){
       return function(c){
          console.log(a + b + c);
       }
    }
}

plusFunc(1)(2)(4);  // 7
```

장점

- 재사용이 가능합니다
- 생산성이 향상됩니다. (코드의 양이 줄어듭니다.)
- 가독성이 좋아집니다.

단점

- 커링을 과용하면 메모리와 속도에 문제점 발생 가능성이 있습니다.





## ES6 주요 문법



### spread 문법

주로 배열을 풀어서 인자로 전달하거나, 배열을 풀어서 각각의 요소로 넣을 때에 사용합니다.

```javascript
let parts = ['shoulders', 'knees'];
let lyrics = ['head', ...parts, 'and', 'toes'];

console.log(lyrics) 
// ['head', 'shoulders', 'knees', 'and', 'toes'];

let obj1 = { foo: 'bar', x: 42 };
let obj2 = { foo: 'baz', y: 13 };

let clonedObj = { ...obj1 };
// clonedObj = { foo: 'bar', x: 42};
let mergedObj = { ...obj1, ...obj2 };
// mergeObj = {foo: 'baz', x:42, y:13}
// 객체에서 사용시 같은 키값이 나열되면 나중에 선언된 값으로 정의되고 선언된 적 없는 키값은 밸류값과 매칭되어 포함됩니다.
```



### 구조분해할당

구조 분해 할당은 spread 문법을 이용하여 값을 해체한 후, 개별 값을 변수에 새로 할당하는 과정을 말합니다.

```javascript
const [a, b, ...arr] = [10, 20, 30, 40, 50];
// arr = [30, 40, 50]
const {one, two, ...obj} = {a: 10, b: 20, c: 30, d: 40}
// obj = {c: 30, d: 40}
```



