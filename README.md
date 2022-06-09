# argo-probe-nagios

This plugin checks the status of the Nagios process on the local machine. The plugin will check to make sure the Nagios status log is no older that the number of minutes specified by the expires option. It also checks the process table for a process matching the command argument.

## Synopsis

The probe has a number of arguments:

```
# /usr/libexec/argo/probes/nagios/check_nagios -h
check_nagios 1.0

This nagios plugin is free software, and comes with ABSOLUTELY NO WARRANTY.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Copyright 2017 Emir Imamagic

Probe for checking Nagios status.

Usage: check_nagios --nagios-host=mon --nagios-service=service1,service2

 -?, --usage
   Print usage information
 -h, --help
   Print detailed help screen
 -V, --version
   Print version information
 --extra-opts=[section][@file]
   Read options from an ini file. See http://nagiosplugins.org/extra-opts
   for usage and examples.
 -H, --hostname=STRING
   H|hostname
   Name or IP address of host to check.
   (default: localhost)
 -p, --port=INTEGER
   p|port
   Port of the service.
   (default: 443)
 --url=STRING
   url
   Nagios interface URL.
   (default: /nagios)
 --capath=/location/...
   Location where CA certificates are stored.
   (default: /etc/grid-security/certificates)
 --cert=/location/...
   Location of certificate used for authentication.

 --key=/location/...
   Location of key used for authentication.

 --username
   Username used for authentication.

 --password=STRING
   password
   Password used for authentication.

 --realm=STRING
   realm
   Realm used for authentication.

 --nagios-host=hostname
   Hostname on remote nagios to check.

 --nagios-service=service1,service2
   List of services on remote nagios to check.

 --age=INTEGER
   age
   Raise CRITICAL if last check is older than age in seconds.
   (default: 3600)
 --ignore-state
   ignore-state
   Ignore state of services, just check freshness.
   (default: )
 -t, --timeout=INTEGER
   Seconds before plugin times out (default: 15)
 -v, --verbose
   Show details for command-line debugging (can repeat up to 3 times)
```

Example execution of the probe:
```
# /usr/libexec/argo/probes/nagios/check_nagios -H "argo-mon-biomed.cro-ngi.hr" -t 60 --cert /etc/nagios/globus/hostcert.pem --key /etc/nagios/globus/hostkey.pem --nagios-service org.nagios.NagiosCmdFile
check_nagios OK - Service argo-mon-biomed.cro-ngi.hr/org.nagios.NagiosCmdFile on Nagios argo-mon-biomed.cro-ngi.hr has OK status.
```
