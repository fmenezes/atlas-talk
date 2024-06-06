## atlas projects create

Create a project in your organization.


### Synopsis

Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, and alert settings.

To use this command, you must authenticate with a user account or an API key with the Project Data Access Read/Write role.


### Usage
```
atlas projects create <projectName> [flags]
```

### Aliases
```

atlas projects create
atlas project create
```

### Examples

```
  # Create a project in the organization with the ID 5e2211c17a3e5a48f5497de3 using default alert settings:
  atlas projects create my-project --orgId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
      --govCloudRegionsOnly           Flag that designates that the project uses only the AWS GovCloud region. Use this option only for Atlas for Government projects. If unspecified, the project uses only the AWS Standard region for AWS deployments. You can't deploy clusters across AWS GovCloud and AWS Standard regions in the same project.
  -h, --help                          help for create
      --orgId string                  Organization ID to use. This option overrides the settings in the configuration file or environment variable.
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --ownerId string                Unique 24-digit string that identifies the Atlas user to be granted the Project Owner role on the specified project. If unspecified, this value defaults to the user ID of the oldest Organization Owner.
      --tag stringToString            List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the project. (default [])
      --withoutDefaultAlertSettings   Flag that creates the new project without the default alert settings enabled. This flag defaults to false. This option is useful if you create projects programmatically and want to create your own alerts instead of using the default alert settings.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas projects](atlas_projects.md)	- Manage your Atlas projects.



