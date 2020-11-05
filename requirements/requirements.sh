echo Installer for linux by Castellani Davide >> ./../log/log.log

sudo apt-get install python3 >> ./../log/log.log
sudo apt-get install python3-pip >> ./../log/log.log
sudo pip3 install -r ./requirements.txt >> ./../log/log.log

echo >> ./../log/log.log