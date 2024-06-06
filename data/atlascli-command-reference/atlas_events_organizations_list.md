## atlas events organizations list

Return all events for the specified organization.


### Usage
```
atlas events organizations list [flags]
```

### Aliases
```

atlas events organizations list
atlas events organizations ls
atlas events organization list
atlas events organization ls
atlas events orgs list
atlas events orgs ls
atlas events org list
atlas events org ls
atlas event organizations list
atlas event organizations ls
atlas event organization list
atlas event organization ls
atlas event orgs list
atlas event orgs ls
atlas event org list
atlas event org ls
```

### Examples

```
  # Return a JSON-formatted list of events for the organization with the ID 5dd5a6b6f10fab1d71a58495:
  atlas events organizations list --orgId 5dd5a6b6f10fab1d71a58495 --output json
```


### Flags

```
  -h, --help             help for list
      --limit int        Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --maxDate string   Maximum created date. This option returns events whose created date is less than or equal to the specified value.
      --minDate string   Minimum created date. This option returns events whose created date is greater than or equal to the specified value.
      --omitCount        Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
      --orgId string     Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string    Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int         Page number that specifies a page of results. (default 1)
      --type strings     Type of event that triggered the alert. To learn which values the CLI accepts, see the Enum for eventTypeName in the Atlas Admin API spec: https://dochub.mongodb.org/core/atlas-event-names.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas events organizations](atlas_events_organizations.md)	- Organization operations.



