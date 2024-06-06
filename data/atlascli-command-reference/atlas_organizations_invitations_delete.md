## atlas organizations invitations delete

Remove the specified pending invitation to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations invitations delete <invitationId> [flags]
atlas organizations invitations rm <invitationId> [flags]
atlas organizations invitation delete <invitationId> [flags]
atlas organizations invitation rm <invitationId> [flags]
atlas organization invitations delete <invitationId> [flags]
atlas organization invitations rm <invitationId> [flags]
atlas organization invitation delete <invitationId> [flags]
atlas organization invitation rm <invitationId> [flags]
atlas orgs invitations delete <invitationId> [flags]
atlas orgs invitations rm <invitationId> [flags]
atlas orgs invitation delete <invitationId> [flags]
atlas orgs invitation rm <invitationId> [flags]
atlas org invitations delete <invitationId> [flags]
atlas org invitations rm <invitationId> [flags]
atlas org invitation delete <invitationId> [flags]
atlas org invitation rm <invitationId> [flags]
```

### Examples

```
  # Remove the pending invitation with the ID 5dd56c847a3e5a1f363d424d from the organization with the ID 5f71e5255afec75a3d0f96dc:
  atlas organizations invitations delete 5dd56c847a3e5a1f363d424d --orgId 5f71e5255afec75a3d0f96dc
```


### Flags

```
      --force          Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help           help for delete
      --orgId string   Organization ID to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



