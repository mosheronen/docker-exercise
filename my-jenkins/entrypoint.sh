#!/bin/bash

# Start the ssh server
/etc/init.d/ssh start

# Start the Jenkins
/sbin/tini -- /usr/local/bin/jenkins.sh
