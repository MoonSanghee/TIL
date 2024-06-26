## IPv4

IPv4주소는 전화번호와 같이 국내에서 표준을 정하고 정책을 수립하여 이용자에게 무한히 할당할 수 있는 자원이 아니라 전 세계적으로 관리되는 유한한 자원입니다. (약 43억개)

주소 규정에 의하여 사용이 제한적이기 때문에 IP주소 할당 정책에 따라 부여하여 사용합니다.



#### 구성

IPv4주소는 네트워크의 크기나 호스트의 수에 따라 A, B, C, D, E 클래스로 나누어집니다. A, B, C 클래스는 일반 사용자에게 부여하는 네트워크 구성용, D 클래스는 멀티캐스트용, E 클래스는 향후 사용을 위하여 예약된 주소입니다.



#### CIDR(Classless Inter-Domain Routing)에 의한 IP주소 할당

인터넷의 크기가 커짐에 따라 클래스 단위의 IP주소 할당은 라우팅 테이블을 복잡하게 하고, 인터넷 주소공간을 낭비하는 문제점을 야기합니다. 이에 따라 클래스의 제한을 두지 않고 필요한 호스트의 수에 따라 적당한 크기의 IP주소를 할당하는 CIDR 방식이 사용됩니다.



## IPv6

IPv6주소는 IPv4의 주소 고갈 문제를 해결하기 위하여 기존의 IPv4주소 체계를 128비트 크기로 확장한 차세대 인터넷 프로토콜 주소입니다.



#### 구성

IPv6주소의 경우 일반적으로 16비트 단위로 나누어지며 각 16비트 블록은 다시 4자리 16진수로 변환되고 콜론으로 구분되어집니다.



| 구분               | IPv4                                   | IPv6                                                      |
| ------------------ | -------------------------------------- | --------------------------------------------------------- |
| 주소길이           | 32비트                                 | 128비트                                                   |
| 표시방법           | 8비트씩 4부분으로 10진수로 표시        | 16비트씩 8부분 16진수로 표시                              |
| 주소개수           | 약 43억개                              | 약 43억**4                                                |
| 주소할당           | A, B, C 등 클래스 당위의 비순차적 할당 | 네트워크 규모 및 단말기 수에 따른 순차적 할당             |
| 품질제어           | 지원 수단 없음                         | 등급별, 서비스별로 패킷을 구분할 수 있어 품질 보장이 용이 |
| 보안               | IPsec 프로토콜 별도 설치               | 확장기능에서 기본으로 제공                                |
| 플러그 앤드 플레이 | 지원 수단 없음                         | 지원 수단 있음                                            |
| 모바일 IP          | 상당히 곤란                            | 용이                                                      |
| 웹캐스팅           | 곤란                                   | 용이                                                      |

IPSec

네트워크에서의 안전한 연결을 설정하기 위한 통신 규칙 또는 프로토콜 세트



플러그 앤드 플레이

사용자가 컴퓨터에 새로운 장치를 연결/제거 하였을 때 컴퓨터를 재부팅 하면서 플러그 앤 플레이 바이오스가 자동으로 새로운 장치를 감지하여 필요한 환경 값을 설정해 주는 가능 입니다. 때문에 사용자가 장치를 변경하는데 보다 손쉽게 컴퓨터를 작동하게 해줍니다.



웹 캐스팅

월드와이드웹과 브로드캐스팅의 합성어

인터넷방송을 의미
