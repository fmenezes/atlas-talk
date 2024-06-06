## atlas events projects list

Return all events for the specified project.


### Usage
```
atlas events projects list [flags]
```

### Aliases
```

atlas events projects list
atlas events projects ls
atlas events project list
atlas events project ls
atlas event projects list
atlas event projects ls
atlas event project list
atlas event project ls
```

### Examples

```
  # Return a JSON-formatted list of events for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas events projects list --Id 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for list
      --limit int          Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --maxDate string     Maximum created date. This option returns events whose created date is less than or equal to the specified value.
      --minDate string     Minimum created date. This option returns events whose created date is greater than or equal to the specified value.
      --omitCount          Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int           Page number that specifies a page of results. (default 1)
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type strings       Type of event that triggered the alert. To learn which values the CLI accepts, see the Enum for eventTypeName in the Atlas Admin API spec: https://dochub.mongodb.org/core/atlas-event-names.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas events projects](atlas_events_projects.md)	- Project operations.



