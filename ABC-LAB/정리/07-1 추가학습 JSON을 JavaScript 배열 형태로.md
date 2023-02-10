## JSON

**JSON** (JavaScript Object Notation)은 경량의 DATA-교환 형식입니다. 이 형식은 사람이 읽고 쓰기에 용이하며, 기계가 분석하고 생성함에도 용이합니다.



**값만 배열로 추출** : JSON 데이터가 "이름:값"의 가장 단순한 형태인 경우, 값만 배열로 추출할 수 있습니다.

```javascript
json1 = {value1:13, value2:10, value3:5, value4:40};

console.log(Object.values(json1));
```



**순환 메서드를 이용해 배열로 변환** : JSON 값이 배열인 경우 순환 메서드로 값을 추출할 수 있습니다.

```javascript
json2 = {data:[{value:13}, {value:10}, {value:5}, {value:40}]};
let result2 = [];

json2.data.forEach((item,idx)=>{
  result2.push(parseInt(item.value));
});

console.log(result2);
```



**여러값을 중첩 배열로 가져오기**

```javascript
json3 = {data:[{name:'라이언', value:13}, {name:'콘', value:10}, {name:'무지', value:5}, {name: '프로도', value:40}]};
let result3 = [];

json3.data.forEach((item)=>{
  result3.push([item.name, parseInt(item.value)]);
})

console.log(result3);
```

