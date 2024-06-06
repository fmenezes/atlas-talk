## atlas organizations apiKeys delete

Remove the specified API key for your organization.


### Synopsis

To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.



```

atlas organizations apiKeys delete <ID> [flags]
atlas organizations apiKeys rm <ID> [flags]
atlas organizations apikeys delete <ID> [flags]
atlas organizations apikeys rm <ID> [flags]
atlas organizations api-keys delete <ID> [flags]
atlas organizations api-keys rm <ID> [flags]
atlas organizations apiKey delete <ID> [flags]
atlas organizations apiKey rm <ID> [flags]
atlas organizations apikey delete <ID> [flags]
atlas organizations apikey rm <ID> [flags]
atlas organizations api-key delete <ID> [flags]
atlas organizations api-key rm <ID> [flags]
atlas organization apiKeys delete <ID> [flags]
atlas organization apiKeys rm <ID> [flags]
atlas organization apikeys delete <ID> [flags]
atlas organization apikeys rm <ID> [flags]
atlas organization api-keys delete <ID> [flags]
atlas organization api-keys rm <ID> [flags]
atlas organization apiKey delete <ID> [flags]
atlas organization apiKey rm <ID> [flags]
atlas organization apikey delete <ID> [flags]
atlas organization apikey rm <ID> [flags]
atlas organization api-key delete <ID> [flags]
atlas organization api-key rm <ID> [flags]
atlas orgs apiKeys delete <ID> [flags]
atlas orgs apiKeys rm <ID> [flags]
atlas orgs apikeys delete <ID> [flags]
atlas orgs apikeys rm <ID> [flags]
atlas orgs api-keys delete <ID> [flags]
atlas orgs api-keys rm <ID> [flags]
atlas orgs apiKey delete <ID> [flags]
atlas orgs apiKey rm <ID> [flags]
atlas orgs apikey delete <ID> [flags]
atlas orgs apikey rm <ID> [flags]
atlas orgs api-key delete <ID> [flags]
atlas orgs api-key rm <ID> [flags]
atlas org apiKeys delete <ID> [flags]
atlas org apiKeys rm <ID> [flags]
atlas org apikeys delete <ID> [flags]
atlas org apikeys rm <ID> [flags]
atlas org api-keys delete <ID> [flags]
atlas org api-keys rm <ID> [flags]
atlas org apiKey delete <ID> [flags]
atlas org apiKey rm <ID> [flags]
atlas org apikey delete <ID> [flags]
atlas org apikey rm <ID> [flags]
atlas org api-key delete <ID> [flags]
atlas org api-key rm <ID> [flags]
```

### Examples

```
  # Remove the organization API key with the ID 5f24084d8dbffa3ad3f21234 for the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys delete 5f24084d8dbffa3ad3f21234 --orgId 5a1b39eec902201990f12345
```


### Flags

```
      --force          Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help           help for delete
      --orgId string   Organization ID to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



