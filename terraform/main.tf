module "kubernetes_cluster" {
  source = "git::https://github.com/juliazuin/infra-flask-api.git?ref=main"

  cidr_block   = "10.34.0.0/16"
  project_name = "restapi"
  region       = "sa-east-1"
  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}