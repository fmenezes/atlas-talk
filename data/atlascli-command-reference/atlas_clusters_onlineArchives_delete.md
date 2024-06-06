## atlas clusters onlineArchives delete

Remove the specified online archive from your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters onlineArchives delete <archiveId> [flags]
```

### Aliases
```

atlas clusters onlineArchives delete
atlas clusters onlineArchives rm
atlas clusters onlinearchives delete
atlas clusters onlinearchives rm
atlas clusters online-archives delete
atlas clusters online-archives rm
atlas clusters onlineArchive delete
atlas clusters onlineArchive rm
atlas clusters onlinearchive delete
atlas clusters onlinearchive rm
atlas clusters online-archive delete
atlas clusters online-archive rm
atlas cluster onlineArchives delete
atlas cluster onlineArchives rm
atlas cluster onlinearchives delete
atlas cluster onlinearchives rm
atlas cluster online-archives delete
atlas cluster online-archives rm
atlas cluster onlineArchive delete
atlas cluster onlineArchive rm
atlas cluster onlinearchive delete
atlas cluster onlinearchive rm
atlas cluster online-archive delete
atlas cluster online-archive rm
```

### Examples

```
  # Remove an online archive with the ID 5f189832e26ec075e10c32d3 for the cluster named myCluster:
  atlas clusters onlineArchives delete 5f189832e26ec075e10c32d3 --clusterName myCluster
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

### See Also


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



