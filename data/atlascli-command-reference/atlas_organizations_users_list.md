## atlas organizations users list

Return all users for an organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas organizations users list [flags]
atlas organizations users ls [flags]
atlas organizations user list [flags]
atlas organizations user ls [flags]
atlas organization users list [flags]
atlas organization users ls [flags]
atlas organization user list [flags]
atlas organization user ls [flags]
atlas orgs users list [flags]
atlas orgs users ls [flags]
atlas orgs user list [flags]
atlas orgs user ls [flags]
atlas org users list [flags]
atlas org users ls [flags]
atlas org user list [flags]
atlas org user ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of all users for the organization with the ID 5e2211c17a3e5a48f5497de3:
  atlas organizations users list --orgId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
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


* [atlas organizations users](atlas_organizations_users.md)	- Manage your Atlas users.



