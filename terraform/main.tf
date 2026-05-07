provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_security_group" "devops_sg" {
  name = "devops-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 9092
    to_port     = 9092
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 2181
    to_port     = 2181
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "devops_server" {
  ami                    = "ami-0d52744d6551d851e"
  instance_type          = "t2.micro"
  key_name               = "ap-northeast-1"
  vpc_security_group_ids = [aws_security_group.devops_sg.id]

  tags = {
    Name = "devops-platform-server"
  }
}

output "server_ip" {
  value = aws_instance.devops_server.public_ip
}
