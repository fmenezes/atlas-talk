## atlas dataLakePipelines trigger

Trigger the specified data lake pipeline for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataLakePipelines trigger <pipelineName> [flags]
atlas datalakepipelines trigger <pipelineName> [flags]
atlas data-lake-pipelines trigger <pipelineName> [flags]
atlas dataLakePipeline trigger <pipelineName> [flags]
atlas datalakepipeline trigger <pipelineName> [flags]
atlas data-lake-pipeline trigger <pipelineName> [flags]
```

### Examples

```
# trigger pipeline 'Pipeline1':
  atlas dataLakePipelines trigger Pipeline1

```


### Flags

```
  -h, --help                help for trigger
  -o, --output string       Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --snapshotId string   Unique identifier of the snapshot.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



