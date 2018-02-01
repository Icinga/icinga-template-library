# IPMI Devices <a id="ipmi"></a>

This category includes all plugins for IPMI devices.

## ipmi-alive <a id="ipmi-alive"></a>

The `ipmi-alive` check commands allows you to create a ping check for the IPMI Interface.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name         | Description
-------------|------------
ping_address | The address of the IPMI interface. Defaults to "$address$" if the IPMI interface's `address` attribute is set, "$address6$" otherwise.
ping_wrta    | The RTA warning threshold in milliseconds. Defaults to 5000.
ping_wpl     | The packet loss warning threshold in %. Defaults to 100.
ping_crta    | The RTA critical threshold in milliseconds. Defaults to 5000.
ping_cpl     | The packet loss critical threshold in %. Defaults to 100.
ping_packets | The number of packets to send. Defaults to 1.
ping_timeout | The plugin timeout in seconds. Defaults to 0 (no timeout).

## ipmi-sensor <a id="ipmi-sensor"></a>

The [check_ipmi_sensor](https://github.com/thomas-krenn/check_ipmi_sensor_v3) plugin
uses the `ipmimonitoring` binary to monitor sensor data for IPMI devices. Please
read the [documentation](https://www.thomas-krenn.com/en/wiki/IPMI_Sensor_Monitoring_Plugin)
for installation and configuration details.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                             | Description
---------------------------------|------------
ipmi_address                     | **Required.** Specifies the remote host (IPMI device) to check. Defaults to "$address$".
ipmi_config_file                 | Path to the FreeIPMI configuration file. It should contain IPMI username, IPMI password, and IPMI privilege-level.
ipmi_username                    | The IPMI username.
ipmi_password                    | The IPMI password.
ipmi_privilege_level             | The IPMI privilege level of the IPMI user.
ipmi_backward_compatibility_mode | Enable backward compatibility mode, useful for FreeIPMI 0.5.\* (this omits FreeIPMI options "--quiet-cache" and "--sdr-cache-recreate").
ipmi_sensor_type                 | Limit sensors to query based on IPMI sensor type. Examples for IPMI sensor types are 'Fan', 'Temperature' and 'Voltage'.
ipmi_sel_type                    | Limit SEL entries to specific types, run 'ipmi-sel -L' for a list of types. All sensors are populated to the SEL and per default all sensor types are monitored.
ipmi_exclude_sensor_id           | Exclude sensor matching ipmi_sensor_id.
ipmi_exclude_sensor              | Exclude sensor based on IPMI sensor type. (Comma-separated)
ipmi_exclude_sel                 | Exclude SEL entries of specific sensor types. (comma-separated list).
ipmi_sensor_id                   | Include sensor matching ipmi_sensor_id.
ipmi_protocol_lan_version        | Change the protocol LAN version. Defaults to "LAN_2_0".
ipmi_number_of_active_fans       | Number of fans that should be active. Otherwise a WARNING state is returned.
ipmi_show_fru                    | Print the product serial number if it is available in the IPMI FRU data.
ipmi_no_sel_checking             | Turn off system event log checking via ipmi-sel.
ipmi_no_thresholds               | Turn off performance data thresholds from output-sensor-thresholds.
ipmi_verbose                     | Be Verbose multi line output, also with additional details for warnings.
ipmi_debug                       | Be Verbose debugging output, followed by normal multi line output.
