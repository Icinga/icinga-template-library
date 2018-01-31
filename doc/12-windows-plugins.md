# Windows Plugins for Icinga 2 <a id="windows-plugins"></a>

To allow a basic monitoring of Windows clients Icinga 2 comes with a set of Windows only plugins. While trying to mirror the functionalities of their linux cousins from the monitoring-plugins package, the differences between Windows and Linux are too big to be able use the same CheckCommands for both systems.

A check-commands-windows.conf comes with Icinga 2, it assumes that the Windows Plugins are installed in the PluginDir set in your constants.conf. To enable them the following include directive is needed in you icinga2.conf:

```
include <windows-plugins>
```

One of the differences between the Windows plugins and their linux counterparts is that they consistently do not require thresholds to run, functioning like dummies without.

## Threshold syntax <a id="windows-plugins-thresholds"></a>

So not specified differently the thresholds for the plugins all follow the same pattern

Threshold  | Meaning
-----------|--------
"29"       | The threshold is 29.
"!29"      | The threshold is 29, but the negative of the result is returned.
"[10-40]"  | The threshold is a range from (including) 10 to 40, a value inside means the threshold has been exceeded.
"![10-40]" | Same as above, but the result is inverted.

## disk-windows <a id="windows-plugins-disk-windows"></a>

Check command object for the `check_disk.exe` plugin.
Aggregates the disk space of all volumes and mount points it can find, or the ones defined in `disk_win_path`. Ignores removable storage like flash drives and discs (CD, DVD etc.).
The data collection is instant and free disk space (default, see `disk_win_show_used`) is used for threshold computation.

> **Note**
>
> Percentage based thresholds can be used by adding a '%' to the threshold
> value.

Custom attributes:

Name               | Description
-------------------|------------
disk_win_warn      | **Optional**. The warning threshold.
disk_win_crit      | **Optional**. The critical threshold.
disk_win_path      | **Optional**. Check only these paths, default checks all.
disk_win_unit      | **Optional**. Use this unit to display disk space, thresholds are interpreted in this unit. Defaults to "mb", possible values are: b, kb, mb, gb and tb.
disk_win_exclude   | **Optional**. Exclude these drives from check.
disk_win_show_used | **Optional**. Use used instead of free space.

## load-windows <a id="windows-plugins-load-windows"></a>

