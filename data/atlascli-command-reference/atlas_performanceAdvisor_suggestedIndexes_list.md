## atlas performanceAdvisor suggestedIndexes list

Return the suggested indexes for collections experiencing slow queries.


### Synopsis

The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas performanceAdvisor suggestedIndexes list [flags]
```

### Aliases
```

atlas performanceAdvisor suggestedIndexes list
atlas performanceAdvisor suggestedIndexes ls
atlas performanceAdvisor suggestedindexes list
atlas performanceAdvisor suggestedindexes ls
atlas performanceAdvisor suggested-indexes list
atlas performanceAdvisor suggested-indexes ls
atlas performanceAdvisor suggestedIndex list
atlas performanceAdvisor suggestedIndex ls
atlas performanceAdvisor suggestedindex list
atlas performanceAdvisor suggestedindex ls
atlas performanceAdvisor suggested-index list
atlas performanceAdvisor suggested-index ls
atlas performanceadvisor suggestedIndexes list
atlas performanceadvisor suggestedIndexes ls
atlas performanceadvisor suggestedindexes list
atlas performanceadvisor suggestedindexes ls
atlas performanceadvisor suggested-indexes list
atlas performanceadvisor suggested-indexes ls
atlas performanceadvisor suggestedIndex list
atlas performanceadvisor suggestedIndex ls
atlas performanceadvisor suggestedindex list
atlas performanceadvisor suggestedindex ls
atlas performanceadvisor suggested-index list
atlas performanceadvisor suggested-index ls
atlas performance-advisor suggestedIndexes list
atlas performance-advisor suggestedIndexes ls
atlas performance-advisor suggestedindexes list
atlas performance-advisor suggestedindexes ls
atlas performance-advisor suggested-indexes list
atlas performance-advisor suggested-indexes ls
atlas performance-advisor suggestedIndex list
atlas performance-advisor suggestedIndex ls
atlas performance-advisor suggestedindex list
atlas performance-advisor suggestedindex ls
atlas performance-advisor suggested-index list
atlas performance-advisor suggested-index ls
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

### See Also


* [atlas performanceAdvisor suggestedIndexes](atlas_performanceAdvisor_suggestedIndexes.md)	- Get suggested indexes for collections experiencing slow queries



