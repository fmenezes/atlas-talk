## atlas clusters search indexes describe

Return the details for the search index for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas clusters search indexes describe <indexId> [flags]
```

### Aliases
```

atlas clusters search indexes describe
atlas clusters search index describe
atlas clusters fts indexes describe
atlas clusters fts index describe
atlas cluster search indexes describe
atlas cluster search index describe
atlas cluster fts indexes describe
atlas cluster fts index describe
```

### Examples

```
  # Return the JSON-formatted details for the search index with the ID 5f1f40842f2ac35f49190c20 for the cluster named myCluster:
  atlas clusters search indexes describe 5f1f40842f2ac35f49190c20 --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for describe
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search indexes](atlas_clusters_search_indexes.md)	- Manage Atlas Search indexes for your cluster.



