## atlas config list

Return a list of available profiles by name.


### Synopsis

If you did not specify a name for your profile, it displays as the default profile.



```

atlas config list [flags]
atlas config ls [flags]
```

### Examples

```
  atlas config ls
```


### Flags

```
  -h, --help            help for list
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas config](atlas_config.md)	- Configure and manage your user profiles.



