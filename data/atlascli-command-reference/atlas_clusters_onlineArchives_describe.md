## atlas clusters onlineArchives describe

Return the details for the specified online archive for your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas clusters onlineArchives describe <archiveId> [flags]
atlas clusters onlinearchives describe <archiveId> [flags]
atlas clusters online-archives describe <archiveId> [flags]
atlas clusters onlineArchive describe <archiveId> [flags]
atlas clusters onlinearchive describe <archiveId> [flags]
atlas clusters online-archive describe <archiveId> [flags]
atlas cluster onlineArchives describe <archiveId> [flags]
atlas cluster onlinearchives describe <archiveId> [flags]
atlas cluster online-archives describe <archiveId> [flags]
atlas cluster onlineArchive describe <archiveId> [flags]
atlas cluster onlinearchive describe <archiveId> [flags]
atlas cluster online-archive describe <archiveId> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the online archive with the ID 5f189832e26ec075e10c32d3 for the cluster named myCluster:
  atlas clusters onlineArchives describe 5f189832e26ec075e10c32d3 --clusterName myCluster --output json
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for describe
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



