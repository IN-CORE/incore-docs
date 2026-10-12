# 3. Developer: clients

Work on an existing IN-CORE client **or build your own**. All clients talk to the same REST services.

| Client | Stack | Repo |
|--------|-------|------|
| **Your own client** (web app, script, dashboard, any language) | Anything that speaks HTTP + OIDC | — see {ref}`3d <dev-guides-own-client>` |
| incore-ui (Web tools: Data/Hazard/DFR3 viewers) | React/Redux, webpack, Node ≥ 20 | https://github.com/IN-CORE/incore-ui |
| incore-studio (projects, workflows, hazard creation) | React + TypeScript, esbuild, Node ≥ 20 | https://github.com/IN-CORE/incore-studio |
| incore-playbook (NIST resilience playbook, shared library) | React/Redux, webpack | https://github.com/IN-CORE/incore-playbook |
| Testbed playbooks (consume incore-playbook) | React | [Joplin](https://github.com/IN-CORE/Joplin-Playbook) · [Galveston](https://github.com/IN-CORE/Galveston-Playbook) · [SLC](https://github.com/IN-CORE/SLC-Playbook) |
| pyincore | Python ≥ 3.11, conda | https://github.com/IN-CORE/pyincore |
| pyincore-viz | Python, conda | https://github.com/IN-CORE/pyincore-viz |

Pick a backend:

| Option | Backend | Auth | When |
|--------|---------|------|------|
| 3a | `https://dev.in-core.org` (shared) | Keycloak, approved account | Default for client work |
| 3b | Your machine, pointing at dev/prod | Keycloak | Same as 3a, your own tooling |
| 3c | `http://localhost:8080` (local services) | Headers, no Keycloak | Client + service changes together, offline |

All web clients read the backend from `INCORE_REMOTE_HOSTNAME`.

(dev-guides-cors)=
## CORS (browser clients only)

A browser app on `localhost` calling a remote IN-CORE service will be blocked unless the service allows your origin. Scripts, notebooks and backend code (pyincore, curl) are **not** affected.

| Backend | What to do |
|---------|------------|
| **Prod** (`tools.in-core.org`) | Not available — prod does not allow external origins. Use dev, or call prod from your own backend/proxy (server-to-server has no CORS). |
| **Dev** (`dev.in-core.org`) | `http://localhost:3000` and `:5000` are allowed. Need another origin? See {ref}`3a <dev-guides-dev-access>`. |
| **Your own services** | Configure it yourself (below). |

Configure CORS on services you host (env vars on every service):

```bash
export SERVICES_ALLOW_ORIGIN="http://localhost:3000,https://myapp.example.org"   # comma-separated
export SERVICES_ALLOW_METHODS="GET,POST,DELETE,PUT,PATCH,OPTIONS"
export SERVICES_ALLOW_HEADERS="authorization,content-type,accept"
```

Helm deploy: set `cors.origin` (list), `cors.methods`, `cors.headers` in your values file — see `values-incore-dev.yaml` in https://github.com/IN-CORE/incore-helm.

> Always set `SERVICES_ALLOW_ORIGIN` when running services yourself; if it's unset, browser requests (which send an `Origin` header) fail with a server error.

---

(dev-guides-dev-access)=
## 3a. Remote dev service (approval required)

1. Have an IN-CORE account: [IN-CORE Account](../account.md)
2. Discuss your idea/contribution with the community on [Slack](https://in-core.slack.com) (`#developer`) or [GitHub Discussions](https://github.com/orgs/IN-CORE/discussions).
   Can't? Email incore-dev@lists.illinois.edu — we'll tell you the next steps.
3. Once approved, log in at https://dev.in-core.org.

Dev data is shared and may be reset — don't rely on it persisting.

## 3b. Your own dev env, remote backend

Web clients must run on **http://localhost:3000** (or `:5000`) and point at **dev** — see {ref}`CORS <dev-guides-cors>`. Pointing a local web client at prod will fail.

**incore-ui**

```bash
git clone https://github.com/IN-CORE/incore-ui.git && cd incore-ui
npm install
npm run start:dev          # → https://dev.in-core.org
```

Build `npm run build` · Test `npm run test:headless` · Lint `npm run lint`

**incore-studio**

```bash
git clone https://github.com/IN-CORE/incore-studio.git && cd incore-studio
npm install
npm run start:dev          # esbuild watch + serve on :3000, → https://dev.in-core.org
```

Build `npm run build` · Test `npm test` · Lint `npm run lint` · Types `npm run type-check`

**incore-playbook** (library) **+ a testbed playbook**

```bash
git clone https://github.com/IN-CORE/incore-playbook.git && cd incore-playbook
npm install && pre-commit install
yarn link                                   # register local library

cd .. && git clone https://github.com/IN-CORE/Joplin-Playbook.git && cd Joplin-Playbook
npm install && yarn link incore-playbook    # use your local library
export INCORE_REMOTE_HOSTNAME=https://dev.in-core.org && npm start
```

> `npm run start:dev` in playbook repos still points to the retired `incore-dev.ncsa.illinois.edu` — use the `export` above.
> Library is published as `@in-core/incore-playbook`; bump its version and the testbed's dependency when releasing.

Build `npm run build` · Test `npm run test:headless` · Lint `npm run lint`

**pyincore / pyincore-viz**

```bash
git clone https://github.com/IN-CORE/pyincore.git && cd pyincore
conda env create -f environment.yml && conda activate pyincore
pip install -e .
pre-commit install
```

```python
from pyincore import IncoreClient
client = IncoreClient("https://dev.in-core.org")   # default (no arg) = https://tools.in-core.org
client.clear_cache()                               # if cached datasets look stale
```

Tests run against dev and need a credentials file at `tests/pyincore/.incorepw` (ask the team):

```bash
pytest tests/pyincore/analyses/buildingdamage
```

For pyincore-viz, do the same and `pip install -e ../pyincore` if you also change pyincore.

## 3c. Local services

What you need running:

| Piece | Required? | Notes |
|-------|-----------|-------|
| MongoDB | Yes | One DB per service (data, dfr3, hazard, space, semantics, project) |
| incore-services (`./gradlew farmRun`) | Yes | All services on `:8080`, see [Services](services.md) |
| Data directory (`DATA_REPO_DATA_DIR`) | Yes | Where dataset files are stored |
| Seed data (datasets, DFR3, hazards) | For real analyses | Copy from dev or create via pyincore |
| GeoServer | No | Set `GEOSERVER_ENABLE=false` (map layers in UI/Studio won't render) |
| DataWolf | Studio workflows only | `DATAWOLF_URL` |
| Keycloak / incore-auth | No for pyincore; check for web clients | Local services trust `x-auth-userinfo` header |

Point clients at it:

```python
client = IncoreClient(service_url="http://localhost:8080", local=True,
                      username="incrtest", usergroups=["incore_ncsa"])
```

```bash
export INCORE_REMOTE_HOSTNAME=http://localhost:8080 && npm start
```

Set `SERVICES_ALLOW_ORIGIN=http://localhost:3000` on the services first — see {ref}`CORS <dev-guides-cors>`.

> TODO: web-client login flow against local services (Keycloak realm in `incore-helm/keycloak-incore-realm.json`) — confirm with team.

(dev-guides-own-client)=
## 3d. Build your own client

You don't need to fork an IN-CORE client. Any app can use the services directly.

**Endpoints** (`<host>` = `https://tools.in-core.org` or `https://dev.in-core.org`)

| Service | Base URL | Examples |
|---------|----------|----------|
| Data | `<host>/data/api` | `/datasets`, `/datasets/{id}/blob` |
| Hazard | `<host>/hazard/api` | `/earthquakes`, `/tornadoes`, `/hurricanes`, `/hurricaneWindfields`, `/floods`, `/tsunamis` |
| DFR3 | `<host>/dfr3/api` | `/fragilities`, `/mappings`, `/repairs`, `/restorations` |
| Space | `<host>/space/api` | `/spaces` |
| Semantics | `<host>/semantics/api` | `/types` |
| Project | `<host>/project/api` | `/projects` |

Full reference (Swagger): https://tools.in-core.org/doc/api/

**Auth** — Keycloak realm `In-core`, client `react-auth`:

```bash
TOKEN=$(curl -s -X POST https://dev.in-core.org/auth/realms/In-core/protocol/openid-connect/token \
  -d grant_type=password -d client_id=react-auth \
  -d username="$INCORE_USER" -d password="$INCORE_PW" | jq -r .access_token)

curl -H "Authorization: Bearer $TOKEN" "https://dev.in-core.org/data/api/datasets?limit=5"
```

| Client type | How to authenticate |
|-------------|---------------------|
| Script / backend service | Password grant above, or reuse pyincore (`IncoreClient` + `DataService`, `HazardService`, …) as an SDK |
| Browser app (SPA) | OIDC auth-code + PKCE (e.g. `keycloak-js`, `oidc-client-ts`; see `incore-studio/src/app.config.js`). Redirect URI must be registered — see {ref}`3a <dev-guides-dev-access>`. |

**CORS** — see {ref}`CORS <dev-guides-cors>`. In short: dev allows `localhost:3000/5000` (more: {ref}`3a <dev-guides-dev-access>`); prod won't allow your origin, so call prod from your own backend/proxy; your own services — configure it yourself.

**Steps**

1. Get dev access ({ref}`3a <dev-guides-dev-access>`).
2. Prototype against dev with the curl/token flow above.
3. Read-only (GET) works for public data; writes (POST/DELETE) create resources owned by your user.
4. Going to prod: browser apps need a backend/proxy (no CORS on prod); ask us to register your redirect URI for login, then switch `<host>` to `https://tools.in-core.org`.

---

## PR checklist

- Branch from `develop` (incore-ui, incore-studio, pyincore) or `master` (incore-playbook); update `CHANGELOG.md`.
- pyincore: black / flake8 via pre-commit, tests under `tests/pyincore/...`.
- Web clients: `npm run lint` and tests pass.
