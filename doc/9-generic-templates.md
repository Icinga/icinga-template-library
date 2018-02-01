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
