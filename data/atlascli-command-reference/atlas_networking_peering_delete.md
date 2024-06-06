## atlas networking peering delete

Remove the specified peering connection from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas networking peering delete <peerId> [flags]
```

### Aliases
```

atlas networking peering delete
atlas networking peering rm
```

### Examples

```
  # Remove the network peering connection with the ID 5f60c5bd0948295c093565ba in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas networking peering delete 5f60c5bd0948295c093565ba --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas networking peering](atlas_networking_peering.md)	- Manage Network Peering connections.



