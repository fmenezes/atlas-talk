## atlas clusters onlineArchives delete

Remove the specified online archive from your cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.



```

atlas clusters onlineArchives delete <archiveId> [flags]
atlas clusters onlineArchives rm <archiveId> [flags]
atlas clusters onlinearchives delete <archiveId> [flags]
atlas clusters onlinearchives rm <archiveId> [flags]
atlas clusters online-archives delete <archiveId> [flags]
atlas clusters online-archives rm <archiveId> [flags]
atlas clusters onlineArchive delete <archiveId> [flags]
atlas clusters onlineArchive rm <archiveId> [flags]
atlas clusters onlinearchive delete <archiveId> [flags]
atlas clusters onlinearchive rm <archiveId> [flags]
atlas clusters online-archive delete <archiveId> [flags]
atlas clusters online-archive rm <archiveId> [flags]
atlas cluster onlineArchives delete <archiveId> [flags]
atlas cluster onlineArchives rm <archiveId> [flags]
atlas cluster onlinearchives delete <archiveId> [flags]
atlas cluster onlinearchives rm <archiveId> [flags]
atlas cluster online-archives delete <archiveId> [flags]
atlas cluster online-archives rm <archiveId> [flags]
atlas cluster onlineArchive delete <archiveId> [flags]
atlas cluster onlineArchive rm <archiveId> [flags]
atlas cluster onlinearchive delete <archiveId> [flags]
atlas cluster onlinearchive rm <archiveId> [flags]
atlas cluster online-archive delete <archiveId> [flags]
atlas cluster online-archive rm <archiveId> [flags]
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

### SEE ALSO


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



