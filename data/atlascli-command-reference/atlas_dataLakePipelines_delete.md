## atlas dataLakePipelines delete

Remove the specified data lake pipeline from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines delete <pipelineName> [flags]
```

### Aliases
```

atlas dataLakePipelines delete
atlas dataLakePipelines rm
atlas datalakepipelines delete
atlas datalakepipelines rm
atlas data-lake-pipelines delete
atlas data-lake-pipelines rm
atlas dataLakePipeline delete
atlas dataLakePipeline rm
atlas datalakepipeline delete
atlas datalakepipeline rm
atlas data-lake-pipeline delete
atlas data-lake-pipeline rm
```

### Examples

```
# deletes pipeline 'Pipeline1':
  atlas dataLakePipelines delete Pipeline1

```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



