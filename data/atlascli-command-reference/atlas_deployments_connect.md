## atlas deployments connect

Connect to a deployment that is running locally or in Atlas. If the deployment is paused, make sure to run atlas deployments start first.



```

atlas deployments connect <deploymentName> [flags]
atlas deployment connect <deploymentName> [flags]
```



### Flags

```
      --connectWith string            Method for connecting to the deployment. Valid values are mongosh, compass, and skip.
      --connectionStringType string   Type of connection string. If you specify 'private', this option retrieves the connection string for the network peering endpoint. If you specify 'privateEndpoint', this option retrieves the shard optimized connection strings for the private endpoints. (default "standard")
  -h, --help                          help for connect
      --password string               Password for the user.
      --projectId string              Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string                   Type of deployment. Valid values are ATLAS or LOCAL.
      --username string               Username for authenticating to MongoDB.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments](atlas_deployments.md)	- Manage cloud and local deployments.



