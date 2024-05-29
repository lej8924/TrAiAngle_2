
curl  -s -d "payload={\"text\":\"github 저장소 다운로드가 완료되었습니다\n패키지 관리를 시작합니다... \"}" "https://hooks.slack.com/services/blahblahblah"

python3 /home/ubuntu/TrAiAngle_2/scripts/afterInstall.py 1> /home/ubuntu/after.log 2> /home/ubuntu/after.err

curl  -s -d "payload={\"text\":\"배포종료 \"}" "https://hooks.slack.com/services/blahblahblah"