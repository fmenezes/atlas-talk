## atlas dataLakePipelines runs describe

Return the details for the specified data lake pipeline run for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines runs describe <pipelineRunId> [flags]
```

### Aliases
```

atlas dataLakePipelines runs describe
atlas dataLakePipelines run describe
atlas datalakepipelines runs describe
atlas datalakepipelines run describe
atlas data-lake-pipelines runs describe
atlas data-lake-pipelines run describe
atlas dataLakePipeline runs describe
atlas dataLakePipeline run describe
atlas datalakepipeline runs describe
atlas datalakepipeline run describe
atlas data-lake-pipeline runs describe
atlas data-lake-pipeline run describe
```

### Examples

```
# retrieves pipeline run '507f1f77bcf86cd799439011':
  atlas dataLakePipelines runs describe 507f1f77bcf86cd799439011

```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --pipeline string    Name of the Data lake pipeline.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataLakePipelines runs](atlas_dataLakePipelines_runs.md)	- Data Lake pipelines runs.



