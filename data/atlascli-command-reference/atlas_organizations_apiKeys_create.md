## atlas organizations apiKeys create

Create an API Key for your organization.


### Synopsis

MongoDB returns the private API key only once. After you run this command, immediately copy, save, and secure both the public and private API keys.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations apiKeys create [flags]
atlas organizations apikeys create [flags]
atlas organizations api-keys create [flags]
atlas organizations apiKey create [flags]
atlas organizations apikey create [flags]
atlas organizations api-key create [flags]
atlas organization apiKeys create [flags]
atlas organization apikeys create [flags]
atlas organization api-keys create [flags]
atlas organization apiKey create [flags]
atlas organization apikey create [flags]
atlas organization api-key create [flags]
atlas orgs apiKeys create [flags]
atlas orgs apikeys create [flags]
atlas orgs api-keys create [flags]
atlas orgs apiKey create [flags]
atlas orgs apikey create [flags]
atlas orgs api-key create [flags]
atlas org apiKeys create [flags]
atlas org apikeys create [flags]
atlas org api-keys create [flags]
atlas org apiKey create [flags]
atlas org apikey create [flags]
atlas org api-key create [flags]
```

### Examples

```
  # Create an organization API key with organization owner access in the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys create --role ORG_OWNER --desc "My API Key" --orgId 5a1b39eec902201990f12345 --output json
```


### Flags

```
      --desc string     Description of the API key.
  -h, --help            help for create
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --role strings    Role or roles that you want to assign to the API key. To assign more than one role, specify each role with a separate role flag or specify all of the roles as a comma-separated list using one role flag. To learn which values the CLI accepts, see the Items Enum for roles in the Atlas API spec: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Programmatic-API-Keys/operation/createApiKey/.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



