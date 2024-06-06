## atlas clusters failover

Starts a failover test for the specified cluster in the specified project.


### Synopsis

Clusters contain a group of hosts that maintain the same data set. A failover test checks how MongoDB Cloud handles the failure of the cluster's primary node. During the test, MongoDB Cloud shuts down the primary node and elects a new primary.



```

atlas clusters failover <clusterName> [flags]
atlas cluster failover <clusterName> [flags]
```

### Examples

```
  # Test failover for a cluster named myCluster:
  atlas clusters failover myCluster
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for failover
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



