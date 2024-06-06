## atlas clusters sampleData load

Load sample data into the specified cluster for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas clusters sampleData load <clusterName> [flags]
atlas clusters sampledata load <clusterName> [flags]
atlas clusters sample-data load <clusterName> [flags]
atlas clusters sampleDatum load <clusterName> [flags]
atlas clusters sampledatum load <clusterName> [flags]
atlas clusters sample-datum load <clusterName> [flags]
atlas cluster sampleData load <clusterName> [flags]
atlas cluster sampledata load <clusterName> [flags]
atlas cluster sample-data load <clusterName> [flags]
atlas cluster sampleDatum load <clusterName> [flags]
atlas cluster sampledatum load <clusterName> [flags]
atlas cluster sample-datum load <clusterName> [flags]
```

### Examples

```
  # Load sample data into the cluster named myCluster:
  atlas clusters sampleData load myCluster --output json
```


### Flags

```
  -h, --help               help for load
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters sampleData](atlas_clusters_sampleData.md)	- Manage sample data for your cluster.



