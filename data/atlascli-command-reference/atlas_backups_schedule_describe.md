## atlas backups schedule describe

Describe a cloud backup schedule for the cluster you specify.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas backups schedule describe <clusterName> [flags]
atlas backups schedule get <clusterName> [flags]
atlas backup schedule describe <clusterName> [flags]
atlas backup schedule get <clusterName> [flags]
```

### Examples

```
  # Return the cloud backup schedule for the cluster named Cluster0:
  atlas backup schedule describe Cluster0
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


* [atlas backups schedule](atlas_backups_schedule.md)	- Return a cloud backup schedule for the cluster you specify.



