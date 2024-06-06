## atlas projects apiKeys assign

Assign the specified organization API key to your project and modify the API key's roles for the project.


### Synopsis

When you modify the roles for an organization API key with this command, the values you specify overwrite the existing roles assigned to the API key.
		
To view possible values for the ID argument, run atlas organizations apiKeys list.



```

atlas projects apiKeys assign <ID> [flags]
atlas projects apiKeys update <ID> [flags]
atlas projects apikeys assign <ID> [flags]
atlas projects apikeys update <ID> [flags]
atlas projects api-keys assign <ID> [flags]
atlas projects api-keys update <ID> [flags]
atlas projects apiKey assign <ID> [flags]
atlas projects apiKey update <ID> [flags]
atlas projects apikey assign <ID> [flags]
atlas projects apikey update <ID> [flags]
atlas projects api-key assign <ID> [flags]
atlas projects api-key update <ID> [flags]
atlas project apiKeys assign <ID> [flags]
atlas project apiKeys update <ID> [flags]
atlas project apikeys assign <ID> [flags]
atlas project apikeys update <ID> [flags]
atlas project api-keys assign <ID> [flags]
atlas project api-keys update <ID> [flags]
atlas project apiKey assign <ID> [flags]
atlas project apiKey update <ID> [flags]
atlas project apikey assign <ID> [flags]
atlas project apikey update <ID> [flags]
atlas project api-key assign <ID> [flags]
atlas project api-key update <ID> [flags]
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

### SEE ALSO


* [atlas projects apiKeys](atlas_projects_apiKeys.md)	- Manage API Keys for your project.



