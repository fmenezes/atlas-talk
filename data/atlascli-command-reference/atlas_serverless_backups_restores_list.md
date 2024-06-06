## atlas serverless backups restores list

Return all cloud backup restore jobs for the specified serverless instance in your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas serverless backups restores list <clusterName> [flags]
```

### Aliases
```

atlas serverless backups restores list
atlas serverless backups restores ls
atlas serverless backups restore list
atlas serverless backups restore ls
atlas serverless backup restores list
atlas serverless backup restores ls
atlas serverless backup restore list
atlas serverless backup restore ls
atlas sl backups restores list
atlas sl backups restores ls
atlas sl backups restore list
atlas sl backups restore ls
atlas sl backup restores list
atlas sl backup restores ls
atlas sl backup restore list
atlas sl backup restore ls
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

### See Also


* [atlas serverless backups restores](atlas_serverless_backups_restores.md)	- Manage cloud backup restore jobs for your project.



