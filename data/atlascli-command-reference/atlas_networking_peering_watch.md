## atlas networking peering watch

Watch the specified peering connection in your project until it becomes available.


### Synopsis

This command checks the peering connection's status periodically until it becomes available. 
Once it reaches the expected state, the command prints "Network peering changes completed."
If you run the command in the terminal, it blocks the terminal session until the resource is available.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas networking peering watch <peerId> [flags]
```

### Examples

```
  Watch for the network peering connection with the ID 5f621dc701240c5b7c3a888e to become available in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas networking peering watch 5f621dc701240c5b7c3a888e --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for watch
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas networking peering](atlas_networking_peering.md)	- Manage Network Peering connections.



