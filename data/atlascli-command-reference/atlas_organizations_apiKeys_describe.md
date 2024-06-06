## atlas organizations apiKeys describe

Return the details for the specified API key for your organization.


### Synopsis

To view possible values for the ID argument, run atlas organizations apiKeys list.

To use this command, you must authenticate with a user account or an API key with the Organization Member role.


### Usage
```
atlas organizations apiKeys describe <ID> [flags]
```

### Aliases
```

atlas organizations apiKeys describe
atlas organizations apiKeys show
atlas organizations apikeys describe
atlas organizations apikeys show
atlas organizations api-keys describe
atlas organizations api-keys show
atlas organizations apiKey describe
atlas organizations apiKey show
atlas organizations apikey describe
atlas organizations apikey show
atlas organizations api-key describe
atlas organizations api-key show
atlas organization apiKeys describe
atlas organization apiKeys show
atlas organization apikeys describe
atlas organization apikeys show
atlas organization api-keys describe
atlas organization api-keys show
atlas organization apiKey describe
atlas organization apiKey show
atlas organization apikey describe
atlas organization apikey show
atlas organization api-key describe
atlas organization api-key show
atlas orgs apiKeys describe
atlas orgs apiKeys show
atlas orgs apikeys describe
atlas orgs apikeys show
atlas orgs api-keys describe
atlas orgs api-keys show
atlas orgs apiKey describe
atlas orgs apiKey show
atlas orgs apikey describe
atlas orgs apikey show
atlas orgs api-key describe
atlas orgs api-key show
atlas org apiKeys describe
atlas org apiKeys show
atlas org apikeys describe
atlas org apikeys show
atlas org api-keys describe
atlas org api-keys show
atlas org apiKey describe
atlas org apiKey show
atlas org apikey describe
atlas org apikey show
atlas org api-key describe
atlas org api-key show
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

### See Also


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



