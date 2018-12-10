ec2-instance
============

## Overview

This Ansible role is designed to creat EC2 instances in AWS cloud.

## Requirements

None

## Dependencies

Install dependencies:

```
pip install botocore==1.12.28
pip install boto3==1.9.62
```

Populate `boto` configuration file with the respective AWS credentials:

```bash
echo -e "[Credentials]\naws_access_key_id = KEY\naws_secret_access_key = SECRET" > ~/.boto
```

## Example Playbook

Provision a new EC2 instance:

```bash
ansible-playbook -l all deploy.yml -i ansible/hosts --tags create
```

After the new instance is created and launched, one can connect to it with SSH key provided. IP address is used in example `34.244.206.112` will be different in each case.

```bash
ssh -i ~/.ssh/prometheus-server ec2-user@34.244.206.112
```

License
-------

BSD

Author Information
------------------

