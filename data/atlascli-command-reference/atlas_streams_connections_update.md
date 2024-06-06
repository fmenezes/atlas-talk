## atlas streams connections update

Modify the details of the specified connection within your Atlas Stream Processing instance.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas streams connections update <connectionName> [flags]
```

### Aliases
```

atlas streams connections update
atlas streams connection update
atlas stream connections update
atlas stream connection update
```

### Examples

```
# update an Atlas Stream Processing connection:
  atlas streams connection update kafkaprod --instance test01 -f kafkaConfig.json

```


### Flags

```
  -f, --file string        Path to a JSON configuration file that defines an Atlas Stream Processing connection.
  -h, --help               help for update
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



