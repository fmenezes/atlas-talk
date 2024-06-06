## atlas backups exports buckets create

Create an export destination for Atlas backups using an existing AWS S3 bucket.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups exports buckets create <bucketName> [flags]
```

### Aliases
```

atlas backups exports buckets create
atlas backups exports bucket create
atlas backups export buckets create
atlas backups export bucket create
atlas backup exports buckets create
atlas backup exports bucket create
atlas backup export buckets create
atlas backup export bucket create
```

### Examples

```
  # The following command creates an export destination for Atlas backups using the existing AWS S3 bucket named test-bucket:
  atlas backup export buckets create test-bucket --cloudProvider AWS --iamRoleId 12345678f901a234dbdb00ca
```


### Flags

```
      --cloudProvider string   Name of the provider of the cloud service where Atlas can access the S3 bucket. Atlas supports only AWS.
  -h, --help                   help for create
      --iamRoleId string       Unique identifier that Atlas assigns to the cloud provider access role for the bucket. To learn more about setting up and retrieving a cloud provider access role, see: https://dochub.mongodb.org/core/set-up-unified-aws-access.
  -o, --output string          Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string       Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups exports buckets](atlas_backups_exports_buckets.md)	- Manage cloud backup export buckets for your project.



