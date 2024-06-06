## atlas backups compliancePolicy setup

Setup the backup compliance policy for your project with a configuration file.


### Usage
```
atlas backups compliancePolicy setup [flags]
```

### Aliases
```

atlas backups compliancePolicy setup
atlas backups compliancepolicy setup
atlas backups compliance-policy setup
atlas backup compliancePolicy setup
atlas backup compliancepolicy setup
atlas backup compliance-policy setup
```



### Flags

```
  -f, --file string        Path to a JSON configuration file that defines backup compliance policy settings.
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for setup
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
  -w, --watch              Flag that indicates whether to watch the command until it completes its execution or the watch times out.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups compliancePolicy](atlas_backups_compliancePolicy.md)	- Manage cloud backup compliance policy for your project. Use "atlas backups compliancepolicy setup" to enable backup compliance policy with a full configuration. Use "atlas backups compliancepolicy enable" to enable backup compliance policy without any configuration.



