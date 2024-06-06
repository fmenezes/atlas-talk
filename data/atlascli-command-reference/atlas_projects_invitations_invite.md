## atlas projects invitations invite

Invite the specified MongoDB user to your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects invitations invite <email> [flags]
atlas projects invitations create <email> [flags]
atlas projects invitation invite <email> [flags]
atlas projects invitation create <email> [flags]
atlas project invitations invite <email> [flags]
atlas project invitations create <email> [flags]
atlas project invitation invite <email> [flags]
atlas project invitation create <email> [flags]
```

### Examples

```
  # Invite the MongoDB user with the email user@example.com to the project with the ID 5f71e5255afec75a3d0f96dc with GROUP_READ_ONLY access:
  atlas projects invitations invite user@example.com --projectId 5f71e5255afec75a3d0f96dc --role GROUP_READ_ONLY --output json
```


### Flags

```
  -h, --help               help for invite
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       User's roles for the associated project. Valid values include GROUP_CLUSTER_MANAGER, GROUP_DATA_ACCESS_ADMIN, GROUP_DATA_ACCESS_READ_ONLY, GROUP_DATA_ACCESS_READ_WRITE, GROUP_OWNER, and GROUP_READ_ONLY.
      --teamId strings     Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas projects invitations](atlas_projects_invitations.md)	- Invitation operations.



