## atlas backups exports jobs describe

Return one cloud backup export job for your project, cluster and job.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas backups exports jobs describe [flags]
atlas backups exports jobs get [flags]
atlas backups exports job describe [flags]
atlas backups exports job get [flags]
atlas backups export jobs describe [flags]
atlas backups export jobs get [flags]
atlas backups export job describe [flags]
atlas backups export job get [flags]
atlas backup exports jobs describe [flags]
atlas backup exports jobs get [flags]
atlas backup exports job describe [flags]
atlas backup exports job get [flags]
atlas backup export jobs describe [flags]
atlas backup export jobs get [flags]
atlas backup export job describe [flags]
atlas backup export job get [flags]
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

### SEE ALSO


* [atlas backups exports jobs](atlas_backups_exports_jobs.md)	- Manage cloud backup export jobs for your project.



