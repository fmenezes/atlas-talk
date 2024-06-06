## atlas backups snapshots watch

Watch the specified snapshot in your project until it becomes available.


### Synopsis

This command checks the snapshot's status periodically until it reaches a completed or failed status. 
Once the snapshot reaches the expected status, the command prints "Snapshot changes completed."
If you run the command in the terminal, it blocks the terminal session until the resource status completes or fails.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas backups snapshots watch <snapshotId> [flags]
```

### Aliases
```

atlas backups snapshots watch
atlas backups snapshot watch
atlas backup snapshots watch
atlas backup snapshot watch
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

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups snapshots](atlas_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



