## atlas backups compliancePolicy pointInTimeRestores enable

Enable Point-in-Time restores of the backup compliance policy for your project.



```

atlas backups compliancePolicy pointInTimeRestores enable [flags]
atlas backups compliancePolicy pointintimerestores enable [flags]
atlas backups compliancePolicy point-in-time-restores enable [flags]
atlas backups compliancePolicy pointInTimeRestore enable [flags]
atlas backups compliancePolicy pointintimerestore enable [flags]
atlas backups compliancePolicy point-in-time-restore enable [flags]
atlas backups compliancepolicy pointInTimeRestores enable [flags]
atlas backups compliancepolicy pointintimerestores enable [flags]
atlas backups compliancepolicy point-in-time-restores enable [flags]
atlas backups compliancepolicy pointInTimeRestore enable [flags]
atlas backups compliancepolicy pointintimerestore enable [flags]
atlas backups compliancepolicy point-in-time-restore enable [flags]
atlas backups compliance-policy pointInTimeRestores enable [flags]
atlas backups compliance-policy pointintimerestores enable [flags]
atlas backups compliance-policy point-in-time-restores enable [flags]
atlas backups compliance-policy pointInTimeRestore enable [flags]
atlas backups compliance-policy pointintimerestore enable [flags]
atlas backups compliance-policy point-in-time-restore enable [flags]
atlas backup compliancePolicy pointInTimeRestores enable [flags]
atlas backup compliancePolicy pointintimerestores enable [flags]
atlas backup compliancePolicy point-in-time-restores enable [flags]
atlas backup compliancePolicy pointInTimeRestore enable [flags]
atlas backup compliancePolicy pointintimerestore enable [flags]
atlas backup compliancePolicy point-in-time-restore enable [flags]
atlas backup compliancepolicy pointInTimeRestores enable [flags]
atlas backup compliancepolicy pointintimerestores enable [flags]
atlas backup compliancepolicy point-in-time-restores enable [flags]
atlas backup compliancepolicy pointInTimeRestore enable [flags]
atlas backup compliancepolicy pointintimerestore enable [flags]
atlas backup compliancepolicy point-in-time-restore enable [flags]
atlas backup compliance-policy pointInTimeRestores enable [flags]
atlas backup compliance-policy pointintimerestores enable [flags]
atlas backup compliance-policy point-in-time-restores enable [flags]
atlas backup compliance-policy pointInTimeRestore enable [flags]
atlas backup compliance-policy pointintimerestore enable [flags]
atlas backup compliance-policy point-in-time-restore enable [flags]
```



### Flags

```
  -h, --help                    help for enable
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --restoreWindowDays int   Number of days back in time you can restore to with Continuous Cloud Backup accuracy. Must be a positive, non-zero integer. Applies to continuous cloud backups only.
  -w, --watch                   Flag that indicates whether to watch the command until it completes its execution or the watch times out.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups compliancePolicy pointInTimeRestores](atlas_backups_compliancePolicy_pointInTimeRestores.md)	- Manage whether the project uses Continuous Cloud Backups with a Backup Compliance Policy. Read more in the documentation: https://www.mongodb.com/docs/atlas/backup/cloud-backup/configure-backup-policy/#configure-the-restore-window.



