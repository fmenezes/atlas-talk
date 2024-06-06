## atlas clusters search nodes create

Create a search node for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner or Project Owner role.


### Usage
```
atlas clusters search nodes create [flags]
```

### Aliases
```

atlas clusters search nodes create
atlas clusters search node create
atlas clusters fts nodes create
atlas clusters fts node create
atlas cluster search nodes create
atlas cluster search node create
atlas cluster fts nodes create
atlas cluster fts node create
```

### Examples

```
  # Create a search node for the cluster named myCluster using a JSON node spec configuration file named spec.json:
  atlas clusters search nodes create --clusterName myCluster --file spec.json --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -f, --file string          Name of the JSON index configuration file to use.
  -h, --help                 help for create
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
  -w, --watch                Flag that indicates whether to watch the command until it completes its execution or the watch times out.
      --watchTimeout uint    Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters search nodes](atlas_clusters_search_nodes.md)	- Manage Atlas Search nodes for your cluster.



