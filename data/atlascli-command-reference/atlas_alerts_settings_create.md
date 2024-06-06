## atlas alerts settings create

Create an alert configuration for your project.


### Synopsis

To use this command, you must authenticate with a user account or an API key with the Project Owner role.


### Usage
```
atlas alerts settings create [flags]
```

### Aliases
```

atlas alerts settings create
atlas alerts config create
atlas alert settings create
atlas alert config create
```

### Examples

```
  # Create an alert configuration that notifies a user when they join a group for the project with the ID 5df90590f10fab5e33de2305:
  atlas alerts settings create --event JOINED_GROUP --enabled \
  --notificationType USER --notificationEmailEnabled \
  --notificationIntervalMin 60 --notificationUsername john@example.com \
  --output json --projectId 5df90590f10fab5e33de2305
  # Create alert using json file containing alert configuration
  atlas alerts settings create 5d1113b25a115342acc2d1aa --file alerts.json
```


### Flags

```
      --apiKey string                            Datadog API Key, Opsgenie API Key, or VictorOps API key. Required if the notificationType is DATADOG, OPS_GENIE, or VICTOR_OPS, respectively.
      --enabled                                  Flag that indicates whether to enable the alert configuration.
      --event string                             Type of event that triggered the alert. To learn which values the CLI accepts, see the Enum for eventTypeName in the Atlas Admin API spec: https://dochub.mongodb.org/core/atlas-event-names.
  -f, --file string                              Path to the JSON configuration file that defines alert configuration settings. To learn more about alert configuration files for the Atlas CLI, see https://dochub.mongodb.org/core/alert-config-atlas-cli.
  -h, --help                                     help for create
      --matcherFieldName string                  Name of the field in the target object to match on. To learn the valid values, run atlas alerts settings fields type.
      --matcherOperator string                   Comparison operator to apply when checking the current metric against matcherValue. Valid values are CONTAINS, ENDS_WITH, EQUALS, NOT_CONTAINS, NOT_EQUALS, REGEX, STARTS_WITH.
      --matcherValue string                      Value to test with the specified operator. If matcherFieldName is set to TYPE_NAME, you can match on the following values: CONFIG, MONGOS, PRIMARY, SECONDARY, STANDALONE.
      --metricMode string                        Option that indicates whether Atlas computes the current metric value as an average. Valid value is AVERAGE.
      --metricName string                        Name of the metric against which this command checks the configured alert. To learn the valid values, see https://dochub.mongodb.org/core/alert-host-metrics-atlas. This option applies only if the event is set to OUTSIDE_METRIC_THRESHOLD.
      --metricOperator string                    Comparison operator to apply when checking the current metric value. Valid values are LESS_THAN and GREATER_THAN.
      --metricThreshold float                    Threshold value outside of which an alert will be triggered.
      --metricUnits string                       Units for the threshold value. Valid values are BITS, BYTES, DAYS, GIGABITS, GIGABYTES, HOURS, KILOBITS, KILOBYTES, MEGABITS, MEGABYTES, MILLISECONDS, MINUTES, PETABYTES, RAW, SECONDS, TERABYTES.
      --notificationChannelName string           Slack channel name. Required for the SLACK notifications type.
      --notificationDelayMin int                 Number of minutes to wait after an alert condition is detected before sending out the first notification.
      --notificationEmailAddress string          Email address to which alert notifications are sent.
      --notificationEmailEnabled                 Flag that enables email notifications. Configurable for GROUP and USER notification types.
      --notificationIntervalMin int              Number of minutes to wait between successive notifications for unacknowledged alerts that are not resolved.
      --notificationMobileNumber string          Mobile number to which alert notifications are sent.
      --notificationRegion string                Region that indicates which API URL to use.
      --notificationRole strings                 List that contains the one or more organization or project roles that receive the configured alert.
      --notificationServiceKey string            PagerDuty service key.
      --notificationSmsEnabled                   Flag that enables text message notifications.
      --notificationTeamId string                Unique identifier of a team.
      --notificationToken string                 Slack API token, or Bot token.
      --notificationType string                  Type of alert notification. Valid values are DATADOG, EMAIL, GROUP (Project), MICROSOFT_TEAMS, ORG, OPS_GENIE, PAGER_DUTY, SLACK, SMS, TEAM, USER, VICTOR_OPS, or WEBHOOK.
      --notificationUsername string              Name of the Atlas user to which to send notifications.
      --notificationVictorOpsRoutingKey string   Routing key associated with your Splunk On-Call account.
      --notificationWebhookSecret string         Authentication secret for a webhook-based alert.
      --notificationWebhookUrl string            Target URL for a webhook-based alert or Microsoft Teams alert.
  -o, --output string                            Output format. Valid values are json, json-path, go-template, or go-template-file. To see the full output, use the -o json option.
      --projectId string                         Hexadecimal string that identifies the project to use. This option overrides the settings in the configuration file or environment variable.

```


### Flags inherited from parent commands

```
  -P, --profile string   Name of the profile to use from your configuration file. To learn about profiles for the Atlas CLI, see https://dochub.mongodb.org/core/atlas-cli-save-connection-settings.

```

### See Also


* [atlas alerts settings](atlas_alerts_settings.md)	- Manages alerts configuration for your project.



