## atlas projects invitations describe

Return the details for the specified pending invitation to your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects invitations describe <invitationId> [flags]
atlas projects invitations get <invitationId> [flags]
atlas projects invitation describe <invitationId> [flags]
atlas projects invitation get <invitationId> [flags]
atlas project invitations describe <invitationId> [flags]
atlas project invitations get <invitationId> [flags]
atlas project invitation describe <invitationId> [flags]
atlas project invitation get <invitationId> [flags]
```

### Examples

```
  # Return the JSON-formatted details of the pending invitation with the ID 5dd56c847a3e5a1f363d424d for the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects invitations describe 5dd56c847a3e5a1f363d424d --projectId 5f71e5255afec75a3d0f96dc --output json
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas projects invitations](atlas_projects_invitations.md)	- Invitation operations.



