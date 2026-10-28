# EU Cloud Map

Which **EU-owned** cloud product replaces each service you run on **AWS, Google Cloud, Microsoft Azure or DigitalOcean**,
and how hard the move is. Covers UpCloud (Finland), Scaleway (France), Hetzner (Germany) and OVHcloud (France):
companies headquartered in the EU, not EU regions of US providers.

- Interactive version: **https://moveinfra.eu/eu-cloud-map**
- Machine-readable: [`data/eu-cloud-map.json`](data/eu-cloud-map.json) (also served at https://moveinfra.eu/data/eu-cloud-map.json)
- License: [CC BY 4.0](LICENSE). Reuse freely, credit "EU Cloud Map by MoveInfra" with a link.

Why now: under the **EU Data Act** (Article 29), cloud switching charges, including egress for the move, are capped at
cost today and banned from **12 January 2027**. Explainer: https://moveinfra.eu/eu-data-act-switching-fees

## The map

Legend: ✅ automatic migration · 🛠️ assisted (replacement needed) · ❌ no direct equivalent today.
The status describes how the move works with [MoveInfra](https://moveinfra.eu), not the quality of the target cloud.

<!-- map:start -->
### What you use today

| Capability | AWS | Google Cloud | Azure | DigitalOcean |
|---|---|---|---|---|
| **Virtual machines** | EC2 | Compute Engine | Virtual Machines | Droplets |
| **Managed PostgreSQL / MySQL** | RDS, Aurora (provisioned) | Cloud SQL | Azure Database for PostgreSQL / MySQL | Managed Databases |
| **Object storage** | S3 | Cloud Storage | Blob Storage | Spaces |
| **Load balancers** | Elastic Load Balancing (ALB, NLB) | Cloud Load Balancing | Load Balancer, Application Gateway | Load Balancers |
| **Private networks, firewalls** | VPC, security groups | VPC, firewall rules | VNet, network security groups | VPC, Cloud Firewalls |
| **Kubernetes** | EKS | GKE | AKS | DigitalOcean Kubernetes (DOKS) |
| **Redis-compatible cache** | ElastiCache | Memorystore | Azure Cache for Redis | Managed Caching |
| **Queues and messaging** | SQS, SNS | Pub/Sub | Service Bus | — |
| **Serverless functions** | Lambda | Cloud Functions, Cloud Run | Azure Functions | Functions |
| **DNS** | Route 53 | Cloud DNS | Azure DNS | DNS |
| **Proprietary NoSQL** | DynamoDB | Firestore, Bigtable | Cosmos DB | — |
| **Data warehouse** | Redshift | BigQuery | Synapse Analytics | — |

### EU-owned equivalent

| Capability | UpCloud 🇫🇮 | Scaleway 🇫🇷 | Hetzner 🇩🇪 | OVHcloud 🇫🇷 |
|---|---|---|---|---|
| **Virtual machines** | ✅ Cloud Servers<br><sub>Terraform, size-matched</sub> | ✅ Instances<br><sub>Terraform, size-matched</sub> | ✅ Cloud Servers<br><sub>Terraform, size-matched</sub> | ✅ Public Cloud Instances<br><sub>Terraform, size-matched</sub> |
| **Managed PostgreSQL / MySQL** | ✅ Managed PostgreSQL / MySQL<br><sub>Logical replication, then cutover</sub> | ✅ Managed Database for PostgreSQL / MySQL<br><sub>Logical replication, then cutover</sub> | 🛠️ PostgreSQL / MySQL on Cloud Servers<br><sub>Hetzner has no managed database. MoveInfra sets it up on Cloud Servers, then replicates; you or a partner run it afterwards.</sub> | ✅ Managed Databases for PostgreSQL / MySQL<br><sub>Logical replication, then cutover</sub> |
| **Object storage** | ✅ Managed Object Storage<br><sub>rclone mirror with checksums</sub> | ✅ Object Storage<br><sub>rclone mirror with checksums</sub> | ✅ Object Storage<br><sub>S3-compatible. rclone mirror with checksums</sub> | ✅ Object Storage (S3 API)<br><sub>rclone mirror with checksums</sub> |
| **Load balancers** | ✅ Managed Load Balancer<br><sub>Terraform</sub> | ✅ Load Balancer<br><sub>Terraform</sub> | ✅ Load Balancer<br><sub>Terraform</sub> | ✅ Public Cloud Load Balancer<br><sub>Terraform</sub> |
| **Private networks, firewalls** | ✅ SDN private networks, firewall rules<br><sub>Terraform</sub> | ✅ VPC, Private Networks, security groups<br><sub>Terraform</sub> | ✅ Networks, Firewalls<br><sub>Terraform</sub> | ✅ vRack private networks, security groups<br><sub>Terraform</sub> |
| **Kubernetes** | ✅ Managed Kubernetes<br><sub>Terraform + Velero</sub> | ✅ Kubernetes Kapsule<br><sub>Terraform + Velero</sub> | 🛠️ Self-managed Kubernetes on Cloud Servers<br><sub>Hetzner has no managed Kubernetes. MoveInfra sets up a cluster on Cloud Servers, then moves workloads with Velero; you or a partner run it afterwards.</sub> | ✅ Managed Kubernetes Service<br><sub>Terraform + Velero</sub> |
| **Redis-compatible cache** | ✅ Managed Valkey<br><sub>Valkey is Redis-compatible. Fresh cache or snapshot restore</sub> | ✅ Managed Redis<br><sub>Fresh cache or snapshot restore</sub> | 🛠️ Valkey on Cloud Servers<br><sub>Hetzner has no managed cache. MoveInfra sets it up on Cloud Servers.</sub> | ✅ Managed Databases for Caching<br><sub>Fresh cache or snapshot restore</sub> |
| **Queues and messaging** | 🛠️ NATS or RabbitMQ on servers<br><sub>Rebuild, MoveInfra helps</sub> | 🛠️ Queues and Topics (SQS/SNS-compatible)<br><sub>Endpoint swap, MoveInfra helps</sub> | 🛠️ NATS or RabbitMQ on servers<br><sub>Rebuild, MoveInfra helps</sub> | 🛠️ Managed Kafka or RabbitMQ on servers<br><sub>Rebuild, MoveInfra helps</sub> |
| **Serverless functions** | 🛠️ Containers on Kubernetes<br><sub>Repackage, MoveInfra helps</sub> | 🛠️ Serverless Functions / Containers<br><sub>Repackage, MoveInfra helps</sub> | 🛠️ Containers on servers<br><sub>Repackage, MoveInfra helps</sub> | 🛠️ Containers on Kubernetes<br><sub>Repackage, MoveInfra helps</sub> |
| **DNS** | 🛠️ EU DNS provider of your choice<br><sub>Not an UpCloud product. Zone export and import</sub> | 🛠️ Domains and DNS<br><sub>Zone export and import</sub> | 🛠️ Hetzner DNS<br><sub>Zone export and import</sub> | 🛠️ OVHcloud DNS<br><sub>Zone export and import</sub> |
| **Proprietary NoSQL** | ❌ —<br><sub>No direct equivalent. Redesign needed</sub> | ❌ —<br><sub>No direct equivalent. Redesign needed</sub> | ❌ —<br><sub>No direct equivalent. Redesign needed</sub> | ❌ —<br><sub>No direct equivalent. Redesign needed</sub> |
| **Data warehouse** | ❌ —<br><sub>No direct equivalent. Out of scope for MoveInfra today</sub> | ❌ —<br><sub>No direct equivalent. Out of scope for MoveInfra today</sub> | ❌ —<br><sub>No direct equivalent. Out of scope for MoveInfra today</sub> | ❌ —<br><sub>No direct equivalent. Out of scope for MoveInfra today</sub> |
<!-- map:end -->

## Data format

`data/eu-cloud-map.json` has one entry per capability (`compute`, `managed-postgres`, ...):

```json
{
  "id": "compute",
  "label": "Virtual machines",
  "sources": { "aws": { "product": "EC2", "notes": null } },
  "targets": { "upcloud": { "product": "Cloud Servers", "notes": "Terraform, size-matched", "migration": "automatic" } }
}
```

`migration` is one of `automatic`, `assisted`, `not-yet`.

## Contributing

Corrections and new providers (STACKIT, IONOS, Exoscale, ...) are welcome. Open an issue or a pull request that edits
`data/eu-cloud-map.json`, then run `python3 scripts/build-readme.py` to refresh the tables above.
Please link the provider's documentation for any product you add.

Maintained by [MoveInfra](https://moveinfra.eu), a service that moves company infrastructure from US clouds to EU-owned providers.
