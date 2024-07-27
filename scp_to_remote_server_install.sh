#!/usr/bin/env bash
# For web-01
scp 0-setup_web_static.sh ubuntu@54.160.125.157:/home/ubuntu/
ssh ubuntu@54.160.125.157 'sudo /home/ubuntu/0-setup_web_static.sh'

# For web-02
scp 0-setup_web_static.sh ubuntu@52.207.208.124:/home/ubuntu/
ssh ubuntu@52.207.208.124 'sudo /home/ubuntu/0-setup_web_static.sh'
