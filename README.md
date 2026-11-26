<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/terminal-dark.svg">
  <img alt="Terminal: whoami — Jaxon Muñoz, senior software engineer and founder of WildCore Labs" src="./assets/terminal-light.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/jaxon-julian-munoz-avendano/"><img src="https://img.shields.io/badge/linkedin-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:jaxonma@gmail.com"><img src="https://img.shields.io/badge/email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://wildcorelabs.io"><img src="https://img.shields.io/badge/wildcorelabs.io-1b1d21?style=flat-square" alt="WildCore Labs"/></a>
  <a href="https://stackoverflow.com/users/5870012/jaxonjma"><img src="https://img.shields.io/badge/stack%20overflow-F58025?style=flat-square&logo=stackoverflow&logoColor=white" alt="Stack Overflow"/></a>
  <img src="https://komarev.com/ghpvc/?username=jaxonjma&style=flat-square&color=2f6bff&label=visitors" alt="Profile views"/>
</p>

> **TL;DR:** 10+ years shipping backend systems where correctness matters (finance, regulated reporting, national-scale event pipelines). Now founder of **[WildCore Labs](https://wildcorelabs.io)**, building multi-tenant AI infrastructure. Open to senior backend and AI architecture roles.

---

### `$ tree ~/how-i-ship`

How a product moves through my hands, from a fuzzy idea to something you can operate at 3 a.m.:

```mermaid
flowchart LR
    need([💡 Client need]) --> discovery[Discovery<br/>and design]
    discovery --> core{{Multi-tenant core<br/>config over code}}

    subgraph ai [AI layer]
        rag[RAG engine]
        agents[LLM agents<br/>and tool calling]
        msg[Messaging<br/>channels]
    end

    core --> rag
    core --> agents
    core --> msg
    core --> api[FastAPI / Spring<br/>services]
    api --> db[(Postgres<br/>Supabase)]
    api --> events[[Kafka / events]]
    api --> ci[Tests · CI/CD]
    ci --> prod([🚀 Production])

    classDef accent fill:#2f6bff,stroke:#7fd6ff,color:#ffffff
    classDef soft fill:#1b1d21,stroke:#8b93a0,color:#f3f4f6
    class core,prod accent
    class need,discovery,rag,agents,msg,api,db,events,ci soft
    style ai fill:transparent,stroke:#2f6bff,stroke-dasharray:5 5,color:#5aa8ff
```

---

### `$ man jaxon`

<details>
<summary><b>💼 Experience</b>: Apple, EPAM, Unosquare, Makers Solutions, freelance</summary>
<br>

| Company · client | Highlights |
|---|---|
| **Apple** · FNB Ads | Migrations to **AWS**. |
| **EPAM** · CoreLogic | **Reactive microservices on Kafka** for real-estate lead segmentation across **~1.5M U.S. properties**; **GraphQL** APIs. |
| **Unosquare** · Healthcare | Senior backend on **GraphQL** services. |
| **Makers Solutions** · Protección | Investment core: **derivatives valuation** and **regulatory reporting** to the Financial Superintendence. |
| **Makers Solutions** · Bancolombia | **Tech lead → junior architect**; defined **caching strategies**. |
| **Freelance** | **Java** backend features for a Colombian fintech; **Stripe/Whop** payments with idempotency and encryption. |

</details>

<details>
<summary><b>🏢 WildCore Labs</b>: what the studio does</summary>
<br>

*Wild at heart, free by design.* An engineering studio from Medellín:

- **Software engineering end to end**: web and mobile, design, development, testing, documentation, DevOps, cloud.
- **AI agents and automation** for internal processes: docs, reviews, development, marketing, sales.
- **Multi-tenant platforms**: RAG engines, LLM agents and messaging infrastructure, configured per client.
- **Teams**: full IT teams and staff augmentation for companies of any size.
- **Launch and growth**: payments, CRM, funnels, distribution and partnerships.

→ [wildcorelabs.io](https://wildcorelabs.io)

</details>

<details>
<summary><b>🛠️ Stack</b>: what I reach for</summary>
<br>

| Layer | Tools |
|---|---|
| Backend | <img src="https://skillicons.dev/icons?i=java,spring,python,fastapi,nodejs,scala,graphql" height="36" alt="Backend"/> |
| Frontend | <img src="https://skillicons.dev/icons?i=ts,js,react,angular,html,css" height="36" alt="Frontend"/> |
| Data &amp; streaming | <img src="https://skillicons.dev/icons?i=postgres,supabase,mysql,mongodb,firebase,kafka" height="36" alt="Data"/> |
| Cloud &amp; DevOps | <img src="https://skillicons.dev/icons?i=aws,azure,docker,kubernetes,jenkins,git" height="36" alt="Cloud"/> |
| AI | RAG · LLM agents · tool calling · workflow automation |

</details>

<details>
<summary><b>📐 Principles</b>: how I make decisions</summary>
<br>

```yaml
correctness: idempotent by default, explicit failure modes, tests that describe behavior
scale:       design for the second tenant, so the hundredth costs less than the first
stack:       adapt to the client's; default to Python/FastAPI · Supabase · Railway
docs:        if it only lives in my head, it isn't done
```

</details>

<details>
<summary><b>🎓 Learning</b></summary>
<br>

- Diploma in Artificial Intelligence, Universidad de los Llanos.
- Starting a master's degree.

</details>

---

### `$ git log --graph`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jaxonjma/jaxonjma/output/snake-dark.svg">
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/jaxonjma/jaxonjma/output/snake.svg" width="100%">
</picture>

<p align="center"><sub>Medellín, Colombia 🇨🇴 · <code>exit 0</code></sub></p>
