## atlas teams rename

Rename a team in your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.


### Usage
```
atlas teams rename <newName> [flags]
```

### Aliases
```

atlas teams rename
atlas teams update
atlas team rename
atlas team update
```

### Examples

```
  # Rename a team in the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams rename newName --teamId 5e1234c17a3e5a48f5497de3 --orgId 5e1234c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help            help for rename
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --teamId string   Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas teams](atlas_teams.md)	- Manage your Atlas teams.



