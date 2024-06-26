## atlas metrics databases describe

Return the measurements of a database on the specified host.


### Synopsis

To return the hostname and port needed for this command, run
atlas process list


### Usage
```
atlas metrics databases describe <hostname:port> <databaseName> [flags]
```

### Aliases
```

atlas metrics databases describe
atlas metrics database describe
atlas metric databases describe
atlas metric database describe
atlas measurements databases describe
atlas measurements database describe
atlas measurement databases describe
atlas measurement database describe
```

### Examples

```
  # Return the JSON-formatted database metrics from the last 36 hours with 5-minute granularity for the database named testDB in the host atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 
  atlas metrics databases describe atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 testDB --granularity PT1M --period P1DT12H --output json
```


### Flags

```
      --end string           ISO 8601-formatted date and time that specifies when to stop retrieving measurements. You can't set this parameter and period in the same request.
      --granularity string   ISO 8601-formatted duration that specifies the interval between measurement data points. Only the following subset of ISO 8601-formatted time periods are supported: PT10S, PT1M, PT5M, PT1H, P1D. When you specify granularity, you must specify either period or start and end.
  -h, --help                 help for describe
      --limit int            Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int             Page number that specifies a page of results. (default 1)
      --period string        ISO 8601-formatted time period that specifies the length of time in the past to query. You can't set this parameter and the start or end parameter in the same request.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start string         ISO 8601-formatted date and time that specifies when to start retrieving measurements. You can't set this parameter and period in the same request.
      --type strings         Measurements to return. This option returns all measurements by default. Valid values include DATABASE_AVERAGE_OBJECT_SIZE, DATABASE_COLLECTION_COUNT, DATABASE_DATA_SIZE, DATABASE_STORAGE_SIZE, DATABASE_INDEX_SIZE, DATABASE_INDEX_COUNT, DATABASE_EXTENT_COUNT, DATABASE_OBJECT_COUNT, and DATABASE_VIEW_COUNT

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas metrics databases](atlas_metrics_databases.md)	- List available databases or database metrics for a given host.



