## atlas backups schedule update

Modify the backup schedule for the specified cluster for your project.


### Synopsis

The backup schedule defines when MongoDB takes scheduled snapshots and how long it stores those snapshots.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups schedule update [flags]
```

### Aliases
```

atlas backups schedule update
atlas backups schedule updates
atlas backup schedule update
atlas backup schedule updates
```

### Examples

```
  # Update a snapshot backup policy for a cluster named Cluster0 to back up snapshots every 6 hours and, retain for 7 days, and update retention of previously-taken snapshots:
  atlas backup schedule update --clusterName Cluster0 --updateSnapshots --policy 62da8faac84a2721e448d767,62da8faac84a2721e448d768,hourly,6,days,7
  
  # Update a snapshot backup policy for a cluster named Cluster0 to export snapshots monthly to an S3 bucket:
  atlas backup schedule update --clusterName Cluster0 --exportBucketId 62c569f85b7a381c093cc539 --exportFrequencyType monthly
```


### Flags

```
      --autoExport                            Flag that enables automatic export of cloud backup snapshots to the AWS bucket.
      --clusterName string                    Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
      --exportBucketId string                 Unique identifier that Atlas assigns to the bucket.
      --exportFrequencyType string            Frequency associated with the export policy. Value can be daily, weekly, or monthly.
  -f, --file string                           Path to an optional JSON configuration file that defines backup schedule settings. To learn about the cloud backup configuration file for the Atlas CLI, see https://dochub.mongodb.org/core/cloud-backup-config-file.
  -h, --help                                  help for update
      --noAutoExport                          Flag that disables automatic export of cloud backup snapshots to the AWS bucket.
      --noUpdateSnapshots                     Flag that disables applying the retention changes in the updated backup policy to snapshots that Atlas took previously.
      --noUseOrgAndGroupNamesInExportPrefix   Flag that disables usage of organization and project names instead of organization and project UUIDs in the path for the metadata files that Atlas uploads to your S3 bucket after it finishes exporting the snapshots.
  -o, --output string                         Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --policy stringArray                    Array containing a document for each backup policy item in the desired updated backup policy. You must specify it in a format: '--policy policyID,policyItemID,frequencyType,frequencyIntervalNumber,retentionUnit,retentionValue'.
      --projectId string                      Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --referenceHourOfDay int                Hour of the day to schedule snapshots using a 24-hour clock. Accepted values are between 0 and 23 inclusive.
      --referenceMinuteOfHour int             Minute of the hour to schedule snapshots. Accepted values are between 0 and 59 inclusive.
      --restoreWindowDays int                 Number of days back in time you can restore to with Continuous Cloud Backup accuracy. Must be a positive, non-zero integer. Applies to continuous cloud backups only.
      --updateSnapshots                       Flag that enables applying the retention changes in the updated backup policy to snapshots that Atlas took previously.
      --useOrgAndGroupNamesInExportPrefix     Flag that enables usage of organization and project names instead of organization and project UUIDs in the path for the metadata files that Atlas uploads to your S3 bucket after it finishes exporting the snapshots.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups schedule](atlas_backups_schedule.md)	- Return a cloud backup schedule for the cluster you specify.



