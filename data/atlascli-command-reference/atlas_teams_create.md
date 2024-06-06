## atlas teams create

Create a team for your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.



```

atlas teams create <name> [flags]
atlas team create <name> [flags]
```

### Examples

```
  # Create a team named myTeam in the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams create myTeam --username user1@example.com,user2@example.com --orgId 5e1234c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for create
      --orgId string       Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --username strings   Comma-separated list that contains the valid usernames of the MongoDB users to add to the new team. A team must have at least one user. New users must accept the invitation to join an organization before you can add them to a team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas teams](atlas_teams.md)	- Manage your Atlas teams.



