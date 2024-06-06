## atlas maintenanceWindows describe

Return the maintenance window details for your project.


### Synopsis

To learn more about maintenance windows, see https://www.mongodb.com/docs/atlas/tutorial/cluster-maintenance-window/.

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas maintenanceWindows describe [flags]
```

### Aliases
```

atlas maintenanceWindows describe
atlas maintenanceWindows get
atlas maintenancewindows describe
atlas maintenancewindows get
atlas maintenance-windows describe
atlas maintenance-windows get
atlas maintenanceWindow describe
atlas maintenanceWindow get
atlas maintenancewindow describe
atlas maintenancewindow get
atlas maintenance-window describe
atlas maintenance-window get
```

### Examples

```
  # Return the maintenance window for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas maintenanceWindows describe --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for describe
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas maintenanceWindows](atlas_maintenanceWindows.md)	- Manage Atlas maintenance windows.



