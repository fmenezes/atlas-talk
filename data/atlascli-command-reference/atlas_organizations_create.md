## atlas organizations create

Create an organization.


### Synopsis

When authenticating using API keys, the organization to which the API keys belong must have cross-organization billing enabled. The resulting org will be linked to the paying org.


### Usage
```
atlas organizations create <name> [flags]
```

### Aliases
```

atlas organizations create
atlas organization create
atlas orgs create
atlas org create
```

### Examples

```
  # Create an Atlas organization with the name myOrg:
  atlas organizations create myOrg --output json
```


### Flags

```
      --apiKeyDescription string   Description of the API key.Required when creating organizations authenticated with API Keys.
      --apiKeyRole strings         Role or roles that you want to assign to the API key. To assign more than one role, specify each role with a separate role flag or specify all of the roles as a comma-separated list using one role flag. To learn which values the CLI accepts, see the Items Enum for roles in the Atlas API spec: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Programmatic-API-Keys/operation/createApiKey/.Required when creating organizations authenticated with API Keys.
  -h, --help                       help for create
  -o, --output string              Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --ownerId string             Unique 24-digit string that identifies the Atlas user to be granted the Org Owner role on the specified organization. Required if using API keys.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas organizations](atlas_organizations.md)	- Manage your Atlas organizations.



