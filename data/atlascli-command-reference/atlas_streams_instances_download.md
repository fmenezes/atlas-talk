## atlas streams instances download

Download a compressed file that contains the logs for the specified Atlas Stream Processing instance.


### Synopsis

This command downloads a file with a .gz extension. To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas streams instances download <tenantName> [flags]
```

### Aliases
```

atlas streams instances download
atlas streams instance download
atlas stream instances download
atlas stream instance download
```

### Examples

```
  # Download the audit log file from the instance myProcessor for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas streams instance download myProcessor --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
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

### See Also


* [atlas streams instances](atlas_streams_instances.md)	- Manage Atlas Stream Processing instances.



