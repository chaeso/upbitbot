# 소개

헤이비트(heybit)라는 투자봇의 로직을 파이썬으로 비슷하게 구현해 보았습니다.
관련 설명 : https://m.post.naver.com/viewer/postView.nhn?volumeNo=15975365&memberNo=40921089

주의 : 업비트 API 변경으로 코드가 더이상 동작 하지 않습니다. 


# 환경

python3.7

# 백테스팅

- 업비트 기존 데이터를 가져와서 구글 스프레드쉬트를 이용해서 백테스트 해보았습니다. (다만 백테스트 방법과 실제 코드는 조금 다른데 시간이 없어서 그냥 내버려둠)
- https://docs.google.com/spreadsheets/d/1xurOPt5QEoWvyS6dgHW4vVNpHRr1GK3KrWReGd0C7Ec/edit?usp=sharing

# 실행 방법
- upbit_bot.py 파일을 열어서 업비트에서 발급 받은 API 키와 비밀키를 UPBIT_API_KEY, UPBIT_SEC_KEY 변수 각각에 입력
- crontab 설정파일을 수정하여 "python3 upbit_bot.py" 명령어를 매일 새벽 0시에 실행되게 수정

# 주의 사항

- 학습용으로 구현된 코드이고, 그대로 돌리면 손해가 날 수도 있으니 각자 백테스팅하고 튜닝해서 사용하시길 바랍니다.
