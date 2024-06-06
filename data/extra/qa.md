# Questions and Answers

Q: Which command creates clusters?
A: To create clusters you can use `atlas clusters create`

Q: How to get stared?
A: To get started use `atlas setup`

Q: How to create a local cluster / local dev environment?
A: You can use `atlas deployments setup --type LOCAL`

Q: Where can I find atlas cli documentation and manuals?
A: Use `atlas --help` or `atlas <command> --help` or navigate to https://www.mongodb.com/docs/atlas/cli/stable/

Q: How to set clusters via json file?
A: you can use `atlas clusters create --file <path/to/file.json>` the schema is explained by the following partial open api spec. The Json should be an instance of the schema `AdvancedClusterDescription`.
```
components:
  schemas:
    AdvancedAutoScalingSettings:
      type: object
      description: Options that determine how this cluster handles resource scaling.
      properties:
        compute:
          $ref: '#/components/schemas/AdvancedComputeAutoScaling'
        diskGB:
          $ref: '#/components/schemas/DiskGBAutoScaling'
      title: Automatic Scaling Settings
    AdvancedClusterDescription:
      type: object
      properties:
        acceptDataRisksAndForceReplicaSetReconfig:
          type: string
          format: date-time
          description: If reconfiguration is necessary to regain a primary due to a regional outage, submit this field alongside your topology reconfiguration to request a new regional outage resistant topology. Forced reconfigurations during an outage of the majority of electable nodes carry a risk of data loss if replicated writes (even majority committed writes) have not been replicated to the new primary node. MongoDB Atlas docs contain more information. To proceed with an operation which carries that risk, set **acceptDataRisksAndForceReplicaSetReconfig** to the current date.
          externalDocs:
            description: Reconfiguring a Replica Set during a regional outage
            url: https://dochub.mongodb.org/core/regional-outage-reconfigure-replica-set
        backupEnabled:
          type: boolean
          default: false
          description: Flag that indicates whether the cluster can perform backups. If set to `true`, the cluster can perform backups. You must set this value to `true` for NVMe clusters. Backup uses [Cloud Backups](https://docs.atlas.mongodb.com/backup/cloud-backup/overview/) for dedicated clusters and [Shared Cluster Backups](https://docs.atlas.mongodb.com/backup/shared-tier/overview/) for tenant clusters. If set to `false`, the cluster doesn't use backups.
        biConnector:
          $ref: '#/components/schemas/BiConnector'
        clusterType:
          type: string
          description: Configuration of nodes that comprise the cluster.
        connectionStrings:
          $ref: '#/components/schemas/ClusterConnectionStrings'
        createDate:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud created this cluster. This parameter expresses its value in ISO 8601 format in UTC.
          readOnly: true
        diskSizeGB:
          type: number
          format: double
          description: Storage capacity that the host's root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set **replicationSpecs**. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value.  The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.
          maximum: 4096
          minimum: 10
        diskWarmingMode:
          type: string
          default: FULLY_WARMED
          description: Disk warming mode selection.
          externalDocs:
            description: Reduce Secondary Disk Warming Impact
            url: https://docs.atlas.mongodb.com/reference/replica-set-tags/#reduce-secondary-disk-warming-impact
        encryptionAtRestProvider:
          type: string
          description: 'Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster **replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize** setting must be `M10` or higher and `"backupEnabled" : false` or omitted entirely.'
          externalDocs:
            description: Encryption at Rest using Customer Key Management
            url: https://www.mongodb.com/docs/atlas/security-kms-encryption/
        globalClusterSelfManagedSharding:
          type: boolean
          description: |-
            Set this field to configure the Sharding Management Mode when creating a new Global Cluster.

            When set to false, the management mode is set to Atlas-Managed Sharding. This mode fully manages the sharding of your Global Cluster and is built to provide a seamless deployment experience.

            When set to true, the management mode is set to Self-Managed Sharding. This mode leaves the management of shards in your hands and is built to provide an advanced and flexible deployment experience.

            This setting cannot be changed once the cluster is deployed.
          externalDocs:
            description: Creating a Global Cluster
            url: https://dochub.mongodb.org/core/global-cluster-management
        groupId:
          type: string
          description: Unique 24-hexadecimal character string that identifies the project.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        id:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the cluster.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        labels:
          type: array
          deprecated: true
          description: |-
            Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.

            Cluster labels are deprecated and will be removed in a future release. We strongly recommend that you use [resource tags](https://dochub.mongodb.org/core/add-cluster-tag-atlas) instead.
          items:
            $ref: '#/components/schemas/ComponentLabel'
        links:
          type: array
          description: List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.
          externalDocs:
            description: Web Linking Specification (RFC 5988)
            url: https://datatracker.ietf.org/doc/html/rfc5988
          items:
            $ref: '#/components/schemas/Link'
          readOnly: true
        mongoDBMajorVersion:
          type: string
          default: '7.0'
          description: Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version.
        mongoDBVersion:
          type: string
          description: Version of MongoDB that the cluster runs.
          pattern: ([\d]+\.[\d]+\.[\d]+)
          readOnly: true
        name:
          type: string
          description: Human-readable label that identifies the advanced cluster.
          maxLength: 64
          minLength: 1
          pattern: ^[a-zA-Z0-9][a-zA-Z0-9-]*$
        paused:
          type: boolean
          description: Flag that indicates whether the cluster is paused.
        pitEnabled:
          type: boolean
          description: Flag that indicates whether the cluster uses continuous cloud backups.
          externalDocs:
            description: Continuous Cloud Backups
            url: https://docs.atlas.mongodb.com/backup/cloud-backup/overview/
        replicationSpecs:
          type: array
          description: List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global sharded clusters and replica sets, this array has one object representing where your clusters nodes deploy.
          items:
            $ref: '#/components/schemas/ReplicationSpec'
        rootCertType:
          type: string
          default: ISRGROOTX1
          description: Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group.
        stateName:
          type: string
          description: Human-readable label that indicates the current operating condition of this cluster.
          readOnly: true
        tags:
          type: array
          description: List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the cluster.
          externalDocs:
            description: Resource Tags
            url: https://dochub.mongodb.org/core/add-cluster-tag-atlas
          items:
            $ref: '#/components/schemas/ResourceTag'
        terminationProtectionEnabled:
          type: boolean
          default: false
          description: Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.
        versionReleaseSystem:
          type: string
          default: LTS
          description: Method by which the cluster maintains the MongoDB versions. If value is `CONTINUOUS`, you must not specify **mongoDBMajorVersion**.
    AdvancedComputeAutoScaling:
      type: object
      description: Options that determine how this cluster handles CPU scaling.
      properties:
        enabled:
          type: boolean
          description: |-
            Flag that indicates whether someone enabled instance size auto-scaling.

            - Set to `true` to enable instance size auto-scaling. If enabled, you must specify a value for **replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize**.
            - Set to `false` to disable instance size automatic scaling.
        maxInstanceSize:
          $ref: '#/components/schemas/BaseCloudProviderInstanceSize'
        minInstanceSize:
          $ref: '#/components/schemas/BaseCloudProviderInstanceSize'
        scaleDownEnabled:
          type: boolean
          description: 'Flag that indicates whether the instance size may scale down. MongoDB Cloud requires this parameter if `"replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled" : true`. If you enable this option, specify a value for **replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize**.'
      title: Automatic Compute Scaling Settings
    ApiError:
      type: object
      properties:
        detail:
          type: string
          description: Describes the specific conditions or reasons that cause each type of error.
        error:
          type: integer
          format: int32
          description: HTTP status code returned with this error.
          externalDocs:
            url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        errorCode:
          type: string
          description: Application error code returned with this error.
        parameters:
          type: array
          description: Parameters used to give more information about the error.
          items: {}
        reason:
          type: string
          description: Application error message returned with this error.
    BaseCloudProviderInstanceSize:
      type: string
      description: 'Minimum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if `"replicationSpecs[n].regionConfigs[m].autoScaling.compute.scaleDownEnabled" : true`.'
    BiConnector:
      type: object
      description: Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.
      externalDocs:
        description: MongoDB Connector for Business Intelligence
        url: https://docs.mongodb.com/bi-connector/current/
      properties:
        enabled:
          type: boolean
          description: Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster.
        readPreference:
          type: string
          description: Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud. The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to `ANALYTICS` node, or `SECONDARY` if there are no `ANALYTICS` nodes.
          externalDocs:
            description: Read preferences for BI Connector
            url: https://docs.atlas.mongodb.com/cluster-config/enable-bic/#std-label-bic-read-preferences
      title: MongoDB Connector for Business Intelligence Settings
    BillingInvoice:
      type: object
      properties:
        amountBilledCents:
          type: integer
          format: int64
          description: Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        amountPaidCents:
          type: integer
          format: int64
          description: Sum that the specified organization paid toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        created:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud created this invoice. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        creditsCents:
          type: integer
          format: int64
          description: Sum that MongoDB credited the specified organization toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        endDate:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud finished the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        groupId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the project associated to this invoice. This identifying string doesn't appear on all invoices.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        id:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        lineItems:
          type: array
          description: List that contains individual services included in this invoice.
          items:
            $ref: '#/components/schemas/InvoiceLineItem'
          readOnly: true
        linkedInvoices:
          type: array
          description: List that contains the invoices for organizations linked to the paying organization.
          items:
            $ref: '#/components/schemas/BillingInvoice'
          readOnly: true
        links:
          type: array
          description: List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.
          externalDocs:
            description: Web Linking Specification (RFC 5988)
            url: https://datatracker.ietf.org/doc/html/rfc5988
          items:
            $ref: '#/components/schemas/Link'
          readOnly: true
        orgId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the organization charged for services consumed from MongoDB Cloud.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        payments:
          type: array
          description: List that contains funds transferred to MongoDB to cover the specified service noted in this invoice.
          items:
            $ref: '#/components/schemas/BillingPayment'
          readOnly: true
        refunds:
          type: array
          description: List that contains payments that MongoDB returned to the organization for this invoice.
          items:
            $ref: '#/components/schemas/BillingRefund'
          readOnly: true
        salesTaxCents:
          type: integer
          format: int64
          description: Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        startDate:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud began the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        startingBalanceCents:
          type: integer
          format: int64
          description: Sum that the specified organization owed to MongoDB when MongoDB issued this invoice. This parameter expresses its value in US Dollars.
          readOnly: true
        statusName:
          type: string
          description: |
            Phase of payment processing in which this invoice exists when you made this request. Accepted phases include:

            | Phase Value | Reason |
            |---|---|
            | CLOSED | MongoDB finalized all charges in the billing cycle but has yet to charge the customer. |
            | FAILED | MongoDB attempted to charge the provided credit card but charge for that amount failed. |
            | FORGIVEN | Customer initiated payment which MongoDB later forgave. |
            | FREE | All charges totalled zero so the customer won't be charged. |
            | INVOICED | MongoDB handled these charges using elastic invoicing. |
            | PAID | MongoDB succeeded in charging the provided credit card. |
            | PENDING | Invoice includes charges for the current billing cycle. |
            | PREPAID | Customer has a pre-paid plan so they won't be charged. |
        subtotalCents:
          type: integer
          format: int64
          description: Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        updated:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud last updated the value of this payment. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
    BillingPayment:
      type: object
      description: Funds transferred to MongoDB to cover the specified service in this invoice.
      properties:
        amountBilledCents:
          type: integer
          format: int64
          description: Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        amountPaidCents:
          type: integer
          format: int64
          description: Sum that the specified organization paid toward the associated invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        created:
          type: string
          format: date-time
          description: Date and time when the customer made this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        currency:
          type: string
          description: The currency in which payment was paid. This parameter expresses its value in 3-letter ISO 4217 currency code.
          readOnly: true
        id:
          type: string
          description: Unique 24-hexadecimal digit string that identifies this payment toward the associated invoice.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        salesTaxCents:
          type: integer
          format: int64
          description: Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        statusName:
          type: string
          description: |
            Phase of payment processing for the associated invoice when you made this request.

            These phases include:

            | Phase Value | Reason |
            |---|---|
            | `CANCELLED` | Customer or MongoDB cancelled the payment. |
            | `ERROR` | Issue arose when attempting to complete payment. |
            | `FAILED` | MongoDB tried to charge the credit card without success. |
            | `FAILED_AUTHENTICATION` | Strong Customer Authentication has failed. Confirm that your payment method is authenticated. |
            | `FORGIVEN` | Customer initiated payment which MongoDB later forgave. |
            | `INVOICED` | MongoDB issued an invoice that included this line item. |
            | `NEW` | Customer provided a method of payment, but MongoDB hasn't tried to charge the credit card. |
            | `PAID` | Customer submitted a successful payment. |
            | `PARTIAL_PAID` | Customer paid for part of this line item. |
        subtotalCents:
          type: integer
          format: int64
          description: Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).
          readOnly: true
        unitPrice:
          type: string
          description: The unit price applied to amountBilledCents to compute total payment amount. This value is represented as a decimal string.
          readOnly: true
        updated:
          type: string
          format: date-time
          description: Date and time when the customer made an update to this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
      title: Payment
    BillingRefund:
      type: object
      description: One payment that MongoDB returned to the organization for this invoice.
      properties:
        amountCents:
          type: integer
          format: int64
          description: Sum of the funds returned to the specified organization expressed in cents (100th of US Dollar).
          readOnly: true
        created:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud created this refund. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        paymentId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the payment that the organization had made.
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        reason:
          type: string
          description: Justification that MongoDB accepted to return funds to the organization.
          readOnly: true
      title: Refund
    CloudProviderAccessAWSIAMRole:
      type: object
      allOf:
        - $ref: '#/components/schemas/CloudProviderAccessRole'
        - type: object
          properties:
            atlasAWSAccountArn:
              type: string
              description: Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role.
              example: arn:aws:iam::772401394250:role/my-test-aws-role
              maxLength: 2048
              minLength: 20
              readOnly: true
            atlasAssumedRoleExternalId:
              type: string
              format: uuid
              description: Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account.
              readOnly: true
            authorizedDate:
              type: string
              format: date-time
              description: Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
              readOnly: true
            createdDate:
              type: string
              format: date-time
              description: Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
              readOnly: true
            featureUsages:
              type: array
              description: List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.
              items:
                $ref: '#/components/schemas/CloudProviderAccessFeatureUsage'
              readOnly: true
            iamAssumedRoleArn:
              type: string
              description: Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.
              example: arn:aws:iam::123456789012:root
              maxLength: 2048
              minLength: 20
            roleId:
              type: string
              description: Unique 24-hexadecimal digit string that identifies the role.
              example: 32b6e34b3d91647abb20e7b8
              maxLength: 24
              minLength: 24
              pattern: ^([a-f0-9]{24})$
              readOnly: true
      description: Details that describe the features linked to the Amazon Web Services (AWS) Identity and Access Management (IAM) role.
      required:
        - providerName
      properties:
        atlasAWSAccountArn:
          type: string
          description: Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role.
          example: arn:aws:iam::772401394250:role/my-test-aws-role
          maxLength: 2048
          minLength: 20
          readOnly: true
        atlasAssumedRoleExternalId:
          type: string
          format: uuid
          description: Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account.
          readOnly: true
        authorizedDate:
          type: string
          format: date-time
          description: Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        createdDate:
          type: string
          format: date-time
          description: Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        featureUsages:
          type: array
          description: List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.
          items:
            $ref: '#/components/schemas/CloudProviderAccessFeatureUsage'
          readOnly: true
        iamAssumedRoleArn:
          type: string
          description: Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.
          example: arn:aws:iam::123456789012:root
          maxLength: 2048
          minLength: 20
        roleId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the role.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
    CloudProviderAccessFeatureUsage:
      type: object
      description: MongoDB Cloud features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.
      properties:
        featureType:
          type: string
          description: Human-readable label that describes one MongoDB Cloud feature linked to this Amazon Web Services (AWS) Identity and Access Management (IAM) role.
          readOnly: true
        featureId:
          $ref: '#/components/schemas/CloudProviderAccessFeatureUsagePushBasedLogExportFeatureId'
    CloudProviderAccessFeatureUsagePushBasedLogExportFeatureId:
      type: object
      description: Identifying characteristics about the Amazon Web Services (AWS) Simple Storage Service (S3) export bucket linked to this AWS Identity and Access Management (IAM) role.
      properties:
        bucketName:
          type: string
          description: Name of the AWS S3 bucket to which your logs will be exported to.
          readOnly: true
        groupId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies your project.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
    CloudProviderAccessRole:
      type: object
      description: Cloud provider access role.
      properties:
        providerName:
          type: string
          description: Human-readable label that identifies the cloud provider of the role.
        atlasAWSAccountArn:
          type: string
          description: Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role.
          example: arn:aws:iam::772401394250:role/my-test-aws-role
          maxLength: 2048
          minLength: 20
          readOnly: true
        atlasAssumedRoleExternalId:
          type: string
          format: uuid
          description: Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account.
          readOnly: true
        authorizedDate:
          type: string
          format: date-time
          description: Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        createdDate:
          type: string
          format: date-time
          description: |-
            Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.

            Alternatively:
            Date and time when this Azure Service Principal was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        featureUsages:
          type: array
          description: |-
            List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.

            Alternatively:
            List that contains application features associated with this Azure Service Principal.
          items:
            $ref: '#/components/schemas/CloudProviderAccessFeatureUsage'
          readOnly: true
        iamAssumedRoleArn:
          type: string
          description: Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.
          example: arn:aws:iam::123456789012:root
          maxLength: 2048
          minLength: 20
        roleId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the role.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        _id:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the Azure Service Principal in Atlas.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        atlasAzureAppId:
          type: string
          description: Azure Active Directory Application ID of Atlas.
          maxLength: 36
          minLength: 32
          pattern: ^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$
        lastUpdatedDate:
          type: string
          format: date-time
          description: Date and time when this Azure Service Principal was last updated. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        servicePrincipalId:
          type: string
          description: UUID string that identifies the Azure Service Principal.
          maxLength: 36
          minLength: 32
          pattern: ^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$
        tenantId:
          type: string
          description: UUID String that identifies the Azure Active Directory Tenant ID.
          maxLength: 36
          minLength: 32
          pattern: ^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$
      required:
        - providerName
    CloudRegionConfig:
      type: object
      description: Cloud service provider on which MongoDB Cloud provisions the hosts.
      properties:
        electableSpecs:
          $ref: '#/components/schemas/HardwareSpec'
        priority:
          type: integer
          format: int32
          description: |-
            Precedence is given to this region when a primary election occurs. If your **regionConfigs** has only **readOnlySpecs**, **analyticsSpecs**, or both, set this value to `0`. If you have multiple **regionConfigs** objects (your cluster is multi-region or multi-cloud), they must have priorities in descending order. The highest priority is `7`.

            **Example:** If you have three regions, their priorities would be `7`, `6`, and `5` respectively. If you added two more regions for supporting electable nodes, the priorities of those regions would be `4` and `3` respectively.
          maximum: 7
          minimum: 0
        providerName:
          type: string
          description: Cloud service provider on which MongoDB Cloud provisions the hosts. Set dedicated clusters to `AWS`, `GCP`, `AZURE` or `TENANT`.
        regionName:
          type: string
          description: Physical location of your MongoDB cluster nodes. The region you choose can affect network latency for clients accessing your databases. The region name is only returned in the response for single-region clusters. When MongoDB Cloud deploys a dedicated cluster, it checks if a VPC or VPC connection exists for that provider and region. If not, MongoDB Cloud creates them as part of the deployment. It assigns the VPC a Classless Inter-Domain Routing (CIDR) block. To limit a new VPC peering connection to one Classless Inter-Domain Routing (CIDR) block and region, create the connection first. Deploy the cluster after the connection starts. GCP Clusters and Multi-region clusters require one VPC peering connection for each region. MongoDB nodes can use only the peering connection that resides in the same region as the nodes to communicate with the peered VPC.
        analyticsAutoScaling:
          $ref: '#/components/schemas/AdvancedAutoScalingSettings'
        analyticsSpecs:
          $ref: '#/components/schemas/DedicatedHardwareSpec'
        autoScaling:
          $ref: '#/components/schemas/AdvancedAutoScalingSettings'
        readOnlySpecs:
          $ref: '#/components/schemas/DedicatedHardwareSpec'
        backingProviderName:
          type: string
          description: Cloud service provider on which MongoDB Cloud provisioned the multi-tenant cluster. The resource returns this parameter when **providerName** is `TENANT` and **electableSpecs.instanceSize** is `M0`, `M2` or `M5`.
      title: Cloud Service Provider Settings for Multi-Cloud Clusters
    ClusterConnectionStrings:
      type: object
      description: Collection of Uniform Resource Locators that point to the MongoDB database.
      externalDocs:
        description: Connection string URI format.
        url: https://docs.mongodb.com/manual/reference/connection-string/
      properties:
        awsPrivateLink:
          type: object
          additionalProperties:
            type: string
            description: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names.
            externalDocs:
              description: Network Peering Connection
              url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
            readOnly: true
          description: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names.
          externalDocs:
            description: Network Peering Connection
            url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
          readOnly: true
        awsPrivateLinkSrv:
          type: object
          additionalProperties:
            type: string
            description: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to Atlas through the interface endpoint that the key names.
            externalDocs:
              description: Network Peering Connection
              url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
            readOnly: true
          description: Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to Atlas through the interface endpoint that the key names.
          externalDocs:
            description: Network Peering Connection
            url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
          readOnly: true
        private:
          type: string
          description: Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the `mongodb+srv://` protocol. The resource returns this parameter once someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn't, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this resource returns this parameter only if you enable custom DNS.
          externalDocs:
            description: Network Peering Connection
            url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
          readOnly: true
        privateEndpoint:
          type: array
          description: List of private endpoint-aware connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.
          items:
            $ref: '#/components/schemas/ClusterDescriptionConnectionStringsPrivateEndpoint'
          readOnly: true
        privateSrv:
          type: string
          description: Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the `mongodb+srv://` protocol. The resource returns this parameter when someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your driver supports it. If it doesn't, use `connectionStrings.private`. For Amazon Web Services (AWS) clusters, this parameter returns only if you [enable custom DNS](https://docs.atlas.mongodb.com/reference/api/aws-custom-dns-update/).
          externalDocs:
            description: Network Peering Connection
            url: https://docs.atlas.mongodb.com/security-vpc-peering/#std-label-vpc-peering/
          readOnly: true
        standard:
          type: string
          description: Public connection string that you can use to connect to this cluster. This connection string uses the `mongodb://` protocol.
          externalDocs:
            description: Connection String URI Format
            url: https://docs.mongodb.com/manual/reference/connection-string/
          readOnly: true
        standardSrv:
          type: string
          description: Public connection string that you can use to connect to this cluster. This connection string uses the `mongodb+srv://` protocol.
          externalDocs:
            description: Connection String URI Format
            url: https://docs.mongodb.com/manual/reference/connection-string/
          readOnly: true
      readOnly: true
      title: Cluster Connection Strings
    ClusterDescriptionConnectionStringsPrivateEndpoint:
      type: object
      description: Private endpoint-aware connection string that you can use to connect to this cluster through a private endpoint.
      externalDocs:
        description: Private Endpoint for Dedicated Cluster
        url: https://docs.atlas.mongodb.com/security-private-endpoint/
      properties:
        connectionString:
          type: string
          description: Private endpoint-aware connection string that uses the `mongodb://` protocol to connect to MongoDB Cloud through a private endpoint.
          readOnly: true
        endpoints:
          type: array
          description: List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].connectionString** or **connectionStrings.privateEndpoint[n].srvConnectionString**.
          items:
            $ref: '#/components/schemas/ClusterDescriptionConnectionStringsPrivateEndpointEndpoint'
          readOnly: true
        srvConnectionString:
          type: string
          description: Private endpoint-aware connection string that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. The `mongodb+srv` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application supports it. If it doesn't, use connectionStrings.privateEndpoint[n].connectionString.
          readOnly: true
        srvShardOptimizedConnectionString:
          type: string
          description: Private endpoint-aware connection string optimized for sharded clusters that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application and Atlas cluster supports it. If it doesn't, use and consult the documentation for connectionStrings.privateEndpoint[n].srvConnectionString.
          readOnly: true
        type:
          type: string
          description: MongoDB process type to which your application connects. Use `MONGOD` for replica sets and `MONGOS` for sharded clusters.
          readOnly: true
      title: Cluster Private Endpoint Connection String
    ClusterDescriptionConnectionStringsPrivateEndpointEndpoint:
      type: object
      description: Details of a private endpoint deployed for this cluster.
      properties:
        endpointId:
          type: string
          description: Unique string that the cloud provider uses to identify the private endpoint.
          readOnly: true
        providerName:
          type: string
          description: Cloud provider in which MongoDB Cloud deploys the private endpoint.
          readOnly: true
        region:
          type: string
          description: Region where the private endpoint is deployed.
          readOnly: true
      title: Cluster Private Endpoint Connection Strings Endpoint
    ComponentLabel:
      type: object
      description: Human-readable labels applied to this MongoDB Cloud component.
      properties:
        key:
          type: string
          description: Key applied to tag and categorize this component.
          maxLength: 255
          minLength: 1
        value:
          type: string
          description: Value set to the Key applied to tag and categorize this component.
          maxLength: 255
          minLength: 1
      title: Component Label
    DedicatedHardwareSpec:
      type: object
      description: Hardware specifications for read-only nodes in the region. Read-only nodes can never become the primary member, but can enable local reads.If you don't specify this parameter, no read-only nodes are deployed to the region.
      properties:
        nodeCount:
          type: integer
          format: int32
          description: Number of nodes of the given type for MongoDB Cloud to deploy to the region.
        diskIOPS:
          type: integer
          format: int32
          description: |-
            Target throughput desired for storage attached to your AWS-provisioned cluster. Change this parameter only if you:

            - set `"replicationSpecs[n].regionConfigs[m].providerName" : "AWS"`.
            - set `"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30"` or greater not including `Mxx_NVME` tiers.

            The maximum input/output operations per second (IOPS) depend on the selected **.instanceSize** and **.diskSizeGB**.
            This parameter defaults to the cluster tier's standard IOPS value.
            Changing this value impacts cluster cost.
            MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.

            - Instance sizes `M10` to `M40` have a ratio of disk capacity to system memory of 60:1.
            - Instance sizes greater than `M40` have a ratio of 120:1.
        ebsVolumeType:
          type: string
          default: STANDARD
          description: "Type of storage you want to attach to your AWS-provisioned cluster.\n\n- `STANDARD` volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size. \n\n- `PROVISIONED` volume types must fall within the allowable IOPS range for the selected volume size. You must set this value to (`PROVISIONED`) for NVMe clusters."
        instanceSize:
          type: string
          description: Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size.
          title: GCP Instance Sizes
    DiskGBAutoScaling:
      type: object
      description: Setting that enables disk auto-scaling.
      properties:
        enabled:
          type: boolean
          description: Flag that indicates whether this cluster enables disk auto-scaling. The maximum memory allowed for the selected cluster tier and the oplog size can limit storage auto-scaling.
    HardwareSpec:
      type: object
      description: Hardware specifications for all electable nodes deployed in the region. Electable nodes can become the primary and can enable local reads. If you don't specify this option, MongoDB Cloud deploys no electable nodes to the region.
      properties:
        diskIOPS:
          type: integer
          format: int32
          description: |-
            Target throughput desired for storage attached to your AWS-provisioned cluster. Change this parameter only if you:

            - set `"replicationSpecs[n].regionConfigs[m].providerName" : "AWS"`.
            - set `"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : "M30"` or greater not including `Mxx_NVME` tiers.

            The maximum input/output operations per second (IOPS) depend on the selected **.instanceSize** and **.diskSizeGB**.
            This parameter defaults to the cluster tier's standard IOPS value.
            Changing this value impacts cluster cost.
            MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.

            - Instance sizes `M10` to `M40` have a ratio of disk capacity to system memory of 60:1.
            - Instance sizes greater than `M40` have a ratio of 120:1.
        ebsVolumeType:
          type: string
          default: STANDARD
          description: "Type of storage you want to attach to your AWS-provisioned cluster.\n\n- `STANDARD` volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size. \n\n- `PROVISIONED` volume types must fall within the allowable IOPS range for the selected volume size. You must set this value to (`PROVISIONED`) for NVMe clusters."
        instanceSize:
          type: string
          description: Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size.
          title: Tenant Instance Sizes
        nodeCount:
          type: integer
          format: int32
          description: Number of nodes of the given type for MongoDB Cloud to deploy to the region.
    InvoiceLineItem:
      type: object
      description: One service included in this invoice.
      properties:
        clusterName:
          type: string
          description: Human-readable label that identifies the cluster that incurred the charge.
          maxLength: 64
          minLength: 1
          pattern: ^[a-zA-Z0-9][a-zA-Z0-9-]*$
          readOnly: true
        created:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud created this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        discountCents:
          type: integer
          format: int64
          description: Sum by which MongoDB discounted this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar). The resource returns this parameter when a discount applies.
          readOnly: true
        endDate:
          type: string
          format: date-time
          description: Date and time when when MongoDB Cloud finished charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        groupId:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the project associated to this line item.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        groupName:
          type: string
          description: Human-readable label that identifies the project.
        note:
          type: string
          description: Comment that applies to this line item.
          readOnly: true
        percentDiscount:
          type: number
          format: float
          description: Percentage by which MongoDB discounted this line item. The resource returns this parameter when a discount applies.
          readOnly: true
        quantity:
          type: number
          format: double
          description: Number of units included for the line item. These can be expressions of storage (GB), time (hours), or other units.
          readOnly: true
        sku:
          type: string
          description: Human-readable description of the service that this line item provided. This Stock Keeping Unit (SKU) could be the instance type, a support charge, advanced security, or another service.
          readOnly: true
        startDate:
          type: string
          format: date-time
          description: Date and time when MongoDB Cloud began charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.
          readOnly: true
        stitchAppName:
          type: string
          description: Human-readable label that identifies the Atlas App Services application associated with this line item.
          externalDocs:
            description: Create a new Atlas App Service
            url: https://www.mongodb.com/docs/atlas/app-services/manage-apps/create/create-with-ui/
          readOnly: true
        tags:
          type: object
          additionalProperties:
            type: array
            description: A map of key-value pairs corresponding to the tags associated with the line item resource.
            items:
              type: string
              description: A map of key-value pairs corresponding to the tags associated with the line item resource.
              readOnly: true
            readOnly: true
          description: A map of key-value pairs corresponding to the tags associated with the line item resource.
          readOnly: true
        tierLowerBound:
          type: number
          format: double
          description: "Lower bound for usage amount range in current SKU tier. \n\n**NOTE**: **lineItems[n].tierLowerBound** appears only if your **lineItems[n].sku** is tiered."
          readOnly: true
        tierUpperBound:
          type: number
          format: double
          description: "Upper bound for usage amount range in current SKU tier. \n\n**NOTE**: **lineItems[n].tierUpperBound** appears only if your **lineItems[n].sku** is tiered."
          readOnly: true
        totalPriceCents:
          type: integer
          format: int64
          description: Sum of the cost set for this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar) and calculates this value as **unitPriceDollars** × **quantity** × 100.
          readOnly: true
        unit:
          type: string
          description: Element used to express what **quantity** this line item measures. This value can be elements of time, storage capacity, and the like.
          readOnly: true
        unitPriceDollars:
          type: number
          format: double
          description: Value per **unit** for this line item expressed in US Dollars.
          readOnly: true
      title: Line Item
    Link:
      type: object
      properties:
        href:
          type: string
          description: Uniform Resource Locator (URL) that points another API resource to which this response has some relationship. This URL often begins with `https://cloud.mongodb.com/api/atlas`.
          example: https://cloud.mongodb.com/api/atlas
        rel:
          type: string
          description: Uniform Resource Locator (URL) that defines the semantic relationship between this resource and another API resource. This URL often begins with `https://cloud.mongodb.com/api/atlas`.
          example: self
    ReplicationSpec:
      type: object
      description: Details that explain how MongoDB Cloud replicates data on the specified MongoDB database.
      properties:
        id:
          type: string
          description: Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Multi-Cloud Cluster. If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Multi-Cloud Cluster, you may specify this parameter. The request deletes any existing zones in the Multi-Cloud Cluster that you exclude from the request.
          example: 32b6e34b3d91647abb20e7b8
          maxLength: 24
          minLength: 24
          pattern: ^([a-f0-9]{24})$
          readOnly: true
        numShards:
          type: integer
          format: int32
          description: |-
            Positive integer that specifies the number of shards to deploy in each specified zone. If you set this value to `1` and **clusterType** is `SHARDED`, MongoDB Cloud deploys a single-shard sharded cluster. Don't create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don't provide the same benefits as multi-shard configurations.


             If you are upgrading a replica set to a sharded cluster, you cannot increase the number of shards in the same update request.  You should wait until after the cluster has completed upgrading to sharded and you have reconnected all application clients to the MongoDB router before adding additional shards. Otherwise, your data might become inconsistent once MongoDB Cloud begins distributing data across shards.
          minimum: 1
        regionConfigs:
          type: array
          description: |-
            Hardware specifications for nodes set for a given region. Each **regionConfigs** object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each **regionConfigs** object must have either an **analyticsSpecs** object, **electableSpecs** object, or **readOnlySpecs** object. Tenant clusters only require **electableSpecs. Dedicated** clusters can specify any of these specifications, but must have at least one **electableSpecs** object within a **replicationSpec**. Every hardware specification must use the same **instanceSize**.

            **Example:**

            If you set `"replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize" : "M30"`, set `"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize" : `"M30"` if you have electable nodes and `"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize" : `"M30"` if you have read-only nodes.
          items:
            $ref: '#/components/schemas/CloudRegionConfig'
        zoneName:
          type: string
          description: 'Human-readable label that identifies the zone in a Global Cluster. Provide this value only if `"clusterType" : "GEOSHARDED"`.'
      title: Replication Specifications
    ResourceTag:
      type: object
      description: 'Key-value pair that tags and categorizes a MongoDB Cloud organization, project, or cluster. For example, `environment : production`.'
      properties:
        key:
          type: string
          description: 'Constant that defines the set of the tag. For example, `environment` in the `environment : production` tag.'
          maxLength: 255
          minLength: 1
        value:
          type: string
          description: 'Variable that belongs to the set of the tag. For example, `production` in the `environment : production` tag.'
          maxLength: 255
          minLength: 1
      required:
        - key
        - value
      title: Resource Tag
```