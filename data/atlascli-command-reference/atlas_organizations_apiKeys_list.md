## atlas organizations apiKeys list

Return all API keys for your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.


### Usage
```
atlas organizations apiKeys list [flags]
```

### Aliases
```

atlas organizations apiKeys list
atlas organizations apiKeys ls
atlas organizations apikeys list
atlas organizations apikeys ls
atlas organizations api-keys list
atlas organizations api-keys ls
atlas organizations apiKey list
atlas organizations apiKey ls
atlas organizations apikey list
atlas organizations apikey ls
atlas organizations api-key list
atlas organizations api-key ls
atlas organization apiKeys list
atlas organization apiKeys ls
atlas organization apikeys list
atlas organization apikeys ls
atlas organization api-keys list
atlas organization api-keys ls
atlas organization apiKey list
atlas organization apiKey ls
atlas organization apikey list
atlas organization apikey ls
atlas organization api-key list
atlas organization api-key ls
atlas orgs apiKeys list
atlas orgs apiKeys ls
atlas orgs apikeys list
atlas orgs apikeys ls
atlas orgs api-keys list
atlas orgs api-keys ls
atlas orgs apiKey list
atlas orgs apiKey ls
atlas orgs apikey list
atlas orgs apikey ls
atlas orgs api-key list
atlas orgs api-key ls
atlas org apiKeys list
atlas org apiKeys ls
atlas org apikeys list
atlas org apikeys ls
atlas org api-keys list
atlas org api-keys ls
atlas org apiKey list
atlas org apiKey ls
atlas org apikey list
atlas org apikey ls
atlas org api-key list
atlas org api-key ls
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

### See Also


* [atlas organizations apiKeys](atlas_organizations_apiKeys.md)	- Organization API Keys operations.



