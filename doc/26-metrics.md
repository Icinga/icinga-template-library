# Metrics <a id="metrics"></a>

This category includes all plugins for metric-based checks.

## graphite <a id="graphite"></a>

The [check_graphite](https://github.com/obfuscurity/nagios-scripts) plugin
uses the `rest-client` Ruby library to monitor a [Graphite](https://graphiteapp.org) instance.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                   | Description
-----------------------|------------
graphite_url           | **Required.** Target url.
graphite_metric        | **Required.** Metric path string.
graphite_shortname     | Metric short name (used for performance data).
graphite_duration      | Length, in minute of data to parse (default: 5).
graphite_function      | Function applied to metrics for thresholds (default: average).
graphite_warning       | **Required.** Warning threshold.
graphite_critical      | **Required.** Critical threshold.
graphite_units         | Adds a text tag to the metric count in the plugin output. Useful to identify the metric units. Doesn't affect data queries.
graphite_message       | Text message to output (default: "metric count:").
graphite_zero_on_error | Return 0 on a graphite 500 error.
graphite_link_graph    | Add a link in the plugin output, showing a 24h graph for this metric in graphite.
