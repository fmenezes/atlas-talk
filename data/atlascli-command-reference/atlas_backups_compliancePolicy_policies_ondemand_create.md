## atlas backups compliancePolicy policies ondemand create

Create the on-demand policy item of the backup compliance policy for your project.


### Usage
```
atlas backups compliancePolicy policies ondemand create [flags]
```

### Aliases
```

atlas backups compliancePolicy policies ondemand create
atlas backups compliancePolicy policy ondemand create
atlas backups compliancepolicy policies ondemand create
atlas backups compliancepolicy policy ondemand create
atlas backups compliance-policy policies ondemand create
atlas backups compliance-policy policy ondemand create
atlas backup compliancePolicy policies ondemand create
atlas backup compliancePolicy policy ondemand create
atlas backup compliancepolicy policies ondemand create
atlas backup compliancepolicy policy ondemand create
atlas backup compliance-policy policies ondemand create
atlas backup compliance-policy policy ondemand create
```

### Examples

```
  # Create a backup compliance on-demand policy with a retention of two weeks:
  atlas backups compliancepolicy policies ondemand create --retentionUnit weeks --retentionValue 2
```


### Flags

```
  -h, --help                   help for create
  -o, --output string          Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string       Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --retentionUnit string   Unit of time in which Atlas measures snapshot retention: 'days' 'weeks' 'months'. 
      --retentionValue int     Duration in days, weeks, or months that Atlas retains the snapshot. For less frequent policy items, Atlas requires that you specify a value greater than or equal to the value specified for more frequent policy items.
  -w, --watch                  Flag that indicates whether to watch the command until it completes its execution or the watch times out.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups compliancePolicy policies ondemand](atlas_backups_compliancePolicy_policies_ondemand.md)	- Manage the on-demand policy item of the backup compliance policy for your project.



