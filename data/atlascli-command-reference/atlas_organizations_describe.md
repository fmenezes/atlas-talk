## atlas organizations describe

Return the details for the specified organizations.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas organizations describe <ID> [flags]
atlas organizations show <ID> [flags]
atlas organization describe <ID> [flags]
atlas organization show <ID> [flags]
atlas orgs describe <ID> [flags]
atlas orgs show <ID> [flags]
atlas org describe <ID> [flags]
atlas org show <ID> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the organization with the ID 5e2211c17a3e5a48f5497de3:
  atlas organizations describe 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help            help for describe
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations](atlas_organizations.md)	- Manage your Atlas organizations.



