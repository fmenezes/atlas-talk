## atlas projects teams update

Modify the roles for the specified team for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects teams update <teamId> [flags]
atlas projects teams updates <teamId> [flags]
atlas projects team update <teamId> [flags]
atlas projects team updates <teamId> [flags]
atlas project teams update <teamId> [flags]
atlas project teams updates <teamId> [flags]
atlas project team update <teamId> [flags]
atlas project team updates <teamId> [flags]
```

### Examples

```
  # Modify the roles for the team with the ID 5dd56c847a3e5a1f363d424d to grant GROUP_READ_ONLY access to the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects teams update 5dd56c847a3e5a1f363d424d --projectId 5f71e5255afec75a3d0f96dc --role GROUP_READ_ONLY --output json
```


### Flags

```
  -h, --help               help for update
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       User role that applies to all members of the specified team for the associated project. Valid values include GROUP_CLUSTER_MANAGER, GROUP_DATA_ACCESS_ADMIN, GROUP_DATA_ACCESS_READ_ONLY, GROUP_DATA_ACCESS_READ_WRITE, GROUP_OWNER, and GROUP_READ_ONLY. Passing this flag replaces preexisting data.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas projects teams](atlas_projects_teams.md)	- Manage your Atlas teams.



