## atlas clusters onlineArchives watch

Watch for an archive to be available.


### Synopsis

This command checks the archive's status periodically until it reaches a state different from PENDING or PAUSING. 
Once the archive reaches the expected status, the command prints "Online archive available."
If you run the command in the terminal, it blocks the terminal session until the resource status changes to the expected status.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas clusters onlineArchives watch <archiveId> [flags]
```

### Aliases
```

atlas clusters onlineArchives watch
atlas clusters onlinearchives watch
atlas clusters online-archives watch
atlas clusters onlineArchive watch
atlas clusters onlinearchive watch
atlas clusters online-archive watch
atlas cluster onlineArchives watch
atlas cluster onlinearchives watch
atlas cluster online-archives watch
atlas cluster onlineArchive watch
atlas cluster onlinearchive watch
atlas cluster online-archive watch
```

### Examples

```
  atlas cluster onlineArchive watch archiveIdSample --clusterName clusterNameSample
```


### Flags

```
      --clusterName string   Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                 help for watch
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



