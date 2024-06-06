## atlas serverless backups snapshots watch

Watch the specified snapshot in your project until it reaches a completed or failed status.


### Synopsis

This command checks the snapshot's status periodically until it reaches a completed or failed status. 
Command finishes once one of the expected statuses are reached.
If you run the command in the terminal, it blocks the terminal session until the resource status completes or fails.
You can interrupt the command's polling at any time with CTRL-C.
To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas serverless backups snapshots watch [flags]
atlas serverless backups snapshot watch [flags]
atlas serverless backup snapshots watch [flags]
atlas serverless backup snapshot watch [flags]
atlas sl backups snapshots watch [flags]
atlas sl backups snapshot watch [flags]
atlas sl backup snapshots watch [flags]
atlas sl backup snapshot watch [flags]
```

### Examples

```
  # Watch the backup snapshot with the ID 5f4007f327a3bd7b6f4103c5 in the cluster named myDemo until it becomes available:
  atlas backups snapshots watch 5f4007f327a3bd7b6f4103c5 --clusterName myDemo
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for watch
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --snapshotId string    Unique identifier of the snapshot.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas serverless backups snapshots](atlas_serverless_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



