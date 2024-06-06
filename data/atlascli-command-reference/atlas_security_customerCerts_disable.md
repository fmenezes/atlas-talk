## atlas security customerCerts disable

Clear customer-managed X.509 settings on a project, including the uploaded Certificate Authority, and disable self-managed X.509.


### Synopsis

Disabling customer-managed X.509 triggers a rolling restart.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security customerCerts disable [flags]
```

### Aliases
```

atlas security customerCerts disable
atlas security customercerts disable
atlas security customer-certs disable
atlas security customerCert disable
atlas security customercert disable
atlas security customer-cert disable
atlas security certs disable
```

### Examples

```
  # Disable the customer-managed X.509 configuration in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security customerCerts disable --projectId 5e2211c17a3e5a48f5497de3
```


### Flags

```
  -h, --help               help for disable
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas security customerCerts](atlas_security_customerCerts.md)	- Manage customer x509 certificates for your project.



