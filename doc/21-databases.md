# Databases <a id="databases"></a>

This category contains plugins for various database servers.

## db2_health <a id="db2_health"></a>

The [check_db2_health](https://labs.consol.de/nagios/check_db2_health/) plugin
uses the `DBD::DB2` Perl library to monitor a [DB2](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.1.0/)
database.

The Git repository is located on [GitHub](https://github.com/lausser/check_db2_health).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
db2_health_database           | **Required.** The name of the database. (If it was catalogued locally, this parameter is the only you need. Otherwise you must specify database, hostname and port)
db2_health_username           | **Optional.** The username for the database connection.
db2_health_password           | **Optional.** The password for the database connection.
db2_health_port               | **Optional.** The port where DB2 is listening.
db2_health_warning            | **Optional.** The warning threshold depending on the mode.
db2_health_critical           | **Optional.** The critical threshold depending on the mode.
db2_health_mode               | **Required.** The mode uses predefined keywords for the different checks. For example "connection-time", "database-usage" or "sql".
db2_health_method             | **Optional.** This tells the plugin how to connect to the database. The only method implemented yet is “dbi” which is the default. (It means, the plugin uses the perl module DBD::DB2).
db2_health_name               | **Optional.** The tablespace, datafile, wait event, latch, enqueue depending on the mode or SQL statement to be executed with "db2_health_mode" sql.
db2_health_name2              | **Optional.** If "db2_health_name" is a sql statement, "db2_health_name2" can be used to appear in the output and the performance data.
db2_health_regexp             | **Optional.** If set to true, "db2_health_name" will be interpreted as a regular expression. Defaults to false.
db2_health_units              | **Optional.** This is used for a better output of mode=sql and for specifying thresholds for mode=tablespace-free. Possible values are "%", "KB", "MB" and "GB".
db2_health_maxinactivity      | **Optional.** Used for the maximum amount of time a certain event has not happened.
db2_health_mitigation         | **Optional.** Classifies the severity of an offline tablespace.
db2_health_lookback           | **Optional.** How many days in the past db2_health check should look back to calculate exitcode.
db2_health_report             | **Optional.** Report can be used to output only the bad news. Possible values are "short", "long", "html". Defaults to `short`.
db2_health_env_db2_home       | **Required.** Specifies the location of the db2 client libraries as environment variable `DB2_HOME`. Defaults to "/opt/ibm/db2/V10.5".
db2_health_env_db2_version    | **Optional.** Specifies the DB2 version as environment variable `DB2_VERSION`.

## mssql_health <a id="mssql_health"></a>

The [check_mssql_health](https://labs.consol.de/nagios/check_mssql_health/index.html) plugin
uses the `DBD::Sybase` Perl library based on [FreeTDS](http://www.freetds.org/) to monitor a
[MS SQL](https://www.microsoft.com/en-us/sql-server/) server.

The Git repository is located on [GitHub](https://github.com/lausser/check_mssql_health).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
mssql_health_hostname            | **Optional.** Specifies the database hostname or address. No default because you typically use "mssql_health_server".
mssql_health_username            | **Optional.** The username for the database connection.
mssql_health_password            | **Optional.** The password for the database connection.
mssql_health_port                | **Optional.** Specifies the database port. No default because you typically use "mssql_health_server".
mssql_health_server              | **Optional.** The name of a predefined connection (in freetds.conf).
mssql_health_currentdb           | **Optional.** The name of a database which is used as the current database for the connection.
mssql_health_offlineok           | **Optional.** Set this to true if offline databases are perfectly ok for you. Defaults to false.
mssql_health_nooffline           | **Optional.** Set this to true to ignore offline databases. Defaults to false.
mssql_health_dbthresholds        | **Optional.** With this parameter thresholds are read from the database table check_mssql_health_thresholds.
mssql_health_notemp              | **Optional.** Set this to true to ignore temporary databases/tablespaces. Defaults to false.
mssql_health_commit              | **Optional.** Set this to true to turn on autocommit for the dbd::sybase module. Defaults to false.
mssql_health_method              | **Optional.** How the plugin should connect to the database (dbi for the perl module `DBD::Sybase` (default) and `sqlrelay` for the SQLRelay proxy).
mssql_health_mode                | **Required.** The mode uses predefined keywords for the different checks. For example "connection-time", "database-free" or "sql".
mssql_health_regexp              | **Optional.** If set to true, "mssql_health_name" will be interpreted as a regular expression. Defaults to false.
mssql_health_warning             | **Optional.** The warning threshold depending on the mode.
mssql_health_critical            | **Optional.** The critical threshold depending on the mode.
mssql_health_warningx            | **Optional.** A possible override for the warning threshold.
mssql_health_criticalx           | **Optional.** A possible override for the critical threshold.
mssql_health_units               | **Optional.** This is used for a better output of mode=sql and for specifying thresholds for mode=tablespace-free. Possible values are "%", "KB", "MB" and "GB".
mssql_health_name                | **Optional.** Depending on the mode this could be the database name or a SQL statement.
mssql_health_name2               | **Optional.** If "mssql_health_name" is a sql statement, "mssql_health_name2" can be used to appear in the output and the performance data.
mssql_health_name3               | **Optional.** Additional argument used for 'database-file-free' mode for example.
mssql_health_extraopts           | **Optional.** Read command line arguments from an external file.
mssql_health_blacklist           | **Optional.** Blacklist some (missing/failed) components
mssql_health_mitigation          | **Optional.** The parameter allows you to change a critical error to a warning.
mssql_health_lookback            | **Optional.** The amount of time you want to look back when calculating average rates.
mssql_health_environment         | **Optional.** Add a variable to the plugin's environment.
mssql_health_negate              | **Optional.** Emulate the negate plugin. --negate warning=critical --negate unknown=critical.
mssql_health_morphmessage        | **Optional.** Modify the final output message.
mssql_health_morphperfdata       | **Optional.** The parameter allows you to change performance data labels.
mssql_health_selectedperfdata    | **Optional.** The parameter allows you to limit the list of performance data.
mssql_health_report              | **Optional.** Report can be used to output only the bad news. Possible values are "short", "long", "html". Defaults to `short`.
mssql_health_multiline           | **Optional.** Multiline output.
mssql_health_withmymodulesdyndir | **Optional.** Add-on modules for the my-modes will be searched in this directory.
mssql_health_statefilesdir       | **Optional.** An alternate directory where the plugin can save files.
mssql_health_isvalidtime         | **Optional.** Signals the plugin to return OK if now is not a valid check time.
mssql_health_timeout           	 | **Optional.** Plugin timeout. Defaults to 15s.

## mysql_health <a id="mysql_health"></a>

The [check_mysql_health](https://labs.consol.de/nagios/check_mysql_health/index.html) plugin
uses the `DBD::MySQL` Perl library to monitor a
[MySQL](https://dev.mysql.com/downloads/mysql/) or [MariaDB](https://mariadb.org/about/) database.

The Git repository is located on [GitHub](https://github.com/lausser/check_mysql_health).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
mysql_health_hostname            | **Required.** Specifies the database hostname or address. Defaults to "$address$" or "$address6$" if the `address` attribute is not set.
mysql_health_port                | **Optional.** Specifies the database port. Defaults to 3306 (or 1186 for "mysql_health_mode" cluster).
mysql_health_socket              | **Optional.** Specifies the database unix socket. No default.
mysql_health_username            | **Optional.** The username for the database connection.
mysql_health_password            | **Optional.** The password for the database connection.
mysql_health_database            | **Optional.** The database to connect to. Defaults to information_schema.
mysql_health_warning             | **Optional.** The warning threshold depending on the mode.
mysql_health_critical            | **Optional.** The critical threshold depending on the mode.
mysql_health_warningx            | **Optional.** The extended warning thresholds depending on the mode.
mysql_health_criticalx           | **Optional.** The extended critical thresholds depending on the mode.
mysql_health_mode                | **Required.** The mode uses predefined keywords for the different checks. For example "connection-time", "slave-lag" or "sql".
mysql_health_method              | **Optional.** How the plugin should connect to the database (`dbi` for using DBD::Mysql (default), `mysql` for using the mysql-Tool).
mysql_health_commit              | **Optional.** Turns on autocommit for the dbd::\* module.
mysql_health_notemp              | **Optional.** Ignore temporary databases/tablespaces.
mysql_health_nooffline           | **Optional.** Skip the offline databases.
mysql_health_regexp              | **Optional.** Parameter name/name2/name3 will be interpreted as (perl) regular expression.
mysql_health_name                | **Optional.** The name of a specific component to check.
mysql_health_name2               | **Optional.** The secondary name of a component.
mysql_health_name3               | **Optional.** The tertiary name of a component.
mysql_health_units               | **Optional.** This is used for a better output of mode=sql and for specifying thresholds for mode=tablespace-free. Possible values are "%", "KB", "MB" and "GB".
mysql_health_labelformat         | **Optional.** One of those formats pnp4nagios or groundwork. Defaults to pnp4nagios.
mysql_health_extraopts           | **Optional.** Read command line arguments from an external file.
mysql_health_blacklist           | **Optional.** Blacklist some (missing/failed) components
mysql_health_mitigation          | **Optional.** The parameter allows you to change a critical error to a warning.
mysql_health_lookback            | **Optional.** The amount of time you want to look back when calculating average rates.
mysql_health_environment         | **Optional.** Add a variable to the plugin's environment.
mysql_health_morphmessage        | **Optional.** Modify the final output message.
mysql_health_morphperfdata       | **Optional.** The parameter allows you to change performance data labels.
mysql_health_selectedperfdata    | **Optional.** The parameter allows you to limit the list of performance data.
mysql_health_report              | **Optional.** Can be used to shorten the output.
mysql_health_multiline           | **Optional.** Multiline output.
mysql_health_negate              | **Optional.** Emulate the negate plugin. --negate warning=critical --negate unknown=critical.
mysql_health_withmymodulesdyndir | **Optional.** Add-on modules for the my-modes will be searched in this directory.
mysql_health_statefilesdir       | **Optional.** An alternate directory where the plugin can save files.
mysql_health_isvalidtime         | **Optional.** Signals the plugin to return OK if now is not a valid check time.
mysql_health_timeout           	 | **Optional.** Plugin timeout. Defaults to 60s.

## oracle_health <a id="oracle_health"></a>

The [check_oracle_health](https://labs.consol.de/nagios/check_oracle_health/index.html) plugin
uses the `DBD::Oracle` Perl library to monitor an [Oracle](https://www.oracle.com/database/) database.

The Git repository is located on [GitHub](https://github.com/lausser/check_oracle_health).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
oracle_health_connect            | **Required.** Specifies the database connection string (from tnsnames.ora).
oracle_health_username           | **Optional.** The username for the database connection.
oracle_health_password           | **Optional.** The password for the database connection.
oracle_health_warning            | **Optional.** The warning threshold depending on the mode.
oracle_health_critical           | **Optional.** The critical threshold depending on the mode.
oracle_health_mode               | **Required.** The mode uses predefined keywords for the different checks. For example "connection-time", "flash-recovery-area-usage" or "sql".
oracle_health_method             | **Optional.** How the plugin should connect to the database (`dbi` for using DBD::Oracle (default), `sqlplus` for using the sqlplus-Tool).
oracle_health_name               | **Optional.** The tablespace, datafile, wait event, latch, enqueue depending on the mode or SQL statement to be executed with "oracle_health_mode" sql.
oracle_health_name2              | **Optional.** If "oracle_health_name" is a sql statement, "oracle_health_name2" can be used to appear in the output and the performance data.
oracle_health_regexp             | **Optional.** If set to true, "oracle_health_name" will be interpreted as a regular expression. Defaults to false.
oracle_health_units              | **Optional.** This is used for a better output of mode=sql and for specifying thresholds for mode=tablespace-free. Possible values are "%", "KB", "MB" and "GB".
oracle_health_ident              | **Optional.** If set to true, outputs instance and database names. Defaults to false.
oracle_health_commit             | **Optional.** Set this to true to turn on autocommit for the dbd::oracle module. Defaults to false.
oracle_health_noperfdata         | **Optional.** Set this to true if you want to disable perfdata. Defaults to false.
oracle_health_timeout            | **Optional.** Plugin timeout. Defaults to 60s.
oracle_health_report             | **Optional.** Select the plugin output format. Can be short or long. Default to long.

Environment Macros:

Name                | Description
--------------------|------------------------------------------------------------------------------------------------------------------------------------------
ORACLE_HOME         | **Required.** Specifies the location of the oracle instant client libraries. Defaults to "/usr/lib/oracle/11.2/client64/lib". Can be overridden by setting the custom attribute `oracle_home`.
LD_LIBRARY_PATH    | **Required.** Specifies the location of the oracle instant client libraries for the run-time shared library loader. Defaults to "/usr/lib/oracle/11.2/client64/lib". Can be overridden by setting the custom attribute `oracle_ld_library_path`.
TNS_ADMIN           | **Required.** Specifies the location of the tnsnames.ora including the database connection strings. Defaults to "/etc/icinga2/plugin-configs". Can be overridden by setting the custom attribute `oracle_tns_admin`.

## postgres <a id="postgres"></a>

The [check_postgres](https://bucardo.org/wiki/Check_postgres) plugin
uses the `psql` binary to monitor a [PostgreSQL](https://www.postgresql.org/about/) database.

The Git repository is located on [GitHub](https://github.com/bucardo/check_postgres).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
postgres_host        | **Optional.** Specifies the database hostname or address. Defaults to "$address$" or "$address6$" if the `address` attribute is not set. If "postgres_unixsocket" is set to true, falls back to unix socket.
postgres_port        | **Optional.** Specifies the database port. Defaults to 5432.
postgres_dbname      | **Optional.** Specifies the database name to connect to. Defaults to "postgres" or "template1".
postgres_dbuser      | **Optional.** The username for the database connection. Defaults to "postgres".
postgres_dbpass      | **Optional.** The password for the database connection. You can use a .pgpass file instead.
postgres_dbservice   | **Optional.** Specifies the service name to use inside of pg_service.conf.
postgres_warning     | **Optional.** Specifies the warning threshold, range depends on the action.
postgres_critical    | **Optional.** Specifies the critical threshold, range depends on the action.
postgres_include     | **Optional.** Specifies name(s) items to specifically include (e.g. tables), depends on the action.
postgres_exclude     | **Optional.** Specifies name(s) items to specifically exclude (e.g. tables), depends on the action.
postgres_includeuser | **Optional.** Include objects owned by certain users.
postgres_excludeuser | **Optional.** Exclude objects owned by certain users.
postgres_standby     | **Optional.** Assume that the server is in continuous WAL recovery mode if set to true. Defaults to false.
postgres_production  | **Optional.** Assume that the server is in production mode if set to true. Defaults to false.
postgres_action      | **Required.** Determines the test executed.
postgres_unixsocket  | **Optional.** If "postgres_unixsocket" is set to true, the unix socket is used instead of an address. Defaults to false.
postgres_query       | **Optional.** Query for "custom_query" action.
postgres_valtype     | **Optional.** Value type of query result for "custom_query".
postgres_reverse     | **Optional.** If "postgres_reverse" is set, warning and critical values are reversed for "custom_query" action.
postgres_tempdir     | **Optional.** Specify directory for temporary files. The default directory is dependent on the OS. More details [here](https://perldoc.perl.org/File/Spec.html).

## mongodb <a id="mongodb"></a>

The [check_mongodb.py](https://github.com/mzupan/nagios-plugin-mongodb) plugin
uses the `pymongo` Python library to monitor a [MongoDB](https://docs.mongodb.com/manual/) instance.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------------------------------------------------------------------------------------------------------------------------
mongodb_host                     | **Required.** Specifies the hostname or address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
mongodb_port                     | **Required.** The port mongodb is running on.
mongodb_user                     | **Optional.** The username you want to login as.
mongodb_passwd                   | **Optional.** The password you want to use for that user.
mongodb_authdb                   | **Optional.** The database you want to authenticate against.
mongodb_warning                  | **Optional.** The warning threshold we want to set.
mongodb_critical                 | **Optional.** The critical threshold we want to set.
mongodb_action                   | **Required.** The action you want to take.
mongodb_maxlag                   | **Optional.** Get max replication lag (for replication_lag action only).
mongodb_mappedmemory             | **Optional.** Get mapped memory instead of resident (if resident memory can not be read).
mongodb_perfdata                 | **Optional.** Enable output of Nagios performance data.
mongodb_database                 | **Optional.** Specify the database to check.
mongodb_alldatabases             | **Optional.** Check all databases (action database_size).
mongodb_ssl                      | **Optional.** Connect using SSL.
mongodb_replicaset               | **Optional.** Connect to replicaset.
mongodb_replcheck                | **Optional.** If set to true, will enable the mongodb_replicaset value needed for "replica_primary" check.
mongodb_querytype                | **Optional.** The query type to check [query\|insert\|update\|delete\|getmore\|command] from queries_per_second.
mongodb_collection               | **Optional.** Specify the collection to check.
mongodb_sampletime               | **Optional.** Time used to sample number of pages faults.

## elasticsearch <a id="elasticsearch"></a>

The [check_elasticsearch](https://github.com/anchor/nagios-plugin-elasticsearch) plugin
uses the HTTP API to monitor an [Elasticsearch](https://www.elastic.co/products/elasticsearch) node.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                         | Description
-----------------------------|-------------------------------------------------------------------------------------------------------
elasticsearch_host           | **Optional.** Hostname or network address to probe. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
elasticsearch_failuredomain  | **Optional.** A comma-separated list of ElasticSearch attributes that make up your cluster's failure domain.
elasticsearch_masternodes    | **Optional.** Issue a warning if the number of master-eligible nodes in the cluster drops below this number. By default, do not monitor the number of nodes in the cluster.
elasticsearch_port           | **Optional.** TCP port to probe.  The ElasticSearch API should be listening here. Defaults to 9200.
elasticsearch_prefix         | **Optional.** Optional prefix (e.g. 'es') for the ElasticSearch API. Defaults to ''.
elasticsearch_yellowcritical | **Optional.** Instead of issuing a 'warning' for a yellow cluster state, issue a 'critical' alert. Defaults to false.

## redis <a id="redis"></a>

The [check_redis.pl](https://github.com/willixix/naglio-plugins/blob/master/check_redis.pl) plugin
uses the `Redis` Perl library to monitor a [Redis](https://redis.io/) instance. The plugin can
measure response time, hitrate, memory utilization, check replication synchronization, etc. It is
also possible to test data in a specified key and calculate averages or summaries on ranges.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                     | Description
-------------------------|--------------------------------------------------------------------------------------------------------------
redis_hostname           | **Required.** Hostname or IP Address to check. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
redis_port               | **Optional.** Port number to query. Default to "6379".
redis_database           | **Optional.** Database name (usually a number) to query, needed for **redis_query**.
redis_password           | **Optional.** Password for Redis authentication. Safer alternative is to put them in a file and use **redis_credentials**.
redis_credentials        | **Optional.** Credentials file to read for Redis authentication.
redis_timeout            | **Optional.** Allows to set timeout for execution of this plugin.
redis_variables          | **Optional.** List of variables from info data to do threshold checks on.
redis_warn               | **Optional.** This option can only be used if **redis_variables** is used and the number of values listed here must exactly match number of variables specified.
redis_crit               | **Optional.** This option can only be used if **redis_variables** is used and the number of values listed here must exactly match number of variables specified.
redis_perfparse          | **Optional.** This should only be used with variables and causes variable data not only to be printed as part of main status line but also as perfparse compatible output. Defaults to false.
redis_perfvars           | **Optional.** This allows to list variables which values will go only into perfparse output (and not for threshold checking).
redis_prev_perfdata      | **Optional.** If set to true, previous performance data are used to calculate rate of change for counter statistics variables and for proper calculation of hitrate. Defaults to false.
redis_rate_label         | **Optional.** Prefix or Suffix label used to create a new variable which has rate of change of another base variable. You can specify PREFIX or SUFFIX or both as one string separated by ",". Default if not specified is suffix "_rate".
redis_query              | **Optional.** Option specifies key to query and optional variable name to assign the results to after.
redis_option             | **Optional.** Specifiers are separated by "," and must include NAME or PATTERN.
redis_response_time      | **Optional.** If this is used, plugin will measure and output connection response time in seconds. With **redis_perfparse** this would also be provided on perf variables.
redis_hitrate            | **Optional.** Calculates Hitrate and specify values are interpreted as WARNING and CRITICAL thresholds.
redis_memory_utilization | **Optional.** This calculates percent of total memory on system used by redis. Total_memory on server must be specified with **redis_total_memory**. If you specify by itself, the plugin will just output this info. Parameter values are interpreted as WARNING and CRITICAL thresholds.
redis_total_memory       | **Optional.** Amount of memory on a system for memory utilization calculation. Use system memory or max_memory setting of redis.
redis_replication_delay  | **Optional.** Allows to set threshold on replication delay info.
