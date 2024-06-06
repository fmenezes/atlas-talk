## atlas dataLakePipelines update

Modify the details of the specified data lake pipeline for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.



```

atlas dataLakePipelines update <pipelineName> [flags]
atlas datalakepipelines update <pipelineName> [flags]
atlas data-lake-pipelines update <pipelineName> [flags]
atlas dataLakePipeline update <pipelineName> [flags]
atlas datalakepipeline update <pipelineName> [flags]
atlas data-lake-pipeline update <pipelineName> [flags]
```

### Examples

```
# update data lake pipeline:
  atlas dataLakePipelines update Pipeline1 --sinkType CPS --sinkMetadataProvider AWS --sinkMetadataRegion us-east-1 --sinkPartitionField name:0,summary:1 --sourceType PERIODIC_CPS --sourceClusterName Cluster1 --sourceDatabaseName sample_airbnb --sourceCollectionName listingsAndReviews --sourcePolicyItemId 507f1f77bcf86cd799439011 --transform EXCLUDE:space,EXCLUDE:notes
```


### Flags

```
  -f, --file string                   Name of the JSON data lake pipeline configuration file to use.
  -h, --help                          help for update
  -o, --output string                 Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string              Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.
      --sinkMetadataProvider string   Target cloud provider for this data lake pipeline.
      --sinkMetadataRegion string     Target cloud provider region for this data lake pipeline.
      --sinkPartitionField strings    Ordered fields used to physically organize data in the destination. Passing this flag replaces preexisting data.
      --sourceClusterName string      Human-readable label that identifies the source cluster.
      --sourceCollectionName string   Human-readable label that identifies the source collection.
      --sourceDatabaseName string     Human-readable label that identifies the source database.
      --sourcePolicyItemId string     Human-readable label that identifies the policy item.
      --sourceType string             Type of ingestion source for this data lake pipeline.
      --transform strings             Fields to exclude for this data lake pipeline. Passing this flag replaces preexisting data.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataLakePipelines](atlas_dataLakePipelines.md)	- Data Lake pipelines.



