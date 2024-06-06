## atlas projects apiKeys assign

Assign the specified organization API key to your project and modify the API key's roles for the project.


### Synopsis

When you modify the roles for an organization API key with this command, the values you specify overwrite the existing roles assigned to the API key.
		
To view possible values for the ID argument, run atlas organizations apiKeys list.


### Usage
```
atlas projects apiKeys assign <ID> [flags]
```

### Aliases
```

atlas projects apiKeys assign
atlas projects apiKeys update
atlas projects apikeys assign
atlas projects apikeys update
atlas projects api-keys assign
atlas projects api-keys update
atlas projects apiKey assign
atlas projects apiKey update
atlas projects apikey assign
atlas projects apikey update
atlas projects api-key assign
atlas projects api-key update
atlas project apiKeys assign
atlas project apiKeys update
atlas project apikeys assign
atlas project apikeys update
atlas project api-keys assign
atlas project api-keys update
atlas project apiKey assign
atlas project apiKey update
atlas project apikey assign
atlas project apikey update
atlas project api-key assign
atlas project api-key update
```

### Examples

```
  # Assign an organization API key with the ID 5f46ae53d58b421fe3edc115 and grant the GROUP_DATA_ACCESS_READ_WRITE role for the project with ID 5e2211c17a3e5a48f5497de3:
  atlas projects apiKeys assign 5f46ae53d58b421fe3edc115 --projectId 5e1234c17a3e5a48f5497de3 --role GROUP_DATA_ACCESS_READ_WRITE --output json
```


### Flags

```
  -h, --help               help for assign
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



