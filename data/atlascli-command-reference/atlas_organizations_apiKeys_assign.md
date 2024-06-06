## atlas organizations apiKeys assign

Modify the roles or description for the specified organization API key.


### Synopsis

When you modify the roles for an organization API key with this command, the values you specify overwrite the existing roles assigned to the API key.
		
To view possible values for the apiKeyId argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations apiKeys assign <apiKeyId> [flags]
atlas organizations apiKeys updates <apiKeyId> [flags]
atlas organizations apikeys assign <apiKeyId> [flags]
atlas organizations apikeys updates <apiKeyId> [flags]
atlas organizations api-keys assign <apiKeyId> [flags]
atlas organizations api-keys updates <apiKeyId> [flags]
atlas organizations apiKey assign <apiKeyId> [flags]
atlas organizations apiKey updates <apiKeyId> [flags]
atlas organizations apikey assign <apiKeyId> [flags]
atlas organizations apikey updates <apiKeyId> [flags]
atlas organizations api-key assign <apiKeyId> [flags]
atlas organizations api-key updates <apiKeyId> [flags]
atlas organization apiKeys assign <apiKeyId> [flags]
atlas organization apiKeys updates <apiKeyId> [flags]
atlas organization apikeys assign <apiKeyId> [flags]
atlas organization apikeys updates <apiKeyId> [flags]
atlas organization api-keys assign <apiKeyId> [flags]
atlas organization api-keys updates <apiKeyId> [flags]
atlas organization apiKey assign <apiKeyId> [flags]
atlas organization apiKey updates <apiKeyId> [flags]
atlas organization apikey assign <apiKeyId> [flags]
atlas organization apikey updates <apiKeyId> [flags]
atlas organization api-key assign <apiKeyId> [flags]
atlas organization api-key updates <apiKeyId> [flags]
atlas orgs apiKeys assign <apiKeyId> [flags]
atlas orgs apiKeys updates <apiKeyId> [flags]
atlas orgs apikeys assign <apiKeyId> [flags]
atlas orgs apikeys updates <apiKeyId> [flags]
atlas orgs api-keys assign <apiKeyId> [flags]
atlas orgs api-keys updates <apiKeyId> [flags]
atlas orgs apiKey assign <apiKeyId> [flags]
atlas orgs apiKey updates <apiKeyId> [flags]
atlas orgs apikey assign <apiKeyId> [flags]
atlas orgs apikey updates <apiKeyId> [flags]
atlas orgs api-key assign <apiKeyId> [flags]
atlas orgs api-key updates <apiKeyId> [flags]
atlas org apiKeys assign <apiKeyId> [flags]
atlas org apiKeys updates <apiKeyId> [flags]
atlas org apikeys assign <apiKeyId> [flags]
atlas org apikeys updates <apiKeyId> [flags]
atlas org api-keys assign <apiKeyId> [flags]
atlas org api-keys updates <apiKeyId> [flags]
atlas org apiKey assign <apiKeyId> [flags]
atlas org apiKey updates <apiKeyId> [flags]
atlas org apikey assign <apiKeyId> [flags]
atlas org apikey updates <apiKeyId> [flags]
atlas org api-key assign <apiKeyId> [flags]
atlas org api-key updates <apiKeyId> [flags]
```

### Examples

```
  # Modify the role and description for the API key with the ID 5f24084d8dbffa3ad3f21234 for the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys assign 5f24084d8dbffa3ad3f21234 --role ORG_MEMBER --desc "User1 Member Key" --orgId 5a1b39eec902201990f12345 --output json
```


### Flags

```
      --desc string     Description of the API key.
  -h, --help            help for assign
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --role strings    Role or roles that you want to assign to the API key. To assign more than one role, specify each role with a separate role flag or specify all of the roles as a comma-separated list using one role flag. To learn which values the CLI accepts, see the Items Enum for roles in the Atlas API spec: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Programmatic-API-Keys/operation/createApiKey/. Passing this flag replaces preexisting data.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



