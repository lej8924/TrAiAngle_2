print("after")
import os

os.system('sudo chmod -R gu+rwx /home/ubuntu/TrAiAngle_2')

os.system('python3 -m venv /home/ubuntu/TrAiAngle_2/venv')
os.system('sudo chown -R ubuntu.ubuntu /home/ubuntu/TrAiAngle_2')
os.system('sudo chmod -R gu+rwx /home/ubuntu/TrAiAngle_2')
os.system(
    '. /home/ubuntu/TrAiAngle_2/venv/bin/activate && pip install --upgrade pip && pip install -r /home/ubuntu/TrAiAngle_2/requirements.txt && python3 /home/ubuntu/TrAiAngle_2/web/server/manage.py migrate')