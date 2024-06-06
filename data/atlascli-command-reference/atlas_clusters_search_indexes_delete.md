## atlas clusters search indexes delete

Delete the specified search index from the specified cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters search indexes delete <indexId> [flags]
```

### Aliases
```

atlas clusters search indexes delete
atlas clusters search indexes rm
atlas clusters search index delete
atlas clusters search index rm
atlas clusters fts indexes delete
atlas clusters fts indexes rm
atlas clusters fts index delete
atlas clusters fts index rm
atlas cluster search indexes delete
atlas cluster search indexes rm
atlas cluster search index delete
atlas cluster search index rm
atlas cluster fts indexes delete
atlas cluster fts indexes rm
atlas cluster fts index delete
atlas cluster fts index rm
```

### Examples

```
  # Delete the search index with the ID 5f2099cd683fc55fbb30bef6 for the cluster named myCluster without requiring confirmation:
  atlas clusters search indexes delete 5f2099cd683fc55fbb30bef6 --clusterName myCluster --force
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --force                Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                 help for delete
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search indexes](atlas_clusters_search_indexes.md)	- Manage Atlas Search indexes for your cluster.



