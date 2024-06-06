## atlas deployments setup

Create a local deployment.



```

atlas deployments setup <deploymentName> [flags]
atlas deployment setup <deploymentName> [flags]
```



### Flags

```
      --accessListIp strings          IP address to grant access to the deployment.
      --bindIpAll                     Flag that indicates whether the LOCAL deployment port binding should happen for all IPs or only for the localhost interface 127.0.0.1.
      --connectWith string            Method for connecting to the deployment. Valid values are mongosh, compass, and skip.
      --currentIp                     Flag that adds the IP address from the host that is currently executing the command to the access list.
      --enableTerminationProtection   Enables termination protection for your deployment. You can't delete a deployment with termination protection enabled.
      --force                         Flag that indicates whether to skip the request for input and create a deployment with the default settings for any unspecified options.
  -h, --help                          help for setup
      --mdbVersion string             Major MongoDB version of the deployment.
      --password string               Password for the user.
      --port int                      Port that the MongoDB server listens to for client connections.
      --projectId string              Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string               Name of your cloud service provider. Valid values are AWS, AZURE, or GCP.
  -r, --region string                 Physical location of your MongoDB deployment. For a complete list of supported AWS regions, see: https://dochub.mongodb.org/core/aws-atlas. For a complete list of supported Azure regions, see: https://dochub.mongodb.org/core/azure-atlas. For a complete list of supported GCP regions, see: https://dochub.mongodb.org/core/gcp-atlas.
      --skipMongosh                   Flag that indicates whether to skip accessing your deployment with MongoDB Shell.
      --skipSampleData                Flag that indicates whether to skip loading sample data into your MongoDB deployment.
      --tag stringToString            List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the deployment. (default [])
      --tier string                   Tier for each data-bearing server in the deployment. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas. (default "M0")
      --type string                   Type of deployment that you want to create. Valid values are ATLAS or LOCAL.
      --username string               Username for authenticating to MongoDB.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments](atlas_deployments.md)	- Manage cloud and local deployments.



