## atlas setup

Register, authenticate, create, and access an Atlas cluster.


### Synopsis

This command takes you through registration, login, default profile creation, creating your first free tier cluster and connecting to it using MongoDB Shell.



```

atlas setup [flags]
atlas quickstart [flags]
```

### Examples

```
  # Override default cluster settings like name, provider, or database username by using the command options
  atlas setup --clusterName Test --provider GCP --username dbuserTest
```


### Flags

```
      --accessListIp strings          IP address to grant access to the deployment.
      --clusterName string            Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --currentIp                     Flag that adds the IP address from the host that is currently executing the command to the access list.
      --enableTerminationProtection   Enables termination protection for your cluster. You can't delete a cluster with termination protection enabled.
      --force                         Flag that indicates whether to skip the request for input and create a cluster with the default settings for any unspecified options.
      --gov                           Register with Atlas for Government.
  -h, --help                          help for setup
      --noBrowser                     Don't try to open a browser session.
      --password string               Password for the user.
      --projectId string              Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string               Name of your cloud service provider. Valid values are AWS, AZURE, or GCP.
  -r, --region string                 Physical location of your MongoDB cluster. For a complete list of supported AWS regions, see: https://dochub.mongodb.org/core/aws-atlas. For a complete list of supported Azure regions, see: https://dochub.mongodb.org/core/azure-atlas. For a complete list of supported GCP regions, see: https://dochub.mongodb.org/core/gcp-atlas.
      --skipMongosh                   Flag that indicates whether to skip accessing your deployment with MongoDB Shell.
      --skipSampleData                Flag that indicates whether to skip loading sample data into your MongoDB cluster.
      --tag stringToString            List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster. (default [])
      --tier string                   Tier for each data-bearing server in the cluster. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas. (default "M0")
      --username string               Username for authenticating to MongoDB.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas](atlas.md)	- CLI tool to manage MongoDB Atlas.



