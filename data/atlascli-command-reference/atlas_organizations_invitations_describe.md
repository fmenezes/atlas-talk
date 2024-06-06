## atlas organizations invitations describe

Return the details for the specified pending invitation to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations invitations describe <invitationId> [flags]
atlas organizations invitations get <invitationId> [flags]
atlas organizations invitation describe <invitationId> [flags]
atlas organizations invitation get <invitationId> [flags]
atlas organization invitations describe <invitationId> [flags]
atlas organization invitations get <invitationId> [flags]
atlas organization invitation describe <invitationId> [flags]
atlas organization invitation get <invitationId> [flags]
atlas orgs invitations describe <invitationId> [flags]
atlas orgs invitations get <invitationId> [flags]
atlas orgs invitation describe <invitationId> [flags]
atlas orgs invitation get <invitationId> [flags]
atlas org invitations describe <invitationId> [flags]
atlas org invitations get <invitationId> [flags]
atlas org invitation describe <invitationId> [flags]
atlas org invitation get <invitationId> [flags]
```

### Examples

```
  # Return the JSON-formatted details of the pending invitation with the ID 5dd56c847a3e5a1f363d424d for the organization with the ID 5f71e5255afec75a3d0f96dc:
  atlas organizations invitations describe 5dd56c847a3e5a1f363d424d --orgId 5f71e5255afec75a3d0f96dc --output json
```


### Flags

```
  -h, --help            help for describe
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



