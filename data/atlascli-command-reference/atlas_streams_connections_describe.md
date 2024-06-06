## atlas streams connections describe

Return the details for the specified Atlas Stream Processing connection.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams connections describe <streamConnectionName> [flags]
atlas streams connection describe <streamConnectionName> [flags]
atlas stream connections describe <streamConnectionName> [flags]
atlas stream connection describe <streamConnectionName> [flags]
```

### Examples

```
# retrieves stream connection 'ExampleConnection' in instance 'ExampleInstance':
atlas streams connection describe ExampleConnection --instance ExampleInstance

```


### Flags

```
  -h, --help               help for describe
  -i, --instance string    Name of your Atlas Stream Processing instance.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas streams connections](atlas_streams_connections.md)	- Manage Atlas Stream Processing connections.



