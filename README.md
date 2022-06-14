# argo-probe-nagios

Package `argo-probe-nagios` contains two probes: `check_nagios` and `gather_healthy_nodes`.

Probe `check_nagios` checks the status of the Nagios process on the local machine. The plugin will check to make sure the Nagios status log is no older that the number of minutes specified by the expires option. It also checks the process table for a process matching the command argument.

Probe `gather_healthy_nodes` generates list of hostnames with a given service in status OK.

## Synopsis

Example execution of the `check_nagios` probe:
```
# /usr/libexec/argo/probes/nagios/check_nagios -H "argo-mon-biomed.cro-ngi.hr" -t 60 --cert /etc/nagios/globus/hostcert.pem --key /etc/nagios/globus/hostkey.pem --nagios-service org.nagios.NagiosCmdFile
check_nagios OK - Service argo-mon-biomed.cro-ngi.hr/org.nagios.NagiosCmdFile on Nagios argo-mon-biomed.cro-ngi.hr has OK status.
```

Example execution of the `gather_healthy_nodes` probe:

```
# /usr/libexec/argo/probes/nagios/gather_healthy_nodes -t 120 --vo ops --file GoodSEs --dir /var/lib/gridprobes --metric eu.egi.SRM-All
HealthyNodes OK - Successfully generated file with 120 hosts. | hosts=120;;
```
