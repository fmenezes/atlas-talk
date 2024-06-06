## atlas organizations list

Return all organizations.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.



```

atlas organizations list [flags]
atlas organizations ls [flags]
atlas organization list [flags]
atlas organization ls [flags]
atlas orgs list [flags]
atlas orgs ls [flags]
atlas org list [flags]
atlas org ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of all organizations:
  atlas organizations list --output json
  
  # Return a JSON-formatted list that includes the organizations named org1 and Org1, but doesn't return org123:
  atlas organizations list --name org1 --output json
```


### Flags

```
  -h, --help             help for list
      --includeDeleted   Flag that indictaes whether to include deleted organizations in the list. This option applies only to Ops Manager organizations. You can't return deleted Atlas or Cloud Manager organizations.
      --limit int        Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --name string      Organization name to perform a case-insensitive search for.
      --omitCount        Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string    Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int         Page number that specifies a page of results. (default 1)

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations](atlas_organizations.md)	- Manage your Atlas organizations.



