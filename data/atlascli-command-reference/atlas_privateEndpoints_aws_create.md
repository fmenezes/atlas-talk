## atlas privateEndpoints aws create

Create a new AWS private endpoint for your project.


### Synopsis

To learn more about how to set up private endpoints with the Atlas CLI, see the tutorial on the Atlas CLI tab here: https://www.mongodb.com/docs/atlas/security-cluster-private-endpoint/.

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas privateEndpoints aws create [flags]
atlas privateendpoints aws create [flags]
atlas private-endpoints aws create [flags]
atlas privateEndpoint aws create [flags]
atlas privateendpoint aws create [flags]
atlas private-endpoint aws create [flags]
```

### Examples

```
  # Create a private endpoint connection for AWS in the us-east-1 region for the project with the ID 5e2211c17a3e5a48f5497de3:
  atlas privateEndpoints aws create --region us-east-1 --projectId 5e2211c17a3e5a48f5497de3 --output json
```


### Flags

```
  -h, --help               help for create
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --region string      Cloud provider region in which you want to create the private endpoint connection. For a complete list of supported AWS regions, see: https://dochub.mongodb.org/core/aws-atlas. For a complete list of supported Azure regions, see: https://dochub.mongodb.org/core/azure-atlas. For a complete list of supported GCP regions, see: https://dochub.mongodb.org/core/gcp-atlas.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas privateEndpoints aws](atlas_privateEndpoints_aws.md)	- Manage AWS Private Endpoints.



