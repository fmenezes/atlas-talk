## atlas dataLakePipelines list

Returns all data lake pipelines for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas dataLakePipelines list [flags]
atlas dataLakePipelines ls [flags]
atlas datalakepipelines list [flags]
atlas datalakepipelines ls [flags]
atlas data-lake-pipelines list [flags]
atlas data-lake-pipelines ls [flags]
atlas dataLakePipeline list [flags]
atlas dataLakePipeline ls [flags]
atlas datalakepipeline list [flags]
atlas datalakepipeline ls [flags]
atlas data-lake-pipeline list [flags]
atlas data-lake-pipeline ls [flags]
```

### Examples

```
# list all pipelines:
  atlas dataLakePipelines list
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



