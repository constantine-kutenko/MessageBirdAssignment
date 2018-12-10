MessageBird Assignment
======================

## Application

The application that provides functionality for a simple web server was written and tested to be used with Python 2.7.x. It can also be run on Python 3.x and uses as less dependencies as possible. Application can be improved by switching to using an API of one of open services that provides geo and timezone data. Python was chosen because it is the simplest language to prototype and application and powerful enough to get the task solved by using built-in or external packages and libraries.

## Docker image

Docker image is used as a runtime platform to containerized and run the application. The image is base on Alpine Linux since this distribution is tiny and lacks of many unnecessary packages. The platform was used because it allows to run applications everywhere and with the certain set of packages inside. It also has full support from Kubernetes as a native runtime.

## Helm chart

Deployment is written as a Helm chart that allows to deploy and update application to any kind of Kubernetes clusters, be it bare metal or cloud one such as Amazon EKS. Employing Helm allow update deployed releases using CD\CD pipelines.

## Ansible roles

There are two Ansible roles that provision an EC2 instance in Amazon cloud and deploy a Prometheus server respectively.  Ansible was chosen since it is a most powerful and easy-to-use configuration management system.
