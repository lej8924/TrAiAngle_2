if [ -d /home/ubuntu/TrAiAngle_2 ]; then
    sudo rm -rf /home/ubuntu/TrAiAngle_2
fi
sudo mkdir -vp /home/ubuntu/TrAiAngle_2

sudo chmod -R gu+rwx /home/ubuntu/TrAiAngle_2
sudo chown -R ubuntu.ubuntu /home/ubuntu/TrAiAngle_2

#!/bin/bash
cd /home/ubuntu
source env/bin/activate
# cd TrAiAngle_2
pip3 install -r /home/ubuntu/TrAiAngle_2/requirements.txt