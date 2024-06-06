## atlas deployments search indexes create

Create a search index for the specified deployment.


### Usage
```
atlas deployments search indexes create <indexName> [flags]
```

### Aliases
```

atlas deployments search indexes create
atlas deployments search index create
atlas deployment search indexes create
atlas deployment search index create
```



### Flags

```
      --collection string       Name of the collection.
      --db string               Name of the database.
      --deploymentName string   Name of the deployment.
  -f, --file string             Name of the JSON index configuration file to use. To learn about the Atlas Search and Atlas Vector Search index configuration file, see https://dochub.mongodb.org/core/search-index-config-file-atlascli. To learn about the Atlas Search index syntax and options that you can define in your configuration file, see https://dochub.mongodb.org/core/index-definitions-fts. To learn about the Atlas Vector Search index syntax and options that you can define in your configuration file, see https://dochub.mongodb.org/core/index-definition-avs.
  -h, --help                    help for create
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --password string         Password for the user.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string             Type of deployment. Valid values are ATLAS or LOCAL.
      --username string         Username for authenticating to MongoDB.
  -w, --watch                   Flag that indicates whether to watch the command until it completes its execution or the watch times out. To set the time that the watch times out, use the --watchTimeout option.
      --watchTimeout uint       Time in seconds until a watch times out. After a watch times out, the CLI no longer watches the command.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas deployments search indexes](atlas_deployments_search_indexes.md)	- Manage cloud and local search indexes.



