## atlas organizations apiKeys describe

Return the details for the specified API key for your organization.


### Synopsis

To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas organizations apiKeys describe <ID> [flags]
atlas organizations apiKeys show <ID> [flags]
atlas organizations apikeys describe <ID> [flags]
atlas organizations apikeys show <ID> [flags]
atlas organizations api-keys describe <ID> [flags]
atlas organizations api-keys show <ID> [flags]
atlas organizations apiKey describe <ID> [flags]
atlas organizations apiKey show <ID> [flags]
atlas organizations apikey describe <ID> [flags]
atlas organizations apikey show <ID> [flags]
atlas organizations api-key describe <ID> [flags]
atlas organizations api-key show <ID> [flags]
atlas organization apiKeys describe <ID> [flags]
atlas organization apiKeys show <ID> [flags]
atlas organization apikeys describe <ID> [flags]
atlas organization apikeys show <ID> [flags]
atlas organization api-keys describe <ID> [flags]
atlas organization api-keys show <ID> [flags]
atlas organization apiKey describe <ID> [flags]
atlas organization apiKey show <ID> [flags]
atlas organization apikey describe <ID> [flags]
atlas organization apikey show <ID> [flags]
atlas organization api-key describe <ID> [flags]
atlas organization api-key show <ID> [flags]
atlas orgs apiKeys describe <ID> [flags]
atlas orgs apiKeys show <ID> [flags]
atlas orgs apikeys describe <ID> [flags]
atlas orgs apikeys show <ID> [flags]
atlas orgs api-keys describe <ID> [flags]
atlas orgs api-keys show <ID> [flags]
atlas orgs apiKey describe <ID> [flags]
atlas orgs apiKey show <ID> [flags]
atlas orgs apikey describe <ID> [flags]
atlas orgs apikey show <ID> [flags]
atlas orgs api-key describe <ID> [flags]
atlas orgs api-key show <ID> [flags]
atlas org apiKeys describe <ID> [flags]
atlas org apiKeys show <ID> [flags]
atlas org apikeys describe <ID> [flags]
atlas org apikeys show <ID> [flags]
atlas org api-keys describe <ID> [flags]
atlas org api-keys show <ID> [flags]
atlas org apiKey describe <ID> [flags]
atlas org apiKey show <ID> [flags]
atlas org apikey describe <ID> [flags]
atlas org apikey show <ID> [flags]
atlas org api-key describe <ID> [flags]
atlas org api-key show <ID> [flags]
```

### Examples

```
  # Return the JSON-formatted details for the organization API key with the ID 5f24084d8dbffa3ad3f21234 for the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys describe 5f24084d8dbffa3ad3f21234 --orgId 5a1b39eec902201990f12345 -output json
```


### Flags

```
  -h, --help            help for describe
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



