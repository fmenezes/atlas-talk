## atlas projects teams add

Add the specified team to your project.


### Synopsis

All members of the team share the same project access.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas projects teams add <teamId> [flags]
```

### Aliases
```

atlas projects teams add
atlas projects team add
atlas project teams add
atlas project team add
```

### Examples

```
  # Add the team with the ID 5dd58c647a3e5a6c5bce46c7 to the project with the ID 5e2211c17a3e5a48f5497de3 with GROUP_READ_ONLY project access:
  atlas projects teams add 5dd58c647a3e5a6c5bce46c7 --projectId 5e2211c17a3e5a48f5497de3 --role GROUP_READ_ONLY
```


### Flags

```
  -h, --help               help for add
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       User role that applies to all members of the specified team for the associated project. Valid values include GROUP_CLUSTER_MANAGER, GROUP_DATA_ACCESS_ADMIN, GROUP_DATA_ACCESS_READ_ONLY, GROUP_DATA_ACCESS_READ_WRITE, GROUP_OWNER, and GROUP_READ_ONLY.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects teams](atlas_projects_teams.md)	- Manage your Atlas teams.



