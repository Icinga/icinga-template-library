# Virtualization <a id="virtualization"></a>

This category includes all plugins for various virtualization technologies.

## VMware <a id="vmware"></a>

Check commands for the [check_vmware_esx](https://github.com/BaldMansMojo/check_vmware_esx) plugin.

**vmware-esx-dc-volumes**

Check command object for the `check_vmware_esx` plugin. Shows all datastore volumes info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_subselect      | Volume name to be checked the free space.
vmware_gigabyte       | Output in GB instead of MB.
vmware_usedspace      | Output used space instead of free. Defaults to "false".
vmware_alertonly      | List only alerting volumes. Defaults to "false".
vmware_exclude        | Blacklist volumes name. No value defined as default.
vmware_include        | Whitelist volumes name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_dc_volume_used | Output used space instead of free. Defaults to "true".
vmware_warn           | The warning threshold for volumes. Defaults to "80%".
vmware_crit           | The critical threshold for volumes. Defaults to "90%".

**vmware-esx-dc-runtime-info**

Check command object for the `check_vmware_esx` plugin. Shows all runtime info for the datacenter/Vcenter.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-dc-runtime-listvms**

Check command object for the `check_vmware_esx` plugin. List of vmware machines and their power state. BEWARE!! In larger environments systems can cause trouble displaying the informations needed due to the mass of data. Use **vmware_alertonly** to avoid this.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_alertonly      | List only alerting VMs. Important here to avoid masses of data.
vmware_exclude        | Blacklist VMs name. No value defined as default.
vmware_include        | Whitelist VMs name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-dc-runtime-listhost**

Check command object for the `check_vmware_esx` plugin. List of VMware ESX hosts and their power state.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_alertonly      | List only alerting hosts. Important here to avoid masses of data.
vmware_exclude        | Blacklist VMware ESX hosts. No value defined as default.
vmware_include        | Whitelist VMware ESX hosts. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-dc-runtime-listcluster**

Check command object for the `check_vmware_esx` plugin. List of VMware clusters and their states.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_alertonly      | List only alerting hosts. Important here to avoid masses of data.
vmware_exclude        | Blacklist VMware cluster. No value defined as default.
vmware_include        | Whitelist VMware cluster. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-dc-runtime-issues**

Check command object for the `check_vmware_esx` plugin. All issues for the host.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist issues. No value defined as default.
vmware_include        | Whitelist issues. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-dc-runtime-status**

Check command object for the `check_vmware_esx` plugin. Overall object status (gray/green/red/yellow).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-dc-runtime-tools**

Check command object for the `check_vmware_esx` plugin. Vmware Tools status.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | **Required.** Datacenter/vCenter hostname.
vmware_cluster        | ESX or ESXi clustername.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_poweredonly    | List only VMs which are powered on. No value defined as default.
vmware_alertonly      | List only alerting VMs. Important here to avoid masses of data.
vmware_exclude        | Blacklist VMs. No value defined as default.
vmware_include        | Whitelist VMs. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.
vmware_openvmtools    | Prevent CRITICAL state for installed and running Open VM Tools.

**vmware-esx-soap-host-check**

Check command object for the `check_vmware_esx` plugin. Simple check to verify a successful connection to VMware SOAP API.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-uptime**

Check command object for the `check_vmware_esx` plugin. Displays uptime of the VMware host.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-cpu**

Check command object for the `check_vmware_esx` plugin. CPU usage in percentage.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. Defaults to "80%".
vmware_crit           | The critical threshold in percent. Defaults to "90%".

**vmware-esx-soap-host-cpu-ready**

Check command object for the `check_vmware_esx` plugin. Percentage of time that the virtual machine was ready, but could not get scheduled to run on the physical CPU. CPU ready time is dependent on the number of virtual machines on the host and their CPU loads. High or growing ready time can be a hint CPU bottlenecks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-cpu-wait**

Check command object for the `check_vmware_esx` plugin. CPU time spent in wait state. The wait total includes time spent the CPU idle, CPU swap wait, and CPU I/O wait states. High or growing wait time can be a hint I/O bottlenecks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-cpu-usage**

Check command object for the `check_vmware_esx` plugin. Actively used CPU of the host, as a percentage of the total available CPU. Active CPU is approximately equal to the ratio of the used CPU to the available CPU.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. Defaults to "80%".
vmware_crit           | The critical threshold in percent. Defaults to "90%".

**vmware-esx-soap-host-mem**

Check command object for the `check_vmware_esx` plugin. All mem info(except overall and no thresholds).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-mem-usage**

Check command object for the `check_vmware_esx` plugin. Average mem usage in percentage.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. Defaults to "80%".
vmware_crit           | The critical threshold in percent. Defaults to "90%".

**vmware-esx-soap-host-mem-consumed**

Check command object for the `check_vmware_esx` plugin. Amount of machine memory used on the host. Consumed memory includes Includes memory used by the Service Console, the VMkernel vSphere services, plus the total consumed metrics for all running virtual machines in MB.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. No value defined as default.
vmware_crit           | The critical threshold in percent. No value defined as default.

**vmware-esx-soap-host-mem-swapused**

Check command object for the `check_vmware_esx` plugin. Amount of memory that is used by swap. Sum of memory swapped of all powered on VMs and vSphere services on the host in MB. In case of an error all VMs with their swap used will be displayed.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. No value defined as default.
vmware_crit           | The critical threshold in percent. No value defined as default.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-mem-overhead**

Check command object for the `check_vmware_esx` plugin. Additional mem used by VM Server in MB.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Auhentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. No value defined as default.
vmware_crit           | The critical threshold in percent. No value defined as default.

**vmware-esx-soap-host-mem-memctl**

Check command object for the `check_vmware_esx` plugin. The sum of all vmmemctl values in MB for all powered-on virtual machines, plus vSphere services on the host. If the balloon target value is greater than the balloon value, the VMkernel inflates the balloon, causing more virtual machine memory to be reclaimed. If the balloon target value is less than the balloon value, the VMkernel deflates the balloon, which allows the virtual machine to consume additional memory if needed (used by VM memory control driver). In case of an error all VMs with their vmmemctl values will be displayed.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in percent. No value defined as default.
vmware_crit           | The critical threshold in percent. No value defined as default.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-net**

Check command object for the `check_vmware_esx` plugin. Shows net info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist NICs. No value defined as default.
vmware_isregexp       | Treat blacklist expression as regexp.

**vmware-esx-soap-host-net-usage**

Check command object for the `check_vmware_esx` plugin. Overall network usage in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in KBps(Kilobytes per Second). No value defined as default.
vmware_crit           | The critical threshold in KBps(Kilobytes per Second). No value defined as default.

**vmware-esx-soap-host-net-receive**

Check command object for the `check_vmware_esx` plugin. Data receive in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in KBps(Kilobytes per Second). No value defined as default.
vmware_crit           | The critical threshold in KBps(Kilobytes per Second). No value defined as default.

**vmware-esx-soap-host-net-send**

Check command object for the `check_vmware_esx` plugin. Data send in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold in KBps(Kilobytes per Second). No value defined as default.
vmware_crit           | The critical threshold in KBps(Kilobytes per Second). No value defined as default.

**vmware-esx-soap-host-net-nic**

Check command object for the `check_vmware_esx` plugin. Check all active NICs.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist NICs. No value defined as default.
vmware_isregexp       | Treat blacklist expression as regexp.

**vmware-esx-soap-host-volumes**

Check command object for the `check_vmware_esx` plugin. Shows all datastore volumes info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_subselect      | Volume name to be checked the free space.
vmware_gigabyte       | Output in GB instead of MB.
vmware_usedspace      | Output used space instead of free. Defaults to "false".
vmware_alertonly      | List only alerting volumes. Defaults to "false".
vmware_exclude        | Blacklist volumes name. No value defined as default.
vmware_include        | Whitelist volumes name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_warn           | The warning threshold for volumes. Defaults to "80%".
vmware_crit           | The critical threshold for volumes. Defaults to "90%".
vmware_spaceleft      | This has to be used in conjunction with thresholds as mentioned above.

**vmware-esx-soap-host-io**

Check command object for the `check_vmware_esx` plugin. Shows all disk io info. Without subselect no thresholds can be given. All I/O values are aggregated from historical intervals over the past 24 hours with a 5 minute sample rate.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-io-aborted**

Check command object for the `check_vmware_esx` plugin. Number of aborted SCSI commands.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-resets**

Check command object for the `check_vmware_esx` plugin. Number of SCSI bus resets.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-read**

Check command object for the `check_vmware_esx` plugin. Average number of kilobytes read from the disk each second.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-read-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) to process a SCSI read command issued from the Guest OS to the virtual machine.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-write**

