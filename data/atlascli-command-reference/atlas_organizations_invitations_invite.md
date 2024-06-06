## atlas organizations invitations invite

Invite the specified MongoDB user to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations invitations invite <email> [flags]
atlas organizations invitations create <email> [flags]
atlas organizations invitation invite <email> [flags]
atlas organizations invitation create <email> [flags]
atlas organization invitations invite <email> [flags]
atlas organization invitations create <email> [flags]
atlas organization invitation invite <email> [flags]
atlas organization invitation create <email> [flags]
atlas orgs invitations invite <email> [flags]
atlas orgs invitations create <email> [flags]
atlas orgs invitation invite <email> [flags]
atlas orgs invitation create <email> [flags]
atlas org invitations invite <email> [flags]
atlas org invitations create <email> [flags]
atlas org invitation invite <email> [flags]
atlas org invitation create <email> [flags]
```

### Examples

```
  # Invite the MongoDB user with the email user@example.com to the organization with the ID 5f71e5255afec75a3d0f96dc with ORG_OWNER access:
  atlas organizations invitations invite user@example.com --orgId 5f71e5255afec75a3d0f96dc --role ORG_OWNER --output json
```


### Flags

```
  -h, --help             help for invite
      --orgId string     Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string    Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --role strings     User's roles for the associated organization. Valid values include ORG_OWNER, ORG_MEMBER, ORG_GROUP_CREATOR, ORG_BILLING_ADMIN, and ORG_READ_ONLY.
      --teamId strings   Unique 24-digit string that identifies the team.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



