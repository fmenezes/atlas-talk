## atlas organizations apiKeys list

Return all API keys for your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas organizations apiKeys list [flags]
atlas organizations apiKeys ls [flags]
atlas organizations apikeys list [flags]
atlas organizations apikeys ls [flags]
atlas organizations api-keys list [flags]
atlas organizations api-keys ls [flags]
atlas organizations apiKey list [flags]
atlas organizations apiKey ls [flags]
atlas organizations apikey list [flags]
atlas organizations apikey ls [flags]
atlas organizations api-key list [flags]
atlas organizations api-key ls [flags]
atlas organization apiKeys list [flags]
atlas organization apiKeys ls [flags]
atlas organization apikeys list [flags]
atlas organization apikeys ls [flags]
atlas organization api-keys list [flags]
atlas organization api-keys ls [flags]
atlas organization apiKey list [flags]
atlas organization apiKey ls [flags]
atlas organization apikey list [flags]
atlas organization apikey ls [flags]
atlas organization api-key list [flags]
atlas organization api-key ls [flags]
atlas orgs apiKeys list [flags]
atlas orgs apiKeys ls [flags]
atlas orgs apikeys list [flags]
atlas orgs apikeys ls [flags]
atlas orgs api-keys list [flags]
atlas orgs api-keys ls [flags]
atlas orgs apiKey list [flags]
atlas orgs apiKey ls [flags]
atlas orgs apikey list [flags]
atlas orgs apikey ls [flags]
atlas orgs api-key list [flags]
atlas orgs api-key ls [flags]
atlas org apiKeys list [flags]
atlas org apiKeys ls [flags]
atlas org apikeys list [flags]
atlas org apikeys ls [flags]
atlas org api-keys list [flags]
atlas org api-keys ls [flags]
atlas org apiKey list [flags]
atlas org apiKey ls [flags]
atlas org apikey list [flags]
atlas org apikey ls [flags]
atlas org api-key list [flags]
atlas org api-key ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of organization API keys for the organization with the ID 5a1b39eec902201990f12345:
  atlas organizations apiKeys list --orgId 5a1b39eec902201990f12345 --output json
```


### Flags

```
  -c, --compact         Flag that enables the compact array response structure for a json output. The --compact option returns array objects as top-level responses and allows backward compatibility for scripts based on previous CLI versions. Omitting the --compact option for a json output returns array objects within a 'results' sub-array. You must specify --output json to use this option.
  -h, --help            help for list
      --limit int       Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount       Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int        Page number that specifies a page of results. (default 1)

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



