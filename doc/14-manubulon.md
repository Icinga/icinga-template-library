# Plugin Check Commands for Manubulon SNMP <a id="snmp-manubulon-commands"></a>

The `SNMP Manubulon Plugin Check Commands` provide configuration for plugin check
commands provided by the [SNMP Manubulon project](http://nagios.manubulon.com/index_snmp.html).

**Note:** Some plugin parameters are only available in Debian packages or in a
[forked repository](https://github.com/dnsmichi/manubulon-snmp) with patches applied.

The SNMP manubulon plugin check commands assume that the global constant named `ManubulonPluginDir`
is set to the path where the Manubublon SNMP plugins are installed.

You can enable these plugin check commands by adding the following the include directive in your
[icinga2.conf](04-configuring-icinga-2.md#icinga2-conf) configuration file:

```
include <manubulon>
```

## Checks by Host Type

**N/A**      : Not available for this type.

**SNMP**     : Available for simple SNMP query.

**??**       : Untested.

**Specific** : Script name for platform specific checks.

Host type              | Interface | storage | load/cpu | mem  | process | env | specific
-----------------------|-----------|---------|----------|------|---------|-----|---------
Linux                  | Yes       | Yes     | Yes      | Yes  | Yes     | No  |
Windows                | Yes       | Yes     | Yes      | Yes  | Yes     | No  | check_snmp_win.pl
Cisco router/switch    | Yes       | N/A     | Yes      | Yes  | N/A     | Yes |
HP router/switch       | Yes       | N/A     | Yes      | Yes  | N/A     | No  |
Bluecoat proxy         | Yes       | SNMP    | Yes      | SNMP | No      | Yes |
CheckPoint on SPLAT    | Yes       | Yes     | Yes      | Yes  | Yes     | No  | check_snmp_cpfw.pl
CheckPoint on Nokia IP | Yes       | Yes     | Yes      | No   | ??      | No  | check_snmp_vrrp.pl
Boostedge              | Yes       | Yes     | Yes      | Yes  | ??      | No  | check_snmp_boostedge.pl
AS400                  | Yes       | Yes     | Yes      | Yes  | No      | No  |
NetsecureOne Netbox    | Yes       | Yes     | Yes      | ??   | Yes     | No  |
Radware Linkproof      | Yes       | N/A     | SNMP     | SNMP | No      | No  | check_snmp_linkproof_nhr <br> check_snmp_vrrp.pl
IronPort               | Yes       | SNMP    | SNMP     | SNMP | No      | Yes |
Cisco CSS              | Yes       | ??      | Yes      | Yes  | No      | ??  | check_snmp_css.pl

## snmp-env <a id="snmp-env"></a>

Check command object for the [check_snmp_env.pl](http://nagios.manubulon.com/snmp_env.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
snmp_address             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt             | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community           | **Optional.** The SNMP community. Defaults to "public".
snmp_port                | **Optional.** The SNMP port connection.
snmp_v2                  | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                  | **Optional.** SNMP version to 3. Defaults to false.
snmp_login               | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password            | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass     | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol        | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass            | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_env_type            | **Optional.** Environment Type, one of cisco, nokia, bc, iron, foundry or linux. Defaults to "cisco".
snmp_env_fan             | **Optional.** Minimum fan rpm value (only needed for 'iron' & 'linux')
snmp_env_celsius         | **Optional.** Maximum temp in degrees celsius (only needed for 'iron' & 'linux')
snmp_perf                | **Optional.** Enable perfdata values. Defaults to true.
snmp_timeout             | **Optional.** The command timeout in seconds. Defaults to 5 seconds.

## snmp-load <a id="snmp-load"></a>

Check command object for the [check_snmp_load.pl](http://nagios.manubulon.com/snmp_load.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
snmp_address             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt             | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community           | **Optional.** The SNMP community. Defaults to "public".
snmp_port                | **Optional.** The SNMP port connection.
snmp_v2                  | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                  | **Optional.** SNMP version to 3. Defaults to false.
snmp_login               | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password            | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass     | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol        | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass            | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_warn                | **Optional.** The warning threshold. Change the `snmp_load_type` var to "netsl" for using 3 values.
snmp_crit                | **Optional.** The critical threshold. Change the `snmp_load_type` var to "netsl" for using 3 values.
snmp_load_type           | **Optional.** Load type. Defaults to "stand". Check all available types in the [snmp load](http://nagios.manubulon.com/snmp_load.html) documentation.
snmp_perf                | **Optional.** Enable perfdata values. Defaults to true.
snmp_timeout             | **Optional.** The command timeout in seconds. Defaults to 5 seconds.

## snmp-memory <a id="snmp-memory"></a>

Check command object for the [check_snmp_mem.pl](http://nagios.manubulon.com/snmp_mem.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
snmp_address             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt             | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community           | **Optional.** The SNMP community. Defaults to "public".
snmp_port                | **Optional.** The SNMP port connection.
snmp_v2                  | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                  | **Optional.** SNMP version to 3. Defaults to false.
snmp_login               | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password            | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass     | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol        | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass            | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_warn                | **Optional.** The warning threshold.
snmp_crit                | **Optional.** The critical threshold.
snmp_is_cisco            | **Optional.** Change OIDs for Cisco switches. Defaults to false.
snmp_is_hp               | **Optional.** Change OIDs for HP/Procurve switches. Defaults to false.
snmp_perf                | **Optional.** Enable perfdata values. Defaults to true.
snmp_memcached           | **Optional.** Include cached memory in used memory, Defaults to false.
snmp_membuffer           | **Optional.** Exclude buffered memory in used memory, Defaults to false.
snmp_timeout             | **Optional.** The command timeout in seconds. Defaults to 5 seconds.

## snmp-storage <a id="snmp-storage"></a>

Check command object for the [check_snmp_storage.pl](http://nagios.manubulon.com/snmp_storage.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
snmp_address             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt             | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community           | **Optional.** The SNMP community. Defaults to "public".
snmp_port                | **Optional.** The SNMP port connection.
snmp_v2                  | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                  | **Optional.** SNMP version to 3. Defaults to false.
snmp_login               | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password            | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass     | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol        | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass            | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_warn                | **Optional.** The warning threshold.
snmp_crit                | **Optional.** The critical threshold.
snmp_storage_name        | **Optional.** Storage name. Default to regex "^/$$". More options available in the [snmp storage](http://nagios.manubulon.com/snmp_storage.html) documentation.
snmp_perf                | **Optional.** Enable perfdata values. Defaults to true.
snmp_timeout             | **Optional.** The command timeout in seconds. Defaults to 5 seconds.
snmp_storage_olength     | **Optional.** Max-size of the SNMP message, usefull in case of Too Long responses.

## snmp-interface <a id="snmp-interface"></a>

Check command object for the [check_snmp_int.pl](http://nagios.manubulon.com/snmp_int.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                            | Description
--------------------------------|------------
snmp_address                    | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt                    | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community                  | **Optional.** The SNMP community. Defaults to "public".
snmp_port                       | **Optional.** The SNMP port connection.
snmp_v2                         | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                         | **Optional.** SNMP version to 3. Defaults to false.
snmp_login                      | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password                   | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass            | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol        | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol               | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass                   | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_warn                       | **Optional.** The warning threshold.
snmp_crit                       | **Optional.** The critical threshold.
snmp_interface                  | **Optional.** Network interface name. Default to regex "eth0".
snmp_interface_inverse          | **Optional.** Inverse Interface check, down is ok. Defaults to false as it is missing.
snmp_interface_perf             | **Optional.** Check the input/output bandwidth of the interface. Defaults to true.
snmp_interface_label            | **Optional.** Add label before speed in output: in=, out=, errors-out=, etc.
snmp_interface_bits_bytes       | **Optional.** Output performance data in bits/s or Bytes/s. **Depends** on snmp_interface_kbits set to true. Defaults to true.
snmp_interface_percent          | **Optional.** Output performance data in % of max speed. Defaults to false.
snmp_interface_kbits            | **Optional.** Make the warning and critical levels in KBits/s. Defaults to true.
snmp_interface_megabytes        | **Optional.** Make the warning and critical levels in Mbps or MBps. **Depends** on snmp_interface_kbits set to true. Defaults to true.
snmp_interface_64bit            | **Optional.** Use 64 bits counters instead of the standard counters when checking bandwidth & performance data for interface >= 1Gbps. Defaults to false.
snmp_interface_errors           | **Optional.** Add error & discard to Perfparse output. Defaults to true.
snmp_interface_noregexp         | **Optional.** Do not use regexp to match interface name in description OID. Defaults to false.
snmp_interface_delta            | **Optional.** Delta time of perfcheck. Defaults to "300" (5 min).
snmp_interface_warncrit_percent | **Optional.** Make the warning and critical levels in % of reported interface speed. If set, **snmp_interface_megabytes** needs to be set to false. Defaults to false.
snmp_interface_ifname           | **Optional.** Switch from IF-MIB::ifDescr to IF-MIB::ifName when looking up the interface's name.
snmp_interface_ifalias          | **Optional.** Switch from IF-MIB::ifDescr to IF-MIB::ifAlias when looking up the interface's name.
snmp_interface_weathermap       | **Optional.** Output data for ["weathermap" lines](http://docs.nagvis.org/1.9/en_US/lines_weathermap_style.html) in NagVis. **Depends** on `snmp_interface_perf` set to true. Defaults to `false`. **Note**: Available in `check_snmp_int.pl v2.1.0`.
snmp_perf                       | **Optional.** Enable perfdata values. Defaults to true.
snmp_timeout                    | **Optional.** The command timeout in seconds. Defaults to 5 seconds.

## snmp-process <a id="snmp-process"></a>

Check command object for the [check_snmp_process.pl](http://nagios.manubulon.com/snmp_process.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                       | Description
---------------------------|------------
snmp_address               | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt               | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community             | **Optional.** The SNMP community. Defaults to "public".
snmp_port                  | **Optional.** The SNMP port connection.
snmp_v2                    | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                    | **Optional.** SNMP version to 3. Defaults to false.
snmp_login                 | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password              | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass       | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol   | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol          | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass              | **Required.** SNMP version 3 priv password. No value defined as default..
snmp_warn                  | **Optional.** The warning threshold.
snmp_crit                  | **Optional.** The critical threshold.
snmp_process_name          | **Optional.** Name of the process (regexp). No trailing slash!. Defaults to ".*".
snmp_perf                  | **Optional.** Enable perfdata values. Defaults to true.
snmp_timeout               | **Optional.** The command timeout in seconds. Defaults to 5 seconds.
snmp_process_use_params    | **Optional.** Add process parameters to process name for regexp matching. Example: "named.*-t /var/named/chroot" will only select named process with this parameter. Defaults to false.
snmp_process_mem_usage     | **Optional.** Define to check memory usage for the process. Defaults to false.
snmp_process_mem_threshold | **Optional.** Defines the warning and critical thresholds in Mb when snmp_process_mem_usage set to true. Example "512,1024". Defaults to "0,0".
snmp_process_cpu_usage     | **Optional.** Define to check CPU usage for the process. Defaults to false.
snmp_process_cpu_threshold | **Optional.** Defines the warning and critical thresholds in % when snmp_process_cpu_usage set to true. If more than one CPU, value can be > 100% : 100%=1 CPU. Example "15,50". Defaults to "0,0".

## snmp-service <a id="snmp-service"></a>

Check command object for the [check_snmp_win.pl](http://nagios.manubulon.com/snmp_windows.html) plugin.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
snmp_address             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
snmp_nocrypt             | **Optional.** Define SNMP encryption. If set to `false`, `snmp_v3` needs to be enabled. Defaults to `true` (no encryption).
snmp_community           | **Optional.** The SNMP community. Defaults to "public".
snmp_port                | **Optional.** The SNMP port connection.
snmp_v2                  | **Optional.** SNMP version to 2c. Defaults to false.
snmp_v3                  | **Optional.** SNMP version to 3. Defaults to false.
snmp_login               | **Optional.** SNMP version 3 username. Defaults to "snmpuser".
snmp_password            | **Required.** SNMP version 3 password. No value defined as default.
snmp_v3_use_privpass     | **Optional.** Define to use SNMP version 3 priv password. Defaults to false.
snmp_v3_use_authprotocol | **Optional.** Define to use SNMP version 3 authentication protocol. Defaults to false.
snmp_authprotocol        | **Optional.** SNMP version 3 authentication protocol. Defaults to "md5,des".
snmp_privpass            | **Required.** SNMP version 3 priv password. No value defined as default.
snmp_timeout             | **Optional.** The command timeout in seconds. Defaults to 5 seconds.
snmp_service_name        | **Optional.** Comma separated names of services (perl regular expressions can be used for every one). By default, it is not case sensitive. eg. ^dns$. Defaults to ".*".
snmp_service_count       | **Optional.** Compare matching services with a specified number instead of the number of names provided.
snmp_service_showall     | **Optional.** Show all services in the output, instead of only the non-active ones. Defaults to false.
snmp_service_noregexp    | **Optional.** Do not use regexp to match NAME in service description. Defaults to false.
