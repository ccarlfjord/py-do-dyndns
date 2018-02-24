#!/bin/bash

APP="do-dyndns"
DIR=$(pwd)
VIRTUALENVDIR=$HOME/.venv/$APP

virtualenv -p python3 $VIRTUALENVDIR
source $VIRTUALENVDIR/bin/activate

pip3 install -r requirements.txt

systemctl stop $APP

cat << EOF > /etc/systemd/system/$APP.service
[Unit]
Description=$APP
After=network.target

[Service]
WorkingDirectory=$DIR
ExecStart=$VIRTUALENVDIR/bin/python3 $DIR/$APP/$APP.py -c /etc/$APP.yaml

[Install]
WantedBy=default.target
EOF

systemctl daemon-reload
systemctl start $APP
