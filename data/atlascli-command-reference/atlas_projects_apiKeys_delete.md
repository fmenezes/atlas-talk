## atlas projects apiKeys delete

Remove the specified organization API key from your project.


### Synopsis

The API key still exists at the organization level. To reassign the organization API key to a project, run the  atlas projects apiKeys assign command.
		
To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.


### Usage
```
atlas projects apiKeys delete <ID> [flags]
```

### Aliases
```

atlas projects apiKeys delete
atlas projects apiKeys rm
atlas projects apikeys delete
atlas projects apikeys rm
atlas projects api-keys delete
atlas projects api-keys rm
atlas projects apiKey delete
atlas projects apiKey rm
atlas projects apikey delete
atlas projects apikey rm
atlas projects api-key delete
atlas projects api-key rm
atlas project apiKeys delete
atlas project apiKeys rm
atlas project apikeys delete
atlas project apikeys rm
atlas project api-keys delete
atlas project api-keys rm
atlas project apiKey delete
atlas project apiKey rm
atlas project apikey delete
atlas project apikey rm
atlas project api-key delete
atlas project api-key rm
```

### Examples

```
  # Remove an organization API key with the ID 5f46ae53d58b421fe3edc115 from the project with ID 5e2211c17a3e5a48f5497de3:
  atlas projects apiKeys delete 5f46ae53d58b421fe3edc115 --projectId 5e1234c17a3e5a48f5497de3
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects apiKeys](atlas_projects_apiKeys.md)	- Manage API Keys for your project.