Check command object for the `check_vmware_esx` plugin. Average number of kilobytes written to disk each second.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-write-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) taken to process a SCSI write command issued by the Guest OS to the virtual machine.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-usage**

Check command object for the `check_vmware_esx` plugin. Aggregated disk I/O rate. For hosts, this metric includes the rates for all virtual machines running on the host.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-kernel-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) spent by VMkernel processing each SCSI command.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-device-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) to complete a SCSI command from the physical device.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-queue-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) spent in the VMkernel queue.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-io-total-latency**

Check command object for the `check_vmware_esx` plugin. Average amount of time (ms) taken during the collection interval to process a SCSI command issued by the guest OS to the virtual machine. The sum of kernelWriteLatency and deviceWriteLatency.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-host-media**

Check command object for the `check_vmware_esx` plugin. List vm's with attached host mounted media like cd,dvd or floppy drives. This is important for monitoring because a virtual machine with a mount cd or dvd drive can not be moved to another host.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist VMs name. No value defined as default.
vmware_include        | Whitelist VMs name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-service**

Check command object for the `check_vmware_esx` plugin. Shows host service info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist services name. No value defined as default.
vmware_include        | Whitelist services name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-runtime**

Check command object for the `check_vmware_esx` plugin. Shows runtime info: VMs, overall status, connection state, health, storagehealth, temperature and sensor are represented as one value and without thresholds.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-runtime-con**

