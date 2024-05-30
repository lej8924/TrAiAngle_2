print("after")
import os


# os.system('python3 -m venv /home/ubuntu/TrAiAngle_2/venv')


os.system('pip install --upgrade pip && pip install -r /home/ubuntu/TrAiAngle_2/requirements.txt')
os.system('npm install:website && npm install:client && python3 /home/ubuntu/TrAiAngle_2/web/server/manage.py migrate')
os.system('npm run start:website')

# os.system(
    # '. /home/ubuntu/TrAiAngle_2/venv/bin/activate && pip install --upgrade pip && pip install -r /home/ubuntu/TrAiAngle_2/requirements.txt && python3 /home/ubuntu/TrAiAngle_2/web/server/manage.py migrate')