# Operating System <a id="operating-system"></a>

This category contains plugins which receive details about your operating system
or the guest system.

## iostat <a id="iostat"></a>

The [check_iostat](https://github.com/dnsmichi/icinga-plugins/blob/master/scripts/check_iostat) plugin
uses the `iostat` binary to monitor disk I/O on a Linux host. The default thresholds are rather high
so you can use a grapher for baselining before setting your own.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name          | Description
--------------|------------
iostat_disk   | **Required.** The device to monitor without path. e.g. sda or vda. (default: sda).
iostat_wtps   | **Required.** Warning threshold for tps (default: 100).
iostat_wread  | **Required.** Warning threshold for KB/s reads (default: 100).
iostat_wwrite | **Required.** Warning threshold for KB/s writes (default: 100).
iostat_ctps   | **Required.** Critical threshold for tps (default: 200).
iostat_cread  | **Required.** Critical threshold for KB/s reads (default: 200).
iostat_cwrite | **Required.** Critical threshold for KB/s writes (default: 200).

## iostats <a id="iostats"></a>

The [check_iostats](https://github.com/dnsmichi/icinga-plugins/blob/master/scripts/check_iostats) plugin
uses the `iostat` binary to monitor I/O on a Linux host. The default thresholds are rather high
so you can use a grapher for baselining before setting your own.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                   | Description
-----------------------|------------
iostats_disk           | **Required.** The device to monitor without path. e.g. sda or vda. (default: sda).
iostats_warning_tps    | **Required.** Warning threshold for tps (default: 3000).
iostats_warning_read   | **Required.** Warning threshold for KB/s reads (default: 50000).
iostats_warning_write  | **Required.** Warning threshold for KB/s writes (default: 10000).
iostats_warning_wait   | **Required.** Warning threshold for % iowait (default: 50).
iostats_critical_tps   | **Required.** Critical threshold for tps (default: 5000).
iostats_critical_read  | **Required.** Critical threshold for KB/s reads (default: 80000).
iostats_critical_write | **Required.** Critical threshold for KB/s writes (default: 25000).
iostats_critical_wait  | **Required.** Critical threshold for % iowait (default: 80).

## mem <a id="mem"></a>

The [check_mem.pl](https://github.com/justintime/nagios-plugins) plugin checks the
memory usage on linux and unix hosts. It is able to count cache memory as free when
compared to thresholds. More details can be found on [this blog entry](http://sysadminsjourney.com/content/2009/06/04/new-and-improved-checkmempl-nagios-plugin).

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name         | Description
-------------|------------
mem_used     | Tell the plugin to check for used memory in opposite of **mem_free**. Must specify one of these as true.
mem_free     | Tell the plugin to check for free memory in opposite of **mem_used**. Must specify one of these as true.
mem_cache    | If set to true, plugin will count cache as free memory. Defaults to false.
mem_warning  | **Required.** Specify the warning threshold as number interpreted as percent.
mem_critical | **Required.** Specify the critical threshold as number interpreted as percent.

## running_kernel <a id="running_kernel"></a>

The [check_running_kernel](https://packages.debian.org/stretch/nagios-plugins-contrib) plugin
is provided by the `nagios-plugin-contrib` package on Debian/Ubuntu.

Custom attributes:

Name                    | Description
------------------------|------------
running_kernel_use_sudo | Whether to run the plugin with `sudo`. Defaults to false except on Ubuntu where it defaults to true.

## yum <a id="yum"></a>

The [check_yum](https://github.com/calestyo/check_yum) plugin checks the YUM package
management system for package updates.
The plugin requires the `yum-plugin-security` package to differentiate between security and normal updates.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                   | Description
-----------------------|------------
yum_all_updates        | Set to true to not distinguish between security and non-security updates, but returns critical for any available update. This may be used if the YUM security plugin is absent or you want to maintain every single package at the latest version. You may want to use **yum_warn_on_any_update** instead of this option. Defaults to false.
yum_warn_on_any_update | Set to true to warn if there are any (non-security) package updates available. Defaults to false.
yum_cache_only         | If set to true, plugin runs entirely from cache and does not update the cache when running YUM. Useful if you have `yum makecache` cronned. Defaults to false.
yum_no_warn_on_lock    | If set to true, returns OK instead of WARNING when YUM is locked and fails to check for updates due to another instance running. Defaults to false.
yum_no_warn_on_updates | If set to true, returns OK instead of WARNING even when updates are available. The plugin output still shows the number of available updates. Defaults to false.
yum_enablerepo         | Explicitly enables a repository when calling YUM. Can take a comma separated list of repositories. Note that enabling repositories can lead to unexpected results, for example when protected repositories are enabled.
yum_disablerepo        | Explicitly disables a repository when calling YUM. Can take a comma separated list of repositories. Note that enabling repositories can lead to unexpected results, for example when protected repositories are enabled.
yum_installroot        | Specifies another installation root directory (for example a chroot).
yum_timeout            | Set a timeout in seconds after which the plugin will exit (defaults to 55 seconds).
