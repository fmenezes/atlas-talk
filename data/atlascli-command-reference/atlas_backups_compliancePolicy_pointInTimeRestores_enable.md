## atlas backups compliancePolicy pointInTimeRestores enable

Enable Point-in-Time restores of the backup compliance policy for your project.


### Usage
```
atlas backups compliancePolicy pointInTimeRestores enable [flags]
```

### Aliases
```

atlas backups compliancePolicy pointInTimeRestores enable
atlas backups compliancePolicy pointintimerestores enable
atlas backups compliancePolicy point-in-time-restores enable
atlas backups compliancePolicy pointInTimeRestore enable
atlas backups compliancePolicy pointintimerestore enable
atlas backups compliancePolicy point-in-time-restore enable
atlas backups compliancepolicy pointInTimeRestores enable
atlas backups compliancepolicy pointintimerestores enable
atlas backups compliancepolicy point-in-time-restores enable
atlas backups compliancepolicy pointInTimeRestore enable
atlas backups compliancepolicy pointintimerestore enable
atlas backups compliancepolicy point-in-time-restore enable
atlas backups compliance-policy pointInTimeRestores enable
atlas backups compliance-policy pointintimerestores enable
atlas backups compliance-policy point-in-time-restores enable
atlas backups compliance-policy pointInTimeRestore enable
atlas backups compliance-policy pointintimerestore enable
atlas backups compliance-policy point-in-time-restore enable
atlas backup compliancePolicy pointInTimeRestores enable
atlas backup compliancePolicy pointintimerestores enable
atlas backup compliancePolicy point-in-time-restores enable
atlas backup compliancePolicy pointInTimeRestore enable
atlas backup compliancePolicy pointintimerestore enable
atlas backup compliancePolicy point-in-time-restore enable
atlas backup compliancepolicy pointInTimeRestores enable
atlas backup compliancepolicy pointintimerestores enable
atlas backup compliancepolicy point-in-time-restores enable
atlas backup compliancepolicy pointInTimeRestore enable
atlas backup compliancepolicy pointintimerestore enable
atlas backup compliancepolicy point-in-time-restore enable
atlas backup compliance-policy pointInTimeRestores enable
atlas backup compliance-policy pointintimerestores enable
atlas backup compliance-policy point-in-time-restores enable
atlas backup compliance-policy pointInTimeRestore enable
atlas backup compliance-policy pointintimerestore enable
atlas backup compliance-policy point-in-time-restore enable
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

### See Also


* [atlas backups compliancePolicy pointInTimeRestores](atlas_backups_compliancePolicy_pointInTimeRestores.md)	- Manage whether the project uses Continuous Cloud Backups with a Backup Compliance Policy. Read more in the documentation: https://www.mongodb.com/docs/atlas/backup/cloud-backup/configure-backup-policy/#configure-the-restore-window.



