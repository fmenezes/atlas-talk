## atlas deployments pause

Pause a deployment.



```

atlas deployments pause <deploymentName> [flags]
atlas deployments stop <deploymentName> [flags]
atlas deployment pause <deploymentName> [flags]
atlas deployment stop <deploymentName> [flags]
```



### Flags

```
  -h, --help               help for pause
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --type string        Type of deployment. Valid values are ATLAS or LOCAL.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments](atlas_deployments.md)	- Manage cloud and local deployments.



