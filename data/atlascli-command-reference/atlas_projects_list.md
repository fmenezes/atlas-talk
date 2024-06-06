## atlas projects list

Return all projects.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas projects list [flags]
```

### Aliases
```

atlas projects list
atlas projects ls
atlas project list
atlas project ls
```

### Examples

```
  # Return a JSON-formatted list of all projects:
  atlas projects list --output json
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

### See Also


* [atlas projects](atlas_projects.md)	- Manage your Atlas projects.



