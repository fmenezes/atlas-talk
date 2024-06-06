## atlas organizations invitations list

Return all pending invitations to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations invitations list [flags]
atlas organizations invitations ls [flags]
atlas organizations invitation list [flags]
atlas organizations invitation ls [flags]
atlas organization invitations list [flags]
atlas organization invitations ls [flags]
atlas organization invitation list [flags]
atlas organization invitation ls [flags]
atlas orgs invitations list [flags]
atlas orgs invitations ls [flags]
atlas orgs invitation list [flags]
atlas orgs invitation ls [flags]
atlas org invitations list [flags]
atlas org invitations ls [flags]
atlas org invitation list [flags]
atlas org invitation ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of pending invitations to the organization with the ID 5f71e5255afec75a3d0f96dc:
  atlas organizations invitations list --orgId 5f71e5255afec75a3d0f96dc --output json
```


### Flags

```
      --email string    Email address for the user.
  -h, --help            help for list
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



