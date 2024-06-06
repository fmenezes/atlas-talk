## atlas projects apiKeys delete

Remove the specified organization API key from your project.


### Synopsis

The API key still exists at the organization level. To reassign the organization API key to a project, run the  atlas projects apiKeys assign command.
		
To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Project User Admin role.



```

atlas projects apiKeys delete <ID> [flags]
atlas projects apiKeys rm <ID> [flags]
atlas projects apikeys delete <ID> [flags]
atlas projects apikeys rm <ID> [flags]
atlas projects api-keys delete <ID> [flags]
atlas projects api-keys rm <ID> [flags]
atlas projects apiKey delete <ID> [flags]
atlas projects apiKey rm <ID> [flags]
atlas projects apikey delete <ID> [flags]
atlas projects apikey rm <ID> [flags]
atlas projects api-key delete <ID> [flags]
atlas projects api-key rm <ID> [flags]
atlas project apiKeys delete <ID> [flags]
atlas project apiKeys rm <ID> [flags]
atlas project apikeys delete <ID> [flags]
atlas project apikeys rm <ID> [flags]
atlas project api-keys delete <ID> [flags]
atlas project api-keys rm <ID> [flags]
atlas project apiKey delete <ID> [flags]
atlas project apiKey rm <ID> [flags]
atlas project apikey delete <ID> [flags]
atlas project apikey rm <ID> [flags]
atlas project api-key delete <ID> [flags]
atlas project api-key rm <ID> [flags]
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

### SEE ALSO


* [atlas projects apiKeys](atlas_projects_apiKeys.md)	- Manage API Keys for your project.



