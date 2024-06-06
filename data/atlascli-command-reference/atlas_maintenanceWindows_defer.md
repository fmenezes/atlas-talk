## atlas maintenanceWindows defer

Defer scheduled maintenance for your project for one week.


### Synopsis

To learn more about maintenance windows, see https://www.mongodb.com/docs/atlas/tutorial/cluster-maintenance-window/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas maintenanceWindows defer [flags]
atlas maintenancewindows defer [flags]
atlas maintenance-windows defer [flags]
atlas maintenanceWindow defer [flags]
atlas maintenancewindow defer [flags]
atlas maintenance-window defer [flags]
```

### Examples

```
  # Defer scheduled maintenance for one week for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas maintenanceWindows defer --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for defer
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas maintenanceWindows](atlas_maintenanceWindows.md)	- Manage Atlas maintenance windows.



