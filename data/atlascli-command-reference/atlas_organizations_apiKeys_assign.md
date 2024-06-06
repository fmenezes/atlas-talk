## atlas organizations apiKeys assign

Modify the roles or description for the specified organization API key.


### Synopsis

When you modify the roles for an organization API key with this command, the values you specify overwrite the existing roles assigned to the API key.
		
To view possible values for the apiKeyId argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas organizations apiKeys assign <apiKeyId> [flags]
```

### Aliases
```

atlas organizations apiKeys assign
atlas organizations apiKeys updates
atlas organizations apikeys assign
atlas organizations apikeys updates
atlas organizations api-keys assign
atlas organizations api-keys updates
atlas organizations apiKey assign
atlas organizations apiKey updates
atlas organizations apikey assign
atlas organizations apikey updates
atlas organizations api-key assign
atlas organizations api-key updates
atlas organization apiKeys assign
atlas organization apiKeys updates
atlas organization apikeys assign
atlas organization apikeys updates
atlas organization api-keys assign
atlas organization api-keys updates
atlas organization apiKey assign
atlas organization apiKey updates
atlas organization apikey assign
atlas organization apikey updates
atlas organization api-key assign
atlas organization api-key updates
atlas orgs apiKeys assign
atlas orgs apiKeys updates
atlas orgs apikeys assign
atlas orgs apikeys updates
atlas orgs api-keys assign
atlas orgs api-keys updates
atlas orgs apiKey assign
atlas orgs apiKey updates
atlas orgs apikey assign
atlas orgs apikey updates
atlas orgs api-key assign
atlas orgs api-key updates
atlas org apiKeys assign
atlas org apiKeys updates
atlas org apikeys assign
atlas org apikeys updates
atlas org api-keys assign
atlas org api-keys updates
atlas org apiKey assign
atlas org apiKey updates
atlas org apikey assign
atlas org apikey updates
atlas org api-key assign
atlas org api-key updates
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

### See Also


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



