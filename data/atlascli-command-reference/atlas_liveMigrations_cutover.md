## atlas liveMigrations cutover

Start the cutover for a push live migration and confirm when the cutover completes. When the cutover completes, the application completes the live migration process and stops synchronizing with the source cluster.


### Synopsis

To migrate using scripts, use mongomirror instead of the Atlas CLI. To learn more about mongomirror, see https://www.mongodb.com/docs/atlas/reference/mongomirror/.


### Usage
```
atlas liveMigrations cutover [flags]
```

### Aliases
```

atlas liveMigrations cutover
atlas livemigrations cutover
atlas live-migrations cutover
atlas liveMigration cutover
atlas livemigration cutover
atlas live-migration cutover
atlas lm cutover
```



### Flags

```
  -h, --help                     help for cutover
      --liveMigrationId string   Unique 24-hexadecimal digit string that identifies the live migration job.
  -o, --output string            Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string         Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas liveMigrations](atlas_liveMigrations.md)	- Manage a Live Migration to Atlas for your organization.



