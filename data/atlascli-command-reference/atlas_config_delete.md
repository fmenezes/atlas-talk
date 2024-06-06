## atlas config delete

Delete a profile.


### Usage
```
atlas config delete <name> [flags]
```

### Aliases
```

atlas config delete
atlas config rm
```

### Examples

```
  # Delete the default profile configuration:
  atlas config delete default

  # Skip the confirmation question and delete the default profile configuration:
  atlas config delete default --force
```


### Flags

```
      --force   Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help    help for delete

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas config](atlas_config.md)	- Configure and manage your user profiles.



