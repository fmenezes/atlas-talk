## atlas teams list

Return all teams for your organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas teams list [flags]
atlas teams ls [flags]
atlas team list [flags]
atlas team ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of the teams for the organization with ID 5e2211c17a3e5a48f5497de3:
  atlas teams list --orgId 5e1234c17a3e5a48f5497de3 --output json
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


* [atlas teams](atlas_teams.md)	- Manage your Atlas teams.



