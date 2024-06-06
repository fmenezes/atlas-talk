## atlas dataLakePipelines runs list

Returns all data lake pipeline runs for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas dataLakePipelines runs list [flags]
```

### Aliases
```

atlas dataLakePipelines runs list
atlas dataLakePipelines runs ls
atlas dataLakePipelines run list
atlas dataLakePipelines run ls
atlas datalakepipelines runs list
atlas datalakepipelines runs ls
atlas datalakepipelines run list
atlas datalakepipelines run ls
atlas data-lake-pipelines runs list
atlas data-lake-pipelines runs ls
atlas data-lake-pipelines run list
atlas data-lake-pipelines run ls
atlas dataLakePipeline runs list
atlas dataLakePipeline runs ls
atlas dataLakePipeline run list
atlas dataLakePipeline run ls
atlas datalakepipeline runs list
atlas datalakepipeline runs ls
atlas datalakepipeline run list
atlas datalakepipeline run ls
atlas data-lake-pipeline runs list
atlas data-lake-pipeline runs ls
atlas data-lake-pipeline run list
atlas data-lake-pipeline run ls
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

### See Also


* [atlas dataLakePipelines runs](atlas_dataLakePipelines_runs.md)	- Data Lake pipelines runs.



