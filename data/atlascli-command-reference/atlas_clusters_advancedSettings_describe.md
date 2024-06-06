## atlas clusters advancedSettings describe

Retrieve advanced configuration settings for one cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters advancedSettings describe <clusterName> [flags]
atlas clusters advancedSettings get <clusterName> [flags]
atlas clusters advancedsettings describe <clusterName> [flags]
atlas clusters advancedsettings get <clusterName> [flags]
atlas clusters advanced-settings describe <clusterName> [flags]
atlas clusters advanced-settings get <clusterName> [flags]
atlas clusters advancedSetting describe <clusterName> [flags]
atlas clusters advancedSetting get <clusterName> [flags]
atlas clusters advancedsetting describe <clusterName> [flags]
atlas clusters advancedsetting get <clusterName> [flags]
atlas clusters advanced-setting describe <clusterName> [flags]
atlas clusters advanced-setting get <clusterName> [flags]
atlas clusters settings describe <clusterName> [flags]
atlas clusters settings get <clusterName> [flags]
atlas cluster advancedSettings describe <clusterName> [flags]
atlas cluster advancedSettings get <clusterName> [flags]
atlas cluster advancedsettings describe <clusterName> [flags]
atlas cluster advancedsettings get <clusterName> [flags]
atlas cluster advanced-settings describe <clusterName> [flags]
atlas cluster advanced-settings get <clusterName> [flags]
atlas cluster advancedSetting describe <clusterName> [flags]
atlas cluster advancedSetting get <clusterName> [flags]
atlas cluster advancedsetting describe <clusterName> [flags]
atlas cluster advancedsetting get <clusterName> [flags]
atlas cluster advanced-setting describe <clusterName> [flags]
atlas cluster advanced-setting get <clusterName> [flags]
atlas cluster settings describe <clusterName> [flags]
atlas cluster settings get <clusterName> [flags]
```

### Examples

```
  atlas clusters advancedSettings describe Cluster0
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters advancedSettings](atlas_clusters_advancedSettings.md)	- Manage advanced configuration settings for your cluster.



