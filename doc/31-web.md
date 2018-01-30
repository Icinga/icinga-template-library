# Web <a id="web"></a>

This category includes all plugins for web-based checks.

## apache_status <a id="apache_status"></a>

The [check_apache_status.pl](https://github.com/lbetz/check_apache_status) plugin
uses the [/server-status](https://httpd.apache.org/docs/current/mod/mod_status.html)
HTTP endpoint to monitor status metrics for the Apache webserver.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|----------------------------------------------------------------------------------
apache_status_address	| **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, `address6` otherwise.
apache_status_port	| **Optional.** the http port.
apache_status_url	| **Optional.** URL to use, instead of the default (http://`apache_status_address`/server-status).
apache_status_ssl	| **Optional.** set to use ssl connection
apache_status_timeout	| **Optional.** timeout in seconds
apache_status_warning	| **Optional.** Warning threshold (number of open slots, busy workers and idle workers that will cause a WARNING) like ':20,50,:50'.
apache_status_critical	| **Optional.** Critical threshold (number of open slots, busy workers and idle workers that will cause a CRITICAL) like ':10,25,:20'.


## cert <a id="plugin-check-command-ssl_cert"></a>

The [check_ssl_cert](https://github.com/matteocorti/check_ssl_cert) plugin
uses the openssl binary (and optional curl) to check a X.509 certificate.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                      | Description
--------------------------|--------------
ssl_cert_address              | **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
ssl_cert_port                 | **Optional.** TCP port number (default: 443).
ssl_cert_file                 | **Optional.** Local file path. Works only if `ssl_cert_address` is set to "localhost".
ssl_cert_warn                 | **Optional.** Minimum number of days a certificate has to be valid.
ssl_cert_critical             | **Optional.** Minimum number of days a certificate has to be valid to issue a critical status.
ssl_cert_cn                   | **Optional.** Pattern to match the CN of the certificate.
ssl_cert_altnames             | **Optional.** Matches the pattern specified in -n with alternate
ssl_cert_issuer               | **Optional.** Pattern to match the issuer of the certificate.
ssl_cert_org                  | **Optional.** Pattern to match the organization of the certificate.
ssl_cert_email                | **Optional.** Pattern to match the email address contained in the certificate.
ssl_cert_serial               | **Optional.** Pattern to match the serial number.
ssl_cert_noauth               | **Optional.** Ignore authority warnings (expiration only)
ssl_cert_match_host           | **Optional.** Match CN with the host name.
ssl_cert_selfsigned           | **Optional.** Allow self-signed certificate.
ssl_cert_sni                  | **Optional.** Sets the TLS SNI (Server Name Indication) extension.
ssl_cert_timeout              | **Optional.** Seconds before connection times out (default: 15)
ssl_cert_protocol             | **Optional.** Use the specific protocol {http,smtp,pop3,imap,ftp,xmpp,irc,ldap} (default: http).
ssl_cert_clientcert           | **Optional.** Use client certificate to authenticate.
ssl_cert_clientpass           | **Optional.** Set passphrase for client certificate.
ssl_cert_ssllabs              | **Optional.** SSL Labs assessment
ssl_cert_ssllabs_nocache      | **Optional.** Forces a new check by SSL Labs
ssl_cert_rootcert             | **Optional.** Root certificate or directory to be used for certificate validation.
ssl_cert_ignore_signature     | **Optional.** Do not check if the certificate was signed with SHA1 od MD5.
ssl_cert_ssl_version          | **Optional.** Force specific SSL version out of {ssl2,ssl3,tls1,tls1_1,tls1_2}.
ssl_cert_disable_ssl_versions | **Optional.** Disable specific SSL versions out of {ssl2,ssl3,tls1,tls1_1,tls1_2}. Multiple versions can be given as array.
ssl_cert_cipher               | **Optional.** Cipher selection: force {ecdsa,rsa} authentication.
ssl_cert_ignore_expiration    | **Optional.** Ignore expiration date.
ssl_cert_ignore_ocsp          | **Optional.** Do not check revocation with OCSP.


## jmx4perl <a id="jmx4perl"></a>

The [check_jmx4perl](http://search.cpan.org/~roland/jmx4perl/scripts/check_jmx4perl) plugin
uses the HTTP API exposed by the [Jolokia](https://jolokia.org)
web application and queries Java message beans on an application server. It is
part of the `JMX::Jmx4Perl` Perl module which includes detailed
[documentation](http://search.cpan.org/~roland/jmx4perl/scripts/check_jmx4perl).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                         | Description
-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------
jmx4perl_url                 | **Required.** URL to agent web application. Defaults to "http://$address$:8080/jolokia".
jmx4perl_product             | **Optional.** Name of app server product (e.g. jboss), by default is uses an auto detection facility.
jmx4perl_alias               | **Optional.** Alias name for attribute (e.g. MEMORY_HEAP_USED). All available aliases can be viewed by executing `jmx4perl aliases` on the command line.
jmx4perl_mbean               | **Optional.** MBean name (e.g. java.lang:type=Memory).
jmx4perl_attribute           | **Optional.** Attribute name (e.g. HeapMemoryUsage).
jmx4perl_operation           | **Optional.** Operation to execute.
jmx4perl_value               | **Optional.** Shortcut for specifying mbean/attribute/path. Slashes within names must be escaped with backslash.
jmx4perl_delta               | **Optional.** Switches on incremental mode. Optional argument are seconds used for normalizing.
jmx4perl_path                | **Optional.** Inner path for extracting a single value from a complex attribute or return value (e.g. used).
jmx4perl_target              | **Optional.** JSR-160 Service URL specifing the target server.
jmx4perl_target_user         | **Optional.** Username to use for JSR-160 connection.
jmx4perl_target_password     | **Optional.** Password to use for JSR-160 connection.
jmx4perl_proxy               | **Optional.** Proxy to use.
jmx4perl_user                | **Optional.** User for HTTP authentication.
jmx4perl_password            | **Optional.** Password for HTTP authentication.
jmx4perl_name                | **Optional.** Name to use for output, by default a standard value based on the MBean and attribute will be used.
jmx4perl_method              | **Optional.** HTTP method to use, either get or post. By default a method is determined automatically based on the request type.
jmx4perl_base                | **Optional.** Base name, which when given, interprets critical and warning values as relative in the range 0 .. 100%. Must be given in the form mbean/attribute/path.
jmx4perl_base_mbean          | **Optional.** Base MBean name, interprets critical and warning values as relative in the range 0 .. 100%. Requires "jmx4perl_base_attribute".
jmx4perl_base_attribute      | **Optional.** Base attribute for a relative check. Requires "jmx4perl_base_mbean".
jmx4perl_base_path           | **Optional.** Base path for relative checks, where this path is used on the base attribute's value.
jmx4perl_unit                | **Optional.** Unit of measurement of the data retrieved. Recognized values are [B\|KB\|MN\|GB\|TB] for memory values and [us\|ms\|s\|m\|h\|d] for time values.
jmx4perl_null                | **Optional.** Value which should be used in case of a null return value of an operation or attribute. Defaults to null.
jmx4perl_string              | **Optional.** Force string comparison for critical and warning checks. Defaults to false.
jmx4perl_numeric             | **Optional.** Force numeric comparison for critical and warning checks. Defaults to false.
jmx4perl_critical            | **Optional.** Critical threshold for value.
jmx4perl_warning             | **Optional.** Warning threshold for value.
jmx4perl_label               | **Optional.** Label to be used for printing out the result of the check. For placeholders which can be used see the documentation.
jmx4perl_perfdata            | **Optional.** Whether performance data should be omitted, which are included by default. Defaults to "on" for numeric values, to "off" for strings.
jmx4perl_unknown_is_critical | **Optional.** Map UNKNOWN errors to errors with a CRITICAL status. Defaults to false.
jmx4perl_timeout             | **Optional.** Seconds before plugin times out. Defaults to "15".
jmx4perl_config              | **Optional.** Path to configuration file.
jmx4perl_server              | **Optional.** Symbolic name of server url to use, which needs to be configured in the configuration file.
jmx4perl_check               | **Optional.** Name of a check configuration as defined in the configuration file, use array if you need arguments.


## kdc <a id="kdc"></a>

The [check_kdc](https://exchange.nagios.org/directory/Plugins/Security/check_kdc/details) plugin
uses the Kerberos `kinit` binary to monitor Kerberos 5 KDC by acquiring a ticket.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name            | Description
----------------|--------------------------------------------------------------------------
kdc_address	| **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, `address6` otherwise.
kdc_port	| **Optional** Port on which KDC runs (default 88).
kdc_principal	| **Required** Principal name to authenticate as (including realm).
kdc_keytab	| **Required** Keytab file containing principal's key.


## nginx_status <a id="nginx_status"></a>

The [check_nginx_status.pl](https://github.com/regilero/check_nginx_status) plugin
uses the [/nginx_status](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html)
HTTP endpoint which provides metrics for monitoring Nginx.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    	| Description
--------------------------------|----------------------------------------------------------------------------------
nginx_status_host_address	| **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, `address6` otherwise.
nginx_status_port		| **Optional.** the http port.
nginx_status_url		| **Optional.** URL to use, instead of the default (http://`nginx_status_hostname`/nginx_status).
nginx_status_servername		| **Optional.** ServerName to use if you specified an IP to match the good Virtualhost in your target.
nginx_status_ssl		| **Optional.** set to use ssl connection.
nginx_status_disable_sslverify		| **Optional.** set to disable SSL hostname verification.
nginx_status_user		| **Optional.** Username for basic auth.
nginx_status_pass		| **Optional.** Password for basic auth.
nginx_status_realm		| **Optional.** Realm for basic auth.
nginx_status_maxreach		| **Optional.** Number of max processes reached (since last check) that should trigger an alert.
nginx_status_timeout		| **Optional.** timeout in seconds.
nginx_status_warn		| **Optional.** Warning threshold (number of active connections, ReqPerSec or ConnPerSec that will cause a WARNING) like '10000,100,200'.
nginx_status_critical		| **Optional.** Critical threshold (number of active connections, ReqPerSec or ConnPerSec that will cause a CRITICAL) like '20000,200,300'.


## rbl <a id="rbl"></a>

The [check_rbl](https://github.com/matteocorti/check_rbl) plugin
uses the `Net::DNS` Perl library to check whether your SMTP server
is blacklisted.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name            | Description
----------------|--------------------------------------------------------------------------
rbl_hostname	| **Optional.** The address or name of the SMTP server to check. Defaults to "$address$" if the host's `address` attribute is set, `address6` otherwise.
rbl_server	| **Required** List of RBL servers as an array.
rbl_warning	| **Optional** Number of blacklisting servers for a warning.
rbl_critical	| **Optional** Number of blacklisting servers for a critical.
tbl_timeout	| **Optional** Seconds before plugin times out (default: 15).


## squid <a id="squid"></a>

The [check_squid](https://exchange.icinga.com/exchange/check_squid) plugin
uses the `squidclient` binary to monitor a [Squid proxy](http://www.squid-cache.org).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|----------------------------------------------------------------------------------
squid_hostname		| **Optional.** The host's address. Defaults to "$address$" if the host's `address` attribute is set, "$address6$" otherwise.
squid_data		| **Optional.** Data to fetch (default: Connections) available data: Connections Cache Resources Memory FileDescriptors.
squid_port		| **Optional.** Port number (default: 3128).
squid_user		| **Optional.** WWW user.
squid_password		| **Optional.** WWW password.
squid_warning		| **Optional.** Warning threshold. See http://nagiosplug.sourceforge.net/developer-guidelines.html#THRESHOLDFORMAT for the threshold format.
squid_critical		| **Optional.** Critical threshold. See http://nagiosplug.sourceforge.net/developer-guidelines.html#THRESHOLDFORMAT for the threshold format.
squid_client		| **Optional.** Path of squidclient (default: /usr/bin/squidclient).
squid_timeout		| **Optional.** Seconds before plugin times out (default: 15).


## webinject <a id="webinject"></a>

The [check_webinject](https://labs.consol.de/de/nagios/check_webinject/index.html) plugin
uses [WebInject](http://www.webinject.org/manual.html) to test web applications
and web services in an automated fashion.
It can be used to test individual system components that have HTTP interfaces
(JSP, ASP, CGI, PHP, AJAX, Servlets, HTML Forms, XML/SOAP Web Services, REST, etc),
and can be used as a test harness to create a suite of HTTP level automated functional,
acceptance, and regression tests. A test harness allows you to run many test cases
and collect/report your results. WebInject offers real-time results
display and may also be used for monitoring system response times.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|--------------
webinject_config_file   | **Optional.** There is a configuration file named 'config.xml' that is used to store configuration settings for your project. You can use this to specify which test case files to run and to set some constants and settings to be used by WebInject.
webinject_output        | **Optional.** This option is followed by a directory name or a prefix to prepended to the output files. This is used to specify the location for writing output files (http.log, results.html, and results.xml). If a directory name is supplied (use either an absolute or relative path and make sure to add the trailing slash), all output files are written to this directory. If the trailing slash is omitted, it is assumed to a prefix and this will be prepended to the output files. You may also use a combination of a directory and prefix.
webinject_no_output     | **Optional.** Suppresses all output to STDOUT except the results summary.
webinject_timeout       | **Optional.** The value [given in seconds] will be compared to the global time elapsed to run all the tests. If the tests have all been successful, but have taken more time than the 'globaltimeout' value, a warning message is sent back to Icinga.
webinject_report_type   | **Optional.** This setting is used to enable output formatting that is compatible for use with specific external programs. The available values you can set this to are: nagios, mrtg, external and standard.
webinject_testcase_file | **Optional.** When you launch WebInject in console mode, you can optionally supply an argument for a testcase file to run. It will look for this file in the directory that webinject.pl resides in. If no filename is passed from the command line, it will look in config.xml for testcasefile declarations. If no files are specified, it will look for a default file named 'testcases.xml' in the current [webinject] directory. If none of these are found, the engine will stop and give you an error.
