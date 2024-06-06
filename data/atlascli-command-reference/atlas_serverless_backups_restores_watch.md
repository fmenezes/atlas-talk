## atlas serverless backups restores watch

Watch the specified backup restore job until it completes.


### Synopsis

This command checks the restore job's status periodically until it reaches a completed, failed or canceled status. 
Command finishes once one of the expected statuses are reached.
If you run the command in the terminal, it blocks the terminal session until the resource status completes or fails.
You can interrupt the command's polling at any time with CTRL-C.
To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas serverless backups restores watch [flags]
atlas serverless backups restore watch [flags]
atlas serverless backup restores watch [flags]
atlas serverless backup restore watch [flags]
atlas sl backups restores watch [flags]
atlas sl backups restore watch [flags]
atlas sl backup restores watch [flags]
atlas sl backup restore watch [flags]
```

### Examples

```
  # Watch the continuous backup restore job with the ID 507f1f77bcf86cd799439011 for the cluster named Cluster0 until it becomes available:
  atlas serverless backup restore watch --restoreJobId 507f1f77bcf86cd799439011 --clusterName Cluster0
```


### Flags

```
      --clusterName string    Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                  help for watch
  -o, --output string         Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string      Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --restoreJobId string   Unique identifier that identifies the Restore Job.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas serverless backups restores](atlas_serverless_backups_restores.md)	- Manage cloud backup restore jobs for your project.



