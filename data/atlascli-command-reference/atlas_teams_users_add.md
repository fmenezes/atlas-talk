## atlas teams users add

Add the specified MongoDB user to a team for your organization.


### Synopsis

Users must be current members of your organization before you can add them to a team.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas teams users add <userId>... [flags]
```

### Aliases
```

atlas teams users add
atlas teams user add
atlas team users add
atlas team user add
```

### Examples

```
  # Add the users with the IDs 5dd58c647a3e5a6c5bce46c7 and 5dd56c847a3e5a1f363d424d to the team with the ID 5f6a5c6c713184005d72fe6e for the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams users add 5dd58c647a3e5a6c5bce46c7 5dd56c847a3e5a1f363d424d --teamId 5f6a5c6c713184005d72fe6e --orgId 5e1234c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help            help for add
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --teamId string   Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas teams users](atlas_teams_users.md)	- Manage your Atlas users.



