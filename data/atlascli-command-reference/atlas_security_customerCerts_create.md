## atlas security customerCerts create

Saves a customer-managed X.509 configuration for your project.


### Synopsis

Saving a customer-managed X.509 configuration triggers a rolling restart.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security customerCerts create [flags]
```

### Aliases
```

atlas security customerCerts create
atlas security customercerts create
atlas security customer-certs create
atlas security customerCert create
atlas security customercert create
atlas security customer-cert create
atlas security certs create
```

### Examples

```
  # Save the file named ca.pem stored in the files directory to the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security customerCerts create --casFile files/ca.pem --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --casFile string     Path to a PEM file containing one or more CAs for database user authentication.
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas security customerCerts](atlas_security_customerCerts.md)	- Manage customer x509 certificates for your project.



