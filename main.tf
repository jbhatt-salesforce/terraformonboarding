# This provider is only temporarily needed. We'll remove it in a future step.
provider "aws" {}

module "my-terraform-environment" {
  source         = "git@github.com:sfdc-pcg/terraform-aws-tfstate.git//environment?ref=1.2.0"
  name           = "<YOUR_TERRAFORM_ENVIRONMENT_NAME_HERE>"
  public_ssh_key = "<YOUR_TERRAFORM_SSH_KEY_HERE>"
  pgp_key        = "<YOUR_PGP_KEY_HERE>"
  bootstrap      = true

  providers {
    aws = "aws"
  }
}
