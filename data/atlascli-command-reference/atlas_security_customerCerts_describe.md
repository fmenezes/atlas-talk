## atlas security customerCerts describe

Return the details for the current customer-managed X.509 configuration for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas security customerCerts describe [flags]
atlas security customercerts describe [flags]
atlas security customer-certs describe [flags]
atlas security customerCert describe [flags]
atlas security customercert describe [flags]
atlas security customer-cert describe [flags]
atlas security certs describe [flags]
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

### SEE ALSO


* [atlas security customerCerts](atlas_security_customerCerts.md)	- Manage customer x509 certificates for your project.



