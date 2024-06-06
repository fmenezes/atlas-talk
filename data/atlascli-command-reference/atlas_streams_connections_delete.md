## atlas streams connections delete

Remove the specified Atlas Stream Processing connection from your project.


### Synopsis

The command prompts you to confirm the operation when you run the command without the --force option.

Before deleting an Atlas Streams Processing connection, you must first stop all processes associated with it. To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas streams connections delete <connectionName> [flags]
atlas streams connection delete <connectionName> [flags]
atlas stream connections delete <connectionName> [flags]
atlas stream connection delete <connectionName> [flags]
```

### Examples

```
# deletes connection 'ExampleConnection' from instance 'ExampleInstance':
  atlas streams connection delete ExampleConnection --instance ExampleInstance

# deletes connection 'ExampleConnection' from instance 'ExampleInstance' without requiring confirmation:
  atlas streams connection delete ExampleConnection --instance ExampleInstance --force

```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
  -i, --instance string    Name of your Atlas Stream Processing instance.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas streams connections](atlas_streams_connections.md)	- Manage Atlas Stream Processing connections.



