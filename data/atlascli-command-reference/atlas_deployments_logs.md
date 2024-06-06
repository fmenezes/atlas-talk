## atlas deployments logs

Get deployment logs.



```

atlas deployments logs [flags]
atlas deployments log [flags]
atlas deployment logs [flags]
atlas deployment log [flags]
```



### Flags

```
      --deploymentName string   Name of the deployment.
      --end int                 UNIX Epoch-formatted ending date and time for the range of log messages to retrieve. This value defaults to the current timestamp.
      --force                   Flag that indicates whether to overwrite the destination file.
  -h, --help                    help for logs
      --hostname string         Name of the host that stores the log files that you want to download.
      --name string             Name of the log file (e.g. mongodb.gz|mongos.gz|mongosqld.gz|mongodb-audit-log.gz|mongos-audit-log.gz).
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start int               UNIX Epoch-formatted starting date and time for the range of log messages to retrieve. This value defaults to 24 hours prior to the current timestamp.
      --type string             Type of deployment. Valid values are ATLAS or LOCAL.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas deployments](atlas_deployments.md)	- Manage cloud and local deployments.



