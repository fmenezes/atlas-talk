## atlas serverless watch

Monitor the status of serverless instance.


### Synopsis

This command checks the serverless instance's state periodically until the instance reaches an IDLE state. 
Once the instance reaches the expected state, the command prints "Instance available."
If you run the command in the terminal, it blocks the terminal session until the resource becomes idle.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas serverless watch <instanceName> [flags]
atlas sl watch <instanceName> [flags]
```

### Examples

```
  atlas serverless watch instanceNameSample
```


### Flags

```
  -h, --help               help for watch
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas serverless](atlas_serverless.md)	- Manage serverless instances for your project.



