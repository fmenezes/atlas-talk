## atlas performanceAdvisor slowQueryLogs list

Return log lines for slow queries that the Performance Advisor and Query Profiler identified.


### Synopsis

The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. The threshold for slow queries varies based on the average time of operations on your cluster to provide recommendations pertinent to your workload.
		
If you don't set the duration option or the since option, this command returns data from the last 24 hours.

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.



```

atlas performanceAdvisor slowQueryLogs list [flags]
atlas performanceAdvisor slowQueryLogs ls [flags]
atlas performanceAdvisor slowquerylogs list [flags]
atlas performanceAdvisor slowquerylogs ls [flags]
atlas performanceAdvisor slow-query-logs list [flags]
atlas performanceAdvisor slow-query-logs ls [flags]
atlas performanceAdvisor slowQueryLog list [flags]
atlas performanceAdvisor slowQueryLog ls [flags]
atlas performanceAdvisor slowquerylog list [flags]
atlas performanceAdvisor slowquerylog ls [flags]
atlas performanceAdvisor slow-query-log list [flags]
atlas performanceAdvisor slow-query-log ls [flags]
atlas performanceadvisor slowQueryLogs list [flags]
atlas performanceadvisor slowQueryLogs ls [flags]
atlas performanceadvisor slowquerylogs list [flags]
atlas performanceadvisor slowquerylogs ls [flags]
atlas performanceadvisor slow-query-logs list [flags]
atlas performanceadvisor slow-query-logs ls [flags]
atlas performanceadvisor slowQueryLog list [flags]
atlas performanceadvisor slowQueryLog ls [flags]
atlas performanceadvisor slowquerylog list [flags]
atlas performanceadvisor slowquerylog ls [flags]
atlas performanceadvisor slow-query-log list [flags]
atlas performanceadvisor slow-query-log ls [flags]
atlas performance-advisor slowQueryLogs list [flags]
atlas performance-advisor slowQueryLogs ls [flags]
atlas performance-advisor slowquerylogs list [flags]
atlas performance-advisor slowquerylogs ls [flags]
atlas performance-advisor slow-query-logs list [flags]
atlas performance-advisor slow-query-logs ls [flags]
atlas performance-advisor slowQueryLog list [flags]
atlas performance-advisor slowQueryLog ls [flags]
atlas performance-advisor slowquerylog list [flags]
atlas performance-advisor slowquerylog ls [flags]
atlas performance-advisor slow-query-log list [flags]
atlas performance-advisor slow-query-log ls [flags]
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

### SEE ALSO


* [atlas performanceAdvisor slowQueryLogs](atlas_performanceAdvisor_slowQueryLogs.md)	- Get log lines for slow queries for a specified host



