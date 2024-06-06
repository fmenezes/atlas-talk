## atlas clusters connectionStrings describe

Return the SRV connection string for the cluster you specify.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters connectionStrings describe <clusterName> [flags]
```

### Aliases
```

atlas clusters connectionStrings describe
atlas clusters connectionStrings get
atlas clusters connectionstrings describe
atlas clusters connectionstrings get
atlas clusters connection-strings describe
atlas clusters connection-strings get
atlas clusters connectionString describe
atlas clusters connectionString get
atlas clusters connectionstring describe
atlas clusters connectionstring get
atlas clusters connection-string describe
atlas clusters connection-string get
atlas clusters cs describe
atlas clusters cs get
atlas cluster connectionStrings describe
atlas cluster connectionStrings get
atlas cluster connectionstrings describe
atlas cluster connectionstrings get
atlas cluster connection-strings describe
atlas cluster connection-strings get
atlas cluster connectionString describe
atlas cluster connectionString get
atlas cluster connectionstring describe
atlas cluster connectionstring get
atlas cluster connection-string describe
atlas cluster connection-string get
atlas cluster cs describe
atlas cluster cs get
```

### Examples

```
  # Return the JSON-formatted connection strings for the cluster named myCluster:
  atlas clusters connectionStrings describe myCluster --output json
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string        Type of connection string. If you specify 'private', this option retrieves the connection string for the network peering endpoint. If you specify 'privateEndpoint', this option retrieves the shard optimized connection strings for the private endpoints. (default "standard")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters connectionStrings](atlas_clusters_connectionStrings.md)	- Manage MongoDB cluster connection string.



