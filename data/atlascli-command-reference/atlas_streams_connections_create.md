## atlas streams connections create

Creates a connection for an Atlas Stream Processing instance.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams connections create <connectionName> [flags]
atlas streams connection create <connectionName> [flags]
atlas stream connections create <connectionName> [flags]
atlas stream connection create <connectionName> [flags]
```

### Examples

```
# create a new connection for Atlas Stream Processing:
  atlas streams connection create kafkaprod -i test01 -f kafkaConfig.json

# create a new connection using the name from a cluster configuration file
  atlas streams connection create -i test01 -f clusterConfig.json

```


### Flags

```
  -f, --file string        Path to a JSON configuration file that defines an Atlas Stream Processing connection.
  -h, --help               help for create
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



