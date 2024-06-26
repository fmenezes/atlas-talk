## atlas projects delete

Remove the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas projects delete <ID> [flags]
```

### Aliases
```

atlas projects delete
atlas projects rm
atlas project delete
atlas project rm
```

### Examples

```
  # Remove the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas projects delete 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --force   Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help    help for delete

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects](atlas_projects.md)	- Manage your Atlas projects.



