## atlas maintenanceWindows clear

Clear the current maintenance window setting for your project.


### Synopsis

To learn more about maintenance windows, see https://www.mongodb.com/docs/atlas/tutorial/cluster-maintenance-window/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas maintenanceWindows clear [flags]
```

### Aliases
```

atlas maintenanceWindows clear
atlas maintenanceWindows rm
atlas maintenanceWindows delete
atlas maintenancewindows clear
atlas maintenancewindows rm
atlas maintenancewindows delete
atlas maintenance-windows clear
atlas maintenance-windows rm
atlas maintenance-windows delete
atlas maintenanceWindow clear
atlas maintenanceWindow rm
atlas maintenanceWindow delete
atlas maintenancewindow clear
atlas maintenancewindow rm
atlas maintenancewindow delete
atlas maintenance-window clear
atlas maintenance-window rm
atlas maintenance-window delete
```

### Examples

```
  # Clear the current maintenance window for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas maintenanceWindows clear --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --force              Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help               help for clear
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas maintenanceWindows](atlas_maintenanceWindows.md)	- Manage Atlas maintenance windows.



