## Test Techniques
| Black Box | White Box | Experience-Based |
| --- | --- | --- |
| Test conditions, test cases, and test data are derived from a test basis that may include software requirements, specifications, use cases, and user stories | Test conditions, test cases, and test data are derived from a test basis that may include code, software architecture, detailed design, or any other source of information regarding the structure of the software | Test conditions, test cases, and test data are derived from a test basis that may include knowledge and experience of testers, developers, users and other stakeholders |
| | | |
| Test cases may be used to detect gaps between the requirements and the implementation of the requirements, as well as deviations from the requirements | |
| | | |
| Coverage is measured based on the items tested in the test basis and the technique applied to the test basis | Coverage is measured based on the items tested within a selected structure (e.g., the code or interfaces) | |
| | | |
| | Specifications are often used as an additional source of information to determine the expected outcome of test cases | |

## Common Activities 
| test analysis | test design | test implementation | test execution | test completion |
| --- | --- | --- | --- | --- |
| define and prioritize test conditions,<br/>analyze docs,<br/>evaluate docs for omissions, errors, ambiquities, etc,<br/>identify features to be tested,<br/>capture traceability | design/prioritize test cases,<br/>identify test data,<br/>design test env and infra,<br/>capture traceability<br/> | develop/prioritize test procedures,<br/>define test suites,<br/>organize suites into schedules,<br/>build test env,<br/>prepare test data,<br/>update traceability | log activities,<br/>execute,<br/>compare expected vs actual,<br/>analyze anomalies,<br/>report defects,<br/>retest,<br/>update traceability | Check which planned deliverables have been delivered,<br/>check docs, ensure defect reports are closed or created for backlog,<br/>create test summary,<br/>archive test env, data, and infra,<br/>analyze lessons learned,<br/>improve processes

## Common Work Products
| Planning | Monitoring/Control | Analysis | Design | Implementation | Execution | Completion |
| --- | --- | --- | --- | --- | --- | --- 
| plans | reports,<br/> progress reports,<br/> summary reports,<br/> traceability matrix | conditions (and prioritized) | cases,<br/> data,<br/> environment,<br/> identification of infrastructure and tools | procedures and sequencing,<br/> suites,<br/> execution schedule,<br/> automated suites | status of cases or procedures,<br/> defect reports,<br/> specifics on which items, objects, tools, and testware were involved | summary reports,<br/> action items for improving processes

## Common Test Level Characteristics
| | Unit/Component | Integration | System | Acceptance |
| --- | --- | --- | --- | --- |
| Objectives | reducing risk, verify the functional and non-functional behaviors of components, building confidence in the quality, finding defects, preventing defects from escaping | reducing risk, verify the functional and non-functional behaviors of interfaces, building confidence in the quality, finding defects, preventing defects from escaping | reducing risk, verify the functional and non-functional behaviors of system, validating work is complete, building confidence in the quality, finding defects, preventing defects from escaping | building confidence in the quality, validating the work is complete, verifying functional or non-functional behavior
| Test Basis | detailed design, code, data model, component specs | system and software design, sequence diagrams, system architecture, workflow, use cases | system and software requirements, risk analysis, use cases, epics and user stories, models of system behavior, state diagrams, system and user manuals | business processes, user or business reqs, regulations or contracts, use cases, system requirements, system or user docs installation procedures, risk analysis reports
| Objects | components/units/models, code and data structures, classes, database modules | subsystems, databases, infrastructure, API's, microservices, interfaces | applications, hw/sw systems, OS, System under Test, sys config and config data | system under test, sys config and config data, ops procedures
| Defects/ Failures | incorrect functionality, data flow problems, incorrect logic or code | incorrect or missing data, incorrect sequence of calls, interface mismatch, faulty failure handling incorrect assumptions about interactions | incorrect calcs, incorrect functional or non-functional behavior, incorrect control or data flows, failure to properly carry out end-to-end functionality, failure to work in prod, failure to match user and system manuals | workflows that don't meet needs or requirements, incorrect business rules, failure to satisy contractual or regulatory requirements, non-functional failures.
| Performed by | developers | developers | independent testers | customers, business users, product owners, operators, other stakeholders
