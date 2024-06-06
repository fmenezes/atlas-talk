## atlas dataLakePipelines delete

Remove the specified data lake pipeline from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataLakePipelines delete <pipelineName> [flags]
atlas dataLakePipelines rm <pipelineName> [flags]
atlas datalakepipelines delete <pipelineName> [flags]
atlas datalakepipelines rm <pipelineName> [flags]
atlas data-lake-pipelines delete <pipelineName> [flags]
atlas data-lake-pipelines rm <pipelineName> [flags]
atlas dataLakePipeline delete <pipelineName> [flags]
atlas dataLakePipeline rm <pipelineName> [flags]
atlas datalakepipeline delete <pipelineName> [flags]
atlas datalakepipeline rm <pipelineName> [flags]
atlas data-lake-pipeline delete <pipelineName> [flags]
atlas data-lake-pipeline rm <pipelineName> [flags]
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

### SEE ALSO


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



