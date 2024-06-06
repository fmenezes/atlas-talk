## atlas clusters upgrade

Upgrade a shared cluster's tier, disk size, and/or MongoDB version.


### Synopsis

This command is unavailable for dedicated clusters.

To use this command, you must authenticate with a user account or an API key with the Project Cluster Manager role.



```

atlas clusters upgrade <clusterName> [flags]
atlas cluster upgrade <clusterName> [flags]
```

### Examples

```
  # Upgrade the tier, disk size, and MongoDB version for the shared cluster named myCluster in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster upgrade myCluster --projectId 5e2211c17a3e5a48f5497de3 --tier M50 --diskSizeGB 20 --mdbVersion 7.0 --tag env=dev
```


### Flags

```
      --disableTerminationProtection   Disables termination protection for your cluster. You can delete a cluster with termination protection disabled.
      --diskSizeGB float               Capacity, in gigabytes, of the host's root volume.
      --enableTerminationProtection    Enables termination protection for your cluster. You can't delete a cluster with termination protection enabled.
  -f, --file string                    Path to an optional JSON configuration file that defines cluster settings. To learn more about cluster configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/cluster-config-file-atlascli. To learn more about cluster configuration files for MongoCLI, see https://dochub.mongodb.org/core/mms-cluster-settings-file-mcli.
  -h, --help                           help for upgrade
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



