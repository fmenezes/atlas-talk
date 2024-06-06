## atlas dataLakePipelines runs watch

Watch for the specified data lake pipeline run to complete.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines runs watch <pipelineName> [flags]
```

### Aliases
```

atlas dataLakePipelines runs watch
atlas dataLakePipelines run watch
atlas datalakepipelines runs watch
atlas datalakepipelines run watch
atlas data-lake-pipelines runs watch
atlas data-lake-pipelines run watch
atlas dataLakePipeline runs watch
atlas dataLakePipeline run watch
atlas datalakepipeline runs watch
atlas datalakepipeline run watch
atlas data-lake-pipeline runs watch
atlas data-lake-pipeline run watch
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

### See Also


* [atlas dataLakePipelines runs](atlas_dataLakePipelines_runs.md)	- Data Lake pipelines runs.



