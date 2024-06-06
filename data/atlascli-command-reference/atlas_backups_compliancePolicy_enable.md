## atlas backups compliancePolicy enable

Enable Backup Compliance Policy without any configuration.


### Usage
```
atlas backups compliancePolicy enable [flags]
```

### Aliases
```

atlas backups compliancePolicy enable
atlas backups compliancepolicy enable
atlas backups compliance-policy enable
atlas backup compliancePolicy enable
atlas backup compliancepolicy enable
atlas backup compliance-policy enable
```



### Flags

```
      --authorizedEmail string           Email address of a security or legal representative.
      --authorizedUserFirstName string   First name of the user who is authorized to update the Backup Compliance Policy settings.
      --authorizedUserLastName string    Last name of the user who is authorized to update the Backup Compliance Policy settings.
      --force                            Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                             help for enable
  -o, --output string                    Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                 Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
  -w, --watch                            Flag that indicates whether to watch the command until it completes its execution or the watch times out.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups compliancePolicy](atlas_backups_compliancePolicy.md)	- Manage cloud backup compliance policy for your project. Use "atlas backups compliancepolicy setup" to enable backup compliance policy with a full configuration. Use "atlas backups compliancepolicy enable" to enable backup compliance policy without any configuration.



