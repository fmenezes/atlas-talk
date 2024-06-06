## atlas backups restores list

Return all cloud backup restore jobs for your project and cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas backups restores list <clusterName> [flags]
atlas backups restores ls <clusterName> [flags]
atlas backups restore list <clusterName> [flags]
atlas backups restore ls <clusterName> [flags]
atlas backup restores list <clusterName> [flags]
atlas backup restores ls <clusterName> [flags]
atlas backup restore list <clusterName> [flags]
atlas backup restore ls <clusterName> [flags]
```

### Examples

```
  # Return all continuous backup restore jobs for the cluster Cluster0:
  atlas backup restore list Cluster0
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


* [atlas backups restores](atlas_backups_restores.md)	- Manage cloud backup restore jobs for your project.



