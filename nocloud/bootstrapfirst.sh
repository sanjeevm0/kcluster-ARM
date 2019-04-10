#!/bin/bash

sudo apt-get update 
sudo apt-get install -y --no-install-recommends \
  python3-pip \
  python3-pyyaml
mkdir -p ~/tmpconfig
wget -O ~/tmpconfig/bootstrapfirst.py https://raw.githubusercontent.com/sanjeevm0/kcluster-ARM/master/nocloud/bootstrapfirst.py
wget -O ~/tmpconfig/nocloud.yaml https://raw.githubusercontent.com/sanjeevm0/kcluster-ARM/master/nocloud/nocloud.example.yaml
