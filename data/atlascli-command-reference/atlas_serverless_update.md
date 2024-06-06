## atlas serverless update

Updates one serverless instance in the specified project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas serverless update <instanceName> [flags]
atlas sl update <instanceName> [flags]
```



### Flags

```
      --disableServerlessContinuousBackup   Disables Serverless Continuous Backup for your serverless instance. If disabled the serverless instance uses Basic Backup.
      --disableTerminationProtection        Disables termination protection for your cluster. You can delete a cluster with termination protection disabled.
      --enableServerlessContinuousBackup    Flag that enables Serverless Continuous Backup for your serverless instance. If enabled, the serverless instance does not use Basic Backup.
      --enableTerminationProtection         Enables termination protection for your cluster. You can't delete a cluster with termination protection enabled.
  -h, --help                                help for update
  -o, --output string                       Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                    Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --tag stringToString                  List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the serverless instance. Passing this flag replaces preexisting data. (default [])

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas serverless](atlas_serverless.md)	- Manage serverless instances for your project.



