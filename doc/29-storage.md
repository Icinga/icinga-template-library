# Storage <a id="plugins-contrib-storage"></a>

This category includes all plugins for various storage and object storage technologies.

## glusterfs <a id="plugins-contrib-command-glusterfs"></a>

The [glusterfs](https://www.unixadm.org/software/nagios-stuff/checks/check_glusterfs) plugin
is used to check the GlusterFS storage health on the server.
The plugin requires `sudo` permissions.

Custom attributes passed as [command parameters](03-monitoring-basics.md#command-passing-parameters):

Name                       | Description
---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
glusterfs_perfdata         | **Optional.** Print perfdata of all or the specified volume.
glusterfs_warnonfailedheal | **Optional.** Warn if the *heal-failed* log contains entries. The log can be cleared by restarting glusterd.
glusterfs_volume           | **Optional.** Only check the specified *VOLUME*. If --volume is not set, all volumes are checked.
glusterfs_disk_warning     | **Optional.** Warn if disk usage is above *DISKWARN*. Defaults to 90 (percent).
glusterfs_disk_critical    | **Optional.** Return a critical error if disk usage is above *DISKCRIT*. Defaults to 95 (percent).
glusterfs_inode_warning    | **Optional.** Warn if inode usage is above *DISKWARN*. Defaults to 90 (percent).
glusterfs_inode_critical   | **Optional.** Return a critical error if inode usage is above *DISKCRIT*. Defaults to 95 (percent).
