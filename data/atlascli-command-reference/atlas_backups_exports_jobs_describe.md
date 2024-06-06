## atlas backups exports jobs describe

Return one cloud backup export job for your project, cluster and job.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups exports jobs describe [flags]
```

### Aliases
```

atlas backups exports jobs describe
atlas backups exports jobs get
atlas backups exports job describe
atlas backups exports job get
atlas backups export jobs describe
atlas backups export jobs get
atlas backups export job describe
atlas backups export job get
atlas backup exports jobs describe
atlas backup exports jobs get
atlas backup exports job describe
atlas backup exports job get
atlas backup export jobs describe
atlas backup export jobs get
atlas backup export job describe
atlas backup export job get
```

### Examples

```
  # Return the details for the continuous backup export job with the ID 5df90590f10fab5e33de2305 for the cluster named Cluster0:
  atlas backup exports jobs describe --clusterName Cluster0 --exportID 5df90590f10fab5e33de2305
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --exportId string      Unique string that identifies the AWS S3 bucket to which you export your snapshots.
  -h, --help                 help for describe
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups exports jobs](atlas_backups_exports_jobs.md)	- Manage cloud backup export jobs for your project.



