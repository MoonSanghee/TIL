## 고차함수



## 일급 객체

다른 객체들에 일반적으로 적용 가능한 연산을 모두 지원하는 객체를 칭합니다.

특징

- 변수에 할당(assignment) 할 수 있습니다
- 다른 함수의 전달인자(argument)로 전달될 수 있습니다.
- 다른 함수의 결과로서 리턴될 수 있습니다.



## 고차함수

함수를 전달인자로 받을 수 있고, 함수를 리턴하는 함수입니다.

다른 함수의 전달인자로 전달되는 함수를 콜백 함수라고합니다.

다른 함수를 인자로 받는 경우

```javascript
function double(num) {
  return num * 2;
}

function doubleNum(func, num) {
  return func(num);
}

/*
 * 함수 doubleNum은 다른 함수를 인자로 받는 고차 함수입니다.
 * 함수 doubleNum의 첫 번째 인자 func에 함수가 들어올 경우
 * 함수 func는 함수 doubleNum의 콜백 함수입니다.
 * 아래와 같은 경우, 함수 double은 함수 doubleNum의 콜백 함수입니다.
 */
let output = doubleNum(double, 4);
console.log(output); // -> 8
```

함수를 리턴하는 경우

```javascript
function adder(added) {
  return function (num) {
    return num + added;
  };
}

/*
 * 함수 adder는 다른 함수를 리턴하는 고차 함수입니다.
 * adder는 인자 한 개를 입력받아서 함수(익명 함수)를 리턴합니다.
 * 리턴되는 익명 함수는 인자 한 개를 받아서 added와 더한 값을 리턴합니다.
 */

// adder(5)는 함수이므로 함수 호출 연산자 '()'를 사용할 수 있습니다.
let output = adder(5)(3); // -> 8
console.log(output); // -> 8

// adder가 리턴하는 함수를 변수에 저장할 수 있습니다.
// javascript에서 함수는 일급 객체이기 때문입니다.
const add3 = adder(3);
output = add3(2);
console.log(output); // -> 5
```



함수를 인자로 받고, 함수를 리턴하는 경우

```javascript
function double(num) {
  return num * 2;
}

function doubleAdder(added, func) {
  const doubled = func(added);
  return function (num) {
    return num + doubled;
  };
}

/*
 * 함수 doubleAdder는 고차 함수입니다.
 * 함수 doubleAdder의 인자 func는 함수 doubleAdder의 콜백 함수입니다.
 * 함수 double은 함수 doubleAdder의 콜백으로 전달되었습니다.
 */

// doubleAdder(5, double)는 함수이므로 함수 호출 기호 '()'를 사용할 수 있습니다.
doubleAdder(5, double)(3); // -> 13

// doubleAdder가 리턴하는 함수를 변수에 저장할 수 있습니다. (일급 객체)
const addTwice3 = doubleAdder(3, double);
addTwice3(2); // --> 8
```



#### 내장 고차함수

- filter

  특정 조건을 만족한 요소만 걸러냅니다.

```javascript
// 함수 표현식
const isEven = function (num) {
  return num % 2 === 0;
};

let arr = [1, 2, 3, 4];
// let output = arr.filter(짝수);
// '짝수'를 판별하는 함수가 조건으로서 filter 메서드의 전달인자로 전달됩니다.
let output = arr.filter(isEven);
console.log(output); // ->> [2, 4]

const isLteFive = function (str) {
  // Lte = less then equal
  return str.length <= 5;
};

arr = ['hello', 'code', 'states', 'happy', 'hacking'];
// output = arr.filter(길이 5 이하)
// '길이 5 이하'를 판별하는 함수가 조건으로서 filter 메서드의 전달인자로 전달됩니다.
let output = arr.filter(isLteFive);
console.log(output); // ->> ['hello', 'code', 'happy']
```



- map

  하나의 데이터를 다른 데이터로 매핑할 때 사용합니다.

```javascript
// 만화책 모음
const cartoons = [
  {
    id: 1,
    bookType: 'cartoon',
    title: '식객',
    subtitle: '어머니의 쌀',
    createdAt: '2003-09-09',
    genre: '요리',
    artist: '허영만',
    averageScore: 9.66,
  },
  {
    id: 2,
    // .. 이하 생략
  },
  // ... 이하 생략
]; 

// 만화책 한 권의 부제를 리턴하는 로직(함수)
const findSubtitle = function (cartoon) {
  return cartoon.subtitle;
}; 

// 각 책의 부제 모음 
const subtitles = cartoons.map(findSubtitle); // ['어머니의 쌀', ...]
```



- reduce

  배열의 각 요소(1)에 대해 주어진 함수(2)를 실행하고, 하나의 결과값(3)을 반환(4)합니다.

```javascript
// 단행본 모음
const cartoons = [
  {
    id: 1,
    bookType: 'cartoon',
    title: '식객',
    subtitle: '어머니의 쌀',
    createdAt: '2003-09-09',
    genre: '요리',
    artist: '허영만',
    averageScore: 9.66,
  },
  {
    id: 2,
    // .. 이하 생략
  },
  // ... 이하 생략
];

// 단행본 한 권의 평점을 누적값에 더한다.
const scoreReducer = function (sum, cartoon) {
  return sum + cartoon.averageScore;
}; 

// 초기값에 0을 주고, 숫자의 형태로 평점을 누적한다.
let initialValue = 0 
// 모든 책의 평점을 누적한 평균을 구한다.
const cartoonsAvgScore = cartoons.reduce(scoreReducer, initialValue) / cartoons.length;
```



## 추상화

복잡한 어떤 것을 압축해서 핵심만 추출한 상태로 만드는 것입니다.

함수를 통해 얻은 추상화를, 한 단계 더 높인 것이 고차 함수입니다.

- 값 수준의 추상화: 단순히 값(value)을 전달받아 처리하는 수준
- 사고의 추상화: 함수(사고의 묶음)를 전달받아 처리하는 수준

즉, 고차 함수를 통해, 보다 높은 수준에서 생각할 수 있습니다.

- 고차 함수 = 함수를 전달받거나 함수를 리턴한다 = 사고(함수)에 대한 복잡한 로직은 감추어져 있다 = 사고 수준에서의 추상화

추상화의 수준이 높아지는 만큼, 생산성도 비약적으로 상승합니다.
