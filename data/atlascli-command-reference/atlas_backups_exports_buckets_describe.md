## atlas backups exports buckets describe

Return one snapshot export bucket.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas backups exports buckets describe [flags]
```

### Aliases
```

atlas backups exports buckets describe
atlas backups exports buckets get
atlas backups exports bucket describe
atlas backups exports bucket get
atlas backups export buckets describe
atlas backups export buckets get
atlas backups export bucket describe
atlas backups export bucket get
atlas backup exports buckets describe
atlas backup exports buckets get
atlas backup exports bucket describe
atlas backup exports bucket get
atlas backup export buckets describe
atlas backup export buckets get
atlas backup export bucket describe
atlas backup export bucket get
```

### Examples

```
  # Return the details for the continuous backup export bucket with the ID dbdb00ca12345678f901a234:
  atlas backup exports buckets describe dbdb00ca12345678f901a234
```


### Flags

```
      --bucketId string    Unique identifier that Atlas assigns to the bucket.
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas backups exports buckets](atlas_backups_exports_buckets.md)	- Manage cloud backup export buckets for your project.



