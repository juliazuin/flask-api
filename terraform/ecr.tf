resource "aws_ecr_repository" "restapi" {
  name = "restapi"
  force_delete = "true"
}