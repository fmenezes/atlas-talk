## atlas clusters availableRegions list

List available regions that Atlas supports for new deployments.



```

atlas clusters availableRegions list [flags]
atlas clusters availableRegions ls [flags]
atlas clusters availableregions list [flags]
atlas clusters availableregions ls [flags]
atlas clusters available-regions list [flags]
atlas clusters available-regions ls [flags]
atlas clusters availableRegion list [flags]
atlas clusters availableRegion ls [flags]
atlas clusters availableregion list [flags]
atlas clusters availableregion ls [flags]
atlas clusters available-region list [flags]
atlas clusters available-region ls [flags]
atlas cluster availableRegions list [flags]
atlas cluster availableRegions ls [flags]
atlas cluster availableregions list [flags]
atlas cluster availableregions ls [flags]
atlas cluster available-regions list [flags]
atlas cluster available-regions ls [flags]
atlas cluster availableRegion list [flags]
atlas cluster availableRegion ls [flags]
atlas cluster availableregion list [flags]
atlas cluster availableregion ls [flags]
atlas cluster available-region list [flags]
atlas cluster available-region ls [flags]
```

### Examples

```
  # List available regions for a given cloud provider and tier:
  atlas cluster availableRegions list --provider AWS --tier M50

  # List available regions by tier for a given provider:
  atlas cluster availableRegions list --provider GCP
```


### Flags

```
  -h, --help               help for list
  -o, --output string      Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string   Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --provider string    Name of your cloud service provider. Valid values are AWS, AZURE, or GCP.
      --tier string        Tier for each data-bearing server in the cluster. To learn more about cluster tiers, see https://dochub.mongodb.org/core/cluster-tier-atlas.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas clusters availableRegions](atlas_clusters_availableRegions.md)	- Manage available regions for your project.



