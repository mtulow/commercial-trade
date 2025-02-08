
# Creat wto database
resource "snowflake_database" "db" {
  name = "wto_trade"
}

# Create a staging schema
resource "snowflake_schema" "stage" {
  database = snowflake_database.db.name
  name     = "raw"
}

# # Create an imports schema
# resource "snowflake_schema" "imports" {
#   database = snowflake_database.db.name
#   name     = "imports"
# }

# # Create an exports schema
# resource "snowflake_schema" "exports" {
#   database = snowflake_database.db.name
#   name     = "exports"
# }

# Create an analytics schema
resource "snowflake_schema" "exports" {
  database = snowflake_database.db.name
  name     = "exports"
}

resource "snowflake_database_role" "db_role" {
  database = snowflake_database.db.name
  name     = "db_role_name"
}