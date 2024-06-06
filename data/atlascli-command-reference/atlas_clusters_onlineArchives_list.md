## atlas clusters onlineArchives list

Return all online archives for your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters onlineArchives list [flags]
atlas clusters onlineArchives ls [flags]
atlas clusters onlinearchives list [flags]
atlas clusters onlinearchives ls [flags]
atlas clusters online-archives list [flags]
atlas clusters online-archives ls [flags]
atlas clusters onlineArchive list [flags]
atlas clusters onlineArchive ls [flags]
atlas clusters onlinearchive list [flags]
atlas clusters onlinearchive ls [flags]
atlas clusters online-archive list [flags]
atlas clusters online-archive ls [flags]
atlas cluster onlineArchives list [flags]
atlas cluster onlineArchives ls [flags]
atlas cluster onlinearchives list [flags]
atlas cluster onlinearchives ls [flags]
atlas cluster online-archives list [flags]
atlas cluster online-archives ls [flags]
atlas cluster onlineArchive list [flags]
atlas cluster onlineArchive ls [flags]
atlas cluster onlinearchive list [flags]
atlas cluster onlinearchive ls [flags]
atlas cluster online-archive list [flags]
atlas cluster online-archive ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of online archives for the cluster named myCluster:
  atlas clusters onlineArchives list --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for list
      --limit int            Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount            Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int             Page number that specifies a page of results. (default 1)
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



