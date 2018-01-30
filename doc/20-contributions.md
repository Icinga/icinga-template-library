# Contributed Plugin Check Commands <a id="plugin-contrib"></a>

The contributed Plugin Check Commands provides various additional command definitions
contributed by community members.

These check commands assume that the global constant named `PluginContribDir`
is set to the path where the user installs custom plugins and can be enabled by
uncommenting the corresponding line in [icinga2.conf](04-configuring-icinga-2.md#icinga2-conf):

```
vim /etc/icinga2/icinga2.conf

include <plugin-contrib>
```

This is enabled by default since Icinga 2 2.5.0.
