# Plugin Check Commands for NSClient++ <a id="nscp-commands"></a>

There are two methods available for querying NSClient++:

* Query the [HTTP API](10-icinga-template-library.md#nscp-check-api) locally or remotely (requires a running NSClient++ service)
* Run a [local CLI check](10-icinga-template-library.md#nscp-check-local) (does not require NSClient++ as a service)

Both methods have their advantages and disadvantages. One thing to
note: If you rely on performance counter delta calculations such as
CPU utilization, please use the HTTP API instead of the CLI sample call.

## nscp_api <a id="nscp-check-api"></a>

`check_nscp_api` is part of the Icinga 2 plugins. This plugin is available for
both, Windows and Linux/Unix.

Verify that the ITL CheckCommand is included in the [icinga2.conf](04-configuring-icinga-2.md#icinga2-conf) configuration file:

```
vim /etc/icinga2/icinga2.conf

include <plugins>
```

`check_nscp_api` runs queries against the NSClient++ API. Therefore NSClient++ needs to have
the `webserver` module enabled, configured and loaded.

You can install the webserver using the following CLI commands:

```
./nscp.exe web install
./nscp.exe web password — –set icinga
```

Now you can define specific [queries](https://docs.nsclient.org/reference/check/CheckHelpers.html#queries)
and integrate them into Icinga 2.

The check plugin `check_nscp_api` can be integrated with the `nscp_api` CheckCommand object:

Custom attributes:

Name               | Description
-------------------|------------
nscp_api_host      | **Required**. NSCP API host address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
nscp_api_port      | **Optional**. NSCP API port. Defaults to `8443`.
nscp_api_password  | **Required**. NSCP API password. Please check the NSCP documentation for setup details.
nscp_api_query     | **Required**. NSCP API query endpoint. Refer to the NSCP documentation for possible values.
nscp_api_arguments | **Optional**. NSCP API arguments dictionary either as single strings or key-value pairs using `=`. Refer to the NSCP documentation.

`nscp_api_arguments` can be used to pass required thresholds to the executed check. The example below
checks the CPU utilization and specifies warning and critical thresholds.

```
check_nscp_api --host 10.0.10.148 --password icinga --query check_cpu --arguments show-all warning='load>40' critical='load>30'
check_cpu CRITICAL: critical(5m: 48%, 1m: 36%), 5s: 0% | 'total 5m'=48%;40;30 'total 1m'=36%;40;30 'total 5s'=0%;40;30
```

## nscp-local <a id="nscp-check-local"></a>

Icinga 2 can use the `nscp client` command to run arbitrary NSClient++ checks locally on the client.

You can enable these check commands by adding the following the include directive in your
[icinga2.conf](04-configuring-icinga-2.md#icinga2-conf) configuration file:

```
include <nscp>
```

You can also optionally specify an alternative installation directory for NSClient++ by adding
the NscpPath constant in your [constants.conf](04-configuring-icinga-2.md#constants-conf) configuration
file:

```
const NscpPath = "C:\\Program Files (x86)\\NSClient++"
```

By default Icinga 2 uses the Microsoft Installer API to determine where NSClient++ is installed. It should
not be necessary to manually set this constant.

Note that it is not necessary to run NSClient++ as a Windows service for these commands to work.

The check command object for NSClient++ is available as `nscp-local`.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name           | Description
---------------|------------
nscp_log_level | **Optional.** The log level. Defaults to "critical".
nscp_load_all  | **Optional.** Whether to load all modules. Defaults to false.
nscp_modules   | **Optional.** An array of NSClient++ modules to load. Defaults to `[ "CheckSystem" ]`.
nscp_boot      | **Optional.** Whether to use the --boot option. Defaults to true.
nscp_query     | **Required.** The NSClient++ query. Try `nscp client -q x` for a list.
nscp_arguments | **Optional.** An array of query arguments.
nscp_showall   | **Optional.** Shows more details in plugin output, default to false.

## nscp-local-cpu <a id="nscp-check-local-cpu"></a>

Check command object for the `check_cpu` NSClient++ plugin.

Name               | Description
-------------------|------------
nscp_cpu_time      | **Optional.** Calculate average usage for the given time intervals. Value has to be an array, default to [ "1m", "5m", "15m" ].
nscp_cpu_warning   | **Optional.** Threshold for WARNING state in percent, default to 80.
nscp_cpu_critical  | **Optional.** Threshold for CRITICAL state in percent, default to 90.
nscp_cpu_arguments | **Optional.** Additional arguments.
nscp_cpu_showall   | **Optional.** Shows more details in plugin output, default to false.

## nscp-local-memory <a id="nscp-check-local-memory"></a>

Check command object for the `check_memory` NSClient++ plugin.

Name                  | Description
----------------------|------------
nscp_memory_committed | **Optional.** Check for committed memory, default to false.
nscp_memory_physical  | **Optional.** Check for physical memory, default to true.
nscp_memory_free      | **Optional.** Switch between checking free (true) or used memory (false), default to false.
nscp_memory_warning   | **Optional.** Threshold for WARNING state in percent or absolute (use MB, GB, ...), default to 80 (free=false) or 20 (free=true).
nscp_memory_critical  | **Optional.** Threshold for CRITICAL state in percent or absolute (use MB, GB, ...), default to 90 (free=false) or 10 (free=true).
nscp_memory_arguments | **Optional.** Additional arguments.
nscp_memory_showall   | **Optional.** Shows more details in plugin output, default to false.

## nscp-local-os-version <a id="nscp-check-local-os-version"></a>

Check command object for the `check_os_version` NSClient++ plugin.

This command has the same custom attributes like the `nscp-local` check command.

## nscp-local-pagefile <a id="nscp-check-local-pagefile"></a>

Check command object for the `check_pagefile` NSClient++ plugin.

This command has the same custom attributes like the `nscp-local` check command.

## nscp-local-process <a id="nscp-check-local-process"></a>

Check command object for the `check_process` NSClient++ plugin.

This command has the same custom attributes like the `nscp-local` check command.

## nscp-local-service <a id="nscp-check-local-service"></a>

Check command object for the `check_service` NSClient++ plugin.

Name                   | Description
-----------------------|------------
nscp_service_name      | **Required.** Name of service to check.
nscp_service_type      | **Optional.** Type to check, default to state.
nscp_service_ok        | **Optional.** State for return an OK, i.e. for type=state running, stopped, ...
nscp_service_otype     | **Optional.** Dedicate type for nscp_service_ok, default to nscp_service_state.
nscp_service_warning   | **Optional.** State for return an WARNING.
nscp_service_wtype     | **Optional.** Dedicate type for nscp_service_warning, default to nscp_service_state.
nscp_service_critical  | **Optional.** State for return an CRITICAL.
nscp_service_ctype     | **Optional.** Dedicate type for nscp_service_critical, default to nscp_service_state.
nscp_service_arguments | **Optional.** Additional arguments.
nscp_service_showall   | **Optional.** Shows more details in plugin output, default to true.

## nscp-local-uptime <a id="nscp-check-local-uptime"></a>

Check command object for the `check_uptime` NSClient++ plugin.

This command has the same custom attributes like the `nscp-local` check command.

## nscp-local-version <a id="nscp-check-local-version"></a>

Check command object for the `check_version` NSClient++ plugin.

This command has the same custom attributes like the `nscp-local` check command.
In addition to that the default value for `nscp_modules` is set to `[ "CheckHelpers" ]`.

## nscp-local-disk <a id="nscp-check-local-disk"></a>

Check command object for the `check_drivesize` NSClient++ plugin.

Name                | Description
--------------------|------------
nscp_disk_drive     | **Optional.** Drive character, default to all drives.
nscp_disk_free      | **Optional.** Switch between checking free space (free=true) or used space (free=false), default to false.
nscp_disk_warning   | **Optional.** Threshold for WARNING in percent or absolute (use MB, GB, ...), default to 80 (used) or 20 percent (free).
nscp_disk_critical  | **Optional.** Threshold for CRITICAL in percent or absolute (use MB, GB, ...), default to 90 (used) or 10 percent (free).
nscp_disk_arguments | **Optional.** Additional arguments.
nscp_disk_showall   | **Optional.** Shows more details in plugin output, default to true.
nscp_modules        | **Optional.** An array of NSClient++ modules to load. Defaults to `[ "CheckDisk" ]`.

## nscp-local-counter <a id="nscp-check-local-counter"></a>

Check command object for the `check_pdh` NSClient++ plugin.

Name                    | Description
------------------------|------------
nscp_counter_name       | **Required.** Performance counter name.
nscp_counter_warning    | **Optional.** WARNING Threshold.
nscp_counter_critical   | **Optional.** CRITICAL Threshold.
nscp_counter_arguments  | **Optional.** Additional arguments.
nscp_counter_showall    | **Optional.** Shows more details in plugin output, default to false.
nscp_counter_perfsyntax | **Optional.** Apply performance data label, e.g. `Total Processor Time` to avoid special character problems. Defaults to `nscp_counter_name`.
