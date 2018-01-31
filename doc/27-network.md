# Network Components <a id="network-components"></a>

This category includes all plugins for various network components like routers, switches and firewalls.

## interfacetable <a id="interfacetable"></a>

The [check_interfacetable_v3t](http://www.tontonitch.com/tiki/tiki-index.php?page=Nagios+plugins+-+interfacetable_v3t) plugin
generates a html page containing information about the monitored node and all of its interfaces.

The Git repository is located on [GitHub](https://github.com/Tontonitch/interfacetable_v3t).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                               | Description
-----------------------------------|------------
interfacetable_hostquery           | **Required.** Specifies the remote host to poll. Defaults to "$address$".
interfacetable_hostdisplay         | Specifies the hostname to display in the HTML link. Defaults to "$host.display_name$".
interfacetable_regex               | Interface names and property names for some other options will be interpreted as regular expressions. Defaults to false.
interfacetable_outputshort         | Reduce the verbosity of the plugin output. Defaults to false.
interfacetable_exclude             | Comma separated list of interfaces globally excluded from the monitoring.
interfacetable_include             | Comma separated list of interfaces globally included in the monitoring.
interfacetable_aliasmatching       | Allow you to specify alias in addition to interface names. Defaults to false.
interfacetable_excludetraffic      | Comma separated list of interfaces excluded from traffic checks.
interfacetable_includetraffic      | Comma separated list of interfaces included for traffic checks.
interfacetable_warningtraffic      | Interface traffic load percentage leading to a warning alert.
interfacetable_criticaltraffic     | Interface traffic load percentage leading to a critical alert.
interfacetable_pkt                 | Add unicast/non-unicast pkt stats for each interface.
interfacetable_trafficwithpkt      | Enable traffic calculation using pkt counters instead of octet counters. Useful when using 32-bit counters to track the load on > 1GbE interfaces. Defaults to false.
interfacetable_trackproperty       | List of tracked properties.
interfacetable_excludeproperty     | Comma separated list of interfaces excluded from the property tracking.
interfacetable_includeproperty     | Comma separated list of interfaces included in the property tracking.
interfacetable_community           | Specifies the snmp v1/v2c community string. Defaults to "public" if using snmp v1/v2c, ignored using v3.
interfacetable_snmpv2              | Use snmp v2c. Defaults to false.
interfacetable_login               | Login for snmpv3 authentication.
interfacetable_passwd              | Auth password for snmpv3 authentication.
interfacetable_privpass            | Priv password for snmpv3 authentication.
interfacetable_protocols           | Authentication protocol,Priv protocol for snmpv3 authentication.
interfacetable_domain              | SNMP transport domain.
interfacetable_contextname         | Context name for the snmp requests.
interfacetable_port                | SNMP port. Defaults to standard port.
interfacetable_64bits              | Use SNMP 64-bits counters. Defaults to false.
interfacetable_maxrepetitions      | Increasing this value may enhance snmp query performances by gathering more results at one time.
interfacetable_snmptimeout         | Define the Transport Layer timeout for the snmp queries.
interfacetable_snmpretries         | Define the number of times to retry sending a SNMP message.
interfacetable_snmpmaxmsgsize      | Size of the SNMP message in octets, useful in case of too long responses. Be careful with network filters. Range 484 - 65535. Apply only to netsnmp perl bindings. The default is 1472 octets for UDP/IPv4, 1452 octets for UDP/IPv6, 1460 octets for TCP/IPv4, and 1440 octets for TCP/IPv6.
interfacetable_unixsnmp            | Use unix snmp utilities for snmp requests. Defaults to false, which means use the perl bindings.
interfacetable_enableperfdata      | Enable port performance data. Defaults to false.
interfacetable_perfdataformat      | Define which performance data will be generated. Possible values are "full" (default), "loadonly", "globalonly".
interfacetable_perfdatathreshold   | Define which thresholds are printed in the generated performance data. Possible values are "full" (default), "loadonly", "globalonly".
interfacetable_perfdatadir         | When specified, the performance data are also written directly to a file, in the specified location.
interfacetable_perfdataservicedesc | Specify additional parameters for output performance data to PNP. Defaults to "$service.name$", only affects **interfacetable_perfdatadir**.
interfacetable_grapher             | Specify the used graphing solution. Possible values are "pnp4nagios" (default), "nagiosgrapher", "netwaysgrapherv2" and "ingraph".
interfacetable_grapherurl          | Graphing system url. Default depends on **interfacetable_grapher**.
interfacetable_portperfunit        | Traffic could be reported in bits (counters) or in bps (calculated value).
interfacetable_nodetype            | Specify the node type, for specific information to be printed / specific oids to be used. Possible values: "standard" (default), "cisco", "hp", "netscreen", "netapp", "bigip", "bluecoat", "brocade", "brocade-nos", "nortel", "hpux".
interfacetable_duplex              | Add the duplex mode property for each interface in the interface table. Defaults to false.
interfacetable_stp                 | Add the stp state property for each interface in the interface table. Defaults to false.
interfacetable_vlan                | Add the vlan attribution property for each interface in the interface table. Defaults to false. This option is available only for the following nodetypes: "cisco", "hp", "nortel"
interfacetable_noipinfo            | Remove the ip information for each interface from the interface table. Defaults to false.
interfacetable_alias               | Add the alias information for each interface in the interface table. Defaults to false.
interfacetable_accessmethod        | Access method for a shortcut to the host in the HTML page. Format is : <method>[:<target>] Where method can be: ssh, telnet, http or https.
interfacetable_htmltablelinktarget | Specifies the windows or the frame where the [details] link will load the generated html page. Possible values are: "_blank", "_self" (default), "_parent", "_top", or a frame name.
interfacetable_delta               | Set the delta used for interface throughput calculation in seconds.
interfacetable_ifs                 | Input field separator. Defaults to ",".
interfacetable_cache               | Define the retention time of the cached data in seconds.
interfacetable_noifloadgradient    | Disable color gradient from green over yellow to red for the load percentage. Defaults to false.
interfacetable_nohuman             | Do not translate bandwidth usage in human readable format. Defaults to false.
interfacetable_snapshot            | Force the plugin to run like if it was the first launch. Defaults to false.
interfacetable_timeout             | Define the global timeout limit of the plugin in seconds. Defaults to "15s".
interfacetable_css                 | Define the css stylesheet used by the generated html files. Possible values are "classic", "icinga" or "icinga-alternate1".
interfacetable_config              | Specify a config file to load.
interfacetable_noconfigtable       | Disable configuration table on the generated HTML page. Defaults to false.
interfacetable_notips              | Disable the tips in the generated html tables. Defaults to false.
interfacetable_defaulttablesorting | Default table sorting can be "index" (default) or "name".
interfacetable_tablesplit          | Generate multiple interface tables, one per interface type. Defaults to false.
interfacetable_notype              | Remove the interface type for each interface. Defaults to false.

## iftraffic <a id="iftraffic"></a>

The [check_iftraffic](https://exchange.icinga.com/exchange/iftraffic) plugin
checks the utilization of a given interface name using the SNMP protocol.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
iftraffic_address     | **Required.** Specifies the remote host. Defaults to "$address$".
iftraffic_community   | SNMP community. Defaults to "public'" if omitted.
iftraffic_interface   | **Required.** Queried interface name.
iftraffic_bandwidth   | **Required.** Interface maximum speed in kilo/mega/giga/bits per second.
iftraffic_units       | Interface units can be one of these values: `g` (gigabits/s),`m` (megabits/s), `k` (kilobits/s),`b` (bits/s)
iftraffic_warn        | Percent of bandwidth usage necessary to result in warning status (defaults to `85`).
iftraffic_crit        | Percent of bandwidth usage necessary to result in critical status (defaults to `98`).
iftraffic_max_counter | Maximum counter value of net devices in kilo/mega/giga/bytes.

## iftraffic64 <a id="iftraffic64"></a>

The [check_iftraffic64](https://exchange.icinga.com/exchange/iftraffic64) plugin
checks the utilization of a given interface name using the SNMP protocol.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|------------
iftraffic64_address     | **Required.** Specifies the remote host. Defaults to "$address$".
iftraffic64_community   | SNMP community. Defaults to "public'" if omitted.
iftraffic64_interface   | **Required.** Queried interface name.
iftraffic64_bandwidth   | **Required.** Interface maximum speed in kilo/mega/giga/bits per second.
iftraffic64_units       | Interface units can be one of these values: `g` (gigabits/s),`m` (megabits/s), `k` (kilobits/s),`b` (bits/s)
iftraffic64_warn        | Percent of bandwidth usage necessary to result in warning status (defaults to `85`).
iftraffic64_crit        | Percent of bandwidth usage necessary to result in critical status (defaults to `98`).
iftraffic64_max_counter | Maximum counter value of net devices in kilo/mega/giga/bytes.

## interfaces <a id="interfaces"></a>

The [check_interfaces](https://git.netways.org/plugins/check_interfaces) plugin
uses SNMP to monitor network interfaces and their utilization.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
interfaces_address       | The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
interfaces_regex         | Interface list regexp.
interfaces_exclude_regex | Interface list negative regexp.
interfaces_errors        | Number of in errors (CRC errors for cisco) to consider a warning (default 50).
interface_out_errors     | Number of out errors (collisions for cisco) to consider a warning (default same as in errors).
interfaces_perfdata      | perfdata from last check result.
interfaces_prefix        | Prefix interface names with this label.
interfaces_lastcheck     | Last checktime (unixtime).
interfaces_bandwidth     | Bandwidth warn level in percent.
interfaces_speed         | Override speed detection with this value (bits per sec).
interfaces_trim          | Cut this number of characters from the start of interface descriptions.
interfaces_mode          | Special operating mode (default,cisco,nonbulk,bintec).
interfaces_auth_proto    | SNMPv3 Auth Protocol (SHA\|MD5)
interfaces_auth_phrase   | SNMPv3 Auth Phrase
interfaces_priv_proto    | SNMPv3 Privacy Protocol (AES\|DES)
interfaces_priv_phrase   | SNMPv3 Privacy Phrase
interfaces_user          | SNMPv3 User
interfaces_down_is_ok    | Disables critical alerts for down interfaces.
interfaces_aliases       | Retrieves the interface description.
interfaces_match_aliases | Also match against aliases (Option --aliases automatically enabled).
interfaces_timeout       | Sets the SNMP timeout (in ms).
interfaces_sleep         | Sleep between every SNMP query (in ms).
interfaces_names         | If set to true, use ifName instead of ifDescr.

## nwc_health <a id="nwc_health"></a>

The [check_nwc_health](https://labs.consol.de/de/nagios/check_nwc_health/index.html) plugin
uses SNMP to monitor network components. The plugin is able to generate interface statistics,
check hardware (CPU, memory, fan, power, etc.), monitor firewall policies, HRSP, load-balancer
pools, processor and memory usage.

Currently the following network components are supported: Cisco IOS, Cisco Nexus, Cisco ASA,
Cisco PIX, F5 BIG-IP, CheckPoint Firewall1, Juniper NetScreen, HP Procurve, Nortel, Brocade 4100/4900,
EMC DS 4700, EMC DS 24, Allied Telesyn. Blue Coat SG600, Cisco Wireless Lan Controller 5500,
Brocade ICX6610-24-HPOE, Cisco UC Telefonzeugs, FOUNDRY-SN-AGENT-MIB, FRITZ!BOX 7390, FRITZ!DECT 200,
Juniper IVE, Pulse-Gateway MAG4610, Cisco IronPort AsyncOS, Foundry, etc. A complete list can be
found in the plugin [documentation](https://labs.consol.de/nagios/check_nwc_health/index.html).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                         | Description
-----------------------------|------------
nwc_health_hostname          | The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
nwc_health_mode              | The plugin mode. A list of all available modes can be found in the [plugin documentation](https://labs.consol.de/nagios/check_nwc_health/index.html).
nwc_health_timeout           | Seconds before plugin times out (default: 15)
nwc_health_blacklist         | Blacklist some (missing/failed) components.
nwc_health_port              | The SNMP port to use (default: 161).
nwc_health_domain            | The transport domain to use (default: udp/ipv4, other possible values: udp6, udp/ipv6, tcp, tcp4, tcp/ipv4, tcp6, tcp/ipv6).
nwc_health_protocol          | The SNMP protocol to use (default: 2c, other possibilities: 1,3).
nwc_health_community         | SNMP community of the server (SNMP v1/2 only).
nwc_health_username          | The securityName for the USM security model (SNMPv3 only).
nwc_health_authpassword      | The authentication password for SNMPv3.
nwc_health_authprotocol      | The authentication protocol for SNMPv3 (md5\|sha).
nwc_health_privpassword      | The password for authPriv security level.
nwc_health_privprotocol      | The private protocol for SNMPv3 (des\|aes\|aes128\|3des\|3desde).
nwc_health_contextengineid   | The context engine id for SNMPv3 (10 to 64 hex characters).
nwc_health_contextname       | The context name for SNMPv3 (empty represents the default context).
nwc_health_name              | The name of an interface (ifDescr).
nwc_health_drecksptkdb       | This parameter must be used instead of --name, because Devel::ptkdb is stealing the latter from the command line.
nwc_health_alias             | The alias name of a 64bit-interface (ifAlias)
nwc_health_regexp            | A flag indicating that --name is a regular expression
nwc_health_ifspeedin         | Override the ifspeed oid of an interface (only inbound)
nwc_health_ifspeedout        | Override the ifspeed oid of an interface (only outbound)
nwc_health_ifspeed           | Override the ifspeed oid of an interface
nwc_health_units             | One of %, B, KB, MB, GB, Bit, KBi, MBi, GBi. (used for e.g. mode interface-usage)
nwc_health_name2             | The secondary name of a component.
nwc_health_role              | The role of this device in a hsrp group (active/standby/listen).
nwc_health_report            | Can be used to shorten the output. Possible values are: 'long' (default), 'short' (to shorten if available), or 'html' (to produce some html outputs if available)
nwc_health_lookback          | The amount of time you want to look back when calculating average rates. Use it for mode interface-errors or interface-usage. Without --lookback the time between two runs of check_nwc_health is the base for calculations. If you want your checkresult to be based for example on the past hour, use --lookback 3600.
nwc_health_warning           | The warning threshold
nwc_health_critical          | The critical threshold
nwc_health_warningx          | The extended warning thresholds
nwc_health_criticalx         | The extended critical thresholds
nwc_health_mitigation        | The parameter allows you to change a critical error to a warning (1) or ok (0).
nwc_health_selectedperfdata  | The parameter allows you to limit the list of performance data. It's a perl regexp. Only matching perfdata show up in the output.
nwc_health_morphperfdata     | The parameter allows you to change performance data labels. It's a perl regexp and a substitution. --morphperfdata '(.*)ISATAP(.*)'='$1patasi$2'
nwc_health_negate            | The parameter allows you to map exit levels, such as warning=critical.
nwc_health_mymodules-dyn-dir | A directory where own extensions can be found.
nwc_health_servertype        | The type of the network device: cisco (default). Use it if auto-detection is not possible.
nwc_health_statefilesdir     | An alternate directory where the plugin can save files.
nwc_health_oids              | A list of oids which are downloaded and written to a cache file. Use it together with --mode oidcache.
nwc_health_offline           | The maximum number of seconds since the last update of cache file before it is considered too old.
nwc_health_multiline         | Multiline output
