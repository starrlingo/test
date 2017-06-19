#!/usr/bin/env python
from subprocess import call, check_call, check_output
from subprocess import CalledProcessError

call('ls -al', shell=True)

try:
    # raise exception when return code is not 0
    check_call('exit 1', shell=True)
except CalledProcessError as e:
    print e.output
    print e.returncode

out = check_output('echo HelloWorld', shell=True)
print(out)
