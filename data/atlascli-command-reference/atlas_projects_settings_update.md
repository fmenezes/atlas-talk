## atlas projects settings update

Updates settings for a project.


### Usage
```
atlas projects settings update [flags]
```

### Aliases
```

atlas projects settings update
atlas projects settings updates
atlas projects setting update
atlas projects setting updates
atlas project settings update
atlas project settings updates
atlas project setting update
atlas project setting updates
```

### Examples

```
  # This example uses the profile named "myprofile" for accessing Atlas.
  atlas projects settings update --disableCollectDatabaseSpecificsStatistics -P myprofile --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --disableCollectDatabaseSpecificsStatistics   Flag that disables the Collect Database Specific Statistics project setting.
      --disableDataExplorer                         Flag that disables the Data Explorer project setting.
      --disablePerformanceAdvisor                   Flag that disables the Performance Advisor project setting.
      --disableRealtimePerformancePanel             Flag that disables the Real Time Performance Panel project setting.
      --disableSchemaAdvisor                        Flag that disables the Schema Advisor project setting.
      --enableCollectDatabaseSpecificsStatistics    Flag that enables the Collect Database Specific Statistics project setting.
      --enableDataExplorer                          Flag that enables the Data Explorer project setting.
      --enablePerformanceAdvisor                    Flag that enables the Performance Advisor project setting.
      --enableRealtimePerformancePanel              Flag that enables the Real Time Performance Panel project setting.
      --enableSchemaAdvisor                         Flag that enables the Schema Advisor project setting.
  -h, --help                                        help for update
  -o, --output string                               Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                            Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects settings](atlas_projects_settings.md)	- Settings operations.



