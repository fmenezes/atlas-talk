## atlas teams describe

Return the details for the specified team for your organization.


### Synopsis

You can return the details for a team using the team's ID or the team's name. You must specify either the id option or the name option.

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas teams describe [flags]
atlas teams get [flags]
atlas team describe [flags]
atlas team get [flags]
```

### Examples

```
  # Return the JSON-formatted details for the the team with the ID 5e44445ef10fab20b49c0f31 in the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams describe --id 5e44445ef10fab20b49c0f31 --projectId 5e1234c17a3e5a48f5497de3 --output json
  
  # Return the JSON-formatted details for the the team with the name myTeam in the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams describe --name myTeam --projectId 5e1234c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help            help for describe
      --id string       Unique 24-digit string that identifies the team.
      --name string     Label that identifies the team.
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas teams](atlas_teams.md)	- Manage your Atlas teams.



