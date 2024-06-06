## atlas backups restores start

Start a restore job for your project and cluster.


### Synopsis

If you create an automated or pointInTime restore job, Atlas removes all existing data on the target cluster prior to the restore.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.
Atlas supports this command only for M10+ clusters.



```

atlas backups restores start <automated|download|pointInTime> [flags]
atlas backups restore start <automated|download|pointInTime> [flags]
atlas backup restores start <automated|download|pointInTime> [flags]
atlas backup restore start <automated|download|pointInTime> [flags]
```

### Examples

```
  # Create an automated restore:
  atlas backup restore start automated \
         --clusterName myDemo \
         --snapshotId 5e7e00128f8ce03996a47179 \
         --targetClusterName myDemo2 \
         --targetProjectId 1a2345b67c8e9a12f3456de7

  # Create a point-in-time restore:
  atlas backup restore start pointInTime \
         --clusterName myDemo \
         --pointInTimeUTCSeconds 1588523147 \
         --targetClusterName myDemo2 \
         --targetProjectId 1a2345b67c8e9a12f3456de7
  
  # Create a download restore:
  atlas backup restore start download \
         --clusterName myDemo \
         --snapshotId 5e7e00128f8ce03996a47179
```


### Flags

```
      --clusterName string          Name of the cluster. To learn more, see https://dochub.mongodb.org/core/create-cluster-api.
  -h, --help                        help for start
      --oplogInc int                32-bit incrementing ordinal that represents operations within a given second. When paired with oplogTs, they represent the point in time to which your data will be restored.
      --oplogTs int                 Oplog timestamp given as a timestamp in the number of seconds that have elapsed since the UNIX Epoch. When paired with oplogInc, they represent the point in time to which your data will be restored.
  -o, --output string               Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --pointInTimeUTCSeconds int   Timestamp in the number of seconds that have elapsed since the UNIX epoch that represents the point in time to which your data will be restored. This timestamp must be within the last 24 hours of the current time.
      --projectId string            Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --snapshotId string           Unique identifier of the snapshot to restore. You must specify a snapshotId for automated restores.
      --targetClusterName string    Name of the target cluster. For use only with automated restore jobs. You must specify a targetClusterName for automated restores.
      --targetProjectId string      Unique identifier of the project that contains the destination cluster for the restore job. You must specify a targetProjectId for automated restores.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas backups restores](atlas_backups_restores.md)	- Manage cloud backup restore jobs for your project.



