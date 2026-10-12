# 4. Developer: web services (Java)

Repo: https://github.com/IN-CORE/incore-services (branch from `develop`)

| Service | Context path | Mongo DB (default) |
|---------|--------------|--------------------|
| data | `/data` | `mongodb://localhost:27017/datadb` |
| dfr3 | `/dfr3` | `.../dfr3db` |
| hazard | `/hazard` | `.../hazarddb` |
| space | `/space` | `.../spacedb` |
| semantics | `/semantics` | `.../semanticsdb` |
| project | `/project` | `.../projectdb` |

Shared code: `server/incore-common`, `server/tools-common`.
API docs (prod): https://tools.in-core.org/doc/api/

## Prerequisites

- JDK 11+ (`sourceCompatibility = 11`)
- MongoDB running on `localhost:27017` (defaults work, no env needed)
- IntelliJ IDEA (Community is fine)

```bash
docker run -d --name incore-mongo -p 27017:27017 mongo:6
```

## Run

```bash
git clone https://github.com/IN-CORE/incore-services.git
cd incore-services/server
export DATA_REPO_DATA_DIR=$HOME/incore-data   # dataset file storage (data, hazard)
export SERVICES_URL=http://localhost:8080       # hazard → data calls
export GEOSERVER_ENABLE=false
export SERVICES_ALLOW_ORIGIN=http://localhost:3000     # CORS for local web clients
export SERVICES_ALLOW_METHODS=GET,POST,DELETE,PUT,PATCH,OPTIONS
export SERVICES_ALLOW_HEADERS=authorization,content-type,accept
./gradlew farmRun                              # all services on :8080
```

Check: `curl http://localhost:8080/data/api/datasets -H 'x-auth-userinfo: {"preferred_username":"incrtest"}'`

Single service: `./gradlew :hazard-service:appRun`
Tests: `./gradlew test` or `./gradlew :dfr3-service:test`

## IntelliJ

1. **Open** `incore-services/server` (the folder with `settings.gradle`) → trust Gradle project.
2. *Settings → Build Tools → Gradle*: Gradle JVM = JDK 11+.
3. Run config: *Gradle* → task `farmRun`, add the env vars above.
4. Debug: run `farmDebug` (or `appDebug` per service), then *Remote JVM Debug* attach to port `5005`.

## Auth when running locally

There is no Keycloak in front of local services. Pass identity as headers:

```
x-auth-userinfo:  {"preferred_username": "incrtest"}
x-auth-usergroup: {"groups": ["incore_ncsa"]}
```

pyincore does this for you:

```python
IncoreClient(service_url="http://localhost:8080", local=True,
             username="incrtest", usergroups=["incore_ncsa"])
```

In deployed envs, `incore-auth` validates the Keycloak JWT and injects these headers.

## Other env vars (only if needed)

| Var | Used by | Purpose |
|-----|---------|---------|
| `<SVC>_MONGODB_URI` | each service | Override Mongo URI (`DATA_`, `DFR3_`, `HAZARD_`, `SPACE_`, `SEMANTICS_`, `PROJECT_`) |
| `COMMON_MONGODB_URI` | dfr3, hazard | Shared `commondb` |
| `DATA_SERVICE_URL`, `HAZARD_SERVICE_URL`, `SEMANTICS_SERVICE_URL` | data, space, project | Cross-service base URLs |
| `GEOSERVER_URL/_USER/_PW/_WORKSPACE` | data | When `GEOSERVER_ENABLE=true` |
| `DATAWOLF_URL`, `DATAWOLF_USER` | hazard, project | Workflow execution |
| `PG_HOST/PORT/USER/PASSWORD/DATABASE` | data | Postgres-backed features |
| `SERVICES_ALLOW_ORIGIN/_METHODS/_HEADERS` | all | CORS — **set these** if any browser client calls your services ({ref}`details <dev-guides-cors>`) |

## Docker images

```bash
cd incore-services && ./docker.sh     # builds incore/{data,dfr3,hazard,space,semantics}-jetty
```

Deployment: Helm charts in https://github.com/IN-CORE/incore-helm

## Seed data

> TODO: confirm with team — recommended way to get a Mongo dump / sample datasets + DFR3 + hazards for local dev.
