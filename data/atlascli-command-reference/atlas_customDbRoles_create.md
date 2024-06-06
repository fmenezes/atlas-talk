## atlas customDbRoles create

Create a custom database role for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas customDbRoles create <roleName> [flags]
```

### Aliases
```

atlas customDbRoles create
atlas customdbroles create
atlas custom-db-roles create
atlas customDbRole create
atlas customdbrole create
atlas custom-db-role create
atlas customDBRoles create
```

### Examples

```
# Create a custom database role
  atlas customDbRoles create customRole --privilege FIND@databaseName,UPDATE@databaseName.collectionName

  # Create a custom database role on multiple collections
  atlas customDbRoles create customRole --privilege FIND@databaseName,UPDATE@databaseName.firstCollectionName,UPDATE@databaseName.secondCollectionName

  # Create a customer database role with granted action on the cluster resource
  atlas customDbRoles create customRole --privilege GET_CMD_LINE_OPTS

  # Use an inherited role
  atlas customDbRoles create customRole --inheritedRole read@databaseName
```


### Flags

```
  -h, --help                    help for create
      --inheritedRole strings   List of inherited roles and the database on which the role is granted.
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --privilege strings       List of actions per database and collection. If no database or collections are provided, cluster scope is assumed. For details on actions specific to clusters, databases, or collections, see https://dochub.mongodb.org/core/privilege-actions.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas customDbRoles](atlas_customDbRoles.md)	- Manage custom database roles for your project.



