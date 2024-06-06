## atlas clusters sampleData describe

Return the details for the specified sample data load job.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters sampleData describe <id> [flags]
```

### Aliases
```

atlas clusters sampleData describe
atlas clusters sampleData get
atlas clusters sampledata describe
atlas clusters sampledata get
atlas clusters sample-data describe
atlas clusters sample-data get
atlas clusters sampleDatum describe
atlas clusters sampleDatum get
atlas clusters sampledatum describe
atlas clusters sampledatum get
atlas clusters sample-datum describe
atlas clusters sample-datum get
atlas cluster sampleData describe
atlas cluster sampleData get
atlas cluster sampledata describe
atlas cluster sampledata get
atlas cluster sample-data describe
atlas cluster sample-data get
atlas cluster sampleDatum describe
atlas cluster sampleDatum get
atlas cluster sampledatum describe
atlas cluster sampledatum get
atlas cluster sample-datum describe
atlas cluster sample-datum get
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

### See Also


* [atlas clusters sampleData](atlas_clusters_sampleData.md)	- Manage sample data for your cluster.



