## atlas accessLists delete

Remove the specified IP access list entry from your project.


### Synopsis

The command, when run without the force option, prompts you to confirm the operation.

To use this command, you must authenticate with a user account or an API key with the Read Write role.


### Usage
```
atlas accessLists delete <entry> [flags]
```

### Aliases
```

atlas accessLists delete
atlas accessLists rm
atlas accesslists delete
atlas accesslists rm
atlas access-lists delete
atlas access-lists rm
atlas accessList delete
atlas accessList rm
atlas accesslist delete
atlas accesslist rm
atlas access-list delete
atlas access-list rm
atlas whitelists delete
atlas whitelists rm
atlas whitelist delete
atlas whitelist rm
```

### Examples

```
  # Remove the IP address 192.0.2.0 from the access list for the project with the ID 5e2211c17a3e5a48f5497de3 after prompting for a confirmation:
  atlas accessLists delete 192.0.2.0 --projectId 5e2211c17a3e5a48f5497de3
  # Remove the IP address 192.0.2.0 from the access list for the project with the ID 5e2211c17a3e5a48f5497de3 without requiring confirmation:
  atlas accessLists delete 192.0.2.0 --projectId 5e2211c17a3e5a48f5497de3 --force
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


* [atlas accessLists](atlas_accessLists.md)	- Manage the list of IP addresses that can access your Atlas project.



