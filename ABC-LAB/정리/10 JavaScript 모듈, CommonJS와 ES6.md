## 모듈 

독립된 기능을 갖는 것(함수, 파일)들의 모임입니다.



### 특징

- 유지 보수성 : 능들이 모듈화가 잘 되어있다면, 의존성을 그만큼 줄일 수 있기 때문에 어떤 기능을 개선한다거나 수정할 때 훨씬 편하게 할 수 있습니다.
- 네임스페이스화 : 자바스크립트에서 전역변수는 전역공간을 가지기 때문에 코드의 양이 많아질수록 겹치는 네임스페이스가 많아질 수 있다. 그러나 모듈로 분리하면 모듈만의 네임스페이스를 갖기 때문에 그 문제가 해결된다.
- 재사용성 : 똑같은 코드를 반복하지 않고 모듈로 분리시켜서 필요할 때마다 사용할 수 있다.



### CommonJS

CommonJS 포맷은 Node.js (서버사이드 자바스크립트) 의 표준입니다.

내보내기의 경우 exports 및 module.exports, 가져오기의 경우 require 를 사용합니다.



**1-1. exports를 통한 내보내기**

```javascript
//func.js
function func1 (param) {
	// ...
}

function func2 (param) {
	// ...
}

exports.func1 = func1
exports.func2 = func2
```



**1-2. 가져오기**

```javascript
const obj = require('./func')

obj.func1(10)
obj.func2(20)
```



**2-1. module.exports를 통한 내보내기**

```javascript
// func.js
const obj = {
	
    func1: function (num) {
    	// ...
    },
    
    func2: function (num) {
    	// ...
    }
}

module.exports = obj
```

**2-2. 가져오기**

```javascript
const obj = require('./func')

obj.func1(10)
obj.func2(20)
```



기본적으로 가져오는 방법에 대해서는 두 방법이 모두 동일하지만 내보내기를 할 경우 export를 사용하는 경우에는 여러 property를 내보낼 때, module.exports를 사용하는 경우에는 여러 property를 내보낼 때 혹은 단일 Object를 내보낼 때 모두 가능합니다.

\*exports는 module.exports를 참조하고 있는 객체입니다.

즉, exports 에 property를 명시하는 위와같은 방법은 정상적으로 동작하지만, 신규 객체를 할당해버리면 모듈이 동작하지 않습니다.

특별한 상황이 아니라면 module.exports를 사용하는 것이 권장됩니다.



### ECMAScript(mjs) - ES6

CommonJS와 마찬가지로 기본적으로는 원하는 모듈을 내보내고, 가져온다는 것에서는 동일하지만 아직 브라우저들이 es6를 완벽히 지원하지 못하는 상황이므로 webpack 이나 babel 등의 번들러들이 필요한 것이 단점입니다.

기본적으로 내보내기 키워드는 export 및 default. 가져오기 키워드는 import 입니다.



**1-1. export 를 이용한 내보내기**

```javascript
// first_func.js

export function func1 (num) {
	// ...
}

const func2 = function (num) {
	// ...
}

export { func2 }
```



**1-2. 가져오기**

```javascript
// 사용하려는 객체만 선택하여 가져오기
import { func1 } from './first_func'

func1(10)


// 모든 객체를 가져오되 원하는 이름을 붙여서 사용한다.
import * as obj from './first_func'

obj.func1(10)
obj.func2(20)
```



**2-1. export default 를 이용한 내보내기**

```javascript
// second_func.js
const obj = {

    func3: function (num) {
    	// ...
    },
    
    func4: function (num) {
    	// ...
    }
}

export default obj
```



**2-2. 가져오기**

```javascript
// default 키워드를 이용하여 내보냈던 쪽에서 사용한 명칭을 그대로 사용할 필요는 없습니다.
import testObj from './second_func'

testObj.func3(10)
testObj.func4(20)
```