## atlas projects invitations list

Return all pending invitations to your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects invitations list [flags]
atlas projects invitations ls [flags]
atlas projects invitation list [flags]
atlas projects invitation ls [flags]
atlas project invitations list [flags]
atlas project invitations ls [flags]
atlas project invitation list [flags]
atlas project invitation ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of pending invitations to the project with the ID 5f71e5255afec75a3d0f96dc:
  atlas projects invitations list --projectId 5f71e5255afec75a3d0f96dc --output json
```


### Flags

```
      --email string       Email address for the user.
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas projects invitations](atlas_projects_invitations.md)	- Invitation operations.



