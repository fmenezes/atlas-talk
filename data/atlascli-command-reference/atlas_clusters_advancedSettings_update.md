## atlas clusters advancedSettings update

Update advanced configuration settings for one cluster.


### Synopsis

Updates the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings.
Atlas supports this command only for M10+ clusters.




```

atlas clusters advancedSettings update <clusterName> [flags]
atlas clusters advancedsettings update <clusterName> [flags]
atlas clusters advanced-settings update <clusterName> [flags]
atlas clusters advancedSetting update <clusterName> [flags]
atlas clusters advancedsetting update <clusterName> [flags]
atlas clusters advanced-setting update <clusterName> [flags]
atlas clusters settings update <clusterName> [flags]
atlas cluster advancedSettings update <clusterName> [flags]
atlas cluster advancedsettings update <clusterName> [flags]
atlas cluster advanced-settings update <clusterName> [flags]
atlas cluster advancedSetting update <clusterName> [flags]
atlas cluster advancedsetting update <clusterName> [flags]
atlas cluster advanced-setting update <clusterName> [flags]
atlas cluster settings update <clusterName> [flags]
```

### Examples

```
  # Update the minimum oplog size for a cluster:
  atlas cluster advancedSettings update <clusterName> --projectId <projectId> --oplogSizeMB 1000

  # Update the minimum TLS protocol version for a cluster:
  atlas cluster advancedSettings update <clusterName> --projectId <projectId> --minimumEnabledTLSProtocol "TLS1_2"
```


### Flags

```
      --disableFailIndexKeyTooLong             Flag that disables writing documents that exceed 1024 bytes without indexing.
      --disableJavascript                      Flag that disables the execution of operations that perform server-side executions of JavaScript.
      --disableTableScan                       Flag that disables executing any query that requires a collection scan to return results.
      --enableFailIndexKeyTooLong              Flag that enables writing documents that exceed 1024 bytes without indexing.
      --enableJavascript                       Flag that enables the execution of operations that perform server-side executions of JavaScript.
      --enableTableScan                        Flag that enables executing any query that requires a collection scan to return results.
  -h, --help                                   help for update
      --oplogMinRetentionHours float           Minimum retention window for cluster's oplog expressed in hours.
      --oplogSizeMB int                        Storage limit of cluster's oplog expressed in megabytes.
  -o, --output string                          Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                       Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --readConcern string                     Default level of acknowledgment requested from MongoDB for read operations set for this cluster.
      --sampleRefreshIntervalBIConnector int   Interval in seconds at which the mongosqld process re-samples data to create its relational schema. (default -1)
      --sampleSizeBIConnector int              Number of documents per database to sample when gathering schema information. (default -1)
      --tlsProtocol string                     Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections.
      --writeConcern string                    Default level of acknowledgment requested from MongoDB for write operations set for this cluster.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters advancedSettings](atlas_clusters_advancedSettings.md)	- Manage advanced configuration settings for your cluster.



