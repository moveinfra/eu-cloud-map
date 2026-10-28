# Contributing

Corrections and additions are welcome: a product renamed, a better EU equivalent, a missing provider.

## What belongs in the map

- **Targets are EU-owned providers**: the company is headquartered in the EU (or EEA/Switzerland) and is not a
  subsidiary of a non-EU cloud. EU regions of AWS, Google Cloud or Azure do not qualify.
- **Products are generally available** and have a public product or pricing page. No betas, no "contact sales only".
- **One row per capability** that a typical company runs (virtual machines, managed PostgreSQL, object storage, …),
  not one row per product.

## How to change the data

1. Edit `data/eu-cloud-map.json` only. The tables in `README.md` are generated from it.
2. Run `python3 scripts/build-readme.py` to refresh the tables.
3. Open a pull request with a link to the provider's documentation for every product you add or change.

CI checks that the JSON is valid and that `README.md` was regenerated.

## Data format

```json
{
  "id": "managed-postgres",
  "label": "Managed PostgreSQL / MySQL",
  "sources": {
    "aws":   { "product": "RDS, Aurora (provisioned)", "notes": null }
  },
  "targets": {
    "upcloud": { "product": "Managed PostgreSQL / MySQL", "notes": "Logical replication, then cutover", "migration": "automatic" }
  }
}
```

| Field | Rules |
|---|---|
| `id` | lowercase, hyphens, unique, never renamed once published (people link to it) |
| `label` | what the capability is, in plain words |
| `sources.<cloud>.product` | the source cloud's product name(s), comma-separated; `null` or omitted when it has none |
| `targets.<provider>.product` | the EU product name; `null` when there is no direct equivalent (then `migration` is `not-yet`) |
| `targets.<provider>.notes` | one short line: how it maps (e.g. "Terraform, size-matched") or what is different |
| `targets.<provider>.migration` | `automatic`, `assisted` or `not-yet`: see below |

Source clouds: `aws`, `gcp`, `azure`, `digitalocean`. Targets: `upcloud`, `scaleway`, `hetzner`, `ovhcloud`.

### About `migration`

This field says how [MoveInfra](https://moveinfra.eu), the maintainer, moves the capability today:
`automatic` (rebuilt and synced by tooling), `assisted` (a replacement is built with the customer) or `not-yet`.
It describes the migration service, not the quality of the provider's product. If you use the map for something
else, ignore it or use your own values in a fork.

## Adding a provider

Add a key under `targets` for **every** capability (`product: null` where there is no equivalent), add the provider to
`TARGETS` in `scripts/build-readme.py`, and mention it in the README intro. Please open an issue first so we can agree
on the name used as key.

## License

The data is [CC BY 4.0](LICENSE). By contributing you agree that your contribution is published under the same license.
