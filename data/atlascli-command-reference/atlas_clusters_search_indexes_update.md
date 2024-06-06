## atlas clusters search indexes update

Modify a search index for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters search indexes update <indexId> [flags]
```

### Aliases
```

atlas clusters search indexes update
atlas clusters search index update
atlas clusters fts indexes update
atlas clusters fts index update
atlas cluster search indexes update
atlas cluster search index update
atlas cluster fts indexes update
atlas cluster fts index update
```

### Examples

```
  # Modify the search index with the ID 5f2099cd683fc55fbb30bef6 for the cluster named myCluster:
  atlas clusters search indexes update 5f2099cd683fc55fbb30bef6 --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -f, --file string          Name of the JSON index configuration file to use. To learn about the Atlas Search and Atlas Vector Search index configuration file, see https://dochub.mongodb.org/core/search-index-config-file-atlascli. To learn about the Atlas Search index syntax and options that you can define in your configuration file, see https://dochub.mongodb.org/core/index-definitions-fts. To learn about the Atlas Vector Search index syntax and options that you can define in your configuration file, see https://dochub.mongodb.org/core/index-definition-avs.
  -h, --help                 help for update
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search indexes](atlas_clusters_search_indexes.md)	- Manage Atlas Search indexes for your cluster.



