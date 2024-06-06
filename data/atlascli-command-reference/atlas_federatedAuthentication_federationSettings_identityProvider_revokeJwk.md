## atlas federatedAuthentication federationSettings identityProvider revokeJwk

Revoke the JWK token from the specified identity provider from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.



```

atlas federatedAuthentication federationSettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-settings identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationSetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federationsetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityProvider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityprovider revokeJwk <identityProviderId> [flags]
atlas federatedauthentication federation-setting identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsettings identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsettings identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsettings identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-settings identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-settings identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-settings identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationSetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsetting identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsetting identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federationsetting identity-provider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-setting identityProvider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-setting identityprovider revokeJwk <identityProviderId> [flags]
atlas federated-authentication federation-setting identity-provider revokeJwk <identityProviderId> [flags]
```

### Examples

```
  # Revoke the Jwk from the specified identity provider from your federation settings with ID 5d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa.
	atlas federatedAuthentication identityProvider revokeJwk 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa

```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
  -h, --help                          help for revokeJwk
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



