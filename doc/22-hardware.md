# Hardware <a id="hardware"></a>

This category includes all plugin check commands for various hardware checks.

## hpasm <a id="hpasm"></a>

The [check_hpasm](https://labs.consol.de/de/nagios/check_hpasm/index.html) plugin
monitors the hardware health of HP Proliant Servers, provided that the `hpasm`
(HP Advanced Server Management) software is installed. It is also able to monitor
the system health of HP Bladesystems and storage systems.

The plugin can run in two different ways:

1. Local execution using the `hpasmcli` command line tool.
2. Remote SNMP query which invokes the HP Insight Tools on the remote node.

You can either set or omit `hpasm_hostname` custom attribute and select the corresponding node.

The `hpasm_remote` attribute enables the plugin to execute remote SNMP queries if set to `true`.
For compatibility reasons this attribute uses `true` as default value, and ensures that
specifying the `hpasm_hostname` always enables remote checks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                        | Description
----------------------------|------------
hpasm_hostname              | The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
hpasm_community             | SNMP community of the server (SNMP v1/2 only).
hpasm_protocol              | The SNMP protocol to use (default: 2c, other possibilities: 1,3).
hpasm_port                  | The SNMP port to use (default: 161).
hpasm_blacklist             | Blacklist some (missing/failed) components.
hpasm_ignore-dimms          | Ignore "N/A"-DIMM status on misc. servers (e.g. older DL320).
hpasm_ignore-fan-redundancy | Ignore missing redundancy partners.
hpasm_customthresholds      | Use custom thresholds for certain temperatures.
hpasm_eventrange            | Period of time before critical IML events respectively become warnings or vanish. A range is described as a number and a unit (s, m, h, d), e.g. --eventrange 1h/20m.
hpasm_perfdata              | Output performance data. If your performance data string becomes too long and is truncated by Nagios, then you can use --perfdata=short instead. This will output temperature tags without location information.
hpasm_username              | The securityName for the USM security model (SNMPv3 only).
hpasm_authpassword          | The authentication password for SNMPv3.
hpasm_authprotocol          | The authentication protocol for SNMPv3 (md5\|sha).
hpasm_privpassword          | The password for authPriv security level.
hpasm_privprotocol          | The private protocol for SNMPv3 (des\|aes\|aes128\|3des\|3desde).
hpasm_servertype            | The type of the server: proliant (default) or bladesystem.
hpasm_eval-nics             | Check network interfaces (and groups). Try it and report me whyt you think about it. I need to build up some know how on this subject. If you get an error and think, it is not justified for your configuration, please tell me about it. (always send the output of "snmpwalk -On .... 1.3.6.1.4.1.232" and a description how you setup your nics and why it is correct opposed to the plugins error message.
hpasm_remote                | Run remote SNMP checks if enabled. Otherwise checks are executed locally using the `hpasmcli` binary. Defaults to `true`.

## openmanage <a id="openmanage"></a>

The [check_openmanage](http://folk.uio.no/trondham/software/check_openmanage.html) plugin
checks the hardware health of Dell PowerEdge (and some PowerVault) servers.
It uses the Dell OpenManage Server Administrator (OMSA) software, which must be running on
the monitored system. check_openmanage can be used remotely with SNMP or locally with icinga2 agent,
check_by_ssh or similar, whichever suits your needs and particular taste.

The plugin checks the health of the storage subsystem, power supplies, memory modules,
temperature probes etc., and gives an alert if any of the components are faulty or operate outside normal parameters.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                       | Description
---------------------------|------------
openmanage_all             | Check everything, even log content
openmanage_blacklist       | Blacklist missing and/or failed components
openmanage_check           | Fine-tune which components are checked
openmanage_community       | SNMP community string [default=public]
openmanage_config          | Specify configuration file
openmanage_critical        | Custom temperature critical limits
openmanage_extinfo         | Append system info to alerts
openmanage_fahrenheit      | Use Fahrenheit as temperature unit
openmanage_hostname        | Hostname or IP (required for SNMP)
openmanage_htmlinfo        | HTML output with clickable links
openmanage_info            | Prefix any alerts with the service tag
openmanage_ipv6            | Use IPv6 instead of IPv4 [default=no]
openmanage_legacy_perfdata | Legacy performance data output
openmanage_no_storage      | Don't check storage
openmanage_only            | Only check a certain component or alert type
openmanage_perfdata        | Output performance data [default=no]
openmanage_port            | SNMP port number [default=161]
openmanage_protocol        | SNMP protocol version [default=2c]
openmanage_short_state     | Prefix alerts with alert state abbreviated
openmanage_show_blacklist  | Show blacklistings in OK output
openmanage_state           | Prefix alerts with alert state
openmanage_tcp             | Use TCP instead of UDP [default=no]
openmanage_timeout         | Plugin timeout in seconds [default=30]
openmanage_vdisk_critical  | Make any alerts on virtual disks critical
openmanage_warning         | Custom temperature warning limits

## adaptec-raid <a id="adaptec-raid"></a>

The [check_adaptec_raid](https://github.com/thomas-krenn/check_adaptec_raid) plugin
uses the `arcconf` binary to monitor Adaptec RAID controllers.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                      | Description
--------------------------|------------
adaptec_controller_number | **Required.** Controller number to monitor.
arcconf_path              | **Required.** Path to the `arcconf` binary, e.g. "/sbin/arcconf".

## lsi-raid <a id="lsi-raid"></a>

The [check_lsi_raid](https://github.com/thomas-krenn/check_lsi_raid) plugin
uses the `storcli` binary to monitor MegaRAID RAID controllers.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
lsi_controller_number | **Required.** Controller number to monitor.
storcli_path          | **Required.** Path to the `storcli` binary, e.g. "/usr/sbin/storcli".

## smart-attributes <a id="smart-attributes"></a>

The [check_smart_attributes](https://github.com/thomas-krenn/check_smart_attributes) plugin
uses the `smartctl` binary to monitor SMART values of SSDs and HDDs.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                         | Description
-----------------------------|------------
smart_attributes_config_path | **Required.** Path to the smart attributes config file (e.g. check_smartdb.json).
smart_attributes_device      | **Required.** Device name (e.g. /dev/sda) to monitor.
