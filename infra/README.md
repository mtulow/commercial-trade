# <center> Infrastructure-as-Code </center>


## Resources
This folder provisions the following Resources:

| Resource | Description | Name |
|:---------|:------------|------|
| Compute Warehouses | A compute resource that processes queries. | <ul><il>[`loading`](...)</il> <il>[`transforming`](...)</il> <il>[`reporting`](...)</il></ul> |
| Database | A container for schemas, tables, views, etc. | [`wto_trade`](...) |
| Schemas | A container for tables, views, functions, and other objects. | <ul><il>[`raw`](...)</il> <br> <il>[`analytics`](...)</il> <il>[`imports`](...)</il><br><il>[`exports`](...)</il></ul> |
| Roles | A collection of privileges that can be granted to users or other roles. | <ul><il>[`wto_loader`](...)</il> <il>[`wto_transformer`](...)</il> <il>[`wto_reporter`](...)</il></ul> |
| Users | An entity that can connect to Snowflake and execute queries. | <ul><il>[`prefect_user`](...)</il> <il>[`dbt_user`](...)</il> <il>[`<vis_user>`](...)</il></ul>


---


2. RBAC Implementation

__Principle of Least Privilege:__ Grant only the necessary privileges to each role. This minimizes the potential impact of a security breach.

__Separation of Duties:__ Avoid granting all permissions to a single role. Separate responsibilities like data ingestion, transformation, and analysis across different roles.

3. Service Roles


Terraform Role:

Privileges:

CREATE WAREHOUSE
CREATE DATABASE
CREATE SCHEMA
CREATE TABLE
GRANT USAGE ON WAREHOUSE to ROLE
GRANT USAGE ON DATABASE to ROLE
GRANT USAGE ON SCHEMA to ROLE
GRANT ALL ON TABLE to ROLE
... (other necessary privileges for Terraform to manage Snowflake resources)
Rationale: This role provides Terraform with the necessary permissions to create and manage Snowflake resources defined in your infrastructure-as-code.

---

## Custom Roles

| Custom Role | Description | Privileges |
| ----------- | ----------- | ---------- |
| `iac_role` | This role provides the IaC service with the necessary permissions to manage resources. | <ul><il>_CREATE WAREHOUSE_</il> <il>_CREATE DATABASE_</il> <il>_GRANT USAGE ON WAREHOUSE_</il> <il>GRANT USAGE DATABASE</il> </ul>
 |







