## atlas dataFederation logs

Returns logs of the specified data federation database for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas dataFederation logs <name> [flags]
atlas datafederation logs <name> [flags]
atlas data-federation logs <name> [flags]
```

### Examples

```
# download logs of data federation database 'DataFederation1':
  atlas dataFederation logs DataFederation1

```


### Flags

```
      --end int            Timestamp in UNIX epoch format when the logs end.
      --force              Flag that indicates whether to overwrite the destination file.
  -h, --help               help for logs
      --out string         Output file name. This value defaults to the log name.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --start int          Timestamp in UNIX epoch format when the logs start.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataFederation](atlas_dataFederation.md)	- Data federation.



