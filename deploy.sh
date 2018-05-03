#!/usr/bin/env sh
sshpass -p $SSHPASSWORD scp -r dist/* tanay@tanayseven.com:~/tanayseven.com/
