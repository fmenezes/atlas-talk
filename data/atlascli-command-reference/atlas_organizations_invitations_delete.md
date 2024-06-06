## atlas organizations invitations delete

Remove the specified pending invitation to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas organizations invitations delete <invitationId> [flags]
```

### Aliases
```

atlas organizations invitations delete
atlas organizations invitations rm
atlas organizations invitation delete
atlas organizations invitation rm
atlas organization invitations delete
atlas organization invitations rm
atlas organization invitation delete
atlas organization invitation rm
atlas orgs invitations delete
atlas orgs invitations rm
atlas orgs invitation delete
atlas orgs invitation rm
atlas org invitations delete
atlas org invitations rm
atlas org invitation delete
atlas org invitation rm
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

### See Also


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



