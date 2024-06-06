## atlas organizations apiKeys delete

Remove the specified API key for your organization.


### Synopsis

To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization User Admin role.


### Usage
```
atlas organizations apiKeys delete <ID> [flags]
```

### Aliases
```

atlas organizations apiKeys delete
atlas organizations apiKeys rm
atlas organizations apikeys delete
atlas organizations apikeys rm
atlas organizations api-keys delete
atlas organizations api-keys rm
atlas organizations apiKey delete
atlas organizations apiKey rm
atlas organizations apikey delete
atlas organizations apikey rm
atlas organizations api-key delete
atlas organizations api-key rm
atlas organization apiKeys delete
atlas organization apiKeys rm
atlas organization apikeys delete
atlas organization apikeys rm
atlas organization api-keys delete
atlas organization api-keys rm
atlas organization apiKey delete
atlas organization apiKey rm
atlas organization apikey delete
atlas organization apikey rm
atlas organization api-key delete
atlas organization api-key rm
atlas orgs apiKeys delete
atlas orgs apiKeys rm
atlas orgs apikeys delete
atlas orgs apikeys rm
atlas orgs api-keys delete
atlas orgs api-keys rm
atlas orgs apiKey delete
atlas orgs apiKey rm
atlas orgs apikey delete
atlas orgs apikey rm
atlas orgs api-key delete
atlas orgs api-key rm
atlas org apiKeys delete
atlas org apiKeys rm
atlas org apikeys delete
atlas org apikeys rm
atlas org api-keys delete
atlas org api-keys rm
atlas org apiKey delete
atlas org apiKey rm
atlas org apikey delete
atlas org apikey rm
atlas org api-key delete
atlas org api-key rm
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

### See Also


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



