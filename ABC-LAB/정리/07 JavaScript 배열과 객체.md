## JavaScript 배열과 객체

### 배열

순서가 있는 값을 저장할 때 쓰이는 자료구조입니다.

```javascript
let arr = new Array();
let arr = [];
// 위와 같이 두 가지 방법으로 빈 배열을 생성할 수 있고
let fruits = ["사과", "오렌지", "자두"];
// 안에 값을 넣어주어 순서가 있는 배열을 만들 수 있습니다.
```

각 배열 요소엔 **0부터 시작하는 숫자(인덱스)**가 매겨져 있습니다. 



배열은 typeof로 확인시 object로 표시되기 때문에 Array.isArray 메서드를 이용하여 값이 배열인지 확인 할 수 있습니다.

```javascript
let arr = [1, 2, 3]
// console.log(Array.isArray(arr)) => true
let fruit = 'apple'
// console.log(Array.isArray(fruit)) => false
```



 ### 배열에 사용되는 메서드

- push : 배열의 마지막에 새로운 요소를 추가. **변경된 배열의 길이를 반환 **

- pop :배열의 마지막 요소를 제거.**제거한 요소를 반환 **

- reverse : 배열의 순서를 뒤바꿈.**뒤바뀐 배열을 반환함**

  ```javascript
  const arr = [10, 20, 30];
  arr.push(40);//4|arr =>[10, 20, 30, 40]
  arr.pop();//40|arr =>[10, 20, 30]
  arr.reverse();//[30,20,10]
  ```

- shift : 배열의 첫 번째 요소를 제거, **제거한 요소를 반환**

- unshift :배열의 첫 번째 자리에 새로운 요소 추가.**변경된 배열의 길이 반환**

  ```javascript
  const arr = [10, 20, 30];
  arr.shift(); // 10| arr => [20, 30]
  arr.unshift(0); // 3 | arr => [0, 20, 30]
  ```

- splice :배열 요소를 삭제,교체 또는 추가함.**제거된 요소들을 배열로 반환**

  ```javascript
  const arr = [1, 2, 3, 4, 5];
  const arr1 = [1, 2, 3, 4, 5, 6];
  const arr2 = [1, 2, 3, 4];
  const arr3 = [1, 2, 3];
  arr.splice(2); // index2를 포함하여 모두 삭제 arr =>[1, 2]/return=>[3, 4, 5]
  arr1.splice(-2,3,10,20);
  // 마지막에서 두번째 인자를 포함하여 두개까지만 가능하기 때문에 2개를 삭제 후
  // 10,20인자를 추가 arr =>[1, 2, 3, 4, 10, 20] / return => [5, 6]
  arr2.splice(1,0,100);
  // index1위치에 100을 추가 arr => [1, 100, 2, 3, 4] / return => []
  arr3.splice(1,1,100);
  //index1 요소를 삭제하고, 100을 추가 arr =>[1, 100, 3] / return [2]
  ```

- isArray : 들어온 인자가 Array인지 판단 

- at :index를 인자로 받아 해당 인자에 해당하는 요소를 반환

- length :요소들의 개수를 반환

  ```javascript
  const arr =[1,2,3,4,3,2];
  
  Array.isArray(str);//false
  Array.isArray(arr);//true
  
  arr.at(-1);//2(arr[arr.length - 1]와 같음 ) 
  arr.length //6 
  ```

- includes : 배열이 특정 요소를 포함하고 있는지 확인 join :배열이 모든 요소를 연결해 하나의 문자열로 만듦 (인자를 넣지 않을 경우 “,”) 

  \*원시값들만들 요소로 가진 배열에서 이용하세요!

  ```javascript
  const arr =["안녕","하세","요",null,undefined,"?"]; 
  console.log(arr.join());//안녕,하세,요,,,? 
  console.log(arr.join(""));//안녕하세요? 
  console.log(arr.includes("하세"));//true
  ```

- find(callback) : 주어진 판별 함수를 만족하는 첫 번째 요소의 값을 반환 (없을 경우 undefined) findIndex(callback):주어진 판별 함수를 만족하는 첫 번째 요소의 인덱스 반환 (없을 경우 -1)

  \*콜백함수 :간단하게 다른 함수에 매개변수로 넘겨준 함수. 매개변수로 넘겨받은 함수는 일단 넘겨받고,때가 되면 나중에 호출(calledback)

  ```javascript
  배열.find((현재 처리중인 요소[,현재 index [,배열]])=> 찾을 요소의 조건)
  배열.findIndex((현재 처리중인 요소[,현재 index [,배열]])=> 찾을 요소의 조건)
  
  const user = [{name : 'Kim', age : 13}, 
                {name : 'Lee', age : 32}, 
                {name : 'Park', age : 40}]
  //arrowfunction(많이 쓰는 방식 ) 
  users .find((user)=> user .age >30); 
  //{name:"Lee",age:32} 
  users.findIndex((user)=> user.age >30); //1 
  users.find((user)=> { return user.age >30 ; }); 
  users.findIndex((user)=> { return user.age >30 ; }); 
  //function 
  users.find (function (user){ return user.age >30 ; }) 
  users.findIndex (function (){ return user.age >30 ; })
  ```

