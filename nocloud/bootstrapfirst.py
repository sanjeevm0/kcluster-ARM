import os
import sys
import yaml
import pathlib
import json
import base64

if __name__ == '__main__':
    configFile = sys.argv[1]
    config = {
        "cloudProvider": "NoCloud",
        "adminUsername": "core",
        "numberOfInfraVM": 1,
        "minWorkerVM": 0,
        "maxWorkerVM": 0,
        "gitlocation": "sanjeevm0/kcluster/master",
        "gitscript": "scripts/bootstrap.sh",
        "masternode": True,
        "workernode": False,
        "first_infra_node": True,
        "bootstrap": True
    }
    with open(configFile, 'r') as fp:
        config = config.update(yaml.load(fp))
    with open('/home/{0}/.ssh/authorized_keys', 'r') as fp:
        sshKeyData = fp.read().strip()
    config['sshKeyData'] = sshKeyData
    config['gitdeploykeyB'] = base64.b64encode(config['gitdeploykey'].encode()).decode()
    script = "https://raw.githubusercontent.com/sanjeevm0/ARMConfig/master/config.sh"
    pathlib.Path("/home/{0}/tmpconfig".format(config['adminUsername'])).mkdir(parents=True, exist_ok=True)
    os.system("wget {0} -O /home/{1}/tmpconfig/config.sh".format(script, config['adminUsername']))
    commandParams = "{0} {1} '{2}' {3} {4} {0} \\'{5}\\'".format(
            config['adminUsername'], config['gitlocation'], config['gitdeploykeyB'],
            config['gitscript'], config['cloudProvider'], 
            base64.b64encode(json.dumps(config).encode()).decode().replace('"','\\"'))
    os.system("bash /home/{0}/tmpconfig/config.sh {1}".format(config['adminUsername'], commandParams))
