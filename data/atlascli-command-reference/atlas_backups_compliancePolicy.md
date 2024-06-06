## atlas backups compliancePolicy

Manage cloud backup compliance policy for your project. Use "atlas backups compliancepolicy setup" to enable backup compliance policy with a full configuration. Use "atlas backups compliancepolicy enable" to enable backup compliance policy without any configuration.






### Flags

```
  -h, --help   help for compliancePolicy

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups](atlas_backups.md)	- Manage cloud backups for your project.

* [atlas backups compliancePolicy copyProtection](atlas_backups_compliancePolicy_copyProtection.md)	- Manage copy protection of the backup compliance policy for your project. Learn more: https://www.mongodb.com/docs/atlas/backup/cloud-backup/backup-compliance-policy/#-optional--keep-all-snapshots-when-removing-additional-snapshot-regions.

* [atlas backups compliancePolicy describe](atlas_backups_compliancePolicy_describe.md)	- Return the backup compliance policy for your project.

* [atlas backups compliancePolicy enable](atlas_backups_compliancePolicy_enable.md)	- Enable Backup Compliance Policy without any configuration.

* [atlas backups compliancePolicy encryptionAtRest](atlas_backups_compliancePolicy_encryptionAtRest.md)	- Manage encryption-at-rest for the backup compliance policy for your project. Encryption-at-rest enforces all clusters with a Backup Compliance Policy to use Customer Key Management.

* [atlas backups compliancePolicy pointInTimeRestores](atlas_backups_compliancePolicy_pointInTimeRestores.md)	- Manage whether the project uses Continuous Cloud Backups with a Backup Compliance Policy. Read more in the documentation: https://www.mongodb.com/docs/atlas/backup/cloud-backup/configure-backup-policy/#configure-the-restore-window.

* [atlas backups compliancePolicy policies](atlas_backups_compliancePolicy_policies.md)	- Manage the individual policy items of the backup compliance policy for your project.

* [atlas backups compliancePolicy setup](atlas_backups_compliancePolicy_setup.md)	- Setup the backup compliance policy for your project with a configuration file.



