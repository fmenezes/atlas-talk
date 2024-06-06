## atlas dataLakePipelines watch

Watch for the specified data lake pipeline to complete.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines watch <pipelineName> [flags]
```

### Aliases
```

atlas dataLakePipelines watch
atlas datalakepipelines watch
atlas data-lake-pipelines watch
atlas dataLakePipeline watch
atlas datalakepipeline watch
atlas data-lake-pipeline watch
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
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



