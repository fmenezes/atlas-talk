## atlas clusters search indexes delete

Delete the specified search index from the specified cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.



```

atlas clusters search indexes delete <indexId> [flags]
atlas clusters search indexes rm <indexId> [flags]
atlas clusters search index delete <indexId> [flags]
atlas clusters search index rm <indexId> [flags]
atlas clusters fts indexes delete <indexId> [flags]
atlas clusters fts indexes rm <indexId> [flags]
atlas clusters fts index delete <indexId> [flags]
atlas clusters fts index rm <indexId> [flags]
atlas cluster search indexes delete <indexId> [flags]
atlas cluster search indexes rm <indexId> [flags]
atlas cluster search index delete <indexId> [flags]
atlas cluster search index rm <indexId> [flags]
atlas cluster fts indexes delete <indexId> [flags]
atlas cluster fts indexes rm <indexId> [flags]
atlas cluster fts index delete <indexId> [flags]
atlas cluster fts index rm <indexId> [flags]
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

### SEE ALSO


* [atlas clusters search indexes](atlas_clusters_search_indexes.md)	- Manage Atlas Search indexes for your cluster.



