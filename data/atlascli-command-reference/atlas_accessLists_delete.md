## atlas accessLists delete

Remove the specified IP access list entry from your project.


### Synopsis

The command, when run without the force option, prompts you to confirm the operation.

To use this command, you must authenticate with a user account or an API key with the Read Write role.



```

atlas accessLists delete <entry> [flags]
atlas accessLists rm <entry> [flags]
atlas accesslists delete <entry> [flags]
atlas accesslists rm <entry> [flags]
atlas access-lists delete <entry> [flags]
atlas access-lists rm <entry> [flags]
atlas accessList delete <entry> [flags]
atlas accessList rm <entry> [flags]
atlas accesslist delete <entry> [flags]
atlas accesslist rm <entry> [flags]
atlas access-list delete <entry> [flags]
atlas access-list rm <entry> [flags]
atlas whitelists delete <entry> [flags]
atlas whitelists rm <entry> [flags]
atlas whitelist delete <entry> [flags]
atlas whitelist rm <entry> [flags]
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

### SEE ALSO


* [atlas accessLists](atlas_accessLists.md)	- Manage the list of IP addresses that can access your Atlas project.



