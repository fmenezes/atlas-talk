## atlas customDbRoles update

Update a custom database role for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas customDbRoles update <roleName> [flags]
atlas customdbroles update <roleName> [flags]
atlas custom-db-roles update <roleName> [flags]
atlas customDbRole update <roleName> [flags]
atlas customdbrole update <roleName> [flags]
atlas custom-db-role update <roleName> [flags]
atlas customDBRoles update <roleName> [flags]
```



### Flags

```
      --append                  Input action and inheritedRoles to append to the existing role.
  -h, --help                    help for update
      --inheritedRole strings   List of inherited roles and the database on which the role is granted. Passing this flag replaces preexisting data.
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --privilege strings       List of actions per database and collection. If no database or collections are provided, cluster scope is assumed. For details on actions specific to clusters, databases, or collections, see https://dochub.mongodb.org/core/privilege-actions. Passing this flag replaces preexisting data.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas customDbRoles](atlas_customDbRoles.md)	- Manage custom database roles for your project.



