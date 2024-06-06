## atlas backups schedule delete

Delete all backup schedules of a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups schedule delete <clusterName> [flags]
```

### Aliases
```

atlas backups schedule delete
atlas backups schedule rm
atlas backup schedule delete
atlas backup schedule rm
```

### Examples

```
  # Remove all backup schedules for the cluster named Cluster0:
  atlas backup schedule delete Cluster0
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups schedule](atlas_backups_schedule.md)	- Return a cloud backup schedule for the cluster you specify.