Check command object for the `check_vmware_esx` plugin. Shows connection state.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-runtime-listvms**

Check command object for the `check_vmware_esx` plugin. List of VMware machines and their status.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist VMs name. No value defined as default.
vmware_include        | Whitelist VMs name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-runtime-status**

Check command object for the `check_vmware_esx` plugin. Overall object status (gray/green/red/yellow).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-host-runtime-health**

Check command object for the `check_vmware_esx` plugin. Checks cpu/storage/memory/sensor status.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist status name. No value defined as default.
vmware_include        | Whitelist status name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.

**vmware-esx-soap-host-runtime-health-listsensors**

Check command object for the `check_vmware_esx` plugin. List all available sensors(use for listing purpose only).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist status name. No value defined as default.
vmware_include        | Whitelist status name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.

**vmware-esx-soap-host-runtime-health-nostoragestatus**

Check command object for the `check_vmware_esx` plugin. This is to avoid a double alarm if you use **vmware-esx-soap-host-runtime-health** and **vmware-esx-soap-host-runtime-storagehealth**.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist status name. No value defined as default.
vmware_include        | Whitelist status name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.

**vmware-esx-soap-host-runtime-storagehealth**

Check command object for the `check_vmware_esx` plugin. Local storage status check.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist storage name. No value defined as default.
vmware_include        | Whitelist storage name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-runtime-temp**

Check command object for the `check_vmware_esx` plugin. Lists all temperature sensors.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist sensor name. No value defined as default.
vmware_include        | Whitelist sensor name. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-runtime-issues**

Check command object for the `check_vmware_esx` plugin. Lists all configuration issues for the host.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist configuration issues. No value defined as default.
vmware_include        | Whitelist configuration issues. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-storage**

Check command object for the `check_vmware_esx` plugin. Shows Host storage info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist adapters, luns and paths. No value defined as default.
vmware_include        | Whitelist adapters, luns and paths. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.

**vmware-esx-soap-host-storage-adapter**

Check command object for the `check_vmware_esx` plugin. List host bus adapters.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist adapters. No value defined as default.
vmware_include        | Whitelist adapters. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-storage-lun**

Check command object for the `check_vmware_esx` plugin. List SCSI logical units. The listing will include: LUN, canonical name of the disc, all of displayed name which is not part of the canonical name and status.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_exclude        | Blacklist luns. No value defined as default.
vmware_include        | Whitelist luns. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

**vmware-esx-soap-host-storage-path**

