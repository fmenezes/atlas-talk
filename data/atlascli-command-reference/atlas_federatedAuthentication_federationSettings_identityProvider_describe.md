## atlas federatedAuthentication federationSettings identityProvider describe

Describe the specified identity provider from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.


### Usage
```
atlas federatedAuthentication federationSettings identityProvider describe <identityProviderId> [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings identityProvider describe
atlas federatedAuthentication federationSettings identityprovider describe
atlas federatedAuthentication federationSettings identity-provider describe
atlas federatedAuthentication federationsettings identityProvider describe
atlas federatedAuthentication federationsettings identityprovider describe
atlas federatedAuthentication federationsettings identity-provider describe
atlas federatedAuthentication federation-settings identityProvider describe
atlas federatedAuthentication federation-settings identityprovider describe
atlas federatedAuthentication federation-settings identity-provider describe
atlas federatedAuthentication federationSetting identityProvider describe
atlas federatedAuthentication federationSetting identityprovider describe
atlas federatedAuthentication federationSetting identity-provider describe
atlas federatedAuthentication federationsetting identityProvider describe
atlas federatedAuthentication federationsetting identityprovider describe
atlas federatedAuthentication federationsetting identity-provider describe
atlas federatedAuthentication federation-setting identityProvider describe
atlas federatedAuthentication federation-setting identityprovider describe
atlas federatedAuthentication federation-setting identity-provider describe
atlas federatedauthentication federationSettings identityProvider describe
atlas federatedauthentication federationSettings identityprovider describe
atlas federatedauthentication federationSettings identity-provider describe
atlas federatedauthentication federationsettings identityProvider describe
atlas federatedauthentication federationsettings identityprovider describe
atlas federatedauthentication federationsettings identity-provider describe
atlas federatedauthentication federation-settings identityProvider describe
atlas federatedauthentication federation-settings identityprovider describe
atlas federatedauthentication federation-settings identity-provider describe
atlas federatedauthentication federationSetting identityProvider describe
atlas federatedauthentication federationSetting identityprovider describe
atlas federatedauthentication federationSetting identity-provider describe
atlas federatedauthentication federationsetting identityProvider describe
atlas federatedauthentication federationsetting identityprovider describe
atlas federatedauthentication federationsetting identity-provider describe
atlas federatedauthentication federation-setting identityProvider describe
atlas federatedauthentication federation-setting identityprovider describe
atlas federatedauthentication federation-setting identity-provider describe
atlas federated-authentication federationSettings identityProvider describe
atlas federated-authentication federationSettings identityprovider describe
atlas federated-authentication federationSettings identity-provider describe
atlas federated-authentication federationsettings identityProvider describe
atlas federated-authentication federationsettings identityprovider describe
atlas federated-authentication federationsettings identity-provider describe
atlas federated-authentication federation-settings identityProvider describe
atlas federated-authentication federation-settings identityprovider describe
atlas federated-authentication federation-settings identity-provider describe
atlas federated-authentication federationSetting identityProvider describe
atlas federated-authentication federationSetting identityprovider describe
atlas federated-authentication federationSetting identity-provider describe
atlas federated-authentication federationsetting identityProvider describe
atlas federated-authentication federationsetting identityprovider describe
atlas federated-authentication federationsetting identity-provider describe
atlas federated-authentication federation-setting identityProvider describe
atlas federated-authentication federation-setting identityprovider describe
atlas federated-authentication federation-setting identity-provider describe
```

### Examples

```
  # Describe the specified identity provider from your federation settings with ID 5d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa.
	atlas federatedAuthentication identityProvider describe 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa

```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for describe
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



