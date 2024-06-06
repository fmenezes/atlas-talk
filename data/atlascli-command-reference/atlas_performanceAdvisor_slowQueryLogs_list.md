## atlas performanceAdvisor slowQueryLogs list

Return log lines for slow queries that the Performance Advisor and Query Profiler identified.


### Synopsis

The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. The threshold for slow queries varies based on the average time of operations on your cluster to provide recommendations pertinent to your workload.
		
If you don't set the duration option or the since option, this command returns data from the last 24 hours.

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas performanceAdvisor slowQueryLogs list [flags]
```

### Aliases
```

atlas performanceAdvisor slowQueryLogs list
atlas performanceAdvisor slowQueryLogs ls
atlas performanceAdvisor slowquerylogs list
atlas performanceAdvisor slowquerylogs ls
atlas performanceAdvisor slow-query-logs list
atlas performanceAdvisor slow-query-logs ls
atlas performanceAdvisor slowQueryLog list
atlas performanceAdvisor slowQueryLog ls
atlas performanceAdvisor slowquerylog list
atlas performanceAdvisor slowquerylog ls
atlas performanceAdvisor slow-query-log list
atlas performanceAdvisor slow-query-log ls
atlas performanceadvisor slowQueryLogs list
atlas performanceadvisor slowQueryLogs ls
atlas performanceadvisor slowquerylogs list
atlas performanceadvisor slowquerylogs ls
atlas performanceadvisor slow-query-logs list
atlas performanceadvisor slow-query-logs ls
atlas performanceadvisor slowQueryLog list
atlas performanceadvisor slowQueryLog ls
atlas performanceadvisor slowquerylog list
atlas performanceadvisor slowquerylog ls
atlas performanceadvisor slow-query-log list
atlas performanceadvisor slow-query-log ls
atlas performance-advisor slowQueryLogs list
atlas performance-advisor slowQueryLogs ls
atlas performance-advisor slowquerylogs list
atlas performance-advisor slowquerylogs ls
atlas performance-advisor slow-query-logs list
atlas performance-advisor slow-query-logs ls
atlas performance-advisor slowQueryLog list
atlas performance-advisor slowQueryLog ls
atlas performance-advisor slowquerylog list
atlas performance-advisor slowquerylog ls
atlas performance-advisor slow-query-log list
atlas performance-advisor slow-query-log ls
```

### Examples

```
  # Return a JSON-formatted list of log lines for collections with slow queries for the atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 host in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas performanceAdvisor slowQueryLogs list --processName atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --duration int         Length of time in milliseconds for which you want to return results. If you specify the since option, the duration starts at the date and time specified. If you don't set the since option, this command returns data from the duration before the current time.
  -h, --help                 help for list
      --nLog int             Maximum number of log lines to return. (default 20000)
      --namespaces strings   Namespaces from which to retrieve suggested slow query logs formatted as <database>.<collection>. Omit this parameter to return results for all namespaces.
  -o, --output string        Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --processName string   Unique identifier for the host of a MongoDB process in the following format: {hostname}:{port}. You can obtain a list of possible values from the 'id' field when you run the 'atlas processes list' command.
      --projectId string     Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --since int            Date and time from which the query retrieves the suggested indexes. Specify this value as the number of seconds that have elapsed since the UNIX epoch. If you don't set the duration option, this command returns data from the since value to the current time.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas performanceAdvisor slowQueryLogs](atlas_performanceAdvisor_slowQueryLogs.md)	- Get log lines for slow queries for a specified host



