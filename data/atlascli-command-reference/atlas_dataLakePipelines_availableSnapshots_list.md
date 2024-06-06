## atlas dataLakePipelines availableSnapshots list

Return all available backup snapshots for the specified data lake pipeline.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.



```

atlas dataLakePipelines availableSnapshots list [flags]
atlas dataLakePipelines availableSnapshots ls [flags]
atlas dataLakePipelines availablesnapshots list [flags]
atlas dataLakePipelines availablesnapshots ls [flags]
atlas dataLakePipelines available-snapshots list [flags]
atlas dataLakePipelines available-snapshots ls [flags]
atlas dataLakePipelines availableSnapshot list [flags]
atlas dataLakePipelines availableSnapshot ls [flags]
atlas dataLakePipelines availablesnapshot list [flags]
atlas dataLakePipelines availablesnapshot ls [flags]
atlas dataLakePipelines available-snapshot list [flags]
atlas dataLakePipelines available-snapshot ls [flags]
atlas datalakepipelines availableSnapshots list [flags]
atlas datalakepipelines availableSnapshots ls [flags]
atlas datalakepipelines availablesnapshots list [flags]
atlas datalakepipelines availablesnapshots ls [flags]
atlas datalakepipelines available-snapshots list [flags]
atlas datalakepipelines available-snapshots ls [flags]
atlas datalakepipelines availableSnapshot list [flags]
atlas datalakepipelines availableSnapshot ls [flags]
atlas datalakepipelines availablesnapshot list [flags]
atlas datalakepipelines availablesnapshot ls [flags]
atlas datalakepipelines available-snapshot list [flags]
atlas datalakepipelines available-snapshot ls [flags]
atlas data-lake-pipelines availableSnapshots list [flags]
atlas data-lake-pipelines availableSnapshots ls [flags]
atlas data-lake-pipelines availablesnapshots list [flags]
atlas data-lake-pipelines availablesnapshots ls [flags]
atlas data-lake-pipelines available-snapshots list [flags]
atlas data-lake-pipelines available-snapshots ls [flags]
atlas data-lake-pipelines availableSnapshot list [flags]
atlas data-lake-pipelines availableSnapshot ls [flags]
atlas data-lake-pipelines availablesnapshot list [flags]
atlas data-lake-pipelines availablesnapshot ls [flags]
atlas data-lake-pipelines available-snapshot list [flags]
atlas data-lake-pipelines available-snapshot ls [flags]
atlas dataLakePipeline availableSnapshots list [flags]
atlas dataLakePipeline availableSnapshots ls [flags]
atlas dataLakePipeline availablesnapshots list [flags]
atlas dataLakePipeline availablesnapshots ls [flags]
atlas dataLakePipeline available-snapshots list [flags]
atlas dataLakePipeline available-snapshots ls [flags]
atlas dataLakePipeline availableSnapshot list [flags]
atlas dataLakePipeline availableSnapshot ls [flags]
atlas dataLakePipeline availablesnapshot list [flags]
atlas dataLakePipeline availablesnapshot ls [flags]
atlas dataLakePipeline available-snapshot list [flags]
atlas dataLakePipeline available-snapshot ls [flags]
atlas datalakepipeline availableSnapshots list [flags]
atlas datalakepipeline availableSnapshots ls [flags]
atlas datalakepipeline availablesnapshots list [flags]
atlas datalakepipeline availablesnapshots ls [flags]
atlas datalakepipeline available-snapshots list [flags]
atlas datalakepipeline available-snapshots ls [flags]
atlas datalakepipeline availableSnapshot list [flags]
atlas datalakepipeline availableSnapshot ls [flags]
atlas datalakepipeline availablesnapshot list [flags]
atlas datalakepipeline availablesnapshot ls [flags]
atlas datalakepipeline available-snapshot list [flags]
atlas datalakepipeline available-snapshot ls [flags]
atlas data-lake-pipeline availableSnapshots list [flags]
atlas data-lake-pipeline availableSnapshots ls [flags]
atlas data-lake-pipeline availablesnapshots list [flags]
atlas data-lake-pipeline availablesnapshots ls [flags]
atlas data-lake-pipeline available-snapshots list [flags]
atlas data-lake-pipeline available-snapshots ls [flags]
atlas data-lake-pipeline availableSnapshot list [flags]
atlas data-lake-pipeline availableSnapshot ls [flags]
atlas data-lake-pipeline availablesnapshot list [flags]
atlas data-lake-pipeline availablesnapshot ls [flags]
atlas data-lake-pipeline available-snapshot list [flags]
atlas data-lake-pipeline available-snapshot ls [flags]
```

### Examples

```
# list available backup schedules for data lake pipeline called 'Pipeline1':
  atlas dataLakePipelines availableSnapshots list Pipeline1

```


### Flags

```
      --completedAfter string   Date filter for when the backup snapshots were completed. You must use the YYYY-MM-DD format.
  -h, --help                    help for list
      --limit int               Number of items per results page, up to a maximum of 500. If you have more than 500 results, specify the --page option to change the results page. (default 100)
      --omitCount               Flag that indicates whether the JSON response returns the total number of items (totalCount) in the JSON response.
  -o, --output string           Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --page int                Page number that specifies a page of results. (default 1)
      --pipeline string         Name of the Data lake pipeline.
      --projectId string        Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### SEE ALSO


* [atlas dataLakePipelines availableSnapshots](atlas_dataLakePipelines_availableSnapshots.md)	- Manage available backup snapshots for data lake pipelines.



