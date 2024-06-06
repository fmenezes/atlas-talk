## atlas organizations delete

Remove the specified organization.


### Synopsis

Organizations with active projects can't be removed.

To use this command, you must authenticate with a user account or an API key with the Organization Owner role.



```

atlas organizations delete <ID> [flags]
atlas organizations rm <ID> [flags]
atlas organization delete <ID> [flags]
atlas organization rm <ID> [flags]
atlas orgs delete <ID> [flags]
atlas orgs rm <ID> [flags]
atlas org delete <ID> [flags]
atlas org rm <ID> [flags]
```

### Examples

```
  # Remove the organization with the ID 5e2211c17a3e5a48f5497de3:
  atlas organizations delete 5e2211c17a3e5a48f5497de3
```


### Flags

```
      --force   Flag that indicates whether to skip the confirmation prompt before proceeding with the requested action.
  -h, --help    help for delete

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas organizations](atlas_organizations.md)	- Manage your Atlas organizations.



