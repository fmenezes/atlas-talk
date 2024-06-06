## atlas performanceAdvisor slowOperationThreshold disable

Disable the application-managed slow operation threshold for your project.


### Synopsis

The slow operation threshold determines which operations are flagged by the Performance Advisor and Query Profiler. When disabled, the application considers any operation that takes longer than 100 milliseconds to be slow.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas performanceAdvisor slowOperationThreshold disable [flags]
```

### Aliases
```

atlas performanceAdvisor slowOperationThreshold disable
atlas performanceAdvisor slowoperationthreshold disable
atlas performanceAdvisor slow-operation-threshold disable
atlas performanceAdvisor slowOT disable
atlas performanceAdvisor sot disable
atlas performanceAdvisor slowMS disable
atlas performanceadvisor slowOperationThreshold disable
atlas performanceadvisor slowoperationthreshold disable
atlas performanceadvisor slow-operation-threshold disable
atlas performanceadvisor slowOT disable
atlas performanceadvisor sot disable
atlas performanceadvisor slowMS disable
atlas performance-advisor slowOperationThreshold disable
atlas performance-advisor slowoperationthreshold disable
atlas performance-advisor slow-operation-threshold disable
atlas performance-advisor slowOT disable
atlas performance-advisor sot disable
atlas performance-advisor slowMS disable
```



### Flags

```
  -h, --help               help for disable
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas performanceAdvisor slowOperationThreshold](atlas_performanceAdvisor_slowOperationThreshold.md)	- Enable or disable management of the slow operation threshold for your cluster.



