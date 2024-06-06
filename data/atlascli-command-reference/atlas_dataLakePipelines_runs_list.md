## atlas dataLakePipelines runs list

Returns all data lake pipeline runs for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas dataLakePipelines runs list [flags]
atlas dataLakePipelines runs ls [flags]
atlas dataLakePipelines run list [flags]
atlas dataLakePipelines run ls [flags]
atlas datalakepipelines runs list [flags]
atlas datalakepipelines runs ls [flags]
atlas datalakepipelines run list [flags]
atlas datalakepipelines run ls [flags]
atlas data-lake-pipelines runs list [flags]
atlas data-lake-pipelines runs ls [flags]
atlas data-lake-pipelines run list [flags]
atlas data-lake-pipelines run ls [flags]
atlas dataLakePipeline runs list [flags]
atlas dataLakePipeline runs ls [flags]
atlas dataLakePipeline run list [flags]
atlas dataLakePipeline run ls [flags]
atlas datalakepipeline runs list [flags]
atlas datalakepipeline runs ls [flags]
atlas datalakepipeline run list [flags]
atlas datalakepipeline run ls [flags]
atlas data-lake-pipeline runs list [flags]
atlas data-lake-pipeline runs ls [flags]
atlas data-lake-pipeline run list [flags]
atlas data-lake-pipeline run ls [flags]
```

### Examples

```
# list all pipeline runs:
  atlas dataLakePipelines runs list

```


### Flags

```
  -h, --help               help for list
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



