## atlas deployments search indexes describe

Describe a search index for the specified deployment.



```

atlas deployments search indexes describe <indexId> [flags]
atlas deployments search index describe <indexId> [flags]
atlas deployment search indexes describe <indexId> [flags]
atlas deployment search index describe <indexId> [flags]
```



### Flags

```
      --deploymentName string   Name of the deployment.
  -h, --help                    help for describe
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --password string         Password for the user.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string             Type of deployment. Valid values are ATLAS or LOCAL.
      --username string         Username for authenticating to MongoDB.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments search indexes](atlas_deployments_search_indexes.md)	- Manage cloud and local search indexes.



