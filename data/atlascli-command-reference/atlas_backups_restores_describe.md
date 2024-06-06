## atlas backups restores describe

Describe a cloud backup restore job.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas backups restores describe <restoreJobId> [flags]
atlas backups restore describe <restoreJobId> [flags]
atlas backup restores describe <restoreJobId> [flags]
atlas backup restore describe <restoreJobId> [flags]
```

### Examples

```
  # Return the details for the continuous backup restore job with the ID 507f1f77bcf86cd799439011 for the cluster named Cluster0:
  atlas backup restore describe 507f1f77bcf86cd799439011 --clusterName Cluster0
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for describe
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups restores](atlas_backups_restores.md)	- Manage cloud backup restore jobs for your project.



