## atlas dataLakePipelines runs describe

Return the details for the specified data lake pipeline run for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataLakePipelines runs describe <pipelineRunId> [flags]
atlas dataLakePipelines run describe <pipelineRunId> [flags]
atlas datalakepipelines runs describe <pipelineRunId> [flags]
atlas datalakepipelines run describe <pipelineRunId> [flags]
atlas data-lake-pipelines runs describe <pipelineRunId> [flags]
atlas data-lake-pipelines run describe <pipelineRunId> [flags]
atlas dataLakePipeline runs describe <pipelineRunId> [flags]
atlas dataLakePipeline run describe <pipelineRunId> [flags]
atlas datalakepipeline runs describe <pipelineRunId> [flags]
atlas datalakepipeline run describe <pipelineRunId> [flags]
atlas data-lake-pipeline runs describe <pipelineRunId> [flags]
atlas data-lake-pipeline run describe <pipelineRunId> [flags]
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

### SEE ALSO


* [atlas dataLakePipelines runs](atlas_dataLakePipelines_runs.md)	- Data Lake pipelines runs.