Check command object for the `check_vmware_esx` plugin. List multipaths and the associated paths.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_host           | **Required.** ESX or ESXi hostname.
vmware_datacenter     | Datacenter/vCenter hostname. In case the check is done through a Datacenter/vCenter host.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_alertonly      | List only alerting units. Important here to avoid masses of data. Defaults to "false".
vmware_exclude        | Blacklist paths. No value defined as default.
vmware_include        | Whitelist paths. No value defined as default.
vmware_isregexp       | Treat blacklist and whitelist expressions as regexp.
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.
vmware_standbyok      | For storage systems where a standby multipath is ok and not a warning. Defaults to false.

**vmware-esx-soap-vm-cpu**

Check command object for the `check_vmware_esx` plugin. Shows all CPU usage info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-cpu-ready**

Check command object for the `check_vmware_esx` plugin. Percentage of time that the virtual machine was ready, but could not get scheduled to run on the physical CPU.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-cpu-wait**

Check command object for the `check_vmware_esx` plugin. CPU time spent in wait state. The wait total includes time spent the CPU idle, CPU swap wait, and CPU I/O wait states. High or growing wait time can be a hint I/O bottlenecks.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-cpu-usage**

Check command object for the `check_vmware_esx` plugin. Amount of actively used virtual CPU, as a percentage of total available CPU. This is the host's view of the CPU usage, not the guest operating system view. It is the average CPU utilization over all available virtual CPUs in the virtual machine.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | Warning threshold in percent. Defaults to "80%".
vmware_crit           | Critical threshold in percent. Defaults to "90%".

**vmware-esx-soap-vm-mem**

Check command object for the `check_vmware_esx` plugin. Shows all memory info, except overall.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-mem-usage**

Check command object for the `check_vmware_esx` plugin. Average mem usage in percentage of configured virtual machine "physical" memory.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | Warning threshold in percent. Defaults to "80%".
vmware_crit           | Critical threshold in percent. Defaults to "90%".

**vmware-esx-soap-vm-mem-consumed**

Check command object for the `check_vmware_esx` plugin. Amount of guest physical memory in MB consumed by the virtual machine for guest memory. Consumed memory does not include overhead memory. It includes shared memory and memory that might be reserved, but not actually used. Use this metric for charge-back purposes.<br>
**vm consumed memory = memory granted -- memory saved**

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-mem-memctl**

Check command object for the `check_vmware_esx` plugin. Amount of guest physical memory that is currently reclaimed from the virtual machine through ballooning. This is the amount of guest physical memory that has been allocated and pinned by the balloon driver.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-net**

Check command object for the `check_vmware_esx` plugin. Shows net info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-net-usage**

Check command object for the `check_vmware_esx` plugin. Overall network usage in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-net-receive**

Check command object for the `check_vmware_esx` plugin. Receive in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-net-send**

Check command object for the `check_vmware_esx` plugin. Send in KBps(Kilobytes per Second).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-io**

Check command object for the `check_vmware_esx` plugin. Shows all disk io info. Without subselect no thresholds can be given. All I/O values are aggregated from historical intervals over the past 24 hours with a 5 minute sample rate.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-io-read**

Check command object for the `check_vmware_esx` plugin. Average number of kilobytes read from the disk each second.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session - IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-io-write**

Check command object for the `check_vmware_esx` plugin. Average number of kilobytes written to disk each second.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-io-usage**

Check command object for the `check_vmware_esx` plugin. Aggregated disk I/O rate.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-runtime**

Check command object for the `check_vmware_esx` plugin. Shows virtual machine runtime info.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-runtime-con**

Check command object for the `check_vmware_esx` plugin. Shows the connection state.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-runtime-powerstate**

Check command object for the `check_vmware_esx` plugin. Shows virtual machine power state: poweredOn, poweredOff or suspended.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-runtime-status**

Check command object for the `check_vmware_esx` plugin. Overall object status (gray/green/red/yellow).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-runtime-consoleconnections**

Check command object for the `check_vmware_esx` plugin. Console connections to virtual machine.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_warn           | The warning threshold. No value defined as default.
vmware_crit           | The critical threshold. No value defined as default.

**vmware-esx-soap-vm-runtime-gueststate**

Check command object for the `check_vmware_esx` plugin. Guest OS status. Needs VMware Tools installed and running.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd

