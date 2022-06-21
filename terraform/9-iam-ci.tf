resource "aws_iam_user" "ci" {
  name = "ci"
  path = "/ci/"
}

resource "aws_iam_policy" "EKS_admin_policy" {
  name = "EKS_admin_policy"

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "eks:*",
        "ecr:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "eks.amazonaws.com"
        }
      }
    }
  ]
}
POLICY
}

resource "aws_iam_user_policy_attachment" "EKS_admin_policy_attach" {
  user       = aws_iam_user.ci.name
  policy_arn = aws_iam_policy.EKS_admin_policy.arn
}
