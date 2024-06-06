## atlas dataFederation update

Modify the details of the specified data federation database for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation update <name> [flags]
atlas datafederation update <name> [flags]
atlas data-federation update <name> [flags]
```

### Examples

```
# update data lake pipeline:
  atlas dataFederation update DataFederation1

```


### Flags

```
      --awsRoleId string         Amazon Resource Name (ARN) of the role which Atlas Data Federation uses for accessing the data stores.
      --awsTestS3Bucket string   Name of an Amazon S3 data bucket that Atlas Data Federation uses to validate the provided role.
  -f, --file string              Path to an optional JSON configuration file that defines data federation settings. To learn more about data federation configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-json-data-federation-config.
  -h, --help                     help for update
  -o, --output string            Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string         Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string            Name of the region to which Atlas Data Federation routes client connections for data processing.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation](atlas_dataFederation.md)	- Data federation.



