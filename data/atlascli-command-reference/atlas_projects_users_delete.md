## atlas projects users delete

Remove the specified user from your project.


### Synopsis

After you remove a user from your project, the user still exists in the organization in which it was created.

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.


### Usage
```
atlas projects users delete <ID> [flags]
```

### Aliases
```

atlas projects users delete
atlas projects users rm
atlas projects user delete
atlas projects user rm
atlas project users delete
atlas project users rm
atlas project user delete
atlas project user rm
```

### Examples

```
  # Remove the user with the ID 5dd58c647a3e5a6c5bce46c7 from the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas projects users delete 5dd58c647a3e5a6c5bce46c7 --projectId 5e2211c17a3e5a48f5497de3
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

### See Also


* [atlas projects users](atlas_projects_users.md)	- Manage users for a project.



