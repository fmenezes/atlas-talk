## atlas federatedAuthentication federationSettings describe

Return the Federation Settings details for the specified organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.



```

atlas federatedAuthentication federationSettings describe [flags]
atlas federatedAuthentication federationSettings get [flags]
atlas federatedAuthentication federationsettings describe [flags]
atlas federatedAuthentication federationsettings get [flags]
atlas federatedAuthentication federation-settings describe [flags]
atlas federatedAuthentication federation-settings get [flags]
atlas federatedAuthentication federationSetting describe [flags]
atlas federatedAuthentication federationSetting get [flags]
atlas federatedAuthentication federationsetting describe [flags]
atlas federatedAuthentication federationsetting get [flags]
atlas federatedAuthentication federation-setting describe [flags]
atlas federatedAuthentication federation-setting get [flags]
atlas federatedauthentication federationSettings describe [flags]
atlas federatedauthentication federationSettings get [flags]
atlas federatedauthentication federationsettings describe [flags]
atlas federatedauthentication federationsettings get [flags]
atlas federatedauthentication federation-settings describe [flags]
atlas federatedauthentication federation-settings get [flags]
atlas federatedauthentication federationSetting describe [flags]
atlas federatedauthentication federationSetting get [flags]
atlas federatedauthentication federationsetting describe [flags]
atlas federatedauthentication federationsetting get [flags]
atlas federatedauthentication federation-setting describe [flags]
atlas federatedauthentication federation-setting get [flags]
atlas federated-authentication federationSettings describe [flags]
atlas federated-authentication federationSettings get [flags]
atlas federated-authentication federationsettings describe [flags]
atlas federated-authentication federationsettings get [flags]
atlas federated-authentication federation-settings describe [flags]
atlas federated-authentication federation-settings get [flags]
atlas federated-authentication federationSetting describe [flags]
atlas federated-authentication federationSetting get [flags]
atlas federated-authentication federationsetting describe [flags]
atlas federated-authentication federationsetting get [flags]
atlas federated-authentication federation-setting describe [flags]
atlas federated-authentication federation-setting get [flags]
```

### Examples

```
  # Return the JSON-formatted Federation Settings details:
  atlas federatedAuthentication federationSettings describe --orgId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help            help for describe
      --orgId string    Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string   Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas federatedAuthentication federationSettings](atlas_federatedAuthentication_federationSettings.md)	- Manage Atlas Federated Authentication Federation Settings



