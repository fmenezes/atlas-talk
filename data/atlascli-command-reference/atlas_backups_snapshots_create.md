## atlas backups snapshots create

Create a backup snapshot for your project and cluster.


### Synopsis

You can create on-demand backup snapshots for Atlas cluster tiers M10 and larger.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.
Atlas supports this command only for M10+ clusters.


### Usage
```
atlas backups snapshots create <clusterName> [flags]
```

### Aliases
```

atlas backups snapshots create
atlas backups snapshots take
atlas backups snapshot create
atlas backups snapshot take
atlas backup snapshots create
atlas backup snapshots take
atlas backup snapshot create
atlas backup snapshot take
```

### Examples

```
  # Create a backup snapshot for the cluster named myDemo that Atlas retains for 30 days:
  atlas backups snapshots create myDemo --desc "test" --retention 30
```


### Flags

```
      --desc string        Description of the on-demand snapshot.
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --retention int      Number of days that Atlas should retain the on-demand snapshot. Must be at least 1. (default 1)

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups snapshots](atlas_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



