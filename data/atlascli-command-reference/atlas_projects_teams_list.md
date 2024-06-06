## atlas projects teams list

Return all teams for a project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas projects teams list [flags]
atlas projects teams ls [flags]
atlas projects team list [flags]
atlas projects team ls [flags]
atlas project teams list [flags]
atlas project teams ls [flags]
atlas project team list [flags]
atlas project team ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of all teams for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas projects teams list --projectId 5e2211c17a3e5a48f5497de3 --output json
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

### SEE ALSO


* [atlas projects teams](atlas_projects_teams.md)	- Manage your Atlas teams.



