## atlas serverless backups snapshots list

Return all cloud backup snapshots for the specified serverless instance in your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas serverless backups snapshots list <clusterName> [flags]
atlas serverless backups snapshots ls <clusterName> [flags]
atlas serverless backups snapshot list <clusterName> [flags]
atlas serverless backups snapshot ls <clusterName> [flags]
atlas serverless backup snapshots list <clusterName> [flags]
atlas serverless backup snapshots ls <clusterName> [flags]
atlas serverless backup snapshot list <clusterName> [flags]
atlas serverless backup snapshot ls <clusterName> [flags]
atlas sl backups snapshots list <clusterName> [flags]
atlas sl backups snapshots ls <clusterName> [flags]
atlas sl backups snapshot list <clusterName> [flags]
atlas sl backups snapshot ls <clusterName> [flags]
atlas sl backup snapshots list <clusterName> [flags]
atlas sl backup snapshots ls <clusterName> [flags]
atlas sl backup snapshot list <clusterName> [flags]
atlas sl backup snapshot ls <clusterName> [flags]
```

### Examples

```
  # Return a JSON-formatted list of snapshots for the instance named myDemo 
  atlas serverless backups snapshots list myDemo --output json
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


* [atlas serverless backups snapshots](atlas_serverless_backups_snapshots.md)	- Manage cloud backup snapshots for your project.



