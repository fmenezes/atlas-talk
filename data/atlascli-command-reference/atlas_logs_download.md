## atlas logs download

Download a compressed file that contains the MongoDB logs for the specified host.


### Synopsis

This command downloads a file with a .gz extension.

To find the hostnames for an Atlas project, use the process list command.

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.



```

atlas logs download <hostname> <mongodb.gz|mongos.gz|mongosqld.gz|mongodb-audit-log.gz|mongos-audit-log.gz> [flags]
atlas log download <hostname> <mongodb.gz|mongos.gz|mongosqld.gz|mongodb-audit-log.gz|mongos-audit-log.gz> [flags]
```

### Examples

```
  # Download the mongodb log file from the host atlas-123abc-shard-00-00.111xx.mongodb.net for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas logs download  atlas-123abc-shard-00-00.111xx.mongodb.net mongodb.gz --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
  -d, --decompress         Flag that indicates whether to decompress the log files.
      --end int            UNIX Epoch-formatted ending date and time for the range of log messages to retrieve. This value defaults to the current timestamp.
      --force              Flag that indicates whether to overwrite the destination file.
  -h, --help               help for download
      --out string         Output file name. This value defaults to the log name.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start int          UNIX Epoch-formatted starting date and time for the range of log messages to retrieve. This value defaults to 24 hours prior to the current timestamp.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas logs](atlas_logs.md)	- Download host logs for your project.



