resource "aws_ecr_repository" "pyr-zero" {
  name                 = "pyr-zero"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}