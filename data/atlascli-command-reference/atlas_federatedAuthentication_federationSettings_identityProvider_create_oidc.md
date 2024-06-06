## atlas federatedAuthentication federationSettings identityProvider create oidc

Create an OIDC identity provider.


### Usage
```
atlas federatedAuthentication federationSettings identityProvider create oidc <displayName> [flags]
```

### Aliases
```

atlas federatedAuthentication federationSettings identityProvider create oidc
atlas federatedAuthentication federationSettings identityprovider create oidc
atlas federatedAuthentication federationSettings identity-provider create oidc
atlas federatedAuthentication federationsettings identityProvider create oidc
atlas federatedAuthentication federationsettings identityprovider create oidc
atlas federatedAuthentication federationsettings identity-provider create oidc
atlas federatedAuthentication federation-settings identityProvider create oidc
atlas federatedAuthentication federation-settings identityprovider create oidc
atlas federatedAuthentication federation-settings identity-provider create oidc
atlas federatedAuthentication federationSetting identityProvider create oidc
atlas federatedAuthentication federationSetting identityprovider create oidc
atlas federatedAuthentication federationSetting identity-provider create oidc
atlas federatedAuthentication federationsetting identityProvider create oidc
atlas federatedAuthentication federationsetting identityprovider create oidc
atlas federatedAuthentication federationsetting identity-provider create oidc
atlas federatedAuthentication federation-setting identityProvider create oidc
atlas federatedAuthentication federation-setting identityprovider create oidc
atlas federatedAuthentication federation-setting identity-provider create oidc
atlas federatedauthentication federationSettings identityProvider create oidc
atlas federatedauthentication federationSettings identityprovider create oidc
atlas federatedauthentication federationSettings identity-provider create oidc
atlas federatedauthentication federationsettings identityProvider create oidc
atlas federatedauthentication federationsettings identityprovider create oidc
atlas federatedauthentication federationsettings identity-provider create oidc
atlas federatedauthentication federation-settings identityProvider create oidc
atlas federatedauthentication federation-settings identityprovider create oidc
atlas federatedauthentication federation-settings identity-provider create oidc
atlas federatedauthentication federationSetting identityProvider create oidc
atlas federatedauthentication federationSetting identityprovider create oidc
atlas federatedauthentication federationSetting identity-provider create oidc
atlas federatedauthentication federationsetting identityProvider create oidc
atlas federatedauthentication federationsetting identityprovider create oidc
atlas federatedauthentication federationsetting identity-provider create oidc
atlas federatedauthentication federation-setting identityProvider create oidc
atlas federatedauthentication federation-setting identityprovider create oidc
atlas federatedauthentication federation-setting identity-provider create oidc
atlas federated-authentication federationSettings identityProvider create oidc
atlas federated-authentication federationSettings identityprovider create oidc
atlas federated-authentication federationSettings identity-provider create oidc
atlas federated-authentication federationsettings identityProvider create oidc
atlas federated-authentication federationsettings identityprovider create oidc
atlas federated-authentication federationsettings identity-provider create oidc
atlas federated-authentication federation-settings identityProvider create oidc
atlas federated-authentication federation-settings identityprovider create oidc
atlas federated-authentication federation-settings identity-provider create oidc
atlas federated-authentication federationSetting identityProvider create oidc
atlas federated-authentication federationSetting identityprovider create oidc
atlas federated-authentication federationSetting identity-provider create oidc
atlas federated-authentication federationsetting identityProvider create oidc
atlas federated-authentication federationsetting identityprovider create oidc
atlas federated-authentication federationsetting identity-provider create oidc
atlas federated-authentication federation-setting identityProvider create oidc
atlas federated-authentication federation-setting identityprovider create oidc
atlas federated-authentication federation-setting identity-provider create oidc
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


* [atlas federatedAuthentication federationSettings identityProvider create](atlas_federatedAuthentication_federationSettings_identityProvider_create.md)	- Create Federated Authentication Identity Providers.



