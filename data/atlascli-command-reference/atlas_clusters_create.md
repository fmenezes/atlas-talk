## atlas clusters create

Create a cluster for your project.


### Synopsis

To get started quickly, specify a name for your cluster, a cloud provider, and a region to deploy a three-member replica set with the latest MongoDB server version.
For full control of your deployment, or to create multi-cloud clusters, provide a JSON configuration file with the --file flag.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas clusters create <name> [flags]
atlas cluster create <name> [flags]
```

### Examples

```
  # Deploy a free cluster named myCluster for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster create myCluster --projectId 5e2211c17a3e5a48f5497de3 --provider AWS --region US_EAST_1 --tier M0

  # Deploy a free cluster named myCluster for the project with the ID 5e2211c17a3e5a48f5497de3 and tag "env=dev":
  atlas cluster create myCluster --projectId 5e2211c17a3e5a48f5497de3 --provider AWS --region US_EAST_1 --tier M0 --tag env=dev

  # Deploy a three-member replica set named myRS in AWS for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster create myRS --projectId 5e2211c17a3e5a48f5497de3 --provider AWS --region US_EAST_1 --members 3 --tier M10 --mdbVersion 5.0 --diskSizeGB 10

  # Deploy a three-member replica set named myRS in AZURE for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster create myRS --projectId 5e2211c17a3e5a48f5497de3 --provider AZURE --region US_EAST_2 --members 3 --tier M10  --mdbVersion 5.0 --diskSizeGB 10
  
  # Deploy a three-member replica set named myRS in GCP for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster create myRS --projectId 5e2211c17a3e5a48f5497de3 --provider GCP --region EASTERN_US --members 3 --tier M10  --mdbVersion 5.0 --diskSizeGB 10

  # Deploy a cluster or a multi-cloud cluster from a JSON configuration file named myfile.json for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas cluster create --projectId <projectId> --file myfile.json
```


### Flags

```
      --backup                        Flag that enables Continuous Cloud Backup for your deployment. This option is unavailable for clusters smaller than M10.
      --biConnector                   Flag that enables BI Connector for Atlas on the deployment.
      --diskSizeGB float              Capacity, in gigabytes, of the host's root volume. (default 2)
      --enableTerminationProtection   Enables termination protection for your cluster. You can't delete a cluster with termination protection enabled.
  -f, --file string                   Path to an optional JSON configuration file that defines cluster settings. To learn more about cluster configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/cluster-config-file-atlascli. To learn more about cluster configuration files for MongoCLI, see https://dochub.mongodb.org/core/mms-cluster-settings-file-mcli.
  -h, --help                          help for create
      --mdbVersion string             Major MongoDB version of the cluster. (default "7.0")
  -m, --members int                   Number of members in the replica set. (default 3)
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string              Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string               Name of your cloud service provider. Valid values are AWS, AZURE, or GCP. You must specify the provider option if you don't use the --file option.
  -r, --region string                 Physical location of your MongoDB cluster. You must specify the region option if you don't use the --file option. For a complete list of supported AWS regions, see: https://dochub.mongodb.org/core/aws-atlas. For a complete list of supported Azure regions, see: https://dochub.mongodb.org/core/azure-atlas. For a complete list of supported GCP regions, see: https://dochub.mongodb.org/core/gcp-atlas.
  -s, --shards int                    Number of shards in the cluster. (default 1)
      --tag stringToString            List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster. (default [])
      --tier string                   Tier for each data-bearing server in the cluster. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas. (default "M2")
      --type string                   Type of the cluster that you want to create. Valid values are REPLICASET or SHARDED. (default "REPLICASET")
  -w, --watch                         Flag that indicates whether to watch the command until it completes its execution or the watch times out. To set the time that the watch times out, use the --watchTimeout option.
      --watchTimeout uint             Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters](atlas_clusters.md)	- Manage clusters for your project.



