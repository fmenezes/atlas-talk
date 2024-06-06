## atlas federatedAuthentication federationSettings identityProvider describe

Describe the specified identity provider from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.



```

atlas federatedAuthentication federationSettings identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identity-provider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identity-provider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identity-provider describe <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identity-provider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identity-provider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityProvider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityprovider describe <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federationSettings identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federationsettings identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federation-settings identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federationSetting identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federationsetting identity-provider describe <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityProvider describe <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityprovider describe <identityProviderId> [flags]
atlas federatedauthentication federation-setting identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federationSettings identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federationSettings identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federationSettings identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federationsettings identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federationsettings identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federationsettings identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federation-settings identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federation-settings identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federation-settings identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federationSetting identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federationSetting identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federationSetting identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federationsetting identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federationsetting identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federationsetting identity-provider describe <identityProviderId> [flags]
atlas federated-authentication federation-setting identityProvider describe <identityProviderId> [flags]
atlas federated-authentication federation-setting identityprovider describe <identityProviderId> [flags]
atlas federated-authentication federation-setting identity-provider describe <identityProviderId> [flags]
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

### SEE ALSO


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



