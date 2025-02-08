
# Create Terraform Role
resource "snowflake_account_role" "iac" {
  name     = "iac_service_role"
}


# Grant the following privileges to terraform role:
#   - CREATE WAREHOUSE
#   - CREATE DATABASE
#   - CREATE SCHEMA
#   - CREATE TABLE
#   - GRANT USAGE ON WAREHOUSE to ROLE
#   - GRANT USAGE ON DATABASE to ROLE
#   - GRANT USAGE ON SCHEMA to ROLE
#   - GRANT ALL ON TABLE to ROLE

provider "snowflake" {
  alias = "security_admin"
  role  = "SECURITYADMIN"
}


resource "snowflake_account_grant" "create_warehouse" {
  privilege = "CREATE WAREHOUSE"
  grantee   = snowflake_account_role.iac.name
}

resource "snowflake_account_grant" "create_database" {
  privilege = "CREATE DATABASE"
  grantee   = snowflake_role.terraform_role.name
}

resource "snowflake_account_grant" "create_schema" {
  privilege = "CREATE SCHEMA"
  grantee   = snowflake_role.terraform_role.name
}

resource "snowflake_account_grant" "create_table" {
  privilege = "CREATE TABLE"
  grantee   = snowflake_role.terraform_role.name
}
