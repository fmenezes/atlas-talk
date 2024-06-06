## atlas dbusers list

Return all database users for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas dbusers list [flags]
```

### Aliases
```

atlas dbusers list
atlas dbusers ls
atlas dbuser list
atlas dbuser ls
```

### Examples

```
  # Return a JSON-formatted list of all database users for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas dbusers list --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -c, --compact            Flag that enables the compact array response structure for a json output. The --compact option returns array objects as top-level responses and allows backward compatibility for scripts based on previous CLI versions. Omitting the --compact option for a json output returns array objects within a 'results' sub-array. You must specify --output json to use this option.
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


* [atlas dbusers](atlas_dbusers.md)	- Manage database users for your project.



