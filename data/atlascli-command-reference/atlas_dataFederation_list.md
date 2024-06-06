## atlas dataFederation list

Returns all data federation databases for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas dataFederation list [flags]
```

### Aliases
```

atlas dataFederation list
atlas dataFederation ls
atlas datafederation list
atlas datafederation ls
atlas data-federation list
atlas data-federation ls
```

### Examples

```
# list all data federation databases:
  atlas dataFederation list

```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string        Type of Federated Database Instances to return.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas dataFederation](atlas_dataFederation.md)	- Data federation.



