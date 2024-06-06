## atlas federatedAuthentication federationSettings identityProvider revokeJwk

Revoke the JWK token from the specified identity provider from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.


### Usage
```
atlas federatedAuthentication federationSettings identityProvider revokeJwk <identityProviderId> [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings identityProvider revokeJwk
atlas federatedAuthentication federationSettings identityprovider revokeJwk
atlas federatedAuthentication federationSettings identity-provider revokeJwk
atlas federatedAuthentication federationsettings identityProvider revokeJwk
atlas federatedAuthentication federationsettings identityprovider revokeJwk
atlas federatedAuthentication federationsettings identity-provider revokeJwk
atlas federatedAuthentication federation-settings identityProvider revokeJwk
atlas federatedAuthentication federation-settings identityprovider revokeJwk
atlas federatedAuthentication federation-settings identity-provider revokeJwk
atlas federatedAuthentication federationSetting identityProvider revokeJwk
atlas federatedAuthentication federationSetting identityprovider revokeJwk
atlas federatedAuthentication federationSetting identity-provider revokeJwk
atlas federatedAuthentication federationsetting identityProvider revokeJwk
atlas federatedAuthentication federationsetting identityprovider revokeJwk
atlas federatedAuthentication federationsetting identity-provider revokeJwk
atlas federatedAuthentication federation-setting identityProvider revokeJwk
atlas federatedAuthentication federation-setting identityprovider revokeJwk
atlas federatedAuthentication federation-setting identity-provider revokeJwk
atlas federatedauthentication federationSettings identityProvider revokeJwk
atlas federatedauthentication federationSettings identityprovider revokeJwk
atlas federatedauthentication federationSettings identity-provider revokeJwk
atlas federatedauthentication federationsettings identityProvider revokeJwk
atlas federatedauthentication federationsettings identityprovider revokeJwk
atlas federatedauthentication federationsettings identity-provider revokeJwk
atlas federatedauthentication federation-settings identityProvider revokeJwk
atlas federatedauthentication federation-settings identityprovider revokeJwk
atlas federatedauthentication federation-settings identity-provider revokeJwk
atlas federatedauthentication federationSetting identityProvider revokeJwk
atlas federatedauthentication federationSetting identityprovider revokeJwk
atlas federatedauthentication federationSetting identity-provider revokeJwk
atlas federatedauthentication federationsetting identityProvider revokeJwk
atlas federatedauthentication federationsetting identityprovider revokeJwk
atlas federatedauthentication federationsetting identity-provider revokeJwk
atlas federatedauthentication federation-setting identityProvider revokeJwk
atlas federatedauthentication federation-setting identityprovider revokeJwk
atlas federatedauthentication federation-setting identity-provider revokeJwk
atlas federated-authentication federationSettings identityProvider revokeJwk
atlas federated-authentication federationSettings identityprovider revokeJwk
atlas federated-authentication federationSettings identity-provider revokeJwk
atlas federated-authentication federationsettings identityProvider revokeJwk
atlas federated-authentication federationsettings identityprovider revokeJwk
atlas federated-authentication federationsettings identity-provider revokeJwk
atlas federated-authentication federation-settings identityProvider revokeJwk
atlas federated-authentication federation-settings identityprovider revokeJwk
atlas federated-authentication federation-settings identity-provider revokeJwk
atlas federated-authentication federationSetting identityProvider revokeJwk
atlas federated-authentication federationSetting identityprovider revokeJwk
atlas federated-authentication federationSetting identity-provider revokeJwk
atlas federated-authentication federationsetting identityProvider revokeJwk
atlas federated-authentication federationsetting identityprovider revokeJwk
atlas federated-authentication federationsetting identity-provider revokeJwk
atlas federated-authentication federation-setting identityProvider revokeJwk
atlas federated-authentication federation-setting identityprovider revokeJwk
atlas federated-authentication federation-setting identity-provider revokeJwk
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

### See Also


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



