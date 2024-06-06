## atlas clusters search nodes delete

Delete a search node for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner or Project Owner role.



```

atlas clusters search nodes delete [flags]
atlas clusters search node delete [flags]
atlas clusters fts nodes delete [flags]
atlas clusters fts node delete [flags]
atlas cluster search nodes delete [flags]
atlas cluster search node delete [flags]
atlas cluster fts nodes delete [flags]
atlas cluster fts node delete [flags]
```

### Examples

```
  # Delete a search node for the cluster named myCluster:
  atlas clusters search nodes delete --clusterName myCluster
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --force                Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                 help for delete
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
  -w, --watch                Flag that indicates whether to watch the command until it completes its execution or the watch times out.
      --watchTimeout uint    Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters search nodes](atlas_clusters_search_nodes.md)	- Manage Atlas Search nodes for your cluster.