Check command object for the `check_load.exe` plugin.
This plugin collects the inverse of the performance counter `\Processor(_Total)\% Idle Time` two times, with a wait time of one second between the collection. To change this wait time use [`perfmon-windows`](10-icinga-template-library.md#windows-plugins-load-windows).

Custom attributes:

Name          | Description
--------------|------------
load_win_warn | **Optional**. The warning threshold.
load_win_crit | **Optional**. The critical threshold.

## memory-windows <a id="windows-plugins-memory-windows"></a>

Check command object for the `check_memory.exe` plugin.
The memory collection is instant and free memory is used for threshold computation.

> **Note**
>
> Percentage based thresholds can be used by adding a '%' to the threshold
> value. Keep in mind that memory_win_unit is applied before the
> value is calculated.

Custom attributes:

Name            | Description
----------------|------------
memory_win_warn | **Optional**. The warning threshold.
memory_win_crit | **Optional**. The critical threshold.
memory_win_unit | **Optional**. The unit to display the received value in, thresholds are interpreted in this unit. Defaults to "mb" (megabyte), possible values are: b, kb, mb, gb and tb.

## network-windows <a id="windows-plugins-network-windows"></a>

Check command object for the `check_network.exe` plugin.
Collects the total Bytes inbound and outbound for all interfaces in one second, to itemise interfaces or use a different collection interval use [`perfmon-windows`](10-icinga-template-library.md#windows-plugins-load-windows).

Custom attributes:

Name              | Description
------------------|------------
network_win_warn  | **Optional**. The warning threshold.
network_win_crit  | **Optional**. The critical threshold.
network_no_isatap | **Optional**. Do not print ISATAP interfaces.

## perfmon-windows <a id="windows-plugins-perfmon-windows"></a>

Check command object for the `check_perfmon.exe` plugin.
This plugins allows to collect data from a Performance Counter. After the first data collection a second one is done after `perfmon_win_wait` milliseconds. When you know `perfmon_win_counter` only requires one set of data to provide valid data you can set `perfmon_win_wait` to `0`.

To receive a list of possible Performance Counter Objects run `check_perfmon.exe --print-objects` and to view an objects instances and counters run `check_perfmon.exe --print-object-info -P "name of object"`

Custom attributes:

Name                | Description
--------------------|------------
perfmon_win_warn    | **Optional**. The warning threshold.
perfmon_win_crit    | **Optional**. The critical threshold.
perfmon_win_counter | **Required**. The Performance Counter to use. Ex. `\Processor(_Total)\% Idle Time`.
perfmon_win_wait    | **Optional**. Time in milliseconds to wait between data collection (default: 1000).
perfmon_win_type    | **Optional**. Format in which to expect performance values. Possible are: long, int64 and double (default).
perfmon_win_syntax  | **Optional**. Use this in the performance output instead of `perfmon_win_counter`. Exists for graphics compatibility reasons.

## ping-windows <a id="windows-plugins-ping-windows"></a>

Check command object for the `check_ping.exe` plugin.
ping-windows should automatically detect whether `ping_win_address` is an IPv4 or IPv6 address. If not, use ping4-windows and ping6-windows. Also note that check_ping.exe waits at least `ping_win_timeout` milliseconds between the pings.

Custom attributes:

Name             | Description
-----------------|------------
ping_win_warn    | **Optional**. The warning threshold. RTA and package loss separated by comma.
ping_win_crit    | **Optional**. The critical threshold. RTA and package loss separated by comma.
ping_win_address | **Required**. An IPv4 or IPv6 address.
ping_win_packets | **Optional**. Number of packages to send. Default: 5.
ping_win_timeout | **Optional**. The timeout in milliseconds. Default: 1000

## procs-windows <a id="windows-plugins-procs-windows"></a>

Check command object for `check_procs.exe` plugin.
When using `procs_win_user` this plugins needs administrative privileges to access the processes of other users, to just enumerate them no additional privileges are required.

Custom attributes:

Name           | Description
---------------|------------
procs_win_warn | **Optional**. The warning threshold.
procs_win_crit | **Optional**. The critical threshold.
procs_win_user | **Optional**. Count this users processes.

## service-windows <a id="windows-plugins-service-windows"></a>

Check command object for `check_service.exe` plugin.
This checks thresholds work different since the binary decision whether a service is running or not does not allow for three states. As a default `check_service.exe` will return CRITICAL when `service_win_service` is not running, the `service_win_warn` flag changes this to WARNING.

Custom attributes:

Name                    | Description
------------------------|------------
service_win_warn        | **Optional**. Warn when service is not running.
service_win_description | **Optional**. If this is set, `service_win_service` looks at the service description.
service_win_service     | **Required**. Name of the service to check.

## swap-windows <a id="windows-plugins-swap-windows"></a>

Check command object for `check_swap.exe` plugin.
The data collection is instant.

Custom attributes:

Name          | Description
--------------|------------
swap_win_warn | **Optional**. The warning threshold.
swap_win_crit | **Optional**. The critical threshold.
swap_win_unit | **Optional**. The unit to display the received value in, thresholds are interpreted in this unit. Defaults to "mb" (megabyte).

## update-windows <a id="windows-plugins-update-windows"></a>

Check command object for `check_update.exe` plugin.
Querying Microsoft for Windows updates can take multiple seconds to minutes. An update is treated as important when it has the WSUS flag for SecurityUpdates or CriticalUpdates.

> **Note**
>
> The Network Services Account which runs Icinga 2 by default does not have the required
> permissions to run this check.

Custom attributes:

Name              | Description
------------------|------------
update_win_warn   | **Optional**. If set, returns warning when important updates are available.
update_win_crit   | **Optional**. If set, return critical when important updates that require a reboot are available.
update_win_reboot | **Optional**. Set to treat 'may need update' as 'definitely needs update'. Please Note that this is true for almost every update and is therefore not recommended.

In contrast to most other plugins, the values of check_update's custom attributes do not set thresholds, but just enable/disable the behavior described in the table above.
It can be enabled/disabled for example by setting them to "true" or "false", "1" or "0" would also work.
Thresholds will always be "1".

> **Note**
>
> If they are enabled, performance data will be shown in the web interface.
> If run without the optional parameters, the plugin will output critical if any important updates are available.

## uptime-windows <a id="windows-plugins-uptime-windows"></a>

Check command object for `check_uptime.exe` plugin.
Uses GetTickCount64 to get the uptime, so boot time is not included.

Custom attributes:

Name            | Description
----------------|------------
uptime_win_warn | **Optional**. The warning threshold.
uptime_win_crit | **Optional**. The critical threshold.
uptime_win_unit | **Optional**. The unit to display the received value in, thresholds are interpreted in this unit. Defaults to "s"(seconds), possible values are ms (milliseconds), s, m (minutes), h (hours).

## users-windows <a id="windows-plugins-users-windows"></a>

Check command object for `check_users.exe` plugin.

Custom attributes:

Name           | Description
---------------|------------
users_win_warn | **Optional**. The warning threshold.
users_win_crit | **Optional**. The critical threshold.
