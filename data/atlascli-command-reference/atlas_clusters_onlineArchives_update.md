## atlas clusters onlineArchives update

Modify the archiving rule for the specified online archive for a cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Admin role.


### Usage
```
atlas clusters onlineArchives update <archiveId> [flags]
```

### Aliases
```

atlas clusters onlineArchives update
atlas clusters onlinearchives update
atlas clusters online-archives update
atlas clusters onlineArchive update
atlas clusters onlinearchive update
atlas clusters online-archive update
atlas cluster onlineArchives update
atlas cluster onlinearchives update
atlas cluster online-archives update
atlas cluster onlineArchive update
atlas cluster onlinearchive update
atlas cluster online-archive update
```

### Examples

```
  # Update the archiving rule to archive after 5 days for the online archive with the ID 5f189832e26ec075e10c32d3 for the cluster named myCluster:
  atlas clusters onlineArchives update 5f189832e26ec075e10c32d3 --clusterName --archiveAfter 5 myCluster --output json
```


### Flags

```
      --archiveAfter int      Number of days after which to archive cluster data.
      --clusterName string    Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --expireAfterDays int   Number of days used in the date criteria for nominating documents for deletion.
      --file string           Path to an optional JSON configuration file that defines online archive settings. To learn more about online archive configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-json-online-archive-config.
  -h, --help                  help for update
  -o, --output string         Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string      Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters onlineArchives](atlas_clusters_onlineArchives.md)	- Manage online archives for your cluster.



