# Atlas Marketplace

A small, public GitHub catalog of extensions for Atlas homelab documentation. Atlas reads `catalog.json`; this repository does not execute installers or contain credentials.

## Available extensions

| Category | Extensions |
| --- | --- |
| Connector add-ons | Portainer, SNMP discovery, Kubernetes, UniFi Network, Proxmox VE |
| Device catalogs | Ubiquiti 19-inch rack equipment |
| Icon packs | Homelab essentials: original application and dependency-map graphics |

Individual repositories own their code, data, license and documentation. Published versions are pinned to full Git commit hashes. Listing here does not certify a package or imply live validation against every upstream system. Kubernetes and Proxmox use fixture validation; UniFi needs controller credentials for live verification.

## Use in Atlas

Open **Marketplace**. Browse by category, inspect package details, download and review the pinned files, and confirm the repository before installation. Connector installation does not establish an upstream connection: configure an instance in **Sources & settings** afterwards. Hardware definitions appear in **Device catalogs**. Icon packs appear in **Edit application → Application icon** and support automatic matching.

Updates require a manual refresh and explicit installation review. Installed extensions remain available if their catalog source is disabled or removed. Removing a package retains imported inventory; uninstalling a connector removes its instances and saved credentials. Previous versions installed through Marketplace can be rolled back, provided configurations remain compatible.

## Share a custom catalog

1. Create a public GitHub repository containing `catalog.json` on `main` (or another selected branch).
2. Use the schema below. Point every package at a full 40-character Git commit in its own public repository.
3. In Atlas choose **Marketplace → Sources → Add GitHub catalog**, then refresh.

A single connector can still be installed through **Sources & settings → Add GitHub repository** without creating a catalog.

```json
{
  "schemaVersion": 1,
  "packages": [
    {
      "id": "example-connector",
      "type": "connector",
      "name": "Example connector",
      "description": "Read-only inventory from an upstream system.",
      "repository": "https://github.com/owner/atlas-plugin-example",
      "ref": "0123456789abcdef0123456789abcdef01234567",
      "version": "1.0.0",
      "license": "MIT",
      "permissions": ["Read configured upstream inventory"],
      "documentation": "README.md"
    }
  ]
}
```

Supported types and default manifests:

| Type | Manifest | Contents |
| --- | --- | --- |
| `connector` | `atlas-addin.json` | Connector API 1 package with declared checksummed Python files |
| `device-catalog` | `catalog.json` | Atlas version 1 hardware definitions |
| `icon-pack` | `atlas-icons.json` | Static PNG/JPEG/WebP icons with SHA-256 checksums; no SVG/HTML/code |

Optional fields: `manifest` (relative path, data packages only), `preview` (image path in the package repository), `color` (`#RRGGBB`), `icon` (one of `portainer`, `snmp-discovery`, `kubernetes`, `unifi`, `proxmox`, `rack`, `icons`, `box`). IDs must be unique lower-case slugs. Up to 200 entries per source. Documentation and preview paths must remain within the package repository. Connector manifests currently reside at the repository root.

Sources are public; existing private GitHub access is still available through the direct connector installer. Source discovery never installs or runs code. No automatic package updates are performed.

## Contribute

Submit a pull request adding or updating an entry. Include an accessible repository, accurate description and access requirements, documentation/license, a working manifest and a pinned release commit. Each connector should document read-only upstream permissions and its test coverage. Do not include passwords, personal inventory or tokens.

To publish an update, release the new version in its own repository, then propose the matching version and commit here. Atlas owners review the update themselves.

## License

Catalog metadata: MIT, copyright (c) 2026 42bios. Extension code, artwork and manufacturer assets retain their respective repository licenses and rights.
