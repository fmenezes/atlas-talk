## atlas performanceAdvisor slowOperationThreshold disable

Disable the application-managed slow operation threshold for your project.


### Synopsis

The slow operation threshold determines which operations are flagged by the Performance Advisor and Query Profiler. When disabled, the application considers any operation that takes longer than 100 milliseconds to be slow.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas performanceAdvisor slowOperationThreshold disable [flags]
atlas performanceAdvisor slowoperationthreshold disable [flags]
atlas performanceAdvisor slow-operation-threshold disable [flags]
atlas performanceAdvisor slowOT disable [flags]
atlas performanceAdvisor sot disable [flags]
atlas performanceAdvisor slowMS disable [flags]
atlas performanceadvisor slowOperationThreshold disable [flags]
atlas performanceadvisor slowoperationthreshold disable [flags]
atlas performanceadvisor slow-operation-threshold disable [flags]
atlas performanceadvisor slowOT disable [flags]
atlas performanceadvisor sot disable [flags]
atlas performanceadvisor slowMS disable [flags]
atlas performance-advisor slowOperationThreshold disable [flags]
atlas performance-advisor slowoperationthreshold disable [flags]
atlas performance-advisor slow-operation-threshold disable [flags]
atlas performance-advisor slowOT disable [flags]
atlas performance-advisor sot disable [flags]
atlas performance-advisor slowMS disable [flags]
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

### SEE ALSO


* [atlas performanceAdvisor slowOperationThreshold](atlas_performanceAdvisor_slowOperationThreshold.md)	- Enable or disable management of the slow operation threshold for your cluster.



