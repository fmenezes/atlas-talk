## atlas clusters sampleData describe

Return the details for the specified sample data load job.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters sampleData describe <id> [flags]
atlas clusters sampleData get <id> [flags]
atlas clusters sampledata describe <id> [flags]
atlas clusters sampledata get <id> [flags]
atlas clusters sample-data describe <id> [flags]
atlas clusters sample-data get <id> [flags]
atlas clusters sampleDatum describe <id> [flags]
atlas clusters sampleDatum get <id> [flags]
atlas clusters sampledatum describe <id> [flags]
atlas clusters sampledatum get <id> [flags]
atlas clusters sample-datum describe <id> [flags]
atlas clusters sample-datum get <id> [flags]
atlas cluster sampleData describe <id> [flags]
atlas cluster sampleData get <id> [flags]
atlas cluster sampledata describe <id> [flags]
atlas cluster sampledata get <id> [flags]
atlas cluster sample-data describe <id> [flags]
atlas cluster sample-data get <id> [flags]
atlas cluster sampleDatum describe <id> [flags]
atlas cluster sampleDatum get <id> [flags]
atlas cluster sampledatum describe <id> [flags]
atlas cluster sampledatum get <id> [flags]
atlas cluster sample-datum describe <id> [flags]
atlas cluster sample-datum get <id> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the sample data load job:
  atlas clusters sampleData describe 5e98249d937cfc52efdc2a9f --output json
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters sampleData](atlas_clusters_sampleData.md)	- Manage sample data for your cluster.



