## atlas federatedAuthentication federationSettings identityProvider list

List the identity providers from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.



```

atlas federatedAuthentication federationSettings identityProvider list [flags]
atlas federatedAuthentication federationSettings identityprovider list [flags]
atlas federatedAuthentication federationSettings identity-provider list [flags]
atlas federatedAuthentication federationsettings identityProvider list [flags]
atlas federatedAuthentication federationsettings identityprovider list [flags]
atlas federatedAuthentication federationsettings identity-provider list [flags]
atlas federatedAuthentication federation-settings identityProvider list [flags]
atlas federatedAuthentication federation-settings identityprovider list [flags]
atlas federatedAuthentication federation-settings identity-provider list [flags]
atlas federatedAuthentication federationSetting identityProvider list [flags]
atlas federatedAuthentication federationSetting identityprovider list [flags]
atlas federatedAuthentication federationSetting identity-provider list [flags]
atlas federatedAuthentication federationsetting identityProvider list [flags]
atlas federatedAuthentication federationsetting identityprovider list [flags]
atlas federatedAuthentication federationsetting identity-provider list [flags]
atlas federatedAuthentication federation-setting identityProvider list [flags]
atlas federatedAuthentication federation-setting identityprovider list [flags]
atlas federatedAuthentication federation-setting identity-provider list [flags]
atlas federatedauthentication federationSettings identityProvider list [flags]
atlas federatedauthentication federationSettings identityprovider list [flags]
atlas federatedauthentication federationSettings identity-provider list [flags]
atlas federatedauthentication federationsettings identityProvider list [flags]
atlas federatedauthentication federationsettings identityprovider list [flags]
atlas federatedauthentication federationsettings identity-provider list [flags]
atlas federatedauthentication federation-settings identityProvider list [flags]
atlas federatedauthentication federation-settings identityprovider list [flags]
atlas federatedauthentication federation-settings identity-provider list [flags]
atlas federatedauthentication federationSetting identityProvider list [flags]
atlas federatedauthentication federationSetting identityprovider list [flags]
atlas federatedauthentication federationSetting identity-provider list [flags]
atlas federatedauthentication federationsetting identityProvider list [flags]
atlas federatedauthentication federationsetting identityprovider list [flags]
atlas federatedauthentication federationsetting identity-provider list [flags]
atlas federatedauthentication federation-setting identityProvider list [flags]
atlas federatedauthentication federation-setting identityprovider list [flags]
atlas federatedauthentication federation-setting identity-provider list [flags]
atlas federated-authentication federationSettings identityProvider list [flags]
atlas federated-authentication federationSettings identityprovider list [flags]
atlas federated-authentication federationSettings identity-provider list [flags]
atlas federated-authentication federationsettings identityProvider list [flags]
atlas federated-authentication federationsettings identityprovider list [flags]
atlas federated-authentication federationsettings identity-provider list [flags]
atlas federated-authentication federation-settings identityProvider list [flags]
atlas federated-authentication federation-settings identityprovider list [flags]
atlas federated-authentication federation-settings identity-provider list [flags]
atlas federated-authentication federationSetting identityProvider list [flags]
atlas federated-authentication federationSetting identityprovider list [flags]
atlas federated-authentication federationSetting identity-provider list [flags]
atlas federated-authentication federationsetting identityProvider list [flags]
atlas federated-authentication federationsetting identityprovider list [flags]
atlas federated-authentication federationsetting identity-provider list [flags]
atlas federated-authentication federation-setting identityProvider list [flags]
atlas federated-authentication federation-setting identityprovider list [flags]
atlas federated-authentication federation-setting identity-provider list [flags]
```

### Examples

```
  # List the identity providers from your federation settings with federationSettingsId 5d1113b25a115342acc2d1aa and idpType WORKLOAD
	atlas federatedAuthentication identityProvider list --federationSettingsId 5d1113b25a115342acc2d1aa --idpType WORKLOAD

```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for list
      --idpType string                Type of Identity Provider. Valid values are WORKFORCE or WORKLOAD. (default "WORKFORCE")
      --limit int                     Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int                      Page number that specifies a page of results. (default 1)
      --protocol string               Protocol used to authenticate the user. Valid value is OIDC or SAML. (default "OIDC")

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



