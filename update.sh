sudo systemctl stop tmamanager
mv start.sh start.sh.bak
git pull

mv start.sh.bak start.sh

sudo systemctl start tmamanager
