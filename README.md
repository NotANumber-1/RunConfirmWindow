# Run Confirm Window (한국어)
## 개요
권한 승계를 대신해서 사용할 수 있는 사용자 프롬프트

## 장점
 - '슬라이드하여 허용' 방식으로 빠름
 - 선택 저장 가능
 - 최소한의 코드와 UI (5KB 미만의 작은 용량, 모듈 등 설치 필요 없음)
 - 코드 내 쉽고 빠른 사용

## 사용
 1. 자신의 메인 코드와 같은 디렉토리에 파일을 위치한다
 2. 메인 코드에 예시와 같은 코드 입력

예시: 
main.py
```py
import os
def main():
    os.system("dangerous -code -start")
# User Confirmation
import wconf
if wconf.allowed:
  main()
```
