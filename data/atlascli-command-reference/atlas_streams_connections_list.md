## atlas streams connections list

Returns all Atlas Stream Processing connections from your Atlas Stream Processing instance.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas streams connections list [flags]
```

### Aliases
```

atlas streams connections list
atlas streams connections ls
atlas streams connection list
atlas streams connection ls
atlas stream connections list
atlas stream connections ls
atlas stream connection list
atlas stream connection ls
```

### Examples

```
# list all connections within ExampleInstance:
atlas streams connection list --instance ExampleInstance

```


### Flags

```
  -h, --help               help for list
  -i, --instance string    Name of your Atlas Stream Processing instance.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas streams connections](atlas_streams_connections.md)	- Manage Atlas Stream Processing connections.



