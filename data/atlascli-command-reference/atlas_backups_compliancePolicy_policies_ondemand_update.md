## atlas backups compliancePolicy policies ondemand update

Update the on-demand policy of the backup compliance for your project.



```

atlas backups compliancePolicy policies ondemand update [flags]
atlas backups compliancePolicy policy ondemand update [flags]
atlas backups compliancepolicy policies ondemand update [flags]
atlas backups compliancepolicy policy ondemand update [flags]
atlas backups compliance-policy policies ondemand update [flags]
atlas backups compliance-policy policy ondemand update [flags]
atlas backup compliancePolicy policies ondemand update [flags]
atlas backup compliancePolicy policy ondemand update [flags]
atlas backup compliancepolicy policies ondemand update [flags]
atlas backup compliancepolicy policy ondemand update [flags]
atlas backup compliance-policy policies ondemand update [flags]
atlas backup compliance-policy policy ondemand update [flags]
```

### Examples

```
  # Update a backup compliance on-demand policy and set it's retention to one week:
  atlas backups compliancepolicy policies ondemand update --retentionUnit weeks --retentionValue 1
```


### Flags

```
  -h, --help                   help for update
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

### SEE ALSO


* [atlas backups compliancePolicy policies ondemand](atlas_backups_compliancePolicy_policies_ondemand.md)	- Manage the on-demand policy item of the backup compliance policy for your project.



