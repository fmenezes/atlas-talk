## atlas liveMigrations link create

Create a new link-token for a push live migration.


### Synopsis

To migrate using scripts, use mongomirror instead of the Atlas CLI. To learn more about mongomirror, see https://www.mongodb.com/docs/atlas/reference/mongomirror/.



```

atlas liveMigrations link create [flags]
atlas livemigrations link create [flags]
atlas live-migrations link create [flags]
atlas liveMigration link create [flags]
atlas livemigration link create [flags]
atlas live-migration link create [flags]
atlas lm link create [flags]
```



### Flags

```
      --accessListIp strings   IP address access list entries that are associated with the link-token.
  -h, --help                   help for create
      --orgId string           Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string          Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas liveMigrations link](atlas_liveMigrations_link.md)	- Manage the link-token for your organization.



