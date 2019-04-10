#!/bin/bash

# To use:
# mkdir ~/tmpconfig
# cd ~/tmpconfig
# wget https://raw.githubusercontent.com/sanjeevm0/kcluster-ARM/master/nocloud/bootstrapfirst.sh
# bash ./bootstrapfirst.sh
# edit file nocloud.yaml
# python3 ./bootstrapfirst.py nocloud.yaml

sudo apt-get update 
sudo apt-get install -y --no-install-recommends \
  python3-pip \
  python3-pyyaml
mkdir -p ~/tmpconfig
wget -O ~/tmpconfig/bootstrapfirst.py https://raw.githubusercontent.com/sanjeevm0/kcluster-ARM/master/nocloud/bootstrapfirst.py
wget -O ~/tmpconfig/nocloud.yaml https://raw.githubusercontent.com/sanjeevm0/kcluster-ARM/master/nocloud/nocloud.example.yaml
