## atlas accessLists list

Return all IP access list entries for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Member role.


### Usage
```
atlas accessLists list [flags]
```

### Aliases
```

atlas accessLists list
atlas accessLists ls
atlas accesslists list
atlas accesslists ls
atlas access-lists list
atlas access-lists ls
atlas accessList list
atlas accessList ls
atlas accesslist list
atlas accesslist ls
atlas access-list list
atlas access-list ls
atlas whitelists list
atlas whitelists ls
atlas whitelist list
atlas whitelist ls
```

### Examples

```
  # Return a JSON-formatted list of all access list entries for the project with ID 5e1234c17a3e5a48f5497de3:		
  atlas accessLists list --output json --projectId 5e1234c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for list
      --limit int          Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount          Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int           Page number that specifies a page of results. (default 1)
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas accessLists](atlas_accessLists.md)	- Manage the list of IP addresses that can access your Atlas project.



