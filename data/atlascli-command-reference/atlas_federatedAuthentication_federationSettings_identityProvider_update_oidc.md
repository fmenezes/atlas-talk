## atlas federatedAuthentication federationSettings identityProvider update oidc

Update an OIDC identity provider.


### Usage
```
atlas federatedAuthentication federationSettings identityProvider update oidc <identityProviderId> [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings identityProvider update oidc
atlas federatedAuthentication federationSettings identityprovider update oidc
atlas federatedAuthentication federationSettings identity-provider update oidc
atlas federatedAuthentication federationsettings identityProvider update oidc
atlas federatedAuthentication federationsettings identityprovider update oidc
atlas federatedAuthentication federationsettings identity-provider update oidc
atlas federatedAuthentication federation-settings identityProvider update oidc
atlas federatedAuthentication federation-settings identityprovider update oidc
atlas federatedAuthentication federation-settings identity-provider update oidc
atlas federatedAuthentication federationSetting identityProvider update oidc
atlas federatedAuthentication federationSetting identityprovider update oidc
atlas federatedAuthentication federationSetting identity-provider update oidc
atlas federatedAuthentication federationsetting identityProvider update oidc
atlas federatedAuthentication federationsetting identityprovider update oidc
atlas federatedAuthentication federationsetting identity-provider update oidc
atlas federatedAuthentication federation-setting identityProvider update oidc
atlas federatedAuthentication federation-setting identityprovider update oidc
atlas federatedAuthentication federation-setting identity-provider update oidc
atlas federatedauthentication federationSettings identityProvider update oidc
atlas federatedauthentication federationSettings identityprovider update oidc
atlas federatedauthentication federationSettings identity-provider update oidc
atlas federatedauthentication federationsettings identityProvider update oidc
atlas federatedauthentication federationsettings identityprovider update oidc
atlas federatedauthentication federationsettings identity-provider update oidc
atlas federatedauthentication federation-settings identityProvider update oidc
atlas federatedauthentication federation-settings identityprovider update oidc
atlas federatedauthentication federation-settings identity-provider update oidc
atlas federatedauthentication federationSetting identityProvider update oidc
atlas federatedauthentication federationSetting identityprovider update oidc
atlas federatedauthentication federationSetting identity-provider update oidc
atlas federatedauthentication federationsetting identityProvider update oidc
atlas federatedauthentication federationsetting identityprovider update oidc
atlas federatedauthentication federationsetting identity-provider update oidc
atlas federatedauthentication federation-setting identityProvider update oidc
atlas federatedauthentication federation-setting identityprovider update oidc
atlas federatedauthentication federation-setting identity-provider update oidc
atlas federated-authentication federationSettings identityProvider update oidc
atlas federated-authentication federationSettings identityprovider update oidc
atlas federated-authentication federationSettings identity-provider update oidc
atlas federated-authentication federationsettings identityProvider update oidc
atlas federated-authentication federationsettings identityprovider update oidc
atlas federated-authentication federationsettings identity-provider update oidc
atlas federated-authentication federation-settings identityProvider update oidc
atlas federated-authentication federation-settings identityprovider update oidc
atlas federated-authentication federation-settings identity-provider update oidc
atlas federated-authentication federationSetting identityProvider update oidc
atlas federated-authentication federationSetting identityprovider update oidc
atlas federated-authentication federationSetting identity-provider update oidc
atlas federated-authentication federationsetting identityProvider update oidc
atlas federated-authentication federationsetting identityprovider update oidc
atlas federated-authentication federationsetting identity-provider update oidc
atlas federated-authentication federation-setting identityProvider update oidc
atlas federated-authentication federation-setting identityprovider update oidc
atlas federated-authentication federation-setting identity-provider update oidc
```

### Examples

```
  # Update the audience for the specified identity provider from your federation settings with ID 5d1113b25a115342acc2d1aa, federationSettingsId 5d1113b25a115342acc2d1aa and IdpType WORKFORCE
			atlas federatedAuthentication identityProvider update 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa --idpType WORKFORCE --audience newAudience
		
```


### Flags

```
      --associatedDomain strings      List of domains associated with the Identity Provider.
      --audience string               Identifier of the intended recipient of the token.
      --authorizationType string      Type of authorization. Valid values are NONE, JWT, or SAML.
      --clientId string               Client identifier that is assigned to an application by the Identity Provider.	
      --desc string                   Description of the Identity Provider.
      --federationSettingsId string   Unique identifier of the federation settings.
      --groupsClaim string            Identifier of the claim which contains IdP Group IDs in the token.
  -h, --help                          help for oidc
      --idpType string                Type of Identity Provider. Valid values are WORKFORCE or WORKLOAD.
      --issuerUri string              Unique string that identifies the issuer of the OIDC metadata/discovery document URL.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --requestedScope strings        Scopes that MongoDB applications will request from the authorization endpoint.	
      --userClaim string              Identifier of the claim which contains the user ID in the token.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas federatedAuthentication federationSettings identityProvider update](atlas_federatedAuthentication_federationSettings_identityProvider_update.md)	- Update Federated Authentication Identity Providers.



