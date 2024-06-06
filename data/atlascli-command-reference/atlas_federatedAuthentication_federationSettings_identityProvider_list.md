## atlas federatedAuthentication federationSettings identityProvider list

List the identity providers from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.


### Usage
```
atlas federatedAuthentication federationSettings identityProvider list [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings identityProvider list
atlas federatedAuthentication federationSettings identityprovider list
atlas federatedAuthentication federationSettings identity-provider list
atlas federatedAuthentication federationsettings identityProvider list
atlas federatedAuthentication federationsettings identityprovider list
atlas federatedAuthentication federationsettings identity-provider list
atlas federatedAuthentication federation-settings identityProvider list
atlas federatedAuthentication federation-settings identityprovider list
atlas federatedAuthentication federation-settings identity-provider list
atlas federatedAuthentication federationSetting identityProvider list
atlas federatedAuthentication federationSetting identityprovider list
atlas federatedAuthentication federationSetting identity-provider list
atlas federatedAuthentication federationsetting identityProvider list
atlas federatedAuthentication federationsetting identityprovider list
atlas federatedAuthentication federationsetting identity-provider list
atlas federatedAuthentication federation-setting identityProvider list
atlas federatedAuthentication federation-setting identityprovider list
atlas federatedAuthentication federation-setting identity-provider list
atlas federatedauthentication federationSettings identityProvider list
atlas federatedauthentication federationSettings identityprovider list
atlas federatedauthentication federationSettings identity-provider list
atlas federatedauthentication federationsettings identityProvider list
atlas federatedauthentication federationsettings identityprovider list
atlas federatedauthentication federationsettings identity-provider list
atlas federatedauthentication federation-settings identityProvider list
atlas federatedauthentication federation-settings identityprovider list
atlas federatedauthentication federation-settings identity-provider list
atlas federatedauthentication federationSetting identityProvider list
atlas federatedauthentication federationSetting identityprovider list
atlas federatedauthentication federationSetting identity-provider list
atlas federatedauthentication federationsetting identityProvider list
atlas federatedauthentication federationsetting identityprovider list
atlas federatedauthentication federationsetting identity-provider list
atlas federatedauthentication federation-setting identityProvider list
atlas federatedauthentication federation-setting identityprovider list
atlas federatedauthentication federation-setting identity-provider list
atlas federated-authentication federationSettings identityProvider list
atlas federated-authentication federationSettings identityprovider list
atlas federated-authentication federationSettings identity-provider list
atlas federated-authentication federationsettings identityProvider list
atlas federated-authentication federationsettings identityprovider list
atlas federated-authentication federationsettings identity-provider list
atlas federated-authentication federation-settings identityProvider list
atlas federated-authentication federation-settings identityprovider list
atlas federated-authentication federation-settings identity-provider list
atlas federated-authentication federationSetting identityProvider list
atlas federated-authentication federationSetting identityprovider list
atlas federated-authentication federationSetting identity-provider list
atlas federated-authentication federationsetting identityProvider list
atlas federated-authentication federationsetting identityprovider list
atlas federated-authentication federationsetting identity-provider list
atlas federated-authentication federation-setting identityProvider list
atlas federated-authentication federation-setting identityprovider list
atlas federated-authentication federation-setting identity-provider list
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

### See Also


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



