## atlas federatedAuthentication federationSettings describe

Return the Federation Settings details for the specified organization.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.


### Usage
```
atlas federatedAuthentication federationSettings describe [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings describe
atlas federatedAuthentication federationSettings get
atlas federatedAuthentication federationsettings describe
atlas federatedAuthentication federationsettings get
atlas federatedAuthentication federation-settings describe
atlas federatedAuthentication federation-settings get
atlas federatedAuthentication federationSetting describe
atlas federatedAuthentication federationSetting get
atlas federatedAuthentication federationsetting describe
atlas federatedAuthentication federationsetting get
atlas federatedAuthentication federation-setting describe
atlas federatedAuthentication federation-setting get
atlas federatedauthentication federationSettings describe
atlas federatedauthentication federationSettings get
atlas federatedauthentication federationsettings describe
atlas federatedauthentication federationsettings get
atlas federatedauthentication federation-settings describe
atlas federatedauthentication federation-settings get
atlas federatedauthentication federationSetting describe
atlas federatedauthentication federationSetting get
atlas federatedauthentication federationsetting describe
atlas federatedauthentication federationsetting get
atlas federatedauthentication federation-setting describe
atlas federatedauthentication federation-setting get
atlas federated-authentication federationSettings describe
atlas federated-authentication federationSettings get
atlas federated-authentication federationsettings describe
atlas federated-authentication federationsettings get
atlas federated-authentication federation-settings describe
atlas federated-authentication federation-settings get
atlas federated-authentication federationSetting describe
atlas federated-authentication federationSetting get
atlas federated-authentication federationsetting describe
atlas federated-authentication federationsetting get
atlas federated-authentication federation-setting describe
atlas federated-authentication federation-setting get
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

### See Also


* [atlas federatedAuthentication federationSettings](atlas_federatedAuthentication_federationSettings.md)	- Manage Atlas Federated Authentication Federation Settings



