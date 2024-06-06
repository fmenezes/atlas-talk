## atlas security ldap verify status watch

Watch for an LDAP configuration request to complete.


### Synopsis

This command checks the LDAP configuration's status periodically until it reaches a SUCCESS or FAILED status. 
Once the LDAP configuration reaches the expected status, the command prints "LDAP Configuration request completed."
If you run the command in the terminal, it blocks the terminal session until the resource status succeeds or fails.
You can interrupt the command's polling at any time with CTRL-C.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security ldap verify status watch <requestId> [flags]
```

### Aliases
```

atlas security ldap verify status watch
```

### Examples

```
  atlas security ldap status watch requestIdSample
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

### See Also


* [atlas security ldap verify status](atlas_security_ldap_verify_status.md)	- Get the status of an LDAP configuration request.



