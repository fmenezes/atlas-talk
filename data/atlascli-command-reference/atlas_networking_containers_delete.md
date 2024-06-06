## atlas networking containers delete

Remove the specified network peering container from your project before creating any clusters. Don't run this command if you have clusters in your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas networking containers delete <containerId> [flags]
atlas networking containers rm <containerId> [flags]
atlas networking container delete <containerId> [flags]
atlas networking container rm <containerId> [flags]
```

### Examples

```
  # Remove the network peering container with the ID 5e44103f8d614b2f0b6530d8 from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas networking containers delete 5e44103f8d614b2f0b6530d8 --projectId 5e2211c17a3e5a48f5497de3
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

### SEE ALSO


* [atlas networking containers](atlas_networking_containers.md)	- Manage Network Peering containers.



