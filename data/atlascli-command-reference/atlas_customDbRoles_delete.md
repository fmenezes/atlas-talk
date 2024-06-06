## atlas customDbRoles delete

Remove the specified custom database role from your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas customDbRoles delete <roleName> [flags]
atlas customDbRoles rm <roleName> [flags]
atlas customdbroles delete <roleName> [flags]
atlas customdbroles rm <roleName> [flags]
atlas custom-db-roles delete <roleName> [flags]
atlas custom-db-roles rm <roleName> [flags]
atlas customDbRole delete <roleName> [flags]
atlas customDbRole rm <roleName> [flags]
atlas customdbrole delete <roleName> [flags]
atlas customdbrole rm <roleName> [flags]
atlas custom-db-role delete <roleName> [flags]
atlas custom-db-role rm <roleName> [flags]
atlas customDBRoles delete <roleName> [flags]
atlas customDBRoles rm <roleName> [flags]
```



### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for delete
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas customDbRoles](atlas_customDbRoles.md)	- Manage custom database roles for your project.



