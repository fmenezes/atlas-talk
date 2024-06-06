## atlas metrics processes

Return the process measurements for the specified host.


### Synopsis

To return the hostname and port needed for this command, run
atlas processes list

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas metrics processes <hostname:port> [flags]
```

### Aliases
```

atlas metrics processes
atlas metrics process
atlas metric processes
atlas metric process
atlas measurements processes
atlas measurements process
atlas measurement processes
atlas measurement process
```

### Examples

```
  # Return the JSON-formatted process metrics for the host atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017
  atlas metrics processes atlas-lnmtkm-shard-00-00.ajlj3.mongodb.net:27017 --output json
```


### Flags

```
      --end string           ISO 8601-formatted date and time that specifies when to stop retrieving measurements. You can't set this parameter and period in the same request.
      --granularity string   ISO 8601-formatted duration that specifies the interval between measurement data points. Only the following subset of ISO 8601-formatted time periods are supported: PT10S, PT1M, PT5M, PT1H, P1D. When you specify granularity, you must specify either period or start and end.
  -h, --help                 help for processes
      --limit int            Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int             Page number that specifies a page of results. (default 1)
      --period string        ISO 8601-formatted time period that specifies the length of time in the past to query. You can't set this parameter and the start or end parameter in the same request.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start string         ISO 8601-formatted date and time that specifies when to start retrieving measurements. You can't set this parameter and period in the same request.
      --type strings         Measurements to return. This option returns all measurements by default. To learn which values the CLI accepts, see the Items Enum for m in the Atlas API spec: https://www.mongodb.com/docs/atlas/reference/api-resources-spec/#tag/Monitoring-and-Logs/operation/getHostMeasurements/.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas metrics](atlas_metrics.md)	- Get metrics on the MongoDB process.



