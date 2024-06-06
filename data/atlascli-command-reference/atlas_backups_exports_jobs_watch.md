## atlas backups exports jobs watch

Watch for the specified export job to complete.


### Synopsis

This command checks the export job's status periodically until it reaches a completed, cancelled or failed status. 
Once the export reaches the expected status, the command prints "Export completed."
If you run the command in the terminal, it blocks the terminal session until the resource status completes or fails.
You can interrupt the command's polling at any time with CTRL-C.
To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas backups exports jobs watch <exportJobId> [flags]
atlas backups exports job watch <exportJobId> [flags]
atlas backups export jobs watch <exportJobId> [flags]
atlas backups export job watch <exportJobId> [flags]
atlas backup exports jobs watch <exportJobId> [flags]
atlas backup exports job watch <exportJobId> [flags]
atlas backup export jobs watch <exportJobId> [flags]
atlas backup export job watch <exportJobId> [flags]
```

### Examples

```
  # Watch the continuous backup restore job with the ID 507f1f77bcf86cd799439011 for the cluster named Cluster0 until it becomes available:
  atlas backup restore watch 507f1f77bcf86cd799439011 --clusterName Cluster0
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for watch
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups exports jobs](atlas_backups_exports_jobs.md)	- Manage cloud backup export jobs for your project.



