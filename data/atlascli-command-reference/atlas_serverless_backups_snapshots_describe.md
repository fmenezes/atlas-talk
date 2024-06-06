## atlas serverless backups snapshots describe

Return the details for the specified snapshot for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas serverless backups snapshots describe [flags]
```

### Aliases
```

atlas serverless backups snapshots describe
atlas serverless backups snapshot describe
atlas serverless backup snapshots describe
atlas serverless backup snapshot describe
atlas sl backups snapshots describe
atlas sl backups snapshot describe
atlas sl backup snapshots describe
atlas sl backup snapshot describe
```

### Examples

```
  # Return the details for the backup snapshot with the ID 5f4007f327a3bd7b6f4103c5 for the instance named myDemo:
  atlas serverless backups snapshots describe --snapshotId 5f4007f327a3bd7b6f4103c5 --clusterName myDemo
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for describe
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --snapshotId string    Unique identifier of the snapshot.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas serverless backups snapshots](atlas_serverless_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



