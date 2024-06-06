## atlas config init

Configure a profile to store access settings for your MongoDB deployment.



```

atlas config init [flags]
```

### Examples

```
  # To configure the tool to work with Atlas:
  atlas config init

  # To configure the tool to work with Atlas for Government:
  atlas config init --gov
```


### Flags

```
      --gov    Create a default profile for atlas for gov
  -h, --help   help for init

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas config](atlas_config.md)	- Configure and manage your user profiles.



