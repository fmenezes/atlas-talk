## atlas backups exports jobs list

Return all cloud backup export jobs for your project and cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups exports jobs list <clusterName> [flags]
```

### Aliases
```

atlas backups exports jobs list
atlas backups exports jobs ls
atlas backups exports job list
atlas backups exports job ls
atlas backups export jobs list
atlas backups export jobs ls
atlas backups export job list
atlas backups export job ls
atlas backup exports jobs list
atlas backup exports jobs ls
atlas backup exports job list
atlas backup exports job ls
atlas backup export jobs list
atlas backup export jobs ls
atlas backup export job list
atlas backup export job ls
```

### Examples

```
  # Return all continuous backup export jobs for the cluster named Cluster0:
  atlas backup exports jobs list Cluster0
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


* [atlas backups exports jobs](atlas_backups_exports_jobs.md)	- Manage cloud backup export jobs for your project.



