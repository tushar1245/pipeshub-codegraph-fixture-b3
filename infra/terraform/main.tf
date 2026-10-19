variable "db_password" {
  type      = string
  sensitive = true
}

resource "aws_db_instance" "acme" {
  engine         = "postgres"
  instance_class = "db.t3.medium"
  password       = var.db_password
}
