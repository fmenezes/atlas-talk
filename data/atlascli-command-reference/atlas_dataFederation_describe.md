## atlas dataFederation describe

Return the details for the specified data federation database for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataFederation describe <name> [flags]
atlas datafederation describe <name> [flags]
atlas data-federation describe <name> [flags]
```

### Examples

```
# retrieves data federation 'DataFederation1':
  atlas dataFederation describe DataFederation1

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

### SEE ALSO


* [atlas dataFederation](atlas_dataFederation.md)	- Data federation.



