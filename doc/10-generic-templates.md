# Generic Templates <a id="generic-templates"></a>

By default the generic templates are included in the [icinga2.conf](04-configuring-icinga-2.md#icinga2-conf) configuration file:

```
include <itl>
```

These templates are imported by the provided example configuration.

> **Note**:
>
> These templates are built into the binaries. By convention
> all command and timeperiod objects should import these templates.

## plugin-check-command <a id="plugin-check-command"></a>

Command template for check plugins executed by Icinga 2.

The `plugin-check-command` command does not support any vars.

By default this template is automatically imported into all [CheckCommand](09-object-types.md#objecttype-checkcommand) definitions.

## plugin-notification-command <a id="plugin-notification-command"></a>

Command template for notification scripts executed by Icinga 2.

The `plugin-notification-command` command does not support any vars.

By default this template is automatically imported into all [NotificationCommand](09-object-types.md#objecttype-notificationcommand) definitions.

## plugin-event-command <a id="plugin-event-command"></a>

Command template for event handler scripts executed by Icinga 2.

The `plugin-event-command` command does not support any vars.

By default this template is automatically imported into all [EventCommand](09-object-types.md#objecttype-eventcommand) definitions.

## legacy-timeperiod <a id="legacy-timeperiod"></a>

Timeperiod template for [Timeperiod objects](09-object-types.md#objecttype-timeperiod).

The `legacy-timeperiod` timeperiod does not support any vars.

By default this template is automatically imported into all [TimePeriod](09-object-types.md#objecttype-timeperiod) definitions.

# Check Commands <a id="check-commands"></a>

These check commands are embedded into Icinga 2 and do not require any external
plugin scripts.

## icinga <a id="icinga"></a>

Check command for the built-in `icinga` check. This check returns performance
data for the current Icinga instance and optionally allows for minimum version checks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name               | Description
-------------------|------------
icinga_min_version | **Optional.** Required minimum Icinga 2 version, e.g. `2.8.0`. If not satisfied, the state changes to `Critical`. Release packages only.

## cluster <a id="icinga-cluster"></a>

Check command for the built-in `cluster` check. This check returns performance
data for the current Icinga instance and connected endpoints.

The `cluster` check command does not support any vars.

## cluster-zone <a id="icinga-cluster-zone"></a>

Check command for the built-in `cluster-zone` check.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                 | Description
---------------------|------------
cluster_zone         | **Required.** The zone name. Defaults to `$host.name$`.
cluster_lag_warning  | **Optional.** Warning threshold for log lag in seconds. Applies if the log lag is greater than the threshold.
cluster_lag_critical | **Optional.** Critical threshold for log lag in seconds. Applies if the log lag is greater than the threshold.

## ido <a id="icinga-ido"></a>

Check command for the built-in `ido` check.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                         | Description
-----------------------------|------------
ido_type                     | **Required.** The type of the IDO connection object. Can be either "IdoMysqlConnection" or "IdoPgsqlConnection".
ido_name                     | **Required.** The name of the IDO connection object.
ido_queries_warning          | **Optional.** Warning threshold for queries/s. Applies if the rate is lower than the threshold.
ido_queries_critical         | **Optional.** Critical threshold for queries/s. Applies if the rate is lower than the threshold.
ido_pending_queries_warning  | **Optional.** Warning threshold for pending queries. Applies if pending queries are higher than the threshold. Supersedes the `ido_queries` thresholds above.
ido_pending_queries_critical | **Optional.** Critical threshold for pending queries. Applies if pending queries are higher than the threshold. Supersedes the `ido_queries` thresholds above.

## dummy <a id="dummy"></a>

Check command for the built-in `dummy` check. This allows to set
a check result state and output and can be used in [freshness checks](08-advanced-topics.md#check-result-freshness)
or [runtime object checks](08-advanced-topics.md#access-object-attributes-at-runtime).
In contrast to the [check_dummy](https://www.monitoring-plugins.org/doc/man/check_dummy.html)
plugin, Icinga 2 implements a light-weight in memory check with 2.9+.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name        | Description
------------|------------
dummy_state | **Optional.** The state. Can be one of 0 (ok), 1 (warning), 2 (critical) and 3 (unknown). Defaults to 0.
dummy_text  | **Optional.** Plugin output. Defaults to "Check was successful.".

## random <a id="random"></a>

Check command for the built-in `random` check. This check returns random states
and adds the check source to the check output.

For test and demo purposes only. The `random` check command does not support
any vars.

## exception <a id="exception"></a>

Check command for the built-in `exception` check. This check throws an exception.

For test and demo purposes only. The `exception` check command does not support
any vars.
