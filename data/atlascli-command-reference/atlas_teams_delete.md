## atlas teams delete

Remove the specified team from your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas teams delete <teamId> [flags]
```

### Aliases
```

atlas teams delete
atlas teams rm
atlas team delete
atlas team rm
```

### Examples

```
  # Remove the team with the ID 5e44445ef10fab20b49c0f31 from the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams delete 5e44445ef10fab20b49c0f31 --orgId 5e1234c17a3e5a48f5497de3
```


### Flags

```
      --force          Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help           help for delete
      --orgId string   Organization ID to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas teams](atlas_teams.md)	- Manage your Atlas teams.



