## atlas clusters search nodes list

List all Atlas Search nodes for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters search nodes list [flags]
```

### Aliases
```

atlas clusters search nodes list
atlas clusters search nodes ls
atlas clusters search node list
atlas clusters search node ls
atlas clusters fts nodes list
atlas clusters fts nodes ls
atlas clusters fts node list
atlas clusters fts node ls
atlas cluster search nodes list
atlas cluster search nodes ls
atlas cluster search node list
atlas cluster search node ls
atlas cluster fts nodes list
atlas cluster fts nodes ls
atlas cluster fts node list
atlas cluster fts node ls
```

### Examples

```
  # Return the JSON-formatted list of Atlas search nodes in the cluster named myCluster:
  atlas clusters search nodes list --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for list
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search nodes](atlas_clusters_search_nodes.md)	- Manage Atlas Search nodes for your cluster.



