## atlas logs keyProviders list

Lists all key provider configurations found in the encrypted audit log file.



```

atlas logs keyProviders list [flags]
atlas logs keyProviders ls [flags]
atlas logs keyproviders list [flags]
atlas logs keyproviders ls [flags]
atlas logs key-providers list [flags]
atlas logs key-providers ls [flags]
atlas logs keyProvider list [flags]
atlas logs keyProvider ls [flags]
atlas logs keyprovider list [flags]
atlas logs keyprovider ls [flags]
atlas logs key-provider list [flags]
atlas logs key-provider ls [flags]
atlas logs keys list [flags]
atlas logs keys ls [flags]
atlas log keyProviders list [flags]
atlas log keyProviders ls [flags]
atlas log keyproviders list [flags]
atlas log keyproviders ls [flags]
atlas log key-providers list [flags]
atlas log key-providers ls [flags]
atlas log keyProvider list [flags]
atlas log keyProvider ls [flags]
atlas log keyprovider list [flags]
atlas log keyprovider ls [flags]
atlas log key-provider list [flags]
atlas log key-provider ls [flags]
atlas log keys list [flags]
atlas log keys ls [flags]
```

### Examples

```

  mongocli ops-manager listKeyProvider --file log.gz
```


### Flags

```
  -f, --file string     Path to the file that contains encrypted audit logs.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas logs keyProviders](atlas_logs_keyProviders.md)	- Manage your key collections.



