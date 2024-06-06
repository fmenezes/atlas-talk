## atlas logs keyProviders list

Lists all key provider configurations found in the encrypted audit log file.


### Usage
```
atlas logs keyProviders list [flags]
```

### Aliases
```

atlas logs keyProviders list
atlas logs keyProviders ls
atlas logs keyproviders list
atlas logs keyproviders ls
atlas logs key-providers list
atlas logs key-providers ls
atlas logs keyProvider list
atlas logs keyProvider ls
atlas logs keyprovider list
atlas logs keyprovider ls
atlas logs key-provider list
atlas logs key-provider ls
atlas logs keys list
atlas logs keys ls
atlas log keyProviders list
atlas log keyProviders ls
atlas log keyproviders list
atlas log keyproviders ls
atlas log key-providers list
atlas log key-providers ls
atlas log keyProvider list
atlas log keyProvider ls
atlas log keyprovider list
atlas log keyprovider ls
atlas log key-provider list
atlas log key-provider ls
atlas log keys list
atlas log keys ls
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

### See Also


* [atlas logs keyProviders](atlas_logs_keyProviders.md)	- Manage your key collections.



