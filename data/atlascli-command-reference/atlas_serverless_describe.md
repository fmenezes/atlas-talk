## atlas serverless describe

Return one serverless instance in the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas serverless describe <instanceName> [flags]
```

### Aliases
```

atlas serverless describe
atlas serverless get
atlas sl describe
atlas sl get
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


* [atlas serverless](atlas_serverless.md)	- Manage serverless instances for your project.



