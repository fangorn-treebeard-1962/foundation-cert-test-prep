## Test Techniques
| Black Box | White Box | Experience-Based |
| --- | --- | --- |
| Conditions, cases, and data  derived from a test basis that may include software requirements, specifications, use cases, and user stories | Conditions, cases, and data  derived from a test basis that may include code, software architecture, detailed design, or any other source of information regarding the structure of the software | Conditions, cases, and data  derived from a test basis that may include knowledge and experience of testers, developers, users and other stakeholders |
| | | |
| Test cases may detect gaps between requirements and implementation, as well as deviations from the requirements | |
| | | |
| Coverage based on items tested in the basis and the technique applied to basis | Coverage based on items tested within a selected structure (e.g., the code or interfaces) | |
| | | |
| | Specifications are often used as an additional source of information to determine the expected outcome of test cases | |

## Common Activities 
| test analysis | test design | test implementation | test execution | test completion |
| --- | --- | --- | --- | --- |
| define/prioritize conditions,<br/>analyze docs,<br/>evaluate docs for omissions, errors, ambiquities, etc,<br/>identify features to be tested,<br/>capture traceability | design/prioritize cases,<br/>identify test data,<br/>design test env and infra,<br/>capture traceability<br/> | develop/prioritize procedures,<br/>define test suites,<br/>organize suites into schedules,<br/>build test env,<br/>prepare test data,<br/>update traceability | log activities,<br/>execute,<br/>compare expected vs actual,<br/>analyze anomalies,<br/>report defects,<br/>retest,<br/>update traceability | Check which planned deliverables<br/>have been delivered,<br/>check docs,<br/>ensure defect reports<br/>are closed or created<br/>for backlog,<br/>create test summary,<br/>archive test env, data, and infra,<br/>analyze lessons learned,<br/>improve processes

## Common Work Products
| Planning | Monitoring/Control | Analysis | Design | Implementation | Execution | Completion |
| --- | --- | --- | --- | --- | --- | --- 
| plans | reports,<br/> progress reports,<br/> summary reports,<br/> traceability matrix | conditions<br/>(prioritized) | cases,<br/> data,<br/> environment,<br/> identification of<br/>infra and tools | procedures (sequenced),<br/> suites,<br/> execution schedule,<br/> automated suites | status of cases or procedures,<br/> defect reports,<br/> specifics on which items,<br/>objects, tools, and<br/>testware were involved | summary reports,<br/> action items for<br/>improving processes

## Common Test Level Characteristics
| | Unit/Component | Integration | System | Acceptance |
| --- | --- | --- | --- | --- |
| Objectives | reducing risk, verify the functional and non-functional behaviors of components, building confidence in the quality, finding defects, preventing defects from escaping | reducing risk, verify the functional and non-functional behaviors of interfaces, building confidence in the quality, finding defects, preventing defects from escaping | reducing risk, verify the functional and non-functional behaviors of system, validating work is complete, building confidence in the quality, finding defects, preventing defects from escaping | building confidence in the quality, validating the work is complete, verifying functional or non-functional behavior
| Test Basis | detailed design, code, data model, component specs | system and software design, sequence diagrams, system architecture, workflow, use cases | system and software requirements, risk analysis, use cases, epics and user stories, models of system behavior, state diagrams, system and user manuals | business processes, user or business reqs, regulations or contracts, use cases, system requirements, system or user docs installation procedures, risk analysis reports
| Objects | components/units/models, code and data structures, classes, database modules | subsystems, databases, infrastructure, API's, microservices, interfaces | applications, hw/sw systems, OS, System under Test, sys config and config data | system under test, sys config and config data, ops procedures
| Defects/ Failures | incorrect functionality, data flow problems, incorrect logic or code | incorrect or missing data, incorrect sequence of calls, interface mismatch, faulty failure handling incorrect assumptions about interactions | incorrect calcs, incorrect functional or non-functional behavior, incorrect control or data flows, failure to properly carry out end-to-end functionality, failure to work in prod, failure to match user and system manuals | workflows that don't meet needs or requirements, incorrect business rules, failure to satisy contractual or regulatory requirements, non-functional failures.
| Performed by | developers | developers | independent testers | customers, business users, product owners, operators, other stakeholders

## Reviews

| informal | walkthrough | technical | inspection |
| --- | --- | --- | --- |
| find defects,<br/> done by colleague,<br/> little to no documentation | find defects,<br/> improve code,<br/> consider alternatives,<br/> check conformance,<br/> meeting held,<br/> scribe mandatory,<br/> documentation and checklists optional | find defects,<br/> gain concensus,<br/> review prep required,<br/> meeting if held should be facilitated,<br/> scribe mandatory,<br/> reports generally produced | find potential defects,<br/> gain concensus,<br/> build confidence,<br/> improve knowledge and processes,<br/> formal process,<br/> rules and checklist mandatory,<br/> roles required,<br/> review prep required,<br/> entry and exit criteria required,<br/> meeting required and facilitated,<br/> scribe mandatory,<br/> reports produced,<br/> metrics captured and applied to improve processes