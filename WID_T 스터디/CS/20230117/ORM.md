## ORM

Object Relational Mapping 즉, 객체-관계 매핑의 줄임말입니다. 객체 -관계 매핑을 풀어서 설명하자면 우리가 OOP(Object Oriented Programming)에서 쓰이는 객체라는 개념을 구현한 클래스와 RDB(Relational DataBase)에서 쓰이는 데이터인 테이블을 자동으로 연결하는것을 의미합니다. 그러나 클래스와 테이블은 서로가 기존부터 호환가능성을 두고 만들엊진 것이 아니기 때문에 불일치가 발생하는데, 이를 ORM을 통해 객체 간의 관계를 바탕으로 SQL문을 자동으로 생성하여 불일치를 해결합니다. 따라서 ORM을 이용하면 따로 SQL문을 짤 필요 없이 객체를 통해 간접적으로 데이터베이스를 조작할 수 있게 된됩니다..



### 장단점

### 장점

#### 완벽한 객체지향적인 코드

ORM을 이용하면 SQL문이 아닌 클래스의 메서드를 통해 데이터베이스를 조작할 수 있어, 개발자가 객체 모델만 이용해서 프로그래밍을 하는 데 집중할 수 있게합니다. SQL 문을 사용하면서 같이 필요한 선언문, 할당, 종료 같은 부수적인 코드가 사라지거나 줄어들며, 각종 객체에 대한 코드를 별도로 작성하여 코드의 가독성을 높일 수 있습니다. 객체지향적 접근과 SQL의 절차적/순차적 접근이 혼재되어있던 기존 방식과 달리 오직 객체지향적 접근만 고려하면 되기때문에 생산성이 증가합니다.

#### 재사용, 유지보수, 리팩토링 용이성

ORM은 기존 객체와 독립적으로 작성되어있고, 객체로 작성되었기 때문에 재활용할 수 있다. 또한, 매핑하는 정보가 명확하기 때문에 ERD를 보는 의존도를 낮출 수 있습니다.

#### DBMS(DataBase Management System) 종속성 하락

객체 간의 관계를 바탕으로 SQL문을 자동으로 생성하고, 객체의 자료형 타입까지 사용할 수 있기 때문에 RDBMS의 데이터 구조와 객체지향 모델 사이의 간격을 좁힐 수 있다. 객체에만 집중할 수 있기 때문에 DBMS를 교체하는 큰 작업에도 리스크가 적고 드는 시간도 줄어든다. 예들 들어 자바에서 가공할 경우 `equals`, `hashCode`의 오버라이드 같은 자바의 기능을 이용할 수 있고, 간결하고 빠르게 가공할 수 있다.



### 단점

#### ORM이 모든 걸 해결해줄 수 없다.

ORM을 사용하는 것은 매우 편리하지만 그만큼 신중하게 설계해야합니다. 프로젝트의 복잡성이 커질 수록 난이도도 올라가고 부족한 설계로 잘못 구현되었을 경우 속도 저하 및 일관성을 무너뜨리는 문제점이 생길 수 있습니다. 또한 일부 자주 사용되는 대형 SQL문은 속도를 위해 별도의 튜닝이 필요하기 때문에 결국 SQL문을 써야할 수도 있습니다..

#### 객체-관계 간의 불일치

다음과 같은 특성에서 객체-관계 간의 불일치가 생깁니다.

#### 세분성(Granularity)

경우에 따라서 데이터베이스에 있는 테이블 수보다 더 많은 클래스를 가진 모델이 생길 수 있습니다.

#### 상속성(Inheritance)

RDBMS는 객체지향 프로그래밍 언어의 특징인 상속 개념이 없습니다.

#### 일치(Identity)

RDBMS는 기본키(primary key)를 이용하여 동일성을 정의한다. 그러나 자바는 객체 식별(`a==b`)과 객체 동일성(`a.equals(b)`)을 모두 정의합니다.

#### 연관성(Associations)

객체지향 언어는 방향성이 있는 객체의 참조(reference)를 사용하여 연관성을 나타내지만 RDBMS는 방향성이 없는 외래키(foreign key)를 이용해서 나타냅니다.

#### 탐색(Navigation)

자바와 RDBMS에서 객체를 접근하는 방법이 근본적으로 다르다. 자바는 그래프형태로 하나의 연결에서 다른 연결로 이동하며 탐색한다. 그러나 RDBMS에서는 일반적으로 SQL문을 최소화하고 `JOIN`을 통해 여러 엔티티를 로드하고 원하는 대상 엔티티를 선택하는 방식으로 탐색합니다.