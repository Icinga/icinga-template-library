# Log Management <a id="plugins-contrib-log-management"></a>

This category includes all plugins for log management, for example [Logstash](https://www.elastic.co/products/logstash).

## logstash <a id="plugins-contrib-command-logstash"></a>

The [logstash](https://github.com/widhalmt/check_logstash) plugin connects to
the Node API of Logstash. This plugin requires at least Logstash version 5.0.x.

The Node API is not activated by default. You have to configure your Logstash
installation in order to allow plugin connections.

Name                   | Description
-----------------------|------------
logstash_hostname      | Hostname where Logstash is running. Defaults to `check_address`
logstash_port          | Port where Logstash is listening for API requests. Defaults to 9600
logstash_filedesc_warn | Warning threshold of file descriptor usage in percent. Defaults to 85 (percent).
logstash_filedesc_crit | Critical threshold of file descriptor usage in percent. Defaults to 95 (percent).
logstash_heap_warn     | Warning threshold of heap usage in percent. Defaults to 70 (percent).
logstash_heap_crit     | Critical threshold of heap usage in percent Defaults to 80 (percent).
logstash_inflight_warn | Warning threshold of inflight events.
logstash_inflight_crit | Critical threshold of inflight events.
logstash_cpu_warn      | Warning threshold for cpu usage in percent.
logstash_cpu_crit      | Critical threshold for cpu usage in percent.
