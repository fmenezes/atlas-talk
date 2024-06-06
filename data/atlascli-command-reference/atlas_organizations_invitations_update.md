## atlas organizations invitations update

Modifies the details of the specified pending invitation to your organization.


### Synopsis

You can use either the invitation ID or the user's email address to specify the invitation.

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.


### Usage
```
atlas organizations invitations update <invitationId> [flags]
```

### Aliases
```

atlas organizations invitations update
atlas organizations invitations updates
atlas organizations invitation update
atlas organizations invitation updates
atlas organization invitations update
atlas organization invitations updates
atlas organization invitation update
atlas organization invitation updates
atlas orgs invitations update
atlas orgs invitations updates
atlas orgs invitation update
atlas orgs invitation updates
atlas org invitations update
atlas org invitations updates
atlas org invitation update
atlas org invitation updates
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

### See Also


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



