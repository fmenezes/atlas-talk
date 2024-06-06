## atlas clusters update

Modify the settings of the specified cluster.


### Synopsis

You can specify modifications in a JSON configuration file with the --file flag.
		
You can't change the name of the cluster or downgrade the MongoDB version of your cluster.

You can only update a replica set to a single-shard cluster; you cannot update a replica set to a multi-sharded cluster. To learn more, see https://www.mongodb.com/docs/atlas/scale-cluster/#convert-a-replica-set-to-a-sharded-cluster and https://www.mongodb.com/docs/upcoming/tutorial/convert-replica-set-to-replicated-shard-cluster.

To use this command, you must authenticate with a user account or an API key with the Project Cluster Manager role.
Atlas supports this command only for M10+ clusters



```

atlas clusters update <clusterName> [flags]
atlas cluster update <clusterName> [flags]
```

### Examples

```
  # Update the tier for a cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --tier M50

  # Replace tags cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --tag key1=value1

  # Remove all tags from cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --tag =

  # Update the disk size for a cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --diskSizeGB 20

  # Update the MongoDB version for a cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --mdbVersion 5.0
  
  # Use a configuration file named cluster-config.json to update a cluster named myCluster for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas cluster update myCluster --projectId 5e2211c17a3e5a48f5497de3 --file cluster-config.json --output json
```


### Flags

```
      --disableTerminationProtection   Disables termination protection for your cluster. You can delete a cluster with termination protection disabled.
      --diskSizeGB float               Capacity, in gigabytes, of the host's root volume.
      --enableTerminationProtection    Enables termination protection for your cluster. You can't delete a cluster with termination protection enabled.
  -f, --file string                    Path to an optional JSON configuration file that defines cluster settings. To learn more about cluster configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/cluster-config-file-atlascli. To learn more about cluster configuration files for MongoCLI, see https://dochub.mongodb.org/core/mms-cluster-settings-file-mcli.
  -h, --help                           help for update
      --mdbVersion string              Major MongoDB version of the cluster.
  -o, --output string                  Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string               Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --tag stringToString             List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster. Passing this flag replaces preexisting data. (default [])
      --tier string                    Tier for each data-bearing server in the cluster. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



