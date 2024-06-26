## atlas dataLakePipelines describe

Return the details for the specified data lake pipeline for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas dataLakePipelines describe <pipelineName> [flags]
```

### Aliases
```

atlas dataLakePipelines describe
atlas datalakepipelines describe
atlas data-lake-pipelines describe
atlas dataLakePipeline describe
atlas datalakepipeline describe
atlas data-lake-pipeline describe
```

### Examples

```
# retrieves pipeline 'Pipeline1':
  atlas dataLakePipelines describe Pipeline1

```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



