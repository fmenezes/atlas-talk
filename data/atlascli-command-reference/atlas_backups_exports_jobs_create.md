## atlas backups exports jobs create

Export one backup snapshot for an M10 or higher Atlas cluster to an existing AWS S3 bucket.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas backups exports jobs create [flags]
atlas backups exports job create [flags]
atlas backups export jobs create [flags]
atlas backups export job create [flags]
atlas backup exports jobs create [flags]
atlas backup exports job create [flags]
atlas backup export jobs create [flags]
atlas backup export job create [flags]
```

### Examples

```
  # The following command exports one backup snapshot of the ExampleCluster cluster to an existing AWS S3 bucket:
  atlas backup export jobs create --clusterName ExampleCluster --bucketId 62c569f85b7a381c093cc539 --snapshotId 62c808ceeb4e021d850dfe1b --customData name=test,info=test
```


### Flags

```
      --bucketId string             Unique identifier that Atlas assigns to the bucket.
      --clusterName string          Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --customData stringToString   Custom data to include in the metadata file named .complete that Atlas uploads to the bucket when the export job finishes. Custom data can be specified as key and value pairs. (default [])
  -h, --help                        help for create
  -o, --output string               Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string            Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --snapshotId string           Unique identifier of the snapshot.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups exports jobs](atlas_backups_exports_jobs.md)	- Manage cloud backup export jobs for your project.



