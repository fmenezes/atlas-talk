## atlas serverless backups restores list

Return all cloud backup restore jobs for the specified serverless instance in your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas serverless backups restores list <clusterName> [flags]
atlas serverless backups restores ls <clusterName> [flags]
atlas serverless backups restore list <clusterName> [flags]
atlas serverless backups restore ls <clusterName> [flags]
atlas serverless backup restores list <clusterName> [flags]
atlas serverless backup restores ls <clusterName> [flags]
atlas serverless backup restore list <clusterName> [flags]
atlas serverless backup restore ls <clusterName> [flags]
atlas sl backups restores list <clusterName> [flags]
atlas sl backups restores ls <clusterName> [flags]
atlas sl backups restore list <clusterName> [flags]
atlas sl backups restore ls <clusterName> [flags]
atlas sl backup restores list <clusterName> [flags]
atlas sl backup restores ls <clusterName> [flags]
atlas sl backup restore list <clusterName> [flags]
atlas sl backup restore ls <clusterName> [flags]
```

### Examples

```
  # Return all continuous backup restore jobs for the serverless instance Instance0:
  atlas serverless backup restore list Instance0
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


* [atlas serverless backups restores](atlas_serverless_backups_restores.md)	- Manage cloud backup restore jobs for your project.



