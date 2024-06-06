## atlas alerts settings describe

Return the details for the specified alert settings for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas alerts settings describe <alertConfigId> [flags]
atlas alerts settings get <alertConfigId> [flags]
atlas alerts config describe <alertConfigId> [flags]
atlas alerts config get <alertConfigId> [flags]
atlas alert settings describe <alertConfigId> [flags]
atlas alert settings get <alertConfigId> [flags]
atlas alert config describe <alertConfigId> [flags]
atlas alert config get <alertConfigId> [flags]
```

### Examples

```
  #  Return the JSON-formatted details for the alert settings with the ID 5d1113b25a115342acc2d1aa in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas alerts settings describe 5d1113b25a115342acc2d1aa --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas alerts settings](atlas_alerts_settings.md)	- Manages alerts configuration for your project.



