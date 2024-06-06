## atlas organizations invitations describe

Return the details for the specified pending invitation to your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas organizations invitations describe <invitationId> [flags]
```

### Aliases
```

atlas organizations invitations describe
atlas organizations invitations get
atlas organizations invitation describe
atlas organizations invitation get
atlas organization invitations describe
atlas organization invitations get
atlas organization invitation describe
atlas organization invitation get
atlas orgs invitations describe
atlas orgs invitations get
atlas orgs invitation describe
atlas orgs invitation get
atlas org invitations describe
atlas org invitations get
atlas org invitation describe
atlas org invitation get
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

### See Also


* [atlas organizations invitations](atlas_organizations_invitations.md)	- Invitation operations.



