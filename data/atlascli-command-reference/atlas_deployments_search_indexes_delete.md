## atlas deployments search indexes delete

Delete the specified search index from the specified deployment.


### Usage
```
atlas deployments search indexes delete <indexId> [flags]
```

### Aliases
```

atlas deployments search indexes delete
atlas deployments search indexes rm
atlas deployments search index delete
atlas deployments search index rm
atlas deployment search indexes delete
atlas deployment search indexes rm
atlas deployment search index delete
atlas deployment search index rm
```



### Flags

```
      --deploymentName string   Name of the deployment.
      --force                   Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                    help for delete
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

### See Also


* [atlas deployments search indexes](atlas_deployments_search_indexes.md)	- Manage cloud and local search indexes.



