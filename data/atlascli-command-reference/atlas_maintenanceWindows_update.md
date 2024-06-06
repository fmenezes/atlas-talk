## atlas maintenanceWindows update

Modify the maintenance window for your project.


### Synopsis

To learn more about maintenance windows, see https://www.mongodb.com/docs/atlas/tutorial/cluster-maintenance-window/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas maintenanceWindows update [flags]
```

### Aliases
```

atlas maintenanceWindows update
atlas maintenancewindows update
atlas maintenance-windows update
atlas maintenanceWindow update
atlas maintenancewindow update
atlas maintenance-window update
```

### Examples

```
  # Update the maintenance window to midnight on Saturdays for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas maintenanceWindows update --dayOfWeek 7 --hourOfDay 0 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --dayOfWeek int      Day of the week that you want the maintenance window to start, as a 1-based integer. Use 1 for Sunday, 2 for Monday, 3 for Tuesday, 4 for Wednesday, 5 for Thursday, 6 for Friday, or 7 for Saturday.
  -h, --help               help for update
      --hourOfDay int      Hour of the day that you want the maintenance window to start according to a 24-hour clock. Use 0 for midnight and 12 for noon.
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --startASAP          Flag that starts maintenance immediately upon receiving this request. This flag resets to false after Atlas completes maintenance.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas maintenanceWindows](atlas_maintenanceWindows.md)	- Manage Atlas maintenance windows.



