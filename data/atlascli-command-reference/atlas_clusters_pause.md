## atlas clusters pause

Pause the specified running MongoDB cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Cluster Manager role.
Atlas supports this command only for M10+ clusters.


### Usage
```
atlas clusters pause <clusterName> [flags]
```

### Aliases
```

atlas clusters pause
atlas cluster pause
```

### Examples

```
  # Pause the cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas clusters pause myCluster --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for pause
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



