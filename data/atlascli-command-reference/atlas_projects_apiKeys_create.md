## atlas projects apiKeys create

Create an organization API key and assign it to your project.


### Synopsis

MongoDB returns the private API key only once. After you run this command, immediately copy, save, and secure both the public and private API keys.

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.


### Usage
```
atlas projects apiKeys create [flags]
```

### Aliases
```

atlas projects apiKeys create
atlas projects apikeys create
atlas projects api-keys create
atlas projects apiKey create
atlas projects apikey create
atlas projects api-key create
atlas project apiKeys create
atlas project apikeys create
atlas project api-keys create
atlas project apiKey create
atlas project apikey create
atlas project api-key create
```

### Examples

```
  # Create an organization API key with the ORG_OWNER role and assign it to the project with ID 5e2211c17a3e5a48f5497de3:
  atlas projects apiKeys create --desc "My API key" --projectId 5e1234c17a3e5a48f5497de3 --role ORG_OWNER --output json
```


### Flags

```
      --desc string        Description of the API key.
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --role strings       Role or roles that you want to assign to the API key. To assign more than one role, specify each role with a separate role flag or specify all of the roles as a comma-separated list using one role flag. To learn which values the CLI accepts, see the Items Enum for roles in the Atlas API spec: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Programmatic-API-Keys/operation/createProjectApiKey/.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects apiKeys](atlas_projects_apiKeys.md)	- Manage API Keys for your project.



