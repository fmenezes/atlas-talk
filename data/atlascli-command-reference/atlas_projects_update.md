## atlas projects update

Update a project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas projects update <ID> [flags]
```

### Aliases
```

atlas projects update
atlas project update
```

### Examples

```
  # Update a project with the ID 5e2211c17a3e5a48f5497de3 using the JSON file named myProject.json:
  atlas projects update 5f4007f327a3bd7b6f4103c5 --file myProject.json --output json
```


### Flags

```
  -f, --file string     Path to the JSON configuration file that defines project configuration settings. To learn more about project configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/project-config-file.
  -h, --help            help for update
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects](atlas_projects.md)	- Manage your Atlas projects.



