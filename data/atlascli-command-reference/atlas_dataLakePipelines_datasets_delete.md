## atlas dataLakePipelines datasets delete

Remove the specified data lake pipeline dataset from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines datasets delete <pipelineRunId> [flags]
```

### Aliases
```

atlas dataLakePipelines datasets delete
atlas dataLakePipelines dataset delete
atlas datalakepipelines datasets delete
atlas datalakepipelines dataset delete
atlas data-lake-pipelines datasets delete
atlas data-lake-pipelines dataset delete
atlas dataLakePipeline datasets delete
atlas dataLakePipeline dataset delete
atlas datalakepipeline datasets delete
atlas datalakepipeline dataset delete
atlas data-lake-pipeline datasets delete
atlas data-lake-pipeline dataset delete
```

### Examples

```
# delete dataset '507f1f77bcf86cd799439011' for data lake pipeline called 'Pipeline1':
  atlas dataLakePipelines datasets delete 507f1f77bcf86cd799439011 --pipeline Pipeline1

```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --pipeline string    Name of the Data lake pipeline.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataLakePipelines datasets](atlas_dataLakePipelines_datasets.md)	- Manage datasets for the specified data lake pipeline.



