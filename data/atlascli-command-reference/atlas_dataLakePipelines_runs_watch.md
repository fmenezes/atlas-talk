## atlas dataLakePipelines runs watch

Watch for the specified data lake pipeline run to complete.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataLakePipelines runs watch <pipelineName> [flags]
atlas dataLakePipelines run watch <pipelineName> [flags]
atlas datalakepipelines runs watch <pipelineName> [flags]
atlas datalakepipelines run watch <pipelineName> [flags]
atlas data-lake-pipelines runs watch <pipelineName> [flags]
atlas data-lake-pipelines run watch <pipelineName> [flags]
atlas dataLakePipeline runs watch <pipelineName> [flags]
atlas dataLakePipeline run watch <pipelineName> [flags]
atlas datalakepipeline runs watch <pipelineName> [flags]
atlas datalakepipeline run watch <pipelineName> [flags]
atlas data-lake-pipeline runs watch <pipelineName> [flags]
atlas data-lake-pipeline run watch <pipelineName> [flags]
```

### Examples

```
# watches the pipeline 'Pipeline1':
  atlas dataLakePipelines watch Pipeline1

```


### Flags

```
  -h, --help               help for watch
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



