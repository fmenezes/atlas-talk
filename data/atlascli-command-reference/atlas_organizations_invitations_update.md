## atlas organizations invitations update

Modifies the details of the specified pending invitation to your organization.


### Synopsis

You can use either the invitation ID or the user's email address to specify the invitation.

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.



```

atlas organizations invitations update <invitationId> [flags]
atlas organizations invitations updates <invitationId> [flags]
atlas organizations invitation update <invitationId> [flags]
atlas organizations invitation updates <invitationId> [flags]
atlas organization invitations update <invitationId> [flags]
atlas organization invitations updates <invitationId> [flags]
atlas organization invitation update <invitationId> [flags]
atlas organization invitation updates <invitationId> [flags]
atlas orgs invitations update <invitationId> [flags]
atlas orgs invitations updates <invitationId> [flags]
atlas orgs invitation update <invitationId> [flags]
atlas orgs invitation updates <invitationId> [flags]
atlas org invitations update <invitationId> [flags]
atlas org invitations updates <invitationId> [flags]
atlas org invitation update <invitationId> [flags]
atlas org invitation updates <invitationId> [flags]
```

### Examples

```
  # Modify the pending invitation with the ID 5dd56c847a3e5a1f363d424d to grant ORG_OWNER access the organization with the ID 5f71e5255afec75a3d0f96dc:
  atlas organizations invitations update 5dd56c847a3e5a1f363d424d --orgId 5f71e5255afec75a3d0f96dc --role ORG_OWNER --output json
		
  # Modify the invitation for the user with the email address user@example.com to grant ORG_OWNER access the organization with the ID 5f71e5255afec75a3d0f96dc:
  atlas organizations invitations update --email user@example.com --orgId 5f71e5255afec75a3d0f96dc --role ORG_OWNER --output json
```


### Flags

```
      --email string    Email address for the user.
  -h, --help            help for update
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --role strings    User's roles for the associated organization. Valid values include ORG_OWNER, ORG_MEMBER, ORG_GROUP_CREATOR, ORG_BILLING_ADMIN, and ORG_READ_ONLY. Passing this flag replaces preexisting data.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



