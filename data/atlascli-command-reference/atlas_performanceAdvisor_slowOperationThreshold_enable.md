## atlas performanceAdvisor slowOperationThreshold enable

Enable the application-managed slow operation threshold for your project.


### Synopsis

The slow operation threshold determines which operations are flagged by the Performance Advisor and Query Profiler. When enabled, the application uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. Application-managed slow operation threshold is enabled by default for dedicated clusters (M10+).

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas performanceAdvisor slowOperationThreshold enable [flags]
atlas performanceAdvisor slowOperationThreshold ls [flags]
atlas performanceAdvisor slowoperationthreshold enable [flags]
atlas performanceAdvisor slowoperationthreshold ls [flags]
atlas performanceAdvisor slow-operation-threshold enable [flags]
atlas performanceAdvisor slow-operation-threshold ls [flags]
atlas performanceAdvisor slowOT enable [flags]
atlas performanceAdvisor slowOT ls [flags]
atlas performanceAdvisor sot enable [flags]
atlas performanceAdvisor sot ls [flags]
atlas performanceAdvisor slowMS enable [flags]
atlas performanceAdvisor slowMS ls [flags]
atlas performanceadvisor slowOperationThreshold enable [flags]
atlas performanceadvisor slowOperationThreshold ls [flags]
atlas performanceadvisor slowoperationthreshold enable [flags]
atlas performanceadvisor slowoperationthreshold ls [flags]
atlas performanceadvisor slow-operation-threshold enable [flags]
atlas performanceadvisor slow-operation-threshold ls [flags]
atlas performanceadvisor slowOT enable [flags]
atlas performanceadvisor slowOT ls [flags]
atlas performanceadvisor sot enable [flags]
atlas performanceadvisor sot ls [flags]
atlas performanceadvisor slowMS enable [flags]
atlas performanceadvisor slowMS ls [flags]
atlas performance-advisor slowOperationThreshold enable [flags]
atlas performance-advisor slowOperationThreshold ls [flags]
atlas performance-advisor slowoperationthreshold enable [flags]
atlas performance-advisor slowoperationthreshold ls [flags]
atlas performance-advisor slow-operation-threshold enable [flags]
atlas performance-advisor slow-operation-threshold ls [flags]
atlas performance-advisor slowOT enable [flags]
atlas performance-advisor slowOT ls [flags]
atlas performance-advisor sot enable [flags]
atlas performance-advisor sot ls [flags]
atlas performance-advisor slowMS enable [flags]
atlas performance-advisor slowMS ls [flags]
```



### Flags

```
  -h, --help               help for enable
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas performanceAdvisor slowOperationThreshold](atlas_performanceAdvisor_slowOperationThreshold.md)	- Enable or disable management of the slow operation threshold for your cluster.



