## atlas teams users list

Return all users for a team.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas teams users list [flags]
atlas teams users ls [flags]
atlas teams user list [flags]
atlas teams user ls [flags]
atlas team users list [flags]
atlas team users ls [flags]
atlas team user list [flags]
atlas team user ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of the users for the team with the ID 5f6a5c6c713184005d72fe6e in the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams users list --teamId 5f6a5c6c713184005d72fe6e --orgId 5e1234c17a3e5a48f5497de3 --output json
```


### Flags

```
  -c, --compact         Flag that enables the compact array response structure for a json output. The --compact option returns array objects as top-level responses and allows backward compatibility for scripts based on previous CLI versions. Omitting the --compact option for a json output returns array objects within a 'results' sub-array. You must specify --output json to use this option.
  -h, --help            help for list
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --teamId string   Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas teams users](atlas_teams_users.md)	- Manage your Atlas users.