**vmware-esx-soap-vm-runtime-tools**

Check command object for the `check_vmware_esx` plugin. Guest OS status. VMware tools  status.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_openvmtools    | Prevent CRITICAL state for installed and running Open VM Tools.

**vmware-esx-soap-vm-runtime-issues**

Check command object for the `check_vmware_esx` plugin. All issues for the virtual machine.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                  | Description
----------------------|------------
vmware_datacenter     | Datacenter/vCenter hostname. Conflicts with **vmware_host**.
vmware_host           | ESX or ESXi hostname. Conflicts with **vmware_datacenter**.
vmware_vmname         | **Required.** Virtual machine name.
vmware_sslport        | SSL port connection. Defaults to "443".
vmware_ignoreunknown  | Sometimes 3 (unknown) is returned from a component. But the check itself is ok. With this option the plugin will return OK (0) instead of UNKNOWN (3). Defaults to "false".
vmware_ignorewarning  | Sometimes 2 (warning) is returned from a component. But the check itself is ok (from an operator view). With this option the plugin will return OK (0) instead of WARNING (1). Defaults to "false".
vmware_timeout        | Seconds before plugin times out. Defaults to "90".
vmware_trace          | Set verbosity level of vSphere API request/respond trace.
vmware_sessionfile    | Session file name enhancement.
vmware_sessionfiledir | Path to store the **vmware_sessionfile** file. Defaults to "/var/spool/icinga2/tmp".
vmware_nosession      | No auth session -- IT SHOULD BE USED FOR TESTING PURPOSES ONLY!. Defaults to "false".
vmware_username       | The username to connect to Host or vCenter server. No value defined as default.
vmware_password       | The username's password. No value defined as default.
vmware_authfile       | Use auth file instead username/password to session connect. No effect if **vmware_username** and **vmware_password** are defined <br> **Authentication file content:** <br>  username=vmuser <br> password=p@ssw0rd
vmware_multiline      | Multiline output in overview. This mean technically that a multiline output uses a HTML **\<br\>** for the GUI. No value defined as default.

## esxi_hardware <a id="esxi-hardware"></a>

The [check_esxi_hardware.py](https://www.claudiokuenzler.com/nagios-plugins/check_esxi_hardware.php) plugin
uses the [pywbem](https://pywbem.github.io/pywbem/) Python library to monitor the hardware of ESXi servers
through the [VMWare API](https://www.vmware.com/support/pubs/sdk_pubs.html) and CIM service.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                    | Description
------------------------|------------
esxi_hardware_host      | **Required.** Specifies the host to monitor. Defaults to "$address$".
esxi_hardware_user      | **Required.** Specifies the user for polling. Must be a local user of the root group on the system. Can also be provided as a file path file:/path/to/.passwdfile, then first string of file is used.
esxi_hardware_pass      | **Required.** Password of the user. Can also be provided as a file path file:/path/to/.passwdfile, then second string of file is used.
esxi_hardware_port      | Specifies the CIM port to connect to. Defaults to 5989.
esxi_hardware_vendor    | Defines the vendor of the server: "auto", "dell", "hp", "ibm", "intel", "unknown" (default).
esxi_hardware_html      | Add web-links to hardware manuals for Dell servers (use your country extension). Only useful with **esxi_hardware_vendor** = dell.
esxi_hardware_ignore    | Comma separated list of elements to ignore.
esxi_hardware_perfdata  | Add performcedata for graphers like PNP4Nagios to the output. Defaults to false.
esxi_hardware_nopower   | Do not collect power performance data, when **esxi_hardware_perfdata** is set to true. Defaults to false.
esxi_hardware_novolts   | Do not collect voltage performance data, when **esxi_hardware_perfdata** is set to true. Defaults to false.
esxi_hardware_nocurrent | Do not collect current performance data, when **esxi_hardware_perfdata** is set to true. Defaults to false.
esxi_hardware_notemp    | Do not collect temperature performance data, when **esxi_hardware_perfdata** is set to true. Defaults to false.
esxi_hardware_nofan     | Do not collect fan performance data, when **esxi_hardware_perfdata** is set to true. Defaults to false.
esxi_hardware_nolcd     | Do not collect lcd/display status data. Defaults to false.
