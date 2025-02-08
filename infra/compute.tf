

resource "snowflake_warehouse" "compute_wh" {
  name           = "wto_etl_wh"
  warehouse_size = "xsmall"
  auto_suspend   = 60
}