## atlas clusters search nodes list

List all Atlas Search nodes for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters search nodes list [flags]
atlas clusters search nodes ls [flags]
atlas clusters search node list [flags]
atlas clusters search node ls [flags]
atlas clusters fts nodes list [flags]
atlas clusters fts nodes ls [flags]
atlas clusters fts node list [flags]
atlas clusters fts node ls [flags]
atlas cluster search nodes list [flags]
atlas cluster search nodes ls [flags]
atlas cluster search node list [flags]
atlas cluster search node ls [flags]
atlas cluster fts nodes list [flags]
atlas cluster fts nodes ls [flags]
atlas cluster fts node list [flags]
atlas cluster fts node ls [flags]
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

### SEE ALSO


* [atlas clusters search nodes](atlas_clusters_search_nodes.md)	- Manage Atlas Search nodes for your cluster.