- filter(callback) : 조건이 true인 요소로 이루어진 새로운 배열.모두 false인 경우 빈 배열 반환

  ```javascript
  const users =[ { name: "kim", age: 13, },
                { name: "lee", age: 32, },
                { name: "park", age: 40, }, ];
  users.filter((user)=> user.age >30); //[{name:'lee',age:32},{name:'park',age:40}]
  ```

- forEach(callback) :배열 요소 각각에 대해서 callback실행 (for문과 비슷한 개념)반환값 없음 (undefined)

  ```javascript
  배열.forEach((현재 처리중인 요소[,현재 index [,배열]])=> {실행문 })
  
  const arr =[1,2,3,4]; 
  arr.forEach((item)=> { console.log(item); }); 
  arr.forEach((item)=> console.log(item));
  ------
  1
  2
  3
  4
  ```

- map(callback) :배열의 모든 요소에 각각 실행문을 호출한 결과를 모아 새로운 배열 반환

  ```javascript
  배열.map((현재 처리중인 요소[,현재 index[,배열]])=> {실행문})
  const arr =[1,2,3,4,5,6]; 
  
  //2를 곱한 값들을 구해보자 
  const twiceArr =arr.map((item)=> item *2); 
  //[2,4,6,8,10,12]; 
  
  const mapEvenArr =arr.map((item)=> { if (item %2 ===0)return item; });
  // [ undefined, 2, undefined, 4, undefined, 6 ]
  
  const filterEvenArr =arr.map((item)=> { if (item %2 ===0)return item; }).filter(Boolean)
  // [ 2, 4, 6 ]
  ```

- reduce(callback) :배열의 각 요소에 대해 주어진 리듀서 함수를 실행하고,하나의 결과값을 반환 (초기값이 없는 경우 배열의 첫번째 요소를 초기값으로.빈 배열일 경우 오류 발생)

  ```javascript
  배열.reduce((누산기,현재 처리중인 요소[,현재 index[,배열]])=> {실행문,반환}[,초기값])
  
  const result = arr.reduce((acc,cur) => {
  if (cur % 2 ===0)
  return acc + cur *3;
  else return acc +
  cur *2;},0);
  
  // console.log(result) => 36
  
  const result2 = arr.reduce((acc, cur) => {
    if (cur % 2 === 0) acc.push(cur*3);
    else acc.push(cur*2);
    return acc;
  }, []);
  
  // console.log(result2) => [ 2, 6, 6, 12, 10 ]
  ```



### 객체 (object)

key(string) : value(모든 자료형) 쌍으로 구성된 프로퍼티들의 집합입니다.

```javascript
const user ={ name: '나란 남자', } 
// user ='hi!';//ERROR 
user.isFemale =false;//가능! 
delete user.isFemale //isFemale property삭제 
console.log('name' in user);//true
let keyword = 'name'
// console.log(user.keyword) => undefined
// console.log(user['keyword']) => undefined
// console.log(user[keyword]) => 나란 남자
```



### 객체에서 사용되는 메서드

- keys : 프로퍼티의 key들을 문자열 배열로 반환 [“key1”, “key2”,…] 

- values : 프로퍼티의 value들을 배열로 반환 [value1, value2,…] 

- entries : 프로퍼티의 [key,value]쌍들을 배열로 반환 (2중 배열) [[“key1”,value1],[“key1”,value1…]

  ```javascript
  Object.keys(obj); //['name','age','address','phoneNumber'] 
  Object.values(obj); //['Kim',12,null,'01012345678'] 
  Object.entries(obj); //[['name','Kim'],['age',12],['address',null],['phoneNumber','01012345678']]
  ```



### 깊은 복사와 얕은 복사

- 얕은 복사 (shallow copy) : 데이터가 저장한 '메모리 주소 값'을 복사하는것을 의미합니다. 복사한 객체가 변경된다면 기존의 객체도 변경이 됩니다.
- 깊은 복사(Deep copy) : 새로운 메모리 공간을 확보해 완전히 복사하는 것을 의미합니다.
