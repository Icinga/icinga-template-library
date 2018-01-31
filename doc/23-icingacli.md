# IcingaCLI <a id="icingacli"></a>

This category includes all plugins using the icingacli provided by Icinga Web 2.

The user running Icinga 2 needs sufficient permissions to read the Icinga Web 2 configuration directory. e.g. `usermod -a -G icingaweb2 icinga`. You need to restart, not reload Icinga 2 for the new group membership to work.

## Business Process <a id="icingacli-businessprocess"></a>

This subcommand is provided by the [business process module](https://exchange.icinga.com/icinga/Business+Process)
and executed as `icingacli businessprocess` CLI command.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                                | Description
------------------------------------|------------
icingacli_businessprocess_process   | **Required.** Business process to monitor.
icingacli_businessprocess_config    | **Optional.** Configuration file containing your business process without file extension.
icingacli_businessprocess_details   | **Optional.** Get details for root cause analysis. Defaults to false.
icingacli_businessprocess_statetype | **Optional.** Define which state type to look at, `soft` or `hard`. Overrides the default value inside the businessprocess module, if configured.

## Director <a id="icingacli-director"></a>

This subcommand is provided by the [director module](https://github.com/Icinga/icingaweb2-module-director) > 1.4.2 and executed as `icingacli director health check`. Please refer to the [documentation](https://github.com/Icinga/icingaweb2-module-director/blob/master/doc/60-CLI.md#health-check-plugin) for all available sub-checks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|------------
icingacli_director_check | **Optional.** Run only a specific test suite.
icingacli_director_db    | **Optional.** Use a specific Icinga Web DB resource.
