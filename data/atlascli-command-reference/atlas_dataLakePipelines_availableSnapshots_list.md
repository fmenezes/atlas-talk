## atlas dataLakePipelines availableSnapshots list

Return all available backup snapshots for the specified data lake pipeline.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Read Only role.


### Usage
```
atlas dataLakePipelines availableSnapshots list [flags]
```

### Aliases
```

atlas dataLakePipelines availableSnapshots list
atlas dataLakePipelines availableSnapshots ls
atlas dataLakePipelines availablesnapshots list
atlas dataLakePipelines availablesnapshots ls
atlas dataLakePipelines available-snapshots list
atlas dataLakePipelines available-snapshots ls
atlas dataLakePipelines availableSnapshot list
atlas dataLakePipelines availableSnapshot ls
atlas dataLakePipelines availablesnapshot list
atlas dataLakePipelines availablesnapshot ls
atlas dataLakePipelines available-snapshot list
atlas dataLakePipelines available-snapshot ls
atlas datalakepipelines availableSnapshots list
atlas datalakepipelines availableSnapshots ls
atlas datalakepipelines availablesnapshots list
atlas datalakepipelines availablesnapshots ls
atlas datalakepipelines available-snapshots list
atlas datalakepipelines available-snapshots ls
atlas datalakepipelines availableSnapshot list
atlas datalakepipelines availableSnapshot ls
atlas datalakepipelines availablesnapshot list
atlas datalakepipelines availablesnapshot ls
atlas datalakepipelines available-snapshot list
atlas datalakepipelines available-snapshot ls
atlas data-lake-pipelines availableSnapshots list
atlas data-lake-pipelines availableSnapshots ls
atlas data-lake-pipelines availablesnapshots list
atlas data-lake-pipelines availablesnapshots ls
atlas data-lake-pipelines available-snapshots list
atlas data-lake-pipelines available-snapshots ls
atlas data-lake-pipelines availableSnapshot list
atlas data-lake-pipelines availableSnapshot ls
atlas data-lake-pipelines availablesnapshot list
atlas data-lake-pipelines availablesnapshot ls
atlas data-lake-pipelines available-snapshot list
atlas data-lake-pipelines available-snapshot ls
atlas dataLakePipeline availableSnapshots list
atlas dataLakePipeline availableSnapshots ls
atlas dataLakePipeline availablesnapshots list
atlas dataLakePipeline availablesnapshots ls
atlas dataLakePipeline available-snapshots list
atlas dataLakePipeline available-snapshots ls
atlas dataLakePipeline availableSnapshot list
atlas dataLakePipeline availableSnapshot ls
atlas dataLakePipeline availablesnapshot list
atlas dataLakePipeline availablesnapshot ls
atlas dataLakePipeline available-snapshot list
atlas dataLakePipeline available-snapshot ls
atlas datalakepipeline availableSnapshots list
atlas datalakepipeline availableSnapshots ls
atlas datalakepipeline availablesnapshots list
atlas datalakepipeline availablesnapshots ls
atlas datalakepipeline available-snapshots list
atlas datalakepipeline available-snapshots ls
atlas datalakepipeline availableSnapshot list
atlas datalakepipeline availableSnapshot ls
atlas datalakepipeline availablesnapshot list
atlas datalakepipeline availablesnapshot ls
atlas datalakepipeline available-snapshot list
atlas datalakepipeline available-snapshot ls
atlas data-lake-pipeline availableSnapshots list
atlas data-lake-pipeline availableSnapshots ls
atlas data-lake-pipeline availablesnapshots list
atlas data-lake-pipeline availablesnapshots ls
atlas data-lake-pipeline available-snapshots list
atlas data-lake-pipeline available-snapshots ls
atlas data-lake-pipeline availableSnapshot list
atlas data-lake-pipeline availableSnapshot ls
atlas data-lake-pipeline availablesnapshot list
atlas data-lake-pipeline availablesnapshot ls
atlas data-lake-pipeline available-snapshot list
atlas data-lake-pipeline available-snapshot ls
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

### See Also


* [atlas dataLakePipelines availableSnapshots](atlas_dataLakePipelines_availableSnapshots.md)	- Manage available backup snapshots for data lake pipelines.



