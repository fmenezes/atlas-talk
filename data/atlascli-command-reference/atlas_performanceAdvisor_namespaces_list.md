## atlas performanceAdvisor namespaces list

Return up to 20 namespaces for collections experiencing slow queries on the specified host.


### Synopsis

Namespaces appear in the following format: {database}.{collection}.
		
If you don't set the duration option or the since option, this command returns data from the last 24 hours.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas performanceAdvisor namespaces list [flags]
atlas performanceAdvisor namespaces ls [flags]
atlas performanceAdvisor namespace list [flags]
atlas performanceAdvisor namespace ls [flags]
atlas performanceadvisor namespaces list [flags]
atlas performanceadvisor namespaces ls [flags]
atlas performanceadvisor namespace list [flags]
atlas performanceadvisor namespace ls [flags]
atlas performance-advisor namespaces list [flags]
atlas performance-advisor namespaces ls [flags]
atlas performance-advisor namespace list [flags]
atlas performance-advisor namespace ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of namespaces for collections with slow queries for the atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 host in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas performanceAdvisor namespaces list --processName atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --duration int         Length of time in milliseconds for which you want to return results. If you specify the since option, the duration starts at the date and time specified. If you don't set the since option, this command returns data from the duration before the current time.
  -h, --help                 help for list
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


* [atlas performanceAdvisor namespaces](atlas_performanceAdvisor_namespaces.md)	- Retrieve namespaces for collections experiencing slow queries



