## atlas clusters advancedSettings describe

Retrieve advanced configuration settings for one cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters advancedSettings describe <clusterName> [flags]
```

### Aliases
```

atlas clusters advancedSettings describe
atlas clusters advancedSettings get
atlas clusters advancedsettings describe
atlas clusters advancedsettings get
atlas clusters advanced-settings describe
atlas clusters advanced-settings get
atlas clusters advancedSetting describe
atlas clusters advancedSetting get
atlas clusters advancedsetting describe
atlas clusters advancedsetting get
atlas clusters advanced-setting describe
atlas clusters advanced-setting get
atlas clusters settings describe
atlas clusters settings get
atlas cluster advancedSettings describe
atlas cluster advancedSettings get
atlas cluster advancedsettings describe
atlas cluster advancedsettings get
atlas cluster advanced-settings describe
atlas cluster advanced-settings get
atlas cluster advancedSetting describe
atlas cluster advancedSetting get
atlas cluster advancedsetting describe
atlas cluster advancedsetting get
atlas cluster advanced-setting describe
atlas cluster advanced-setting get
atlas cluster settings describe
atlas cluster settings get
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

### See Also


* [atlas clusters advancedSettings](atlas_clusters_advancedSettings.md)	- Manage advanced configuration settings for your cluster.



