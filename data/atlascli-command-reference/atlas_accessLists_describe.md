## atlas accessLists describe

Return the details for the specified IP access list entry.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas accessLists describe <entry> [flags]
atlas accessLists get <entry> [flags]
atlas accesslists describe <entry> [flags]
atlas accesslists get <entry> [flags]
atlas access-lists describe <entry> [flags]
atlas access-lists get <entry> [flags]
atlas accessList describe <entry> [flags]
atlas accessList get <entry> [flags]
atlas accesslist describe <entry> [flags]
atlas accesslist get <entry> [flags]
atlas access-list describe <entry> [flags]
atlas access-list get <entry> [flags]
atlas whitelists describe <entry> [flags]
atlas whitelists get <entry> [flags]
atlas whitelist describe <entry> [flags]
atlas whitelist get <entry> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the access list entry 192.0.2.0/24 in the project with ID 5e2211c17a3e5a48f5497de3:
  atlas accessLists describe 192.0.2.0/24 --output json --projectId 5e1234c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas accessLists](atlas_accessLists.md)	- Manage the list of IP addresses that can access your Atlas project.



