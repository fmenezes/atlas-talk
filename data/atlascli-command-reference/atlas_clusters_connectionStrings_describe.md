## atlas clusters connectionStrings describe

Return the SRV connection string for the cluster you specify.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters connectionStrings describe <clusterName> [flags]
atlas clusters connectionStrings get <clusterName> [flags]
atlas clusters connectionstrings describe <clusterName> [flags]
atlas clusters connectionstrings get <clusterName> [flags]
atlas clusters connection-strings describe <clusterName> [flags]
atlas clusters connection-strings get <clusterName> [flags]
atlas clusters connectionString describe <clusterName> [flags]
atlas clusters connectionString get <clusterName> [flags]
atlas clusters connectionstring describe <clusterName> [flags]
atlas clusters connectionstring get <clusterName> [flags]
atlas clusters connection-string describe <clusterName> [flags]
atlas clusters connection-string get <clusterName> [flags]
atlas clusters cs describe <clusterName> [flags]
atlas clusters cs get <clusterName> [flags]
atlas cluster connectionStrings describe <clusterName> [flags]
atlas cluster connectionStrings get <clusterName> [flags]
atlas cluster connectionstrings describe <clusterName> [flags]
atlas cluster connectionstrings get <clusterName> [flags]
atlas cluster connection-strings describe <clusterName> [flags]
atlas cluster connection-strings get <clusterName> [flags]
atlas cluster connectionString describe <clusterName> [flags]
atlas cluster connectionString get <clusterName> [flags]
atlas cluster connectionstring describe <clusterName> [flags]
atlas cluster connectionstring get <clusterName> [flags]
atlas cluster connection-string describe <clusterName> [flags]
atlas cluster connection-string get <clusterName> [flags]
atlas cluster cs describe <clusterName> [flags]
atlas cluster cs get <clusterName> [flags]
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

### SEE ALSO


* [atlas clusters connectionStrings](atlas_clusters_connectionStrings.md)	- Manage MongoDB cluster connection string.



