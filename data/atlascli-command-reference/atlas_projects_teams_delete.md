## atlas projects teams delete

Remove the specified team from your project.


### Synopsis

After you remove a team from your project, the team still exists in the organization in which it was created.

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects teams delete <teamId> [flags]
atlas projects teams rm <teamId> [flags]
atlas projects team delete <teamId> [flags]
atlas projects team rm <teamId> [flags]
atlas project teams delete <teamId> [flags]
atlas project teams rm <teamId> [flags]
atlas project team delete <teamId> [flags]
atlas project team rm <teamId> [flags]
```

### Examples

```
  # Remove the team with the ID 5dd58c647a3e5a6c5bce46c7 from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas projects teams delete 5dd58c647a3e5a6c5bce46c7 --projectId 5e2211c17a3e5a48f5497de3
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


* [atlas projects teams](atlas_projects_teams.md)	- Manage your Atlas teams.



