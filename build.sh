#!/bin/bash

APP="do-dyndns"
DIR=$(pwd)
VIRTUALENVDIR=$HOME/.venv/$APP

virtualenv -p python3 $VIRTUALENVDIR
source $VIRTUALENVDIR/bin/activate

pip3 install -f requirements.txt

systemctl stop $APP

cat << EOF > /etc/systemd/system/$APP.service
[Unit]
Description=$APP
After=network.target

[Service]
WorkingDirectory=$VIRTUALENVDIR
ExecStart=$DIR/$APP/$APP.py -f $DIR/settings.yaml

[Install]
WantedBy=default.target
EOF

systemctl daemon-reload
systemctl start $APP
