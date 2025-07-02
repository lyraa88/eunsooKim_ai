## 7/2 

### 저번 시간 복습
1. vs code에서 내용을 수정한 뒤 반드시 저장을 하고 add -> commit -> push 할 것

2. 새롭게 시작할 때엔 이미 저장소 연결이 끝났기 때문에 수정하고 add -> commit -> push만 하면 됨

### 새로운 지식 및 인사이트
1. 코드 내에서 줄바꿈을 하고 싶다면?

`with open('/content/sample_data/anscombe.json') as file_1, \
     open('test.json', 'w') as file_2:
      file_2.write(file_1.read())
      `
### 코드 내에서 줄바꿈을 하고 싶으면 \를 마지막에 붙일 것 


2. 유용한 명령어
`!pwd  # 경로 확인
%time  # 해당 줄 코드 경과 시간
%%time  # 모든 코드 경과 시간
`
