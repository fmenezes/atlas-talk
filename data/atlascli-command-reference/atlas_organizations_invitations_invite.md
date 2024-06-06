## atlas organizations invitations invite

Invite the specified MongoDB user to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas organizations invitations invite <email> [flags]
```

### Aliases
```

atlas organizations invitations invite
atlas organizations invitations create
atlas organizations invitation invite
atlas organizations invitation create
atlas organization invitations invite
atlas organization invitations create
atlas organization invitation invite
atlas organization invitation create
atlas orgs invitations invite
atlas orgs invitations create
atlas orgs invitation invite
atlas orgs invitation create
atlas org invitations invite
atlas org invitations create
atlas org invitation invite
atlas org invitation create
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

### See Also


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



