## atlas clusters onlineArchives list

Return all online archives for your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters onlineArchives list [flags]
```

### Aliases
```

atlas clusters onlineArchives list
atlas clusters onlineArchives ls
atlas clusters onlinearchives list
atlas clusters onlinearchives ls
atlas clusters online-archives list
atlas clusters online-archives ls
atlas clusters onlineArchive list
atlas clusters onlineArchive ls
atlas clusters onlinearchive list
atlas clusters onlinearchive ls
atlas clusters online-archive list
atlas clusters online-archive ls
atlas cluster onlineArchives list
atlas cluster onlineArchives ls
atlas cluster onlinearchives list
atlas cluster onlinearchives ls
atlas cluster online-archives list
atlas cluster online-archives ls
atlas cluster onlineArchive list
atlas cluster onlineArchive ls
atlas cluster onlinearchive list
atlas cluster onlinearchive ls
atlas cluster online-archive list
atlas cluster online-archive ls
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

### See Also


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



