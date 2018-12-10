prometheus-server
=================

## Overview

An Ansible role to install and configure Prometheus server

## Requirements

None

## Dependencies

None

## Example Playbook

```yaml
- hosts: prometheus-server
  become: yes
  vars:
    prometheus_config:
      global:
        evaluation_interval: 60s
        external_labels:
            monitor: codelab-monitor
        scrape_timeout: 30s
        scrape_interval: 30s
      rule_files:
      scrape_configs:
        - job_name: 'prometheus'
          static_configs:
            - targets:
                - '127.0.0.1:9090'
              labels:
                host: 'prometheus-server'
                environment: 'testing'
        - job_name: 'web-server'
          static_configs:
            - targets:
                - '10.1.140.221'
              labels:
                host: 'web-server'
                environment: 'testing'
  roles:
    - prometheus-server
```

License
-------

BSD

Author Information
------------------
