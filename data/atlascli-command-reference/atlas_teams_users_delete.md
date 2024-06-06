## atlas teams users delete

Remove the specified user from a team for your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas teams users delete <userId> [flags]
atlas teams users rm <userId> [flags]
atlas teams user delete <userId> [flags]
atlas teams user rm <userId> [flags]
atlas team users delete <userId> [flags]
atlas team users rm <userId> [flags]
atlas team user delete <userId> [flags]
atlas team user rm <userId> [flags]
```

### Examples

```
  # Remove the user with the ID 5dd58c647a3e5a6c5bce46c7 from the team with the ID 5f6a5c6c713184005d72fe6e for the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams users delete 5dd58c647a3e5a6c5bce46c7 --teamId 5f6a5c6c713184005d72fe6e --orgId 5e1234c17a3e5a48f5497de3
```


### Flags

```
      --force           Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help            help for delete
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
      --teamId string   Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas teams users](atlas_teams_users.md)	- Manage your Atlas users.



