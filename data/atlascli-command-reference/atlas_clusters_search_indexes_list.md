## atlas clusters search indexes list

List all Atlas Search indexes for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas clusters search indexes list [flags]
```

### Aliases
```

atlas clusters search indexes list
atlas clusters search indexes ls
atlas clusters search index list
atlas clusters search index ls
atlas clusters fts indexes list
atlas clusters fts indexes ls
atlas clusters fts index list
atlas clusters fts index ls
atlas cluster search indexes list
atlas cluster search indexes ls
atlas cluster search index list
atlas cluster search index ls
atlas cluster fts indexes list
atlas cluster fts indexes ls
atlas cluster fts index list
atlas cluster fts index ls
```

### Examples

```
  # Return the JSON-formatted list of Atlas search indexes on the sample_mflix.movies database in the cluster named myCluster:
  atlas clusters search indexes list --clusterName myCluster --db sample_mflix --collection movies --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --collection string    Name of the collection.
      --db string            Name of the database.
  -h, --help                 help for list
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search indexes](atlas_clusters_search_indexes.md)	- Manage Atlas Search indexes for your cluster.



