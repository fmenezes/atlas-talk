## atlas performanceAdvisor slowOperationThreshold enable

Enable the application-managed slow operation threshold for your project.


### Synopsis

The slow operation threshold determines which operations are flagged by the Performance Advisor and Query Profiler. When enabled, the application uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. Application-managed slow operation threshold is enabled by default for dedicated clusters (M10+).

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas performanceAdvisor slowOperationThreshold enable [flags]
```

### Aliases
```

atlas performanceAdvisor slowOperationThreshold enable
atlas performanceAdvisor slowOperationThreshold ls
atlas performanceAdvisor slowoperationthreshold enable
atlas performanceAdvisor slowoperationthreshold ls
atlas performanceAdvisor slow-operation-threshold enable
atlas performanceAdvisor slow-operation-threshold ls
atlas performanceAdvisor slowOT enable
atlas performanceAdvisor slowOT ls
atlas performanceAdvisor sot enable
atlas performanceAdvisor sot ls
atlas performanceAdvisor slowMS enable
atlas performanceAdvisor slowMS ls
atlas performanceadvisor slowOperationThreshold enable
atlas performanceadvisor slowOperationThreshold ls
atlas performanceadvisor slowoperationthreshold enable
atlas performanceadvisor slowoperationthreshold ls
atlas performanceadvisor slow-operation-threshold enable
atlas performanceadvisor slow-operation-threshold ls
atlas performanceadvisor slowOT enable
atlas performanceadvisor slowOT ls
atlas performanceadvisor sot enable
atlas performanceadvisor sot ls
atlas performanceadvisor slowMS enable
atlas performanceadvisor slowMS ls
atlas performance-advisor slowOperationThreshold enable
atlas performance-advisor slowOperationThreshold ls
atlas performance-advisor slowoperationthreshold enable
atlas performance-advisor slowoperationthreshold ls
atlas performance-advisor slow-operation-threshold enable
atlas performance-advisor slow-operation-threshold ls
atlas performance-advisor slowOT enable
atlas performance-advisor slowOT ls
atlas performance-advisor sot enable
atlas performance-advisor sot ls
atlas performance-advisor slowMS enable
atlas performance-advisor slowMS ls
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

### See Also


* [atlas performanceAdvisor slowOperationThreshold](atlas_performanceAdvisor_slowOperationThreshold.md)	- Enable or disable management of the slow operation threshold for your cluster.



