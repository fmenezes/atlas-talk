## atlas backups snapshots delete

Remove the specified backup snapshot.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.
Atlas supports this command only for M10+ clusters.


### Usage
```
atlas backups snapshots delete <snapshotId> [flags]
```

### Aliases
```

atlas backups snapshots delete
atlas backups snapshots rm
atlas backups snapshot delete
atlas backups snapshot rm
atlas backup snapshots delete
atlas backup snapshots rm
atlas backup snapshot delete
atlas backup snapshot rm
```

### Examples

```
  # Remove the backup snapshot with the ID 5f4007f327a3bd7b6f4103c5 for the cluster named myDemo:
  atlas backups snapshots delete 5f4007f327a3bd7b6f4103c5 --clusterName myDemo
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --force                Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                 help for delete
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups snapshots](atlas_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



