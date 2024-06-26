## atlas backups exports buckets list

List cloud backup restore buckets for your project and cluster.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas backups exports buckets list [flags]
```

### Aliases
```

atlas backups exports buckets list
atlas backups exports buckets ls
atlas backups exports bucket list
atlas backups exports bucket ls
atlas backups export buckets list
atlas backups export buckets ls
atlas backups export bucket list
atlas backups export bucket ls
atlas backup exports buckets list
atlas backup exports buckets ls
atlas backup exports bucket list
atlas backup exports bucket ls
atlas backup export buckets list
atlas backup export buckets ls
atlas backup export bucket list
atlas backup export bucket ls
```

### Examples

```
  # Return all continuous backup export buckets for your project:
  atlas backup exports buckets list
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


* [atlas backups exports buckets](atlas_backups_exports_buckets.md)	- Manage cloud backup export buckets for your project.



