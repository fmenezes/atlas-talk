## atlas projects invitations delete

Remove the specified pending invitation to your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.


### Usage
```
atlas projects invitations delete <invitationId> [flags]
```

### Aliases
```

atlas projects invitations delete
atlas projects invitations rm
atlas projects invitation delete
atlas projects invitation rm
atlas project invitations delete
atlas project invitations rm
atlas project invitation delete
atlas project invitation rm
```

### Examples

```
  # Remove the pending invitation with the ID 5dd56c847a3e5a1f363d424d from the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects invitations delete 5dd56c847a3e5a1f363d424d --projectId 5f71e5255afec75a3d0f96dc
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


* [atlas projects invitations](atlas_projects_invitations.md)	- Invitation operations.



