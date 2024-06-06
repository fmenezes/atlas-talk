## atlas metrics databases list

Return all databases running on the specified host for your project.


### Synopsis

To return the hostname and port needed for this command, run
atlas processes list

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas metrics databases list <hostname:port> [flags]
```

### Aliases
```

atlas metrics databases list
atlas metrics databases ls
atlas metrics database list
atlas metrics database ls
atlas metric databases list
atlas metric databases ls
atlas metric database list
atlas metric database ls
atlas measurements databases list
atlas measurements databases ls
atlas measurements database list
atlas measurements database ls
atlas measurement databases list
atlas measurement databases ls
atlas measurement database list
atlas measurement database ls
```

### Examples

```
  # Return a JSON-formatted list of available databases for the host atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017
  atlas metrics databases list atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 --output json
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


* [atlas metrics databases](atlas_metrics_databases.md)	- List available databases or database metrics for a given host.



