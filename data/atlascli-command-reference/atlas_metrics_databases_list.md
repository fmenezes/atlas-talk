## atlas metrics databases list

Return all databases running on the specified host for your project.


### Synopsis

To return the hostname and port needed for this command, run
atlas processes list

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas metrics databases list <hostname:port> [flags]
atlas metrics databases ls <hostname:port> [flags]
atlas metrics database list <hostname:port> [flags]
atlas metrics database ls <hostname:port> [flags]
atlas metric databases list <hostname:port> [flags]
atlas metric databases ls <hostname:port> [flags]
atlas metric database list <hostname:port> [flags]
atlas metric database ls <hostname:port> [flags]
atlas measurements databases list <hostname:port> [flags]
atlas measurements databases ls <hostname:port> [flags]
atlas measurements database list <hostname:port> [flags]
atlas measurements database ls <hostname:port> [flags]
atlas measurement databases list <hostname:port> [flags]
atlas measurement databases ls <hostname:port> [flags]
atlas measurement database list <hostname:port> [flags]
atlas measurement database ls <hostname:port> [flags]
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

### SEE ALSO


* [atlas metrics databases](atlas_metrics_databases.md)	- List available databases or database metrics for a given host.



