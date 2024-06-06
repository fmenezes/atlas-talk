## atlas projects invitations update

Modifies the details of the specified pending invitation to your project.


### Synopsis

You can use either the invitation ID or the user's email address to specify the invitation.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas projects invitations update <invitationId> [flags]
```

### Aliases
```

atlas projects invitations update
atlas projects invitations updates
atlas projects invitation update
atlas projects invitation updates
atlas project invitations update
atlas project invitations updates
atlas project invitation update
atlas project invitation updates
```

### Examples

```
  # Modify the pending invitation with the ID 5dd56c847a3e5a1f363d424d to grant GROUP_READ_ONLY access the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects invitations update 5dd56c847a3e5a1f363d424d --projectId 5f71e5255afec75a3d0f96dc --role GROUP_READ_ONLY --output json
  
  # Modify the invitation for the user with the email address user@example.com to grant GROUP_READ_ONLY access the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects invitations update --email user@example.com --projectId 5f71e5255afec75a3d0f96dc --role GROUP_READ_ONLY --output json
```


### Flags

```
      --email string       Email address for the user.
  -h, --help               help for update
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       User's roles for the associated organization. Valid values include ORG_OWNER, ORG_MEMBER, ORG_GROUP_CREATOR, ORG_BILLING_ADMIN, and ORG_READ_ONLY. Passing this flag replaces preexisting data.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects invitations](atlas_projects_invitations.md)	- Invitation operations.



