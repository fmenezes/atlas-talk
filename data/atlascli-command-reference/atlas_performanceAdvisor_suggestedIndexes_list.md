## atlas performanceAdvisor suggestedIndexes list

Return the suggested indexes for collections experiencing slow queries.


### Synopsis

The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas performanceAdvisor suggestedIndexes list [flags]
atlas performanceAdvisor suggestedIndexes ls [flags]
atlas performanceAdvisor suggestedindexes list [flags]
atlas performanceAdvisor suggestedindexes ls [flags]
atlas performanceAdvisor suggested-indexes list [flags]
atlas performanceAdvisor suggested-indexes ls [flags]
atlas performanceAdvisor suggestedIndex list [flags]
atlas performanceAdvisor suggestedIndex ls [flags]
atlas performanceAdvisor suggestedindex list [flags]
atlas performanceAdvisor suggestedindex ls [flags]
atlas performanceAdvisor suggested-index list [flags]
atlas performanceAdvisor suggested-index ls [flags]
atlas performanceadvisor suggestedIndexes list [flags]
atlas performanceadvisor suggestedIndexes ls [flags]
atlas performanceadvisor suggestedindexes list [flags]
atlas performanceadvisor suggestedindexes ls [flags]
atlas performanceadvisor suggested-indexes list [flags]
atlas performanceadvisor suggested-indexes ls [flags]
atlas performanceadvisor suggestedIndex list [flags]
atlas performanceadvisor suggestedIndex ls [flags]
atlas performanceadvisor suggestedindex list [flags]
atlas performanceadvisor suggestedindex ls [flags]
atlas performanceadvisor suggested-index list [flags]
atlas performanceadvisor suggested-index ls [flags]
atlas performance-advisor suggestedIndexes list [flags]
atlas performance-advisor suggestedIndexes ls [flags]
atlas performance-advisor suggestedindexes list [flags]
atlas performance-advisor suggestedindexes ls [flags]
atlas performance-advisor suggested-indexes list [flags]
atlas performance-advisor suggested-indexes ls [flags]
atlas performance-advisor suggestedIndex list [flags]
atlas performance-advisor suggestedIndex ls [flags]
atlas performance-advisor suggestedindex list [flags]
atlas performance-advisor suggestedindex ls [flags]
atlas performance-advisor suggested-index list [flags]
atlas performance-advisor suggested-index ls [flags]
```

### Examples

```
  # Return a JSON-formatted list of suggested indexes for the atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 host in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas performanceAdvisor suggestedIndexes list --processName atlas-111ggi-shard-00-00.111xx.mongodb.net:27017 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --duration int         Length of time in milliseconds for which you want to return results. If you specify the since option, the duration starts at the date and time specified. If you don't set the since option, this command returns data from the duration before the current time.
  -h, --help                 help for list
      --nExamples int        Maximum number of example queries to provide that a suggested index will improve.
      --nIndexes int         Maximum number of indexes to suggest.
      --namespaces strings   Namespaces from which to retrieve suggested indexes.
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


* [atlas performanceAdvisor suggestedIndexes](atlas_performanceAdvisor_suggestedIndexes.md)	- Get suggested indexes for collections experiencing slow queries



