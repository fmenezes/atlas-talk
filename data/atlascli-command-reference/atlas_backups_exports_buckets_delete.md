## atlas backups exports buckets delete

Delete a snapshot export bucket.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas backups exports buckets delete [flags]
```

### Aliases
```

atlas backups exports buckets delete
atlas backups exports buckets rm
atlas backups exports bucket delete
atlas backups exports bucket rm
atlas backups export buckets delete
atlas backups export buckets rm
atlas backups export bucket delete
atlas backups export bucket rm
atlas backup exports buckets delete
atlas backup exports buckets rm
atlas backup exports bucket delete
atlas backup exports bucket rm
atlas backup export buckets delete
atlas backup export buckets rm
atlas backup export bucket delete
atlas backup export bucket rm
```

### Examples

```
  # The following deletes the continuous backup export bucket specified by ID:
  atlas backup exports buckets delete --bucketId dbdb00ca12345678f901a234
```


### Flags

```
      --bucketId string    Unique identifier that Atlas assigns to the bucket.
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups exports buckets](atlas_backups_exports_buckets.md)	- Manage cloud backup export buckets for your project.



