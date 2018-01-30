# Network Components <a id="network-components"></a>

This category includes all plugins for various network components like routers, switches and firewalls.

## interfacetable <a id="interfacetable"></a>

The [check_interfacetable_v3t](http://www.tontonitch.com/tiki/tiki-index.php?page=Nagios+plugins+-+interfacetable_v3t) plugin
generates a html page containing information about the monitored node and all of its interfaces.

The Git repository is located on [GitHub](https://github.com/Tontonitch/interfacetable_v3t).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                                | Description
------------------------------------|-----------------------------------------------------------------------------------------------------
interfacetable_hostquery            | **Required.** Specifies the remote host to poll. Defaults to "$address$".
interfacetable_hostdisplay          | **Optional.** Specifies the hostname to display in the HTML link. Defaults to "$host.display_name$".
interfacetable_regex                | **Optional.** Interface names and property names for some other options will be interpreted as regular expressions. Defaults to false.
interfacetable_outputshort          | **Optional.** Reduce the verbosity of the plugin output. Defaults to false.
interfacetable_exclude              | **Optional.** Comma separated list of interfaces globally excluded from the monitoring.
interfacetable_include              | **Optional.** Comma separated list of interfaces globally included in the monitoring.
interfacetable_aliasmatching        | **Optional.** Allow you to specify alias in addition to interface names. Defaults to false.
interfacetable_excludetraffic       | **Optional.** Comma separated list of interfaces excluded from traffic checks.
interfacetable_includetraffic       | **Optional.** Comma separated list of interfaces included for traffic checks.
interfacetable_warningtraffic       | **Optional.** Interface traffic load percentage leading to a warning alert.
interfacetable_criticaltraffic      | **Optional.** Interface traffic load percentage leading to a critical alert.
interfacetable_pkt                  | **Optional.** Add unicast/non-unicast pkt stats for each interface.
interfacetable_trafficwithpkt       | **Optional.** Enable traffic calculation using pkt counters instead of octet counters. Useful when using 32-bit counters to track the load on > 1GbE interfaces. Defaults to false.
interfacetable_trackproperty        | **Optional.** List of tracked properties.
interfacetable_excludeproperty      | **Optional.** Comma separated list of interfaces excluded from the property tracking.
interfacetable_includeproperty      | **Optional.** Comma separated list of interfaces included in the property tracking.
interfacetable_community            | **Optional.** Specifies the snmp v1/v2c community string. Defaults to "public" if using snmp v1/v2c, ignored using v3.
interfacetable_snmpv2               | **Optional.** Use snmp v2c. Defaults to false.
interfacetable_login                | **Optional.** Login for snmpv3 authentication.
interfacetable_passwd               | **Optional.** Auth password for snmpv3 authentication.
interfacetable_privpass             | **Optional.** Priv password for snmpv3 authentication.
interfacetable_protocols            | **Optional.** Authentication protocol,Priv protocol for snmpv3 authentication.
interfacetable_domain               | **Optional.** SNMP transport domain.
interfacetable_contextname          | **Optional.** Context name for the snmp requests.
interfacetable_port                 | **Optional.** SNMP port. Defaults to standard port.
interfacetable_64bits               | **Optional.** Use SNMP 64-bits counters. Defaults to false.
interfacetable_maxrepetitions       | **Optional.** Increasing this value may enhance snmp query performances by gathering more results at one time.
interfacetable_snmptimeout          | **Optional.** Define the Transport Layer timeout for the snmp queries.
interfacetable_snmpretries          | **Optional.** Define the number of times to retry sending a SNMP message.
interfacetable_snmpmaxmsgsize       | **Optional.** Size of the SNMP message in octets, useful in case of too long responses. Be careful with network filters. Range 484 - 65535. Apply only to netsnmp perl bindings. The default is 1472 octets for UDP/IPv4, 1452 octets for UDP/IPv6, 1460 octets for TCP/IPv4, and 1440 octets for TCP/IPv6.
interfacetable_unixsnmp             | **Optional.** Use unix snmp utilities for snmp requests. Defaults to false, which means use the perl bindings.
interfacetable_enableperfdata       | **Optional.** Enable port performance data. Defaults to false.
interfacetable_perfdataformat       | **Optional.** Define which performance data will be generated. Possible values are "full" (default), "loadonly", "globalonly".
interfacetable_perfdatathreshold    | **Optional.** Define which thresholds are printed in the generated performance data. Possible values are "full" (default), "loadonly", "globalonly".
interfacetable_perfdatadir          | **Optional.** When specified, the performance data are also written directly to a file, in the specified location.
interfacetable_perfdataservicedesc  | **Optional.** Specify additional parameters for output performance data to PNP. Defaults to "$service.name$", only affects **interfacetable_perfdatadir**.
interfacetable_grapher              | **Optional.** Specify the used graphing solution. Possible values are "pnp4nagios" (default), "nagiosgrapher", "netwaysgrapherv2" and "ingraph".
interfacetable_grapherurl           | **Optional.** Graphing system url. Default depends on **interfacetable_grapher**.
interfacetable_portperfunit         | **Optional.** Traffic could be reported in bits (counters) or in bps (calculated value).
interfacetable_nodetype             | **Optional.** Specify the node type, for specific information to be printed / specific oids to be used. Possible values: "standard" (default), "cisco", "hp", "netscreen", "netapp", "bigip", "bluecoat", "brocade", "brocade-nos", "nortel", "hpux".
interfacetable_duplex               | **Optional.** Add the duplex mode property for each interface in the interface table. Defaults to false.
interfacetable_stp                  | **Optional.** Add the stp state property for each interface in the interface table. Defaults to false.
interfacetable_vlan                 | **Optional.** Add the vlan attribution property for each interface in the interface table. Defaults to false. This option is available only for the following nodetypes: "cisco", "hp", "nortel"
interfacetable_noipinfo             | **Optional.** Remove the ip information for each interface from the interface table. Defaults to false.
interfacetable_alias                | **Optional.** Add the alias information for each interface in the interface table. Defaults to false.
interfacetable_accessmethod         | **Optional.** Access method for a shortcut to the host in the HTML page. Format is : <method>[:<target>] Where method can be: ssh, telnet, http or https.
interfacetable_htmltablelinktarget  | **Optional.** Specifies the windows or the frame where the [details] link will load the generated html page. Possible values are: "_blank", "_self" (default), "_parent", "_top", or a frame name.
interfacetable_delta                | **Optional.** Set the delta used for interface throughput calculation in seconds.
interfacetable_ifs                  | **Optional.** Input field separator. Defaults to ",".
interfacetable_cache                | **Optional.** Define the retention time of the cached data in seconds.
interfacetable_noifloadgradient     | **Optional.** Disable color gradient from green over yellow to red for the load percentage. Defaults to false.
interfacetable_nohuman              | **Optional.** Do not translate bandwidth usage in human readable format. Defaults to false.
interfacetable_snapshot             | **Optional.** Force the plugin to run like if it was the first launch. Defaults to false.
interfacetable_timeout              | **Optional.** Define the global timeout limit of the plugin in seconds. Defaults to "15s".
interfacetable_css                  | **Optional.** Define the css stylesheet used by the generated html files. Possible values are "classic", "icinga" or "icinga-alternate1".
interfacetable_config               | **Optional.** Specify a config file to load.
interfacetable_noconfigtable        | **Optional.** Disable configuration table on the generated HTML page. Defaults to false.
interfacetable_notips               | **Optional.** Disable the tips in the generated html tables. Defaults to false.
interfacetable_defaulttablesorting  | **Optional.** Default table sorting can be "index" (default) or "name".
interfacetable_tablesplit           | **Optional.** Generate multiple interface tables, one per interface type. Defaults to false.
interfacetable_notype               | **Optional.** Remove the interface type for each interface. Defaults to false.

## iftraffic <a id="iftraffic"></a>

The [check_iftraffic](https://exchange.icinga.com/exchange/iftraffic) plugin
checks the utilization of a given interface name using the SNMP protocol.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|---------------------------------------------------------
iftraffic_address	| **Required.** Specifies the remote host. Defaults to "$address$".
iftraffic_community	| **Optional.** SNMP community. Defaults to "public'" if omitted.
iftraffic_interface	| **Required.** Queried interface name.
iftraffic_bandwidth	| **Required.** Interface maximum speed in kilo/mega/giga/bits per second.
iftraffic_units		| **Optional.** Interface units can be one of these values: `g` (gigabits/s),`m` (megabits/s), `k` (kilobits/s),`b` (bits/s)
iftraffic_warn		| **Optional.** Percent of bandwidth usage necessary to result in warning status (defaults to `85`).
iftraffic_crit		| **Optional.** Percent of bandwidth usage necessary to result in critical status (defaults to `98`).
iftraffic_max_counter	| **Optional.** Maximum counter value of net devices in kilo/mega/giga/bytes.

## iftraffic64 <a id="iftraffic64"></a>

The [check_iftraffic64](https://exchange.icinga.com/exchange/iftraffic64) plugin
checks the utilization of a given interface name using the SNMP protocol.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|---------------------------------------------------------
iftraffic64_address     | **Required.** Specifies the remote host. Defaults to "$address$".
iftraffic64_community   | **Optional.** SNMP community. Defaults to "public'" if omitted.
iftraffic64_interface   | **Required.** Queried interface name.
iftraffic64_bandwidth   | **Required.** Interface maximum speed in kilo/mega/giga/bits per second.
iftraffic64_units       | **Optional.** Interface units can be one of these values: `g` (gigabits/s),`m` (megabits/s), `k` (kilobits/s),`b` (bits/s)
iftraffic64_warn        | **Optional.** Percent of bandwidth usage necessary to result in warning status (defaults to `85`).
iftraffic64_crit        | **Optional.** Percent of bandwidth usage necessary to result in critical status (defaults to `98`).
iftraffic64_max_counter	| **Optional.** Maximum counter value of net devices in kilo/mega/giga/bytes.

## interfaces <a id="interfaces"></a>

The [check_interfaces](https://git.netways.org/plugins/check_interfaces) plugin
uses SNMP to monitor network interfaces and their utilization.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                      | Description
--------------------------|---------------------------------------------------------
interfaces_address        | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
interfaces_regex          | **Optional.** Interface list regexp.
interfaces_exclude_regex  | **Optional.** Interface list negative regexp.
interfaces_errors         | **Optional.** Number of in errors (CRC errors for cisco) to consider a warning (default 50).
interface_out_errors      | **Optional.** Number of out errors (collisions for cisco) to consider a warning (default same as in errors).
interfaces_perfdata       | **Optional.** perfdata from last check result.
interfaces_prefix         | **Optional.** Prefix interface names with this label.
interfaces_lastcheck      | **Optional.** Last checktime (unixtime).
interfaces_bandwidth      | **Optional.** Bandwidth warn level in percent.
interfaces_speed          | **Optional.** Override speed detection with this value (bits per sec).
interfaces_trim           | **Optional.** Cut this number of characters from the start of interface descriptions.
interfaces_mode           | **Optional.** Special operating mode (default,cisco,nonbulk,bintec).
interfaces_auth_proto     | **Optional.** SNMPv3 Auth Protocol (SHA\|MD5)
interfaces_auth_phrase    | **Optional.** SNMPv3 Auth Phrase
interfaces_priv_proto     | **Optional.** SNMPv3 Privacy Protocol (AES\|DES)
interfaces_priv_phrase    | **Optional.** SNMPv3 Privacy Phrase
interfaces_user           | **Optional.** SNMPv3 User
interfaces_down_is_ok     | **Optional.** Disables critical alerts for down interfaces.
interfaces_aliases        | **Optional.** Retrieves the interface description.
interfaces_match_aliases  | **Optional.** Also match against aliases (Option --aliases automatically enabled).
interfaces_timeout        | **Optional.** Sets the SNMP timeout (in ms).
interfaces_sleep          | **Optional.** Sleep between every SNMP query (in ms).
interfaces_names          | **Optional.** If set to true, use ifName instead of ifDescr.

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

Name                      	| Description
--------------------------------|---------------------------------------------------------
nwc_health_hostname             | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
nwc_health_mode                 | **Optional.** The plugin mode. A list of all available modes can be found in the [plugin documentation](https://labs.consol.de/nagios/check_nwc_health/index.html).
nwc_health_timeout	  	| **Optional.** Seconds before plugin times out (default: 15)
nwc_health_blacklist	  	| **Optional.** Blacklist some (missing/failed) components.
nwc_health_port		  	| **Optional.** The SNMP port to use (default: 161).
nwc_health_domain	  	| **Optional.** The transport domain to use (default: udp/ipv4, other possible values: udp6, udp/ipv6, tcp, tcp4, tcp/ipv4, tcp6, tcp/ipv6).
nwc_health_protocol	  	| **Optional.** The SNMP protocol to use (default: 2c, other possibilities: 1,3).
nwc_health_community	  	| **Optional.** SNMP community of the server (SNMP v1/2 only).
nwc_health_username	  	| **Optional.** The securityName for the USM security model (SNMPv3 only).
nwc_health_authpassword	  	| **Optional.** The authentication password for SNMPv3.
nwc_health_authprotocol	  	| **Optional.** The authentication protocol for SNMPv3 (md5\|sha).
nwc_health_privpassword   	| **Optional.** The password for authPriv security level.
nwc_health_privprotocol		| **Optional.** The private protocol for SNMPv3 (des\|aes\|aes128\|3des\|3desde).
nwc_health_contextengineid	| **Optional.** The context engine id for SNMPv3 (10 to 64 hex characters).
nwc_health_contextname		| **Optional.** The context name for SNMPv3 (empty represents the default context).
nwc_health_name			| **Optional.** The name of an interface (ifDescr).
nwc_health_drecksptkdb		| **Optional.** This parameter must be used instead of --name, because Devel::ptkdb is stealing the latter from the command line.
nwc_health_alias		| **Optional.** The alias name of a 64bit-interface (ifAlias)
nwc_health_regexp		| **Optional.** A flag indicating that --name is a regular expression
nwc_health_ifspeedin		| **Optional.** Override the ifspeed oid of an interface (only inbound)
nwc_health_ifspeedout		| **Optional.** Override the ifspeed oid of an interface (only outbound)
nwc_health_ifspeed		| **Optional.** Override the ifspeed oid of an interface
nwc_health_units		| **Optional.** One of %, B, KB, MB, GB, Bit, KBi, MBi, GBi. (used for e.g. mode interface-usage)
nwc_health_name2		| **Optional.** The secondary name of a component.
nwc_health_role			| **Optional.** The role of this device in a hsrp group (active/standby/listen).
nwc_health_report		| **Optional.** Can be used to shorten the output. Possible values are: 'long' (default), 'short' (to shorten if available), or 'html' (to produce some html outputs if available)
nwc_health_lookback		| **Optional.** The amount of time you want to look back when calculating average rates. Use it for mode interface-errors or interface-usage. Without --lookback the time between two runs of check_nwc_health is the base for calculations. If you want your checkresult to be based for example on the past hour, use --lookback 3600.
nwc_health_warning		| **Optional.** The warning threshold
nwc_health_critical		| **Optional.** The critical threshold
nwc_health_warningx		| **Optional.** The extended warning thresholds
nwc_health_criticalx		| **Optional.** The extended critical thresholds
nwc_health_mitigation		| **Optional.** The parameter allows you to change a critical error to a warning (1) or ok (0).
nwc_health_selectedperfdata	| **Optional.** The parameter allows you to limit the list of performance data. It's a perl regexp. Only matching perfdata show up in the output.
nwc_health_morphperfdata	| **Optional.** The parameter allows you to change performance data labels. It's a perl regexp and a substitution. --morphperfdata '(.*)ISATAP(.*)'='$1patasi$2'
nwc_health_negate		| **Optional.** The parameter allows you to map exit levels, such as warning=critical.
nwc_health_mymodules-dyn-dir	| **Optional.** A directory where own extensions can be found.
nwc_health_servertype		| **Optional.** The type of the network device: cisco (default). Use it if auto-detection is not possible.
nwc_health_statefilesdir	| **Optional.** An alternate directory where the plugin can save files.
nwc_health_oids			| **Optional.** A list of oids which are downloaded and written to a cache file. Use it together with --mode oidcache.
nwc_health_offline		| **Optional.** The maximum number of seconds since the last update of cache file before it is considered too old.
nwc_health_multiline		| **Optional.** Multiline output
