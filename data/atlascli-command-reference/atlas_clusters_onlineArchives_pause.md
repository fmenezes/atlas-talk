## atlas clusters onlineArchives pause

Pause the specfied online archive for your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters onlineArchives pause <archiveId> [flags]
```

### Aliases
```

atlas clusters onlineArchives pause
atlas clusters onlinearchives pause
atlas clusters online-archives pause
atlas clusters onlineArchive pause
atlas clusters onlinearchive pause
atlas clusters online-archive pause
atlas cluster onlineArchives pause
atlas cluster onlinearchives pause
atlas cluster online-archives pause
atlas cluster onlineArchive pause
atlas cluster onlinearchive pause
atlas cluster online-archive pause
```

### Examples

```
  # Pause the online archive with the ID 5f189832e26ec075e10c32d3 for the cluster named myCluster:
  atlas clusters onlineArchives pause 5f189832e26ec075e10c32d3 --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for pause
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



