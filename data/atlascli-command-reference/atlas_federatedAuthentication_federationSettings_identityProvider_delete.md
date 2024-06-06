## atlas federatedAuthentication federationSettings identityProvider delete

Remove the specified identity provider from your federation settings.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Org Owner role.



```

atlas federatedAuthentication federationSettings identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federationSettings identity-provider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsettings identity-provider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-settings identity-provider delete <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federationSetting identity-provider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federationsetting identity-provider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityProvider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identityprovider delete <identityProviderId> [flags]
atlas federatedAuthentication federation-setting identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federationSettings identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federationSettings identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federationsettings identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federationsettings identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federation-settings identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federation-settings identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federationSetting identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federationSetting identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federationsetting identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federationsetting identity-provider delete <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityProvider delete <identityProviderId> [flags]
atlas federatedauthentication federation-setting identityprovider delete <identityProviderId> [flags]
atlas federatedauthentication federation-setting identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federationSettings identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federationSettings identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federationSettings identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federationsettings identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federationsettings identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federationsettings identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federation-settings identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federation-settings identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federation-settings identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federationSetting identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federationSetting identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federationSetting identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federationsetting identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federationsetting identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federationsetting identity-provider delete <identityProviderId> [flags]
atlas federated-authentication federation-setting identityProvider delete <identityProviderId> [flags]
atlas federated-authentication federation-setting identityprovider delete <identityProviderId> [flags]
atlas federated-authentication federation-setting identity-provider delete <identityProviderId> [flags]
```

### Examples

```
  # Delete the specified identity provider from your federation settings with ID 5d1113b25a115342acc2d1aa and federationSettingsId 5d1113b25a115342acc2d1aa.
	atlas federatedAuthentication identityProvider delete 5d1113b25a115342acc2d1aa --federationSettingsId 5d1113b25a115342acc2d1aa

```


### Flags

```
      --federationSettingsId string   Unique identifier of the federation settings.
      --force                         Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help                          help for delete
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas federatedAuthentication federationSettings identityProvider](atlas_federatedAuthentication_federationSettings_identityProvider.md)	- Manage Federated Authentication Identity Providers.



