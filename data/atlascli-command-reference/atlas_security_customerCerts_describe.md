## atlas security customerCerts describe

Return the details for the current customer-managed X.509 configuration for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas security customerCerts describe [flags]
```

### Aliases
```

atlas security customerCerts describe
atlas security customercerts describe
atlas security customer-certs describe
atlas security customerCert describe
atlas security customercert describe
atlas security customer-cert describe
atlas security certs describe
```

### Examples

```
  # Return the JSON-formatted details for the customer-managed X.509 configuration in the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas security customerCerts describe --projectId 5e2211c17a3e5a48f5497de3 --output json
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


* [atlas security customerCerts](atlas_security_customerCerts.md)	- Manage customer x509 certificates for your project.



