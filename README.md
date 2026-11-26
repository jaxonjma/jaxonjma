<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <img alt="Jaxon Muñoz — Software Engineer & AI Engineer" src="./assets/hero-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/jaxon-julian-munoz-avendano/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:jaxonma@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://stackoverflow.com/users/5870012/jaxonjma"><img src="https://img.shields.io/badge/Stack%20Overflow-F58025?style=for-the-badge&logo=stackoverflow&logoColor=white" alt="Stack Overflow"/></a>
  <img src="https://img.shields.io/badge/Open%20to-remote%20%26%20freelance-2f6bff?style=for-the-badge" alt="Open to remote and freelance"/>
  <img src="https://komarev.com/ghpvc/?username=jaxonjma&style=for-the-badge&color=1b1e23&label=visitors" alt="Profile views"/>
</p>

<p align="center">
  I build backend systems where correctness is not optional (investment cores, regulated reporting, payments,<br>
  national-scale event pipelines, telemedicine) and, increasingly, the AI layer on top of them: RAG, LLM agents and automation.
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/impact-dark.svg">
  <img alt="10+ years · ~1.5M properties in a Kafka pipeline · 50-participant telemedicine · 4 industries" src="./assets/impact-light.svg" width="100%">
</picture>

## 💼 Experience

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/experience-dark.svg">
  <img alt="Experience: Freelance, EPAM · CoreLogic, Makers Solutions, Unosquare, Apple · FNB Ads" src="./assets/experience-light.svg" width="100%">
</picture>

<details>
<summary><b>Plain-text version</b> (searchable, copy-friendly)</summary>
<br>

**Independent · Freelance**, Software Engineer & AI Engineer *(now)*
- Designs and builds new Java backend features for a Colombian fintech.
- Builds multi-tenant RAG engines and LLM agents with FastAPI and Supabase (row-level security).
- Integrates payment gateways (Stripe, Whop and others): transactions, idempotency, encryption of sensitive data.
- Connects products to the WhatsApp Cloud API for conversational flows.

**EPAM · CoreLogic**, Senior Software Engineer
- Reactive microservices on Kafka segmenting real-estate leads across ~1.5M U.S. properties.
- Mortgage and property module with Java/Spring and Angular.
- GraphQL APIs on AWS, event-driven architecture.

**Makers Solutions**, Tech Lead → Software Architect
- Investment core for Protección: derivatives valuation and regulatory reporting to the Colombian Financial Superintendence.
- Bancolombia: defined caching strategies; system design, batch processing, PR review and team leadership.

**Unosquare**, Senior Java Developer
- WebRTC telemedicine with Twilio, up to 50 participants per session.
- Healthcare microservices and GraphQL services.

**Apple · FNB Ads**
- Migrations to AWS and related cloud work for the FNB Ads team.

</details>

## 🧠 AI engineering

How I build retrieval-augmented, agentic systems: one codebase, many tenants, behavior driven by configuration.

```mermaid
flowchart LR
    subgraph ingest [Ingestion]
        docs[Documents<br/>and data] --> chunk[Chunk and<br/>embed] --> vs[(Vector store<br/>per tenant)]
    end

    subgraph runtime [Runtime]
        user([User or channel]) --> api[FastAPI<br/>gateway]
        api --> cfg{{Tenant config}}
        cfg --> agent[LLM agent]
        agent -- retrieve --> vs
        agent -- tools --> tools[APIs, payments,<br/>CRM, messaging]
        agent -- answer --> user
    end

    api --> db[(Postgres<br/>row-level security)]

    classDef accent fill:#2f6bff,stroke:#7fd6ff,color:#ffffff
    classDef soft fill:#1b1e23,stroke:#8b93a0,color:#f3f4f6
    class cfg,agent accent
    class docs,chunk,vs,user,api,tools,db soft
    style ingest fill:transparent,stroke:#3d86ff,stroke-dasharray:5 5,color:#5aa8ff
    style runtime fill:transparent,stroke:#3d86ff,stroke-dasharray:5 5,color:#5aa8ff
```

<table>
  <tr>
    <td width="33%" valign="top"><b>🔎 Retrieval</b><br>RAG pipelines with tenant-isolated knowledge, so each client's data stays theirs.</td>
    <td width="33%" valign="top"><b>🛠️ Agents</b><br>LLM agents with tool calling over real systems: payments, CRMs, messaging channels.</td>
    <td width="33%" valign="top"><b>⚙️ Config over code</b><br>New tenants and behaviors through configuration, not forks.</td>
  </tr>
</table>

## 🛠️ Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/orbit-dark.svg">
  <img alt="Tech constellation: languages, data and streaming, cloud and DevOps, AI engineering" src="./assets/orbit-light.svg" width="100%">
</picture>

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,python,fastapi,ts,react,angular,graphql,postgres,supabase,mongodb,kafka,aws,azure,docker,kubernetes,jenkins,git&perline=9" alt="Stack icons"/>
</p>

## 📐 How I work

```yaml
correctness:   idempotent by default, explicit failure modes, tests that describe behavior
architecture:  design for the second tenant, so the hundredth costs less than the first
data:          sensitive data encrypted, access scoped (row-level security), nothing leaks across tenants
leadership:    clear designs, honest PR reviews, teams that can run the system without me
docs:          if it only lives in my head, it isn't done
```

## 🎓 Learning

- **Diploma in Artificial Intelligence**, Universidad de los Llanos
- **Master's degree**, starting now

## 📈 Activity

<p align="center">
  <img src="./profile-3d-contrib/profile-3d.svg" alt="3D contribution calendar" width="100%"/>
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jaxonjma/jaxonjma/output/snake-dark.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/jaxonjma/jaxonjma/output/snake.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg">
  <img alt="Always building, learning and breaking code to build the future." src="./assets/footer-light.svg" width="100%">
</picture>
